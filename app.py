import json
import boto3
import psycopg2.extras
from flask import Flask, make_response, jsonify
from gevent.pywsgi import WSGIServer

REDSHIFT_RO_KEY = "s2/prod/redshift_ro"
AUTHOR_TOP_CITED_PAPERS_QUERY = "call top_cited_by_author(%s); select * from #temp_top_cited order by n_citations desc;"

app = Flask(__name__)


class NoSuchAuthorError(Exception):
    def __init__(self, author_id: int):
        self.message = "No record exists for paper id: {}".format(str(author_id))

    def __str__(self):
        return self.message


@app.route("/")
def health_check():
    return "Ok"


def _get_secret(secret_key: str) -> str:
    """ Fetch a json secret from AWS Secrets Manager """
    # Create a Secrets Manager client
    client = boto3.client(service_name='secretsmanager', region_name='us-west-2')
    get_secret_value_response = client.get_secret_value(SecretId=secret_key)
    return json.loads(get_secret_value_response['SecretString'])


def _get_redshift_connection():
    secret_key = REDSHIFT_RO_KEY
    secret = _get_secret(secret_key)
    return psycopg2.connect(
        host=secret['host'],
        port=5439,
        database='dev',
        user=secret['user'],
        password=secret['password']
    )


@app.route("/<int:author_id>")
def get_top_cited_papers(author_id: int):
    results = None
    try:
        with _get_redshift_connection() as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
                cursor.execute(AUTHOR_TOP_CITED_PAPERS_QUERY, (author_id,))
                results = cursor.fetchall()
        if results:
            return json.dumps(results[:25])
        else:
            raise NoSuchAuthorError(author_id)
    except NoSuchAuthorError as e:
        return make_response(jsonify(str(e)), 404)


if __name__ == '__main__':
    http_server = WSGIServer(("0.0.0.0", 8080), app)
    http_server.serve_forever()
    # get_top_cited_papers(1701686)

# Semantic Scholar Author Explorer

This repository contains code for using [Semantic Scholar Academic Graph API](https://www.semanticscholar.org/product/api)
for exploring the relationships between authors and the papers they cite.

We were inspired to do this when Twitter exploded about a [list of papers
Ilya Sutskever shared with John Carmack](https://twitter.com/xlr8harder/status/1621528198097047553).
The excitement was enough to prompt a response from [John Carmack](https://twitter.com/ID_AA_Carmack/status/1622673143469858816),
encouraging Sutskever to produce an updated list. That hasn't happened yet.

We don't think a single person's view of AI could possibly contain "90%"
of the field's diversity nor recent momentum. Yet we recognize that Ilya's list almost
certainly gave John Carmack a head-start in a exploding field. So we figured
we'd do our best to level the playing field, and give everyone access to a similar
(and hopefully better) list of our own.

The list and code for producing it is available in a [Jupyter Notebook](./AuthorTopCitedPapers.ipynb)
included in this repository. A portion of the data required for the code isn't
yet available via Semantic Scholar's API (we're working on that). Which means for now
the analysis can only be executed for authors included in [author_citations.json](./author_citations.json).

Take a look and let us know what you think. We hope the list is useful, and
that it might inspire others to do similar analyses using the API and data that
Semantic Scholar makes openly available.

Here's to making AI more open, and collaborative. We think it's more important now
than ever to lay the ground work for that.

## Running the Code

You can run the code like so:

```bash
conda create -n author_explorer python=3.8
conda activate author_explorer
pip install -r requirements.txt
jupyter notebook
```

If you run into rate limits, you can use a Semantic Scholar API key
by creating a file called `key.txt` in the repository root:

```
echo XXX > key.txt
```

The notebook will read the key and use that value when making requests to
the API. You can request a key [here](https://www.semanticscholar.org/product/api#Partner-Form).


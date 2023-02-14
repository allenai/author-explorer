# Semantic Scholar Author Explorer

This repository contains code for using [Semantic Scholar Academic Graph API](https://www.semanticscholar.org/product/api)
for exploring the relationships between authors and the papers they cite.

We were inspired to do this in response to a Twitter thread about a [list of papers
Ilya Sutskever shared with John Carmack](https://twitter.com/xlr8harder/status/1621528198097047553).
The list remains a mystery. We thought it'd be fun to produce a list of our own and
do some analysis on the way.

It's important to stress that this is ultimately an exploratory exercise. AI, like
most fields, is both growing fast and full of diverse perspectives and focus areas. 
Trying to boil that ocean down into a single list of papers from a small set of authors is fraught. 
Never the less we thought it'd be fun to take a look at some data, as to share the
things our APIs and efforts might enable in an open, collaborative fashion.

The analysis is available in a [Jupyter Notebook](./AuthorTopCitedPapers.ipynb)
included in this repository. It's worth noting that the code relies on data that
isn't yet available via Semantic Scholar's API, which means you can't run this
on a set of your own authors. We're working on fixing that, by expanding our API.

We hope you find the data interesting and would love to hear your thoughts, or see
additional analysis. Let us know what you come up with.

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

## Launching with Binder

The notebook can also be directly launched with [Binder](https://mybinder.org/) 
with all the interactive goodness. This makes the plots a lot easier to parser, in
particular. Click the badge below to open the notebook using Binder:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/allenai/author-explorer/main?filepath=AuthorTopCitedPapers.ipynb)

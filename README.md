# Semantic Scholar Author Explorer

This repository contains code for using [Semantic Scholar Academic Graph API](https://www.semanticscholar.org/product/api)
for exploring the relationships between authors and the papers they cite.

We were inspired to do this in response to a Twitter thread about a [list of papers
Ilya Sutskever shared with John Carmack](https://twitter.com/xlr8harder/status/1621528198097047553).
The list remains a mystery. We thought it'd be fun to produce a list of our own and
do some analysis on the way.

So we set out to produce a rough estimate of the papers that might be on Ilya's
list, by examining the papers he repeatedly tends to site. And we figured we'd go
even further by pooling such lists across a set of accomplished AI scientists, hoping
to produce a list that even more diverse and comprehensive. The resulting list
we were able to produce is interesting. Let us know what you think!

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

## Related Work

This work was inspired by recent, related work at AI2 that helps people discover
papers based on the citations of people they know:

```
@inproceedings{Kang2023ComLitteeLD,
  title={ComLittee: Literature Discovery with Personal Elected Author Committees},
  author={Hyeonsu B. Kang and Nouran Soliman and Matt Latzke and Joseph Chee Chang and Jonathan Bragg},
  year={2023}
}
```

You can read more about their approach [Semantic Scholar](https://www.semanticscholar.org/paper/ComLittee%3A-Literature-Discovery-with-Personal-Kang-Soliman/7f95d982f8ed3189d84577f1fdf07f93c99423f2) 
or [ArXiv](https://arxiv.org/abs/2302.06780).

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

## Team

This project was put together at the [Allen Institute for AI](https://allenai.org) by:

- [Amanpreet Singh](https://www.semanticscholar.org/author/Amanpreet-Singh/2116287642)
- [Sam Skjonsberg](https://www.semanticscholar.org/author/Sam-Skjonsberg/46181683)
- [Doug Downey](https://www.semanticscholar.org/author/Doug-Downey/145612610)

We couldn't have built it without the [Semantic Scholar API](https://www.semanticscholar.org/product/api)
nor the hard work of the team behind it.



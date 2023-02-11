# Semantic Scholar Author Explorer

This repository contains code for using [Semantic Scholar Academic Graph API](https://www.semanticscholar.org/product/api)
for exploring the relationships between authors and the papers they cite.

This exercise was inspired after Twitter exploded about a [list of papers
Ilya Sutskever shared with John Carmack](https://twitter.com/xlr8harder/status/1621528198097047553).
The excitement was enough to prompt a response from [John Carmack](https://twitter.com/ID_AA_Carmack/status/1622673143469858816),
encouraging Sutskever to produce an updated list. That hasn't happened yet.

We reject the notion that one person's view of AI could possibly contain "90%"
of the field's diversity nor recent momentum. Yet we also recognize that Ilya's list almost
certainly gave John Carmack a head-start -- despite it's limited perspective.

So we figured we'd try to produce a list of papers that might be on the
said list. And while we're at it we'll supplement it with those from a few other 
influential authors. The idea being to both demonstrate the types of analyses 
we hope to enable via Semantic Scholar, and produce a list of papers that might help
people enter and understand the field of AI.

The code for the analysis is in a [Jupyter Notebook](./AuthorTopCitedPapers.ipynb)
included in this repository. A portion of the data required for the code isn't
yet available via Semantic Scholar's API (we're working on that). Which means for now
the analysis can only be executed for authors included in [author_citations.json](./author_citations.json).

Take a look, let us now what you think and please feel free to fork the repository
and build off of what's here. Not only are we passionate about the open availability 
of this information, we're also big fans of encouraging people to build off it. 
Together we can do bigger, and better things.

Here's to making AI more open.

## Running the Notebook

If you use `conda`:

```bash
conda create -n author_explorer python=3.8
conda activate author_explorer
pip install -r requirements.txt
jupyter notebook
```

You can use `venv` too:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook
```


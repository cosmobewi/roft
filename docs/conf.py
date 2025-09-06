# docs/conf.py
import os
import sys
from datetime import date
from pathlib import Path

BASE = Path(__file__).resolve().parent
SHARED_TEMPLATES = BASE / "_templates"
SHARED_STATIC = BASE / "_static"

project = "RoFT"
author = "Lionel Orcil — Édité et diffusé par IOBEWI"
copyright = f"{date.today().year}, {author}"

sys.path.insert(0, os.path.abspath(".."))

# -- Extensions conseillées -------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.mathjax",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.todo",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.graphviz",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
}

mathjax3_config = {
    "tex": {
        "macros": {
            r"\dd":  r"{\,\mathrm{d}}",
            r"\vect": [r"{\boldsymbol{#1}}", 1],
            r"\avg":  [r"{\langle #1 \rangle}", 1],
        }
    }
}

html_logo = str(SHARED_STATIC / "iobewi.png")
html_theme_options = {
    'logo_only': True,
}

templates_path   = [str(SHARED_TEMPLATES)]
html_static_path = [str(SHARED_STATIC)]

html_theme = "sphinx_rtd_theme"
html_css_files = ["custom.css"]
html_show_sphinx = False
html_show_copyright = False
html_favicon = str(SHARED_STATIC / "favicon.ico")

source_suffix = ".rst"
master_doc = "index"
language = "fr"
autosummary_generate = True
nitpicky = False

rst_prolog = r"""
.. |proj| replace:: Théorie des Horloges Cosmologiques
.. |LCDM| replace:: :math:`\Lambda\mathrm{CDM}`
"""

todo_include_todos = True

html_context = {
    "display_github": True,
    "github_user": "cosmobewi",
    "github_repo": "roft",
    "github_version": "main/docs/",
}

exclude_patterns = []
# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'girder'
copyright = '2022, Kitware, Inc.'
author = 'Kitware, Inc.'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    # "notfound.extension",
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    "sphinx_copybutton",
    "sphinx_panels",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**.ipynb_checkpoints"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "friendly"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

html_title = project
html_short_title = ""
# html_favicon = "_static/favicon.png"
html_extra_path = []  # TODO: "CNAME",
html_use_smartypants = True


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "pydata_sphinx_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_context = {
    "github_user": "girder",
    "github_repo": "girder-4",
    "github_version": "main",
    "doc_path": "doc",
}

html_theme_options = {
    # "google_analytics_id": "",
    "show_prev_next": False,
    "github_url": "https://github.com/girder/girder-4",
    "icon_links": [
        {
            "name": "About",
            "url": "https://kitware.com/",
            "icon": "fa fa-info fa-fw",
        },
    ],
}


# Copy button customization
# exclude traditional Python prompts from the copied code
copybutton_prompt_text = r">>> ?|\.\.\. "
copybutton_prompt_is_regexp = True


def setup(app):
    app.add_css_file("copybutton.css")
    app.add_css_file("no_search_highlight.css")
    app.add_css_file("fontawesome/css/all.css")

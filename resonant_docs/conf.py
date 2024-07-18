# -- Project information -----------------------------------------------------
project = "Resonant"
copyright = "2024, Kitware, Inc."
author = "Kitware, Inc."

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx_copybutton",
    "sphinx_design",
]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**.ipynb_checkpoints"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "friendly"

smartquotes = True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "furo"

html_title = project
html_logo = "_static/img/resonant.png"
html_favicon = "_static/img/favicon.png"
html_extra_path = [
    "../CNAME",
]

html_theme_options = {
    "footer_icons": [
        {
            "name": "Kitware",
            "url": "https://kitware.com/",
            "html": "Kitware",
            "class": "",
        },
        {
            "name": "Resonant",
            "url": "https://github.com/kitware-resonant",
            "html": "Resonant",
            "class": "",
        },
    ],
}

# Copy button customization
# exclude traditional Python prompts from the copied code
copybutton_prompt_text = r">>> ?|\.\.\. "
copybutton_prompt_is_regexp = True

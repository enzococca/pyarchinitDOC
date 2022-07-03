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

import os
import sys
sys.path.insert(0, os.path.abspath('../code/'))

# -- Project information -----------------------------------------------------

project = 'pyArchInit 4.0'
copyright = '2021, AdArte srl'
author = 'Enzo Cocca & Luca Mandolesi'

# The full version, including alpha/beta/rc tags
release = '4'
# The master toctree document.
master_doc = 'index'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
# Add the extension
extensions = [
   'sphinx.ext.autosectionlabel','sphinxcontrib.video','sphinx.ext.autosummary','sphinx.ext.autodoc', 'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.napoleon',]

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = True
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True

# Make sure the target is unique
autosectionlabel_prefix_document = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'it'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_theme_options = {

    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}
html_logo = '_static/pyarchinit_logo.png'
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    'papersize': 'a4paper',

    # The font size ('10pt', '11pt' or '12pt').
    'pointsize': '11pt',

    # Latex figure (float) alignment
    #'figure_align': 'htbp',

    # Don't mangle with UTF-8 chars
    'inputenc': '',
    'utf8extra': '',

    # Set document margins
    'sphinxsetup': '''
        hmargin=0.1in, vmargin=1in,
        parsedliteralwraps=true,
        verbatimhintsturnover=false,
    ''',

    # Additional stuff for the LaTeX preamble.
    'preamble': '''
	% Prevent column squeezing of tabulary.
	\\setlength{\\tymin}{20em}
        % Use some font with UTF-8 support with XeLaTeX
        \\usepackage{fontspec}
        \\setsansfont{DejaVu Sans}
        \\setromanfont{DejaVu Serif}
        \\setmonofont{DejaVu Sans Mono}
     ''',
}
latex_documents = [
    (master_doc, 'versione_01.tex', u'versione\\_01 Documentation',
     u'abc', 'manual'),]
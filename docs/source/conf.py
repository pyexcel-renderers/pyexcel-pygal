# -*- coding: utf-8 -*-
import os
import sys
sys.path.append(os.path.abspath('.'))
DESCRIPTION = (
    'draw simple svg chart via pygal' +
    ''
)
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosummary',
    'sphinxcontrib.excel',
    'sphinxcontrib.spelling',
    'pyexcel_sphinx_integration'
]

intersphinx_mapping = {
    'pyexcel': ('http://pyexcel.readthedocs.io/en/latest/', None),
}
spelling_word_list_filename = 'spelling_wordlist.txt'
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

project = u'pyexcel-pygal'
copyright = u'2015-2017 Onni Software Ltd.'
version = '0.0.2'
release = '0.0.2'
exclude_patterns = []
pygments_style = 'sphinx'
html_theme = 'default'


def setup(app):
    app.add_stylesheet('theme_overrides.css')


html_static_path = ['_static']
htmlhelp_basename = 'pyexcel-pygaldoc'
latex_elements = {}
latex_documents = [
    ('index', 'pyexcel-pygal.tex',
     'pyexcel-pygal Documentation',
     'Onni Software Ltd.', 'manual'),
]
man_pages = [
    ('index', 'pyexcel-pygal',
     'pyexcel-pygal Documentation',
     [u'Onni Software Ltd.'], 1)
]
texinfo_documents = [
    ('index', 'pyexcel-pygal',
     'pyexcel-pygal Documentation',
     'Onni Software Ltd.', 'pyexcel-pygal',
     DESCRIPTION,
     'Miscellaneous'),
]

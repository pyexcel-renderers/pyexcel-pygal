# -*- coding: utf-8 -*-
import os
import sys
sys.path.append(os.path.abspath('.'))
DESCRIPTION = (
    'A wrapper library of pygal to visualize pyexcel data' +
    ''
)
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'pyexcel_sphinx_integration'
]

intersphinx_mapping = {
    'pyexcel': ('http://pyexcel.readthedocs.org/en/latest/', None),
}
spelling_word_list_filename = 'spelling_wordlist.txt'
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

project = u'pyexcel-chart'
copyright = u'2015-2017 Onni Software Ltd.'
version = '0.0.1'
release = '0.0.1'
exclude_patterns = []
pygments_style = 'sphinx'
html_theme = 'default'
html_static_path = ['_static']
htmlhelp_basename = 'pyexcel-chartdoc'
latex_elements = {}
latex_documents = [
    ('index', 'pyexcel-chart.tex',
     'pyexcel-chart Documentation',
     'Onni Software Ltd.', 'manual'),
]
man_pages = [
    ('index', 'pyexcel-chart',
     'pyexcel-chart Documentation',
     [u'Onni Software Ltd.'], 1)
]
texinfo_documents = [
    ('index', 'pyexcel-chart',
     'pyexcel-chart Documentation',
     'Onni Software Ltd.', 'pyexcel-chart',
     DESCRIPTION,
     'Miscellaneous'),
]

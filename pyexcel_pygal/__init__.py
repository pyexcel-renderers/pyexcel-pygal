"""
    pyexcel_chart
    ~~~~~~~~~~~~~~~~~~~

    chart drawing plugin for pyexcel

    :copyright: (c) 2016-2017 by Onni Software Ltd.
    :license: New BSD License, see LICENSE for further details
"""
from pyexcel.plugins import PyexcelPluginChain


PyexcelPluginChain(__name__).add_a_renderer(
    relative_plugin_class_path='chart.ChartRenderer',
    file_types=['svg']
)

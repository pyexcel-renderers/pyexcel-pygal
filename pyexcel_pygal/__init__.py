from pyexcel.internal.common import ChartPluginChain


ChartPluginChain(__name__).add_a_plugin(
    submodule='chart.SimpleLayout',
    tags=['pie', 'box']
).add_a_plugin(
    submodule='chart.ComplexLayout',
    tags=['line', 'bar', 'stacked_bar', 'radar', 'dot', 'funnel']
).add_a_plugin(
    submodule='chart.Histogram',
    tags=['histogram']
).add_a_plugin(
    submodule='chart.XY',
    tags=['xy']
)

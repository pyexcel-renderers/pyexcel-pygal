Charts
================================================================================

.. testcode::
   :hide:

   >>> import sys
   >>> PY2 = sys.version_info[0] == 2
   >>> PY26 = PY2 and sys.version_info[1] < 7
   >>> 
   >>> if PY26:
   ...     from ordereddict import OrderedDict
   ... else:
   ...     from collections import OrderedDict



Line
--------------------------------------------------------------------------------

.. image:: _static/line.svg
   :width: 600px
   :height: 400px
		   
Here is the source code using pyexcel::

    >>> import pyexcel as pe
    >>> title = 'Browser usage evolution (in %)'
    >>> x_labels = map(str, range(2002, 2013))
    >>> data = {
    ...     'Firefox': [None, None,    0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1],
    ...     'Chrome': [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3],
    ...     'IE': [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1],
    ...     'Others':  [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5]
    ... }
    >>> pe.save_as(
    ...     adict=data,
    ...     dest_title=title,
    ...     dest_x_labels=x_labels,
    ...     dest_chart_type='line',
    ...     dest_file_name='line.svg'
    ... )


Here is the source code `using pygal.Line directly <http://pygal.org/en/stable/documentation/types/line.html#basic>`_


Histogram
--------------------------------------------------------------------------------

.. image:: _static/histogram.svg
   :width: 600px
   :height: 400px
		   
Here is the source code using pyexcel::

    >>> import pyexcel as pe
    >>> data = {
    ...     'Wide bars': [(5, 0, 10), (4, 5, 13), (2, 0, 15)],
    ...     'Narrow bars':  [(10, 1, 2), (12, 4, 4.5), (8, 11, 13)]
    ... }
    >>> pe.save_book_as(
    ...     bookdict=data,
    ...     dest_chart_type='histogram',
    ...     dest_file_name='histogram.svg'
    ... )


Here is the source code `using pygal.Histogram directly <http://pygal.org/en/stable/documentation/types/histogram.html#basic>`_

XY
--------------------------------------------------------------------------------

BASIC
********************************************************************************

Basic XY Lines, drawing cosinus:

.. image:: _static/xy_cosinus.svg
   :width: 600px
   :height: 400px
		   
Here is the source code using pyexcel::

    >>> import pyexcel as pe
    >>> from math import cos
    >>> data = {
    ...     'x = cos(y)': [(cos(x / 10.), x / 10.) for x in range(-50, 50, 5)],
    ...     'y = cos(x)': [(x / 10., cos(x / 10.)) for x in range(-50, 50, 5)],
    ...     'x = 1':  [(1, -5), (1, 5)],
    ...     'x = -1': [(-1, -5), (-1, 5)],
    ...     'y = 1':  [(-5, 1), (5, 1)],
    ...     'y = -1': [(-5, -1), (5, -1)]
    ... }
    >>> pe.save_book_as(
    ...     bookdict=data,
    ...     dest_chart_type='xy',
    ...     dest_title='XY Cosinus',
    ...     dest_file_name='xy_cosinus.svg'
    ... )



Here is the source code `using pygal <http://pygal.org/en/stable/documentation/types/xy.html#basic>`_



Pie chart
--------------------------------------------------------------------------------


.. image:: _static/pie.svg
   :width: 600px
   :height: 400px
		   
Here is the source code using pyexcel::

    >>> title = 'Browser usage in February 2012 (in %)'
    >>> data = OrderedDict()
    >>> data['IE']=[19.5]
    >>> data['Firefox']=[36.6]
    >>> data['Chrome']=[36.3]
    >>> data['Safari']=[4.5]  
    >>> data['Opera']=[2.3]
    >>> pe.save_as(
    ...     adict=data,
    ...     dest_title=title,
    ...     dest_chart_type='pie',
    ...     dest_file_name='pie.svg'
    ... )

Here is the source code `using pygal.Pie directly <http://pygal.org/en/stable/documentation/types/pie.html#basic>`_


Radar chart
--------------------------------------------------------------------------------

.. image:: _static/radar.svg
   :width: 600px
   :height: 400px
		   
Here is the source code using pyexcel::

    >>> title = 'V8 benchmark results'
    >>> x_labels = ['Richards', 'DeltaBlue', 'Crypto', 'RayTrace', 'EarleyBoyer', 'RegExp', 'Splay', 'NavierStokes']
    >>> data = {
    ...     'Chrome': [6395, 8212, 7520, 7218, 12464, 1660, 2123, 8607],
    ...     'Firefox': [7473, 8099, 11700, 2651, 6361, 1044, 3797, 9450],
    ...     'Opera': [3472, 2933, 4203, 5229, 5810, 1828, 9013, 4669],
    ...     'IE': [43, 41, 59, 79, 144, 136, 34, 102],
    ... }
    >>> pe.save_as(
    ...     adict=data,
    ...     dest_x_labels=x_labels,
    ...     dest_title=title,
    ...     dest_chart_type='radar',
    ...     dest_file_name='radar.svg'
    ... )

Here is the source code `using pygal.Radar directly <http://pygal.org/en/stable/documentation/types/radar.html#basic>`_
 

Box chart
--------------------------------------------------------------------------------

.. image:: _static/box.svg
   :width: 600px
   :height: 400px
		   
Here is the source code using pyexcel::

    >>> title = 'V8 benchmark results'
    >>> data = OrderedDict()
    >>> data['Chrome'] = [6395, 8212, 7520, 7218, 12464, 1660, 2123, 8607] 
    >>> data['Firefox'] = [7473, 8099, 11700, 2651, 6361, 1044, 3797, 9450]
    >>> data['Opera'] = [3472, 2933, 4203, 5229, 5810, 1828, 9013, 4669]
    >>> data['IE'] = [43, 41, 59, 79, 144, 136, 34, 102]
    >>> pe.save_as(
    ...     adict=data,
    ...     dest_title=title,
    ...     dest_chart_type='box',
    ...     dest_file_name='box.svg'
    ... )

Here is the source code `using pygal.Box directly <http://pygal.org/en/stable/documentation/types/box.html#basic>`_



Dot chart
--------------------------------------------------------------------------------

.. image:: _static/dot.svg
   :width: 600px
   :height: 400px
		   
Here is the source code using pyexcel::

    >>> title = 'V8 benchmark results'
    >>> data = OrderedDict()
	>>> data['x labels'] = ['Richards', 'DeltaBlue', 'Crypto', 'RayTrace', 'EarleyBoyer', 'RegExp', 'Splay', 'NavierStokes']
    >>> data['Chrome'] = [6395, 8212, 7520, 7218, 12464, 1660, 2123, 8607] 
    >>> data['Firefox'] = [7473, 8099, 11700, 2651, 6361, 1044, 3797, 9450]
    >>> data['Opera'] = [3472, 2933, 4203, 5229, 5810, 1828, 9013, 4669]
    >>> data['IE'] = [43, 41, 59, 79, 144, 136, 34, 102]
    >>> pe.save_as(
    ...     adict=data,
    ...     dest_title=title,
    ...     dest_chart_type='dot',
    ...     dest_file_name='dot.svg',
    ...     dest_x_label_rotation=30
    ... )

Here is the source code `using pygal.Dot directly <http://pygal.org/en/stable/documentation/types/dot.html#basic>`_


Funnel chart
--------------------------------------------------------------------------------

.. image:: _static/funnel.svg
   :width: 600px
   :height: 400px
		   
Here is the source code using pyexcel::

    >>> title = 'V8 benchmark results'
    >>> data = OrderedDict()
    >>> data['x labels'] = ['Richards', 'DeltaBlue', 'Crypto', 'RayTrace', 'EarleyBoyer', 'RegExp', 'Splay', 'NavierStokes']
    >>> data['Chrome'] = [6395, 8212, 7520, 7218, 12464, 1660, 2123, 8607] 
    >>> data['Firefox'] = [7473, 8099, 11700, 2651, 6361, 1044, 3797, 9450]
    >>> data['Opera'] = [3472, 2933, 4203, 5229, 5810, 1828, 9013, 4669]
    >>> pe.save_as(
    ...     adict=data,
    ...     dest_title=title,
    ...     dest_chart_type='funnel',
    ...     dest_file_name='funnel.svg'
    ... )

Here is the source code `using pygal.Funnel directly <http://pygal.org/en/stable/documentation/types/funnel.html#basic>`_




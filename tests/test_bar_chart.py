import os
import sys
import pyexcel as pe
from filecmp import cmp
PY2 = sys.version_info[0] == 2
PY26 = PY2 and sys.version_info[1] < 7

if PY26:
    from ordereddict import OrderedDict
else:
    from collections import OrderedDict


def test_line_chart():
    title = 'Browser usage evolution (in %)'
    x_labels = map(str, range(2002, 2013))
    data = {
        'Firefox': [None, None, 0, 16.6, 25, 31, 36.4, 45.5, 46.3, 42.8, 37.1],
        'Chrome': [None, None, None, None, None, None, 0, 3.9, 10.8, 23.8, 35.3],
        'IE': [85.8, 84.6, 84.7, 74.5, 66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1],
        'Others': [14.2, 15.4, 15.3, 8.9, 9, 10.4, 8.9, 5.8, 6.7, 6.8, 7.5]
    }
    pe.save_as(
        adict=data,
        dest_title=title,
        dest_x_labels=x_labels,
        dest_chart_type='line',
        dest_file_name='line.svg',
        dest_no_prefix=True
    )
    _validate_and_remove('line.svg')


def test_histogram():
    data = {
        'Wide bars': [(5, 0, 10), (4, 5, 13), (2, 0, 15)],
        'Narrow bars':  [(10, 1, 2), (12, 4, 4.5), (8, 11, 13)]
    }
    pe.save_book_as(
        bookdict=data,
        dest_chart_type='histogram',
        dest_file_name='histogram.svg',
        dest_no_prefix=True
    )
    _validate_and_remove('histogram.svg')


def test_xy_lines():
    from math import cos
    data = {
        'x = cos(y)': [(cos(x / 10.), x / 10.) for x in range(-50, 50, 5)],
        'y = cos(x)': [(x / 10., cos(x / 10.)) for x in range(-50, 50, 5)],
        'x = 1':  [(1, -5), (1, 5)],
        'x = -1': [(-1, -5), (-1, 5)],
        'y = 1':  [(-5, 1), (5, 1)],
        'y = -1': [(-5, -1), (5, -1)]
    }
    pe.save_book_as(
        bookdict=data,
        dest_chart_type='xy',
        dest_title='XY Cosinus',
        dest_file_name='xy_cosinus.svg',
        dest_no_prefix=True
    )
    _validate_and_remove('xy_cosinus.svg')


def test_pie():
    title = 'Browser usage in February 2012 (in %)'
    data = OrderedDict()
    data['IE'] = [19.5]
    data['Firefox'] = [36.6]
    data['Chrome'] = [36.3]
    data['Safari'] = [4.5]
    data['Opera'] = [2.3]
    pe.save_as(
        adict=data,
        dest_title=title,
        dest_chart_type='pie',
        dest_file_name='pie.svg',
        dest_no_prefix=True
    )
    _validate_and_remove('pie.svg')


def test_radar():
    title = 'V8 benchmark results'
    x_labels = [
        'Richards', 'DeltaBlue', 'Crypto', 'RayTrace',
        'EarleyBoyer', 'RegExp', 'Splay', 'NavierStokes']
    data = {
        'Chrome': [6395, 8212, 7520, 7218, 12464, 1660, 2123, 8607],
        'Firefox': [7473, 8099, 11700, 2651, 6361, 1044, 3797, 9450],
        'Opera': [3472, 2933, 4203, 5229, 5810, 1828, 9013, 4669],
        'IE': [43, 41, 59, 79, 144, 136, 34, 102],
    }
    pe.save_as(
        adict=data,
        dest_x_labels=x_labels,
        dest_title=title,
        dest_chart_type='radar',
        dest_file_name='radar.svg',
        dest_no_prefix=True
    )
    _validate_and_remove('radar.svg')


def test_box():
    title = 'V8 benchmark results'
    data = OrderedDict()
    data['Chrome'] = [6395, 8212, 7520, 7218, 12464, 1660, 2123, 8607]
    data['Firefox'] = [7473, 8099, 11700, 2651, 6361, 1044, 3797, 9450]
    data['Opera'] = [3472, 2933, 4203, 5229, 5810, 1828, 9013, 4669]
    data['IE'] = [43, 41, 59, 79, 144, 136, 34, 102]
    pe.save_as(
        adict=data,
        dest_title=title,
        dest_chart_type='box',
        dest_file_name='box.svg',
        dest_no_prefix=True
    )
    _validate_and_remove('box.svg')


def test_dot():
    title = 'V8 benchmark results'
    data = OrderedDict()
    data['x labels'] = [
        'Richards', 'DeltaBlue', 'Crypto',
        'RayTrace', 'EarleyBoyer', 'RegExp',
        'Splay', 'NavierStokes']
    data['Chrome'] = [6395, 8212, 7520, 7218, 12464, 1660, 2123, 8607]
    data['Firefox'] = [7473, 8099, 11700, 2651, 6361, 1044, 3797, 9450]
    data['Opera'] = [3472, 2933, 4203, 5229, 5810, 1828, 9013, 4669]
    data['IE'] = [43, 41, 59, 79, 144, 136, 34, 102]
    pe.save_as(
        adict=data,
        dest_title=title,
        dest_chart_type='dot',
        dest_file_name='dot.svg',
        dest_x_label_rotation=30,
        dest_no_prefix=True
    )
    _validate_and_remove('dot.svg')


def test_funnel():
    title = 'V8 benchmark results'
    data = OrderedDict()
    data['x labels'] = [
        'Richards', 'DeltaBlue', 'Crypto',
        'RayTrace', 'EarleyBoyer', 'RegExp',
        'Splay', 'NavierStokes']
    data['Chrome'] = [6395, 8212, 7520, 7218, 12464, 1660, 2123, 8607]
    data['Firefox'] = [7473, 8099, 11700, 2651, 6361, 1044, 3797, 9450]
    data['Opera'] = [3472, 2933, 4203, 5229, 5810, 1828, 9013, 4669]
    pe.save_as(
        adict=data,
        dest_title=title,
        dest_chart_type='funnel',
        dest_file_name='funnel.svg',
        dest_no_prefix=True
    )
    _validate_and_remove('funnel.svg')


def _validate_and_remove(file_name):
    status = cmp(file_name, _fixture_file(file_name))
    assert status is True
    os.unlink(file_name)


def _fixture_file(file_name):
    return os.path.join("tests", "fixtures", file_name)

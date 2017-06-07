import os
import pyexcel as pe


def test_bar_chart():
    data = [['a', 'b'], [1, 2]]
    pe.save_as(array=data, dest_file_name='test.bar.svg')
    os.unlink('test.bar.svg')


def test_chart_parameters():
    data = [
        ["x", "y", "z"],
        [1, 2, 3],
        [1, 2, 13]
    ]
    x_labels = [2011, 2012]
    pe.save_as(
        array=data,
        dest_chart_type="bar",
        dest_file_name="y.svg",
        dest_x_labels=x_labels
    )
    os.unlink('y.svg')

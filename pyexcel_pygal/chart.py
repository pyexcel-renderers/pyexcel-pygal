import pygal


DEFAULT_TITLE = 'pyexcel chart rendered by pygal'
KEYWORD_CHART_TYPE = 'chart_type'
DEFAULT_CHART_TYPE = 'bar'
CHART_TYPES = dict(
    pie='Pie',
    box='Box',
    line='Line',
    bar='Bar',
    stacked_bar='StackedBar',
    radar='Radar',
    dot='Dot',
    funnel='Funnel',
    xy='XY',
    histogram='Histogram')


class Chart(object):

    def __init__(self, cls_name):
        self._chart_class = CHART_TYPES.get(cls_name, 'line')


class SimpleLayout(Chart):

    def render_sheet(self, sheet, title=DEFAULT_TITLE,
                     label_y_in_row=0,
                     **keywords):
        params = {}
        self.params = {}
        if len(sheet.colnames) == 0:
            sheet.name_columns_by_row(label_y_in_row)
        params.update(keywords)
        the_dict = sheet.to_dict()
        cls = getattr(pygal, self._chart_class)
        instance = cls(title=title, **params)
        for key in the_dict:
            data_array = [value for value in the_dict[key] if value != '']
            instance.add(key, data_array)
        chart_content = instance.render()
        return chart_content


class ComplexLayout(Chart):

    def render_sheet(self, sheet, title=DEFAULT_TITLE,
                     label_x_in_column=0, label_y_in_row=0,
                     **keywords):
        params = {}
        self.params = {}
        if len(sheet.colnames) == 0:
            sheet.name_columns_by_row(label_y_in_row)
        if len(sheet.rownames) == 0:
            sheet.name_rows_by_column(label_x_in_column)
        params['x_labels'] = sheet.rownames
        params.update(keywords)
        the_dict = sheet.to_dict()
        cls = getattr(pygal, self._chart_class)
        instance = cls(title=title, **params)
        for key in the_dict:
            data_array = [value for value in the_dict[key] if value != '']
            instance.add(key, data_array)
        chart_content = instance.render()
        return chart_content


class Histogram(Chart):
    def render_sheet(self, sheet, title=DEFAULT_TITLE,
                     height_in_column=0, start_in_column=1,
                     stop_in_column=2,
                     **keywords):
        histograms = zip(sheet.column[height_in_column],
                         sheet.column[start_in_column],
                         sheet.column[stop_in_column])
        cls = getattr(pygal, self._chart_class)
        instance = cls(title=title, **keywords)
        instance.add(sheet.name, histograms)
        chart_content = instance.render()
        return chart_content

    def render_book(self, book, title=DEFAULT_TITLE,
                    height_in_column=0, start_in_column=1,
                    stop_in_column=2,
                    **keywords):
        from pyexcel.book import to_book
        cls = getattr(pygal, self._chart_class)
        instance = cls(title=title, **keywords)
        for sheet in to_book(book):
            histograms = zip(sheet.column[height_in_column],
                             sheet.column[start_in_column],
                             sheet.column[stop_in_column])
            instance.add(sheet.name, histograms)
        chart_content = instance.render()
        return chart_content


class XY(Chart):

    def render_sheet(self, sheet, title=DEFAULT_TITLE,
                     x_in_column=0,
                     y_in_column=1,
                     **keywords):
        cls = getattr(pygal, self._chart_class)
        instance = cls(title=title, **keywords)
        points = zip(sheet.column[x_in_column],
                     sheet.column[y_in_column])
        instance.add(sheet.name, points)
        chart_content = instance.render()
        return chart_content

    def render_book(self, book, title=DEFAULT_TITLE,
                    x_in_column=0,
                    y_in_column=1,
                    **keywords):
        from pyexcel.book import to_book
        cls = getattr(pygal, self._chart_class)
        instance = cls(title=title, **keywords)
        for sheet in to_book(book):
            points = zip(sheet.column[x_in_column],
                         sheet.column[y_in_column])
            instance.add(sheet.name, points)
        chart_content = instance.render()
        return chart_content

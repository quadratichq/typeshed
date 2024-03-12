"""
This type stub file was generated by pyright.
"""

from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType

class Header(_BaseTraceHierarchyType):
    _parent_path_str = ...
    _path_str = ...
    _valid_props = ...
    @property
    def align(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the horizontal alignment of the `text` within the box. Has
        an effect only if `text` spans two or more lines (i.e. `text`
        contains one or more <br> HTML tags) or if an explicit width is
        set to override the text width.

        The 'align' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['left', 'center', 'right']
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        Any|numpy.ndarray
        """
        ...
    
    @align.setter
    def align(self, val): # -> None:
        ...
    
    @property
    def alignsrc(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the source reference on Chart Studio Cloud for `align`.

        The 'alignsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        ...
    
    @alignsrc.setter
    def alignsrc(self, val): # -> None:
        ...
    
    @property
    def fill(self): # -> tuple[Any, ...] | Self | None:
        """
        The 'fill' property is an instance of Fill
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.table.header.Fill`
          - A dict of string/value properties that will be passed
            to the Fill constructor

            Supported dict properties:

                color
                    Sets the cell fill color. It accepts either a
                    specific color or an array of colors or a 2D
                    array of colors.
                colorsrc
                    Sets the source reference on Chart Studio Cloud
                    for `color`.

        Returns
        -------
        plotly.graph_objs.table.header.Fill
        """
        ...
    
    @fill.setter
    def fill(self, val): # -> None:
        ...
    
    @property
    def font(self): # -> tuple[Any, ...] | Self | None:
        """
        The 'font' property is an instance of Font
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.table.header.Font`
          - A dict of string/value properties that will be passed
            to the Font constructor

            Supported dict properties:

                color

                colorsrc
                    Sets the source reference on Chart Studio Cloud
                    for `color`.
                family
                    HTML font family - the typeface that will be
                    applied by the web browser. The web browser
                    will only be able to apply a font if it is
                    available on the system which it operates.
                    Provide multiple font families, separated by
                    commas, to indicate the preference in which to
                    apply fonts if they aren't available on the
                    system. The Chart Studio Cloud (at
                    https://chart-studio.plotly.com or on-premise)
                    generates images on a server, where only a
                    select number of fonts are installed and
                    supported. These include "Arial", "Balto",
                    "Courier New", "Droid Sans",, "Droid Serif",
                    "Droid Sans Mono", "Gravitas One", "Old
                    Standard TT", "Open Sans", "Overpass", "PT Sans
                    Narrow", "Raleway", "Times New Roman".
                familysrc
                    Sets the source reference on Chart Studio Cloud
                    for `family`.
                size

                sizesrc
                    Sets the source reference on Chart Studio Cloud
                    for `size`.

        Returns
        -------
        plotly.graph_objs.table.header.Font
        """
        ...
    
    @font.setter
    def font(self, val): # -> None:
        ...
    
    @property
    def format(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the cell value formatting rule using d3 formatting mini-
        languages which are very similar to those in Python. For
        numbers, see:
        https://github.com/d3/d3-format/tree/v1.4.5#d3-format.

        The 'format' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        ...
    
    @format.setter
    def format(self, val): # -> None:
        ...
    
    @property
    def formatsrc(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the source reference on Chart Studio Cloud for `format`.

        The 'formatsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        ...
    
    @formatsrc.setter
    def formatsrc(self, val): # -> None:
        ...
    
    @property
    def height(self): # -> tuple[Any, ...] | Self | None:
        """
        The height of cells.

        The 'height' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        ...
    
    @height.setter
    def height(self, val): # -> None:
        ...
    
    @property
    def line(self): # -> tuple[Any, ...] | Self | None:
        """
        The 'line' property is an instance of Line
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.table.header.Line`
          - A dict of string/value properties that will be passed
            to the Line constructor

            Supported dict properties:

                color

                colorsrc
                    Sets the source reference on Chart Studio Cloud
                    for `color`.
                width

                widthsrc
                    Sets the source reference on Chart Studio Cloud
                    for `width`.

        Returns
        -------
        plotly.graph_objs.table.header.Line
        """
        ...
    
    @line.setter
    def line(self, val): # -> None:
        ...
    
    @property
    def prefix(self): # -> tuple[Any, ...] | Self | None:
        """
        Prefix for cell values.

        The 'prefix' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        str|numpy.ndarray
        """
        ...
    
    @prefix.setter
    def prefix(self, val): # -> None:
        ...
    
    @property
    def prefixsrc(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the source reference on Chart Studio Cloud for `prefix`.

        The 'prefixsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        ...
    
    @prefixsrc.setter
    def prefixsrc(self, val): # -> None:
        ...
    
    @property
    def suffix(self): # -> tuple[Any, ...] | Self | None:
        """
        Suffix for cell values.

        The 'suffix' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        str|numpy.ndarray
        """
        ...
    
    @suffix.setter
    def suffix(self, val): # -> None:
        ...
    
    @property
    def suffixsrc(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the source reference on Chart Studio Cloud for `suffix`.

        The 'suffixsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        ...
    
    @suffixsrc.setter
    def suffixsrc(self, val): # -> None:
        ...
    
    @property
    def values(self): # -> tuple[Any, ...] | Self | None:
        """
        Header cell values. `values[m][n]` represents the value of the
        `n`th point in column `m`, therefore the `values[m]` vector
        length for all columns must be the same (longer vectors will be
        truncated). Each value must be a finite number or a string.

        The 'values' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        ...
    
    @values.setter
    def values(self, val): # -> None:
        ...
    
    @property
    def valuessrc(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the source reference on Chart Studio Cloud for `values`.

        The 'valuessrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        ...
    
    @valuessrc.setter
    def valuessrc(self, val): # -> None:
        ...
    
    def __init__(self, arg=..., align=..., alignsrc=..., fill=..., font=..., format=..., formatsrc=..., height=..., line=..., prefix=..., prefixsrc=..., suffix=..., suffixsrc=..., values=..., valuessrc=..., **kwargs) -> None:
        """
        Construct a new Header object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.table.Header`
        align
            Sets the horizontal alignment of the `text` within the
            box. Has an effect only if `text` spans two or more
            lines (i.e. `text` contains one or more <br> HTML tags)
            or if an explicit width is set to override the text
            width.
        alignsrc
            Sets the source reference on Chart Studio Cloud for
            `align`.
        fill
            :class:`plotly.graph_objects.table.header.Fill`
            instance or dict with compatible properties
        font
            :class:`plotly.graph_objects.table.header.Font`
            instance or dict with compatible properties
        format
            Sets the cell value formatting rule using d3 formatting
            mini-languages which are very similar to those in
            Python. For numbers, see:
            https://github.com/d3/d3-format/tree/v1.4.5#d3-format.
        formatsrc
            Sets the source reference on Chart Studio Cloud for
            `format`.
        height
            The height of cells.
        line
            :class:`plotly.graph_objects.table.header.Line`
            instance or dict with compatible properties
        prefix
            Prefix for cell values.
        prefixsrc
            Sets the source reference on Chart Studio Cloud for
            `prefix`.
        suffix
            Suffix for cell values.
        suffixsrc
            Sets the source reference on Chart Studio Cloud for
            `suffix`.
        values
            Header cell values. `values[m][n]` represents the value
            of the `n`th point in column `m`, therefore the
            `values[m]` vector length for all columns must be the
            same (longer vectors will be truncated). Each value
            must be a finite number or a string.
        valuessrc
            Sets the source reference on Chart Studio Cloud for
            `values`.

        Returns
        -------
        Header
        """
        ...
    



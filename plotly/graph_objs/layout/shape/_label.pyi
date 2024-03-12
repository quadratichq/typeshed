"""
This type stub file was generated by pyright.
"""

from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType

class Label(_BaseLayoutHierarchyType):
    _parent_path_str = ...
    _path_str = ...
    _valid_props = ...
    @property
    def font(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the shape label text font.

        The 'font' property is an instance of Font
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.shape.label.Font`
          - A dict of string/value properties that will be passed
            to the Font constructor

            Supported dict properties:

                color

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
                size

        Returns
        -------
        plotly.graph_objs.layout.shape.label.Font
        """
        ...
    
    @font.setter
    def font(self, val): # -> None:
        ...
    
    @property
    def padding(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets padding (in px) between edge of label and edge of shape.

        The 'padding' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        ...
    
    @padding.setter
    def padding(self, val): # -> None:
        ...
    
    @property
    def text(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the text to display with shape. It is also used for legend
        item if `name` is not provided.

        The 'text' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        ...
    
    @text.setter
    def text(self, val): # -> None:
        ...
    
    @property
    def textangle(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the angle at which the label text is drawn with respect to
        the horizontal. For lines, angle "auto" is the same angle as
        the line. For all other shapes, angle "auto" is horizontal.

        The 'textangle' property is a angle (in degrees) that may be
        specified as a number between -180 and 180.
        Numeric values outside this range are converted to the equivalent value
        (e.g. 270 is converted to -90).

        Returns
        -------
        int|float
        """
        ...
    
    @textangle.setter
    def textangle(self, val): # -> None:
        ...
    
    @property
    def textposition(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the position of the label text relative to the shape.
        Supported values for rectangles, circles and paths are *top
        left*, *top center*, *top right*, *middle left*, *middle
        center*, *middle right*, *bottom left*, *bottom center*, and
        *bottom right*. Supported values for lines are "start",
        "middle", and "end". Default: *middle center* for rectangles,
        circles, and paths; "middle" for lines.

        The 'textposition' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['top left', 'top center', 'top right', 'middle left',
                'middle center', 'middle right', 'bottom left', 'bottom
                center', 'bottom right', 'start', 'middle', 'end']

        Returns
        -------
        Any
        """
        ...
    
    @textposition.setter
    def textposition(self, val): # -> None:
        ...
    
    @property
    def texttemplate(self): # -> tuple[Any, ...] | Self | None:
        """
        Template string used for rendering the shape's label. Note that
        this will override `text`. Variables are inserted using
        %{variable}, for example "x0: %{x0}". Numbers are formatted
        using d3-format's syntax %{variable:d3-format}, for example
        "Price: %{x0:$.2f}". See
        https://github.com/d3/d3-format/tree/v1.4.5#d3-format for
        details on the formatting syntax. Dates are formatted using
        d3-time-format's syntax %{variable|d3-time-format}, for example
        "Day: %{x0|%m %b %Y}". See https://github.com/d3/d3-time-
        format/tree/v2.2.3#locale_format for details on the date
        formatting syntax. A single multiplication or division
        operation may be applied to numeric variables, and combined
        with d3 number formatting, for example "Length in cm:
        %{x0*2.54}", "%{slope*60:.1f} meters per second." For log axes,
        variable values are given in log units. For date axes, x/y
        coordinate variables and center variables use datetimes, while
        all other variable values use values in ms. Finally, the
        template string has access to variables `x0`, `x1`, `y0`, `y1`,
        `slope`, `dx`, `dy`, `width`, `height`, `length`, `xcenter` and
        `ycenter`.

        The 'texttemplate' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        ...
    
    @texttemplate.setter
    def texttemplate(self, val): # -> None:
        ...
    
    @property
    def xanchor(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the label's horizontal position anchor This anchor binds
        the specified `textposition` to the "left", "center" or "right"
        of the label text. For example, if `textposition` is set to
        *top right* and `xanchor` to "right" then the right-most
        portion of the label text lines up with the right-most edge of
        the shape.

        The 'xanchor' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['auto', 'left', 'center', 'right']

        Returns
        -------
        Any
        """
        ...
    
    @xanchor.setter
    def xanchor(self, val): # -> None:
        ...
    
    @property
    def yanchor(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the label's vertical position anchor This anchor binds the
        specified `textposition` to the "top", "middle" or "bottom" of
        the label text. For example, if `textposition` is set to *top
        right* and `yanchor` to "top" then the top-most portion of the
        label text lines up with the top-most edge of the shape.

        The 'yanchor' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['top', 'middle', 'bottom']

        Returns
        -------
        Any
        """
        ...
    
    @yanchor.setter
    def yanchor(self, val): # -> None:
        ...
    
    def __init__(self, arg=..., font=..., padding=..., text=..., textangle=..., textposition=..., texttemplate=..., xanchor=..., yanchor=..., **kwargs) -> None:
        """
        Construct a new Label object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.layout.shape.Label`
        font
            Sets the shape label text font.
        padding
            Sets padding (in px) between edge of label and edge of
            shape.
        text
            Sets the text to display with shape. It is also used
            for legend item if `name` is not provided.
        textangle
            Sets the angle at which the label text is drawn with
            respect to the horizontal. For lines, angle "auto" is
            the same angle as the line. For all other shapes, angle
            "auto" is horizontal.
        textposition
            Sets the position of the label text relative to the
            shape. Supported values for rectangles, circles and
            paths are *top left*, *top center*, *top right*,
            *middle left*, *middle center*, *middle right*, *bottom
            left*, *bottom center*, and *bottom right*. Supported
            values for lines are "start", "middle", and "end".
            Default: *middle center* for rectangles, circles, and
            paths; "middle" for lines.
        texttemplate
            Template string used for rendering the shape's label.
            Note that this will override `text`. Variables are
            inserted using %{variable}, for example "x0: %{x0}".
            Numbers are formatted using d3-format's syntax
            %{variable:d3-format}, for example "Price: %{x0:$.2f}".
            See
            https://github.com/d3/d3-format/tree/v1.4.5#d3-format
            for details on the formatting syntax. Dates are
            formatted using d3-time-format's syntax
            %{variable|d3-time-format}, for example "Day: %{x0|%m
            %b %Y}". See https://github.com/d3/d3-time-
            format/tree/v2.2.3#locale_format for details on the
            date formatting syntax. A single multiplication or
            division operation may be applied to numeric variables,
            and combined with d3 number formatting, for example
            "Length in cm: %{x0*2.54}", "%{slope*60:.1f} meters per
            second." For log axes, variable values are given in log
            units. For date axes, x/y coordinate variables and
            center variables use datetimes, while all other
            variable values use values in ms. Finally, the template
            string has access to variables `x0`, `x1`, `y0`, `y1`,
            `slope`, `dx`, `dy`, `width`, `height`, `length`,
            `xcenter` and `ycenter`.
        xanchor
            Sets the label's horizontal position anchor This anchor
            binds the specified `textposition` to the "left",
            "center" or "right" of the label text. For example, if
            `textposition` is set to *top right* and `xanchor` to
            "right" then the right-most portion of the label text
            lines up with the right-most edge of the shape.
        yanchor
            Sets the label's vertical position anchor This anchor
            binds the specified `textposition` to the "top",
            "middle" or "bottom" of the label text. For example, if
            `textposition` is set to *top right* and `yanchor` to
            "top" then the top-most portion of the label text lines
            up with the top-most edge of the shape.

        Returns
        -------
        Label
        """
        ...
    



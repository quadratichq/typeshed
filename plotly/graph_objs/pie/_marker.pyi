"""
This type stub file was generated by pyright.
"""

from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType

class Marker(_BaseTraceHierarchyType):
    _parent_path_str = ...
    _path_str = ...
    _valid_props = ...
    @property
    def colors(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the color of each sector. If not specified, the default
        trace color set is used to pick the sector colors.

        The 'colors' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        ...
    
    @colors.setter
    def colors(self, val): # -> None:
        ...
    
    @property
    def colorssrc(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the source reference on Chart Studio Cloud for `colors`.

        The 'colorssrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        ...
    
    @colorssrc.setter
    def colorssrc(self, val): # -> None:
        ...
    
    @property
    def line(self): # -> tuple[Any, ...] | Self | None:
        """
        The 'line' property is an instance of Line
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.pie.marker.Line`
          - A dict of string/value properties that will be passed
            to the Line constructor

            Supported dict properties:

                color
                    Sets the color of the line enclosing each
                    sector.
                colorsrc
                    Sets the source reference on Chart Studio Cloud
                    for `color`.
                width
                    Sets the width (in px) of the line enclosing
                    each sector.
                widthsrc
                    Sets the source reference on Chart Studio Cloud
                    for `width`.

        Returns
        -------
        plotly.graph_objs.pie.marker.Line
        """
        ...
    
    @line.setter
    def line(self, val): # -> None:
        ...
    
    @property
    def pattern(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the pattern within the marker.

        The 'pattern' property is an instance of Pattern
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.pie.marker.Pattern`
          - A dict of string/value properties that will be passed
            to the Pattern constructor

            Supported dict properties:

                bgcolor
                    When there is no colorscale sets the color of
                    background pattern fill. Defaults to a
                    `marker.color` background when `fillmode` is
                    "overlay". Otherwise, defaults to a transparent
                    background.
                bgcolorsrc
                    Sets the source reference on Chart Studio Cloud
                    for `bgcolor`.
                fgcolor
                    When there is no colorscale sets the color of
                    foreground pattern fill. Defaults to a
                    `marker.color` background when `fillmode` is
                    "replace". Otherwise, defaults to dark grey or
                    white to increase contrast with the `bgcolor`.
                fgcolorsrc
                    Sets the source reference on Chart Studio Cloud
                    for `fgcolor`.
                fgopacity
                    Sets the opacity of the foreground pattern
                    fill. Defaults to a 0.5 when `fillmode` is
                    "overlay". Otherwise, defaults to 1.
                fillmode
                    Determines whether `marker.color` should be
                    used as a default to `bgcolor` or a `fgcolor`.
                shape
                    Sets the shape of the pattern fill. By default,
                    no pattern is used for filling the area.
                shapesrc
                    Sets the source reference on Chart Studio Cloud
                    for `shape`.
                size
                    Sets the size of unit squares of the pattern
                    fill in pixels, which corresponds to the
                    interval of repetition of the pattern.
                sizesrc
                    Sets the source reference on Chart Studio Cloud
                    for `size`.
                solidity
                    Sets the solidity of the pattern fill. Solidity
                    is roughly the fraction of the area filled by
                    the pattern. Solidity of 0 shows only the
                    background color without pattern and solidty of
                    1 shows only the foreground color without
                    pattern.
                soliditysrc
                    Sets the source reference on Chart Studio Cloud
                    for `solidity`.

        Returns
        -------
        plotly.graph_objs.pie.marker.Pattern
        """
        ...
    
    @pattern.setter
    def pattern(self, val): # -> None:
        ...
    
    def __init__(self, arg=..., colors=..., colorssrc=..., line=..., pattern=..., **kwargs) -> None:
        """
        Construct a new Marker object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.pie.Marker`
        colors
            Sets the color of each sector. If not specified, the
            default trace color set is used to pick the sector
            colors.
        colorssrc
            Sets the source reference on Chart Studio Cloud for
            `colors`.
        line
            :class:`plotly.graph_objects.pie.marker.Line` instance
            or dict with compatible properties
        pattern
            Sets the pattern within the marker.

        Returns
        -------
        Marker
        """
        ...
    



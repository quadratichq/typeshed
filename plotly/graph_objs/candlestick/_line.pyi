"""
This type stub file was generated by pyright.
"""

from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType

class Line(_BaseTraceHierarchyType):
    _parent_path_str = ...
    _path_str = ...
    _valid_props = ...
    @property
    def width(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the width (in px) of line bounding the box(es). Note that
        this style setting can also be set per direction via
        `increasing.line.width` and `decreasing.line.width`.

        The 'width' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        ...
    
    @width.setter
    def width(self, val): # -> None:
        ...
    
    def __init__(self, arg=..., width=..., **kwargs) -> None:
        """
        Construct a new Line object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.candlestick.Line`
        width
            Sets the width (in px) of line bounding the box(es).
            Note that this style setting can also be set per
            direction via `increasing.line.width` and
            `decreasing.line.width`.

        Returns
        -------
        Line
        """
        ...
    



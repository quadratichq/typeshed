"""
This type stub file was generated by pyright.
"""

from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType

class X(_BaseTraceHierarchyType):
    _parent_path_str = ...
    _path_str = ...
    _valid_props = ...
    @property
    def fill(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the fill ratio of the `slices`. The default fill value of
        the `slices` is 1 meaning that they are entirely shaded. On the
        other hand Applying a `fill` ratio less than one would allow
        the creation of openings parallel to the edges.

        The 'fill' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        ...
    
    @fill.setter
    def fill(self, val): # -> None:
        ...
    
    @property
    def locations(self): # -> tuple[Any, ...] | Self | None:
        """
        Specifies the location(s) of slices on the axis. When not
        specified slices would be created for all points of the axis x
        except start and end.

        The 'locations' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        ...
    
    @locations.setter
    def locations(self, val): # -> None:
        ...
    
    @property
    def locationssrc(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the source reference on Chart Studio Cloud for
        `locations`.

        The 'locationssrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        ...
    
    @locationssrc.setter
    def locationssrc(self, val): # -> None:
        ...
    
    @property
    def show(self): # -> tuple[Any, ...] | Self | None:
        """
        Determines whether or not slice planes about the x dimension
        are drawn.

        The 'show' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        ...
    
    @show.setter
    def show(self, val): # -> None:
        ...
    
    def __init__(self, arg=..., fill=..., locations=..., locationssrc=..., show=..., **kwargs) -> None:
        """
        Construct a new X object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.isosurface.slices.X`
        fill
            Sets the fill ratio of the `slices`. The default fill
            value of the `slices` is 1 meaning that they are
            entirely shaded. On the other hand Applying a `fill`
            ratio less than one would allow the creation of
            openings parallel to the edges.
        locations
            Specifies the location(s) of slices on the axis. When
            not specified slices would be created for all points of
            the axis x except start and end.
        locationssrc
            Sets the source reference on Chart Studio Cloud for
            `locations`.
        show
            Determines whether or not slice planes about the x
            dimension are drawn.

        Returns
        -------
        X
        """
        ...
    


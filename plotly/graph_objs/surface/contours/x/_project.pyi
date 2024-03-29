"""
This type stub file was generated by pyright.
"""

from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType

class Project(_BaseTraceHierarchyType):
    _parent_path_str = ...
    _path_str = ...
    _valid_props = ...
    @property
    def x(self): # -> tuple[Any, ...] | Self | None:
        """
        Determines whether or not these contour lines are projected on
        the x plane. If `highlight` is set to True (the default), the
        projected lines are shown on hover. If `show` is set to True,
        the projected lines are shown in permanence.

        The 'x' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        ...
    
    @x.setter
    def x(self, val): # -> None:
        ...
    
    @property
    def y(self): # -> tuple[Any, ...] | Self | None:
        """
        Determines whether or not these contour lines are projected on
        the y plane. If `highlight` is set to True (the default), the
        projected lines are shown on hover. If `show` is set to True,
        the projected lines are shown in permanence.

        The 'y' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        ...
    
    @y.setter
    def y(self, val): # -> None:
        ...
    
    @property
    def z(self): # -> tuple[Any, ...] | Self | None:
        """
        Determines whether or not these contour lines are projected on
        the z plane. If `highlight` is set to True (the default), the
        projected lines are shown on hover. If `show` is set to True,
        the projected lines are shown in permanence.

        The 'z' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        ...
    
    @z.setter
    def z(self, val): # -> None:
        ...
    
    def __init__(self, arg=..., x=..., y=..., z=..., **kwargs) -> None:
        """
        Construct a new Project object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.surface.contours.x.Project`
        x
            Determines whether or not these contour lines are
            projected on the x plane. If `highlight` is set to True
            (the default), the projected lines are shown on hover.
            If `show` is set to True, the projected lines are shown
            in permanence.
        y
            Determines whether or not these contour lines are
            projected on the y plane. If `highlight` is set to True
            (the default), the projected lines are shown on hover.
            If `show` is set to True, the projected lines are shown
            in permanence.
        z
            Determines whether or not these contour lines are
            projected on the z plane. If `highlight` is set to True
            (the default), the projected lines are shown on hover.
            If `show` is set to True, the projected lines are shown
            in permanence.

        Returns
        -------
        Project
        """
        ...
    



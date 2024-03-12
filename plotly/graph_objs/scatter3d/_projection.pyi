"""
This type stub file was generated by pyright.
"""

from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType

class Projection(_BaseTraceHierarchyType):
    _parent_path_str = ...
    _path_str = ...
    _valid_props = ...
    @property
    def x(self): # -> tuple[Any, ...] | Self | None:
        """
        The 'x' property is an instance of X
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.scatter3d.projection.X`
          - A dict of string/value properties that will be passed
            to the X constructor

            Supported dict properties:

                opacity
                    Sets the projection color.
                scale
                    Sets the scale factor determining the size of
                    the projection marker points.
                show
                    Sets whether or not projections are shown along
                    the x axis.

        Returns
        -------
        plotly.graph_objs.scatter3d.projection.X
        """
        ...
    
    @x.setter
    def x(self, val): # -> None:
        ...
    
    @property
    def y(self): # -> tuple[Any, ...] | Self | None:
        """
        The 'y' property is an instance of Y
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.scatter3d.projection.Y`
          - A dict of string/value properties that will be passed
            to the Y constructor

            Supported dict properties:

                opacity
                    Sets the projection color.
                scale
                    Sets the scale factor determining the size of
                    the projection marker points.
                show
                    Sets whether or not projections are shown along
                    the y axis.

        Returns
        -------
        plotly.graph_objs.scatter3d.projection.Y
        """
        ...
    
    @y.setter
    def y(self, val): # -> None:
        ...
    
    @property
    def z(self): # -> tuple[Any, ...] | Self | None:
        """
        The 'z' property is an instance of Z
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.scatter3d.projection.Z`
          - A dict of string/value properties that will be passed
            to the Z constructor

            Supported dict properties:

                opacity
                    Sets the projection color.
                scale
                    Sets the scale factor determining the size of
                    the projection marker points.
                show
                    Sets whether or not projections are shown along
                    the z axis.

        Returns
        -------
        plotly.graph_objs.scatter3d.projection.Z
        """
        ...
    
    @z.setter
    def z(self, val): # -> None:
        ...
    
    def __init__(self, arg=..., x=..., y=..., z=..., **kwargs) -> None:
        """
        Construct a new Projection object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.scatter3d.Projection`
        x
            :class:`plotly.graph_objects.scatter3d.projection.X`
            instance or dict with compatible properties
        y
            :class:`plotly.graph_objects.scatter3d.projection.Y`
            instance or dict with compatible properties
        z
            :class:`plotly.graph_objects.scatter3d.projection.Z`
            instance or dict with compatible properties

        Returns
        -------
        Projection
        """
        ...
    


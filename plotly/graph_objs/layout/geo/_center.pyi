"""
This type stub file was generated by pyright.
"""

from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType

class Center(_BaseLayoutHierarchyType):
    _parent_path_str = ...
    _path_str = ...
    _valid_props = ...
    @property
    def lat(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the latitude of the map's center. For all projection
        types, the map's latitude center lies at the middle of the
        latitude range by default.

        The 'lat' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        ...
    
    @lat.setter
    def lat(self, val): # -> None:
        ...
    
    @property
    def lon(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the longitude of the map's center. By default, the map's
        longitude center lies at the middle of the longitude range for
        scoped projection and above `projection.rotation.lon`
        otherwise.

        The 'lon' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        ...
    
    @lon.setter
    def lon(self, val): # -> None:
        ...
    
    def __init__(self, arg=..., lat=..., lon=..., **kwargs) -> None:
        """
        Construct a new Center object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.layout.geo.Center`
        lat
            Sets the latitude of the map's center. For all
            projection types, the map's latitude center lies at the
            middle of the latitude range by default.
        lon
            Sets the longitude of the map's center. By default, the
            map's longitude center lies at the middle of the
            longitude range for scoped projection and above
            `projection.rotation.lon` otherwise.

        Returns
        -------
        Center
        """
        ...
    



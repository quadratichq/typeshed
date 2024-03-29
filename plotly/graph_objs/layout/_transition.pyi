"""
This type stub file was generated by pyright.
"""

from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType

class Transition(_BaseLayoutHierarchyType):
    _parent_path_str = ...
    _path_str = ...
    _valid_props = ...
    @property
    def duration(self): # -> tuple[Any, ...] | Self | None:
        """
        The duration of the transition, in milliseconds. If equal to
        zero, updates are synchronous.

        The 'duration' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        ...
    
    @duration.setter
    def duration(self, val): # -> None:
        ...
    
    @property
    def easing(self): # -> tuple[Any, ...] | Self | None:
        """
        The easing function used for the transition

        The 'easing' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['linear', 'quad', 'cubic', 'sin', 'exp', 'circle',
                'elastic', 'back', 'bounce', 'linear-in', 'quad-in',
                'cubic-in', 'sin-in', 'exp-in', 'circle-in', 'elastic-in',
                'back-in', 'bounce-in', 'linear-out', 'quad-out',
                'cubic-out', 'sin-out', 'exp-out', 'circle-out',
                'elastic-out', 'back-out', 'bounce-out', 'linear-in-out',
                'quad-in-out', 'cubic-in-out', 'sin-in-out', 'exp-in-out',
                'circle-in-out', 'elastic-in-out', 'back-in-out',
                'bounce-in-out']

        Returns
        -------
        Any
        """
        ...
    
    @easing.setter
    def easing(self, val): # -> None:
        ...
    
    @property
    def ordering(self): # -> tuple[Any, ...] | Self | None:
        """
        Determines whether the figure's layout or traces smoothly
        transitions during updates that make both traces and layout
        change.

        The 'ordering' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['layout first', 'traces first']

        Returns
        -------
        Any
        """
        ...
    
    @ordering.setter
    def ordering(self, val): # -> None:
        ...
    
    def __init__(self, arg=..., duration=..., easing=..., ordering=..., **kwargs) -> None:
        """
        Construct a new Transition object

        Sets transition options used during Plotly.react updates.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.layout.Transition`
        duration
            The duration of the transition, in milliseconds. If
            equal to zero, updates are synchronous.
        easing
            The easing function used for the transition
        ordering
            Determines whether the figure's layout or traces
            smoothly transitions during updates that make both
            traces and layout change.

        Returns
        -------
        Transition
        """
        ...
    



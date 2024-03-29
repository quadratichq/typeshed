"""
This type stub file was generated by pyright.
"""

from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType

class Line(_BaseTraceHierarchyType):
    _parent_path_str = ...
    _path_str = ...
    _valid_props = ...
    @property
    def backoff(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the line back off from the end point of the nth line
        segment (in px). This option is useful e.g. to avoid overlap
        with arrowhead markers. With "auto" the lines would trim before
        markers if `marker.angleref` is set to "previous".

        The 'backoff' property is a number and may be specified as:
          - An int or float in the interval [0, inf]
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        int|float|numpy.ndarray
        """
        ...
    
    @backoff.setter
    def backoff(self, val): # -> None:
        ...
    
    @property
    def backoffsrc(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the source reference on Chart Studio Cloud for `backoff`.

        The 'backoffsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        ...
    
    @backoffsrc.setter
    def backoffsrc(self, val): # -> None:
        ...
    
    @property
    def color(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the line color.

        The 'color' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color:
                aliceblue, antiquewhite, aqua, aquamarine, azure,
                beige, bisque, black, blanchedalmond, blue,
                blueviolet, brown, burlywood, cadetblue,
                chartreuse, chocolate, coral, cornflowerblue,
                cornsilk, crimson, cyan, darkblue, darkcyan,
                darkgoldenrod, darkgray, darkgrey, darkgreen,
                darkkhaki, darkmagenta, darkolivegreen, darkorange,
                darkorchid, darkred, darksalmon, darkseagreen,
                darkslateblue, darkslategray, darkslategrey,
                darkturquoise, darkviolet, deeppink, deepskyblue,
                dimgray, dimgrey, dodgerblue, firebrick,
                floralwhite, forestgreen, fuchsia, gainsboro,
                ghostwhite, gold, goldenrod, gray, grey, green,
                greenyellow, honeydew, hotpink, indianred, indigo,
                ivory, khaki, lavender, lavenderblush, lawngreen,
                lemonchiffon, lightblue, lightcoral, lightcyan,
                lightgoldenrodyellow, lightgray, lightgrey,
                lightgreen, lightpink, lightsalmon, lightseagreen,
                lightskyblue, lightslategray, lightslategrey,
                lightsteelblue, lightyellow, lime, limegreen,
                linen, magenta, maroon, mediumaquamarine,
                mediumblue, mediumorchid, mediumpurple,
                mediumseagreen, mediumslateblue, mediumspringgreen,
                mediumturquoise, mediumvioletred, midnightblue,
                mintcream, mistyrose, moccasin, navajowhite, navy,
                oldlace, olive, olivedrab, orange, orangered,
                orchid, palegoldenrod, palegreen, paleturquoise,
                palevioletred, papayawhip, peachpuff, peru, pink,
                plum, powderblue, purple, red, rosybrown,
                royalblue, rebeccapurple, saddlebrown, salmon,
                sandybrown, seagreen, seashell, sienna, silver,
                skyblue, slateblue, slategray, slategrey, snow,
                springgreen, steelblue, tan, teal, thistle, tomato,
                turquoise, violet, wheat, white, whitesmoke,
                yellow, yellowgreen

        Returns
        -------
        str
        """
        ...
    
    @color.setter
    def color(self, val): # -> None:
        ...
    
    @property
    def dash(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the dash style of lines. Set to a dash type string
        ("solid", "dot", "dash", "longdash", "dashdot", or
        "longdashdot") or a dash length list in px (eg
        "5px,10px,2px,2px").

        The 'dash' property is an enumeration that may be specified as:
          - One of the following dash styles:
                ['solid', 'dot', 'dash', 'longdash', 'dashdot', 'longdashdot']
          - A string containing a dash length list in pixels or percentages
                (e.g. '5px 10px 2px 2px', '5, 10, 2, 2', '10% 20% 40%', etc.)

        Returns
        -------
        str
        """
        ...
    
    @dash.setter
    def dash(self, val): # -> None:
        ...
    
    @property
    def shape(self): # -> tuple[Any, ...] | Self | None:
        """
        Determines the line shape. With "spline" the lines are drawn
        using spline interpolation. The other available values
        correspond to step-wise line shapes.

        The 'shape' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['linear', 'spline']

        Returns
        -------
        Any
        """
        ...
    
    @shape.setter
    def shape(self, val): # -> None:
        ...
    
    @property
    def smoothing(self): # -> tuple[Any, ...] | Self | None:
        """
        Has an effect only if `shape` is set to "spline" Sets the
        amount of smoothing. 0 corresponds to no smoothing (equivalent
        to a "linear" shape).

        The 'smoothing' property is a number and may be specified as:
          - An int or float in the interval [0, 1.3]

        Returns
        -------
        int|float
        """
        ...
    
    @smoothing.setter
    def smoothing(self, val): # -> None:
        ...
    
    @property
    def width(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the line width (in px).

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
    
    def __init__(self, arg=..., backoff=..., backoffsrc=..., color=..., dash=..., shape=..., smoothing=..., width=..., **kwargs) -> None:
        """
        Construct a new Line object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.scatterpolar.Line`
        backoff
            Sets the line back off from the end point of the nth
            line segment (in px). This option is useful e.g. to
            avoid overlap with arrowhead markers. With "auto" the
            lines would trim before markers if `marker.angleref` is
            set to "previous".
        backoffsrc
            Sets the source reference on Chart Studio Cloud for
            `backoff`.
        color
            Sets the line color.
        dash
            Sets the dash style of lines. Set to a dash type string
            ("solid", "dot", "dash", "longdash", "dashdot", or
            "longdashdot") or a dash length list in px (eg
            "5px,10px,2px,2px").
        shape
            Determines the line shape. With "spline" the lines are
            drawn using spline interpolation. The other available
            values correspond to step-wise line shapes.
        smoothing
            Has an effect only if `shape` is set to "spline" Sets
            the amount of smoothing. 0 corresponds to no smoothing
            (equivalent to a "linear" shape).
        width
            Sets the line width (in px).

        Returns
        -------
        Line
        """
        ...
    



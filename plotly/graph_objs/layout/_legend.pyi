"""
This type stub file was generated by pyright.
"""

from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType

class Legend(_BaseLayoutHierarchyType):
    _parent_path_str = ...
    _path_str = ...
    _valid_props = ...
    @property
    def bgcolor(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the legend background color. Defaults to
        `layout.paper_bgcolor`.

        The 'bgcolor' property is a color and may be specified as:
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
    
    @bgcolor.setter
    def bgcolor(self, val): # -> None:
        ...
    
    @property
    def bordercolor(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the color of the border enclosing the legend.

        The 'bordercolor' property is a color and may be specified as:
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
    
    @bordercolor.setter
    def bordercolor(self, val): # -> None:
        ...
    
    @property
    def borderwidth(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the width (in px) of the border enclosing the legend.

        The 'borderwidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        ...
    
    @borderwidth.setter
    def borderwidth(self, val): # -> None:
        ...
    
    @property
    def entrywidth(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the width (in px or fraction) of the legend. Use 0 to size
        the entry based on the text width, when `entrywidthmode` is set
        to "pixels".

        The 'entrywidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        ...
    
    @entrywidth.setter
    def entrywidth(self, val): # -> None:
        ...
    
    @property
    def entrywidthmode(self): # -> tuple[Any, ...] | Self | None:
        """
        Determines what entrywidth means.

        The 'entrywidthmode' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['fraction', 'pixels']

        Returns
        -------
        Any
        """
        ...
    
    @entrywidthmode.setter
    def entrywidthmode(self, val): # -> None:
        ...
    
    @property
    def font(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the font used to text the legend items.

        The 'font' property is an instance of Font
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.legend.Font`
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
        plotly.graph_objs.layout.legend.Font
        """
        ...
    
    @font.setter
    def font(self, val): # -> None:
        ...
    
    @property
    def groupclick(self): # -> tuple[Any, ...] | Self | None:
        """
        Determines the behavior on legend group item click.
        "toggleitem" toggles the visibility of the individual item
        clicked on the graph. "togglegroup" toggles the visibility of
        all items in the same legendgroup as the item clicked on the
        graph.

        The 'groupclick' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['toggleitem', 'togglegroup']

        Returns
        -------
        Any
        """
        ...
    
    @groupclick.setter
    def groupclick(self, val): # -> None:
        ...
    
    @property
    def grouptitlefont(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the font for group titles in legend. Defaults to
        `legend.font` with its size increased about 10%.

        The 'grouptitlefont' property is an instance of Grouptitlefont
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.legend.Grouptitlefont`
          - A dict of string/value properties that will be passed
            to the Grouptitlefont constructor

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
        plotly.graph_objs.layout.legend.Grouptitlefont
        """
        ...
    
    @grouptitlefont.setter
    def grouptitlefont(self, val): # -> None:
        ...
    
    @property
    def itemclick(self): # -> tuple[Any, ...] | Self | None:
        """
        Determines the behavior on legend item click. "toggle" toggles
        the visibility of the item clicked on the graph. "toggleothers"
        makes the clicked item the sole visible item on the graph.
        False disables legend item click interactions.

        The 'itemclick' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['toggle', 'toggleothers', False]

        Returns
        -------
        Any
        """
        ...
    
    @itemclick.setter
    def itemclick(self, val): # -> None:
        ...
    
    @property
    def itemdoubleclick(self): # -> tuple[Any, ...] | Self | None:
        """
        Determines the behavior on legend item double-click. "toggle"
        toggles the visibility of the item clicked on the graph.
        "toggleothers" makes the clicked item the sole visible item on
        the graph. False disables legend item double-click
        interactions.

        The 'itemdoubleclick' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['toggle', 'toggleothers', False]

        Returns
        -------
        Any
        """
        ...
    
    @itemdoubleclick.setter
    def itemdoubleclick(self, val): # -> None:
        ...
    
    @property
    def itemsizing(self): # -> tuple[Any, ...] | Self | None:
        """
        Determines if the legend items symbols scale with their
        corresponding "trace" attributes or remain "constant"
        independent of the symbol size on the graph.

        The 'itemsizing' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['trace', 'constant']

        Returns
        -------
        Any
        """
        ...
    
    @itemsizing.setter
    def itemsizing(self, val): # -> None:
        ...
    
    @property
    def itemwidth(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the width (in px) of the legend item symbols (the part
        other than the title.text).

        The 'itemwidth' property is a number and may be specified as:
          - An int or float in the interval [30, inf]

        Returns
        -------
        int|float
        """
        ...
    
    @itemwidth.setter
    def itemwidth(self, val): # -> None:
        ...
    
    @property
    def orientation(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the orientation of the legend.

        The 'orientation' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['v', 'h']

        Returns
        -------
        Any
        """
        ...
    
    @orientation.setter
    def orientation(self, val): # -> None:
        ...
    
    @property
    def title(self): # -> tuple[Any, ...] | Self | None:
        """
        The 'title' property is an instance of Title
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.legend.Title`
          - A dict of string/value properties that will be passed
            to the Title constructor

            Supported dict properties:

                font
                    Sets this legend's title font. Defaults to
                    `legend.font` with its size increased about
                    20%.
                side
                    Determines the location of legend's title with
                    respect to the legend items. Defaulted to "top"
                    with `orientation` is "h". Defaulted to "left"
                    with `orientation` is "v". The *top left*
                    options could be used to expand top center and
                    top right are for horizontal alignment legend
                    area in both x and y sides.
                text
                    Sets the title of the legend.

        Returns
        -------
        plotly.graph_objs.layout.legend.Title
        """
        ...
    
    @title.setter
    def title(self, val): # -> None:
        ...
    
    @property
    def tracegroupgap(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the amount of vertical space (in px) between legend
        groups.

        The 'tracegroupgap' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        ...
    
    @tracegroupgap.setter
    def tracegroupgap(self, val): # -> None:
        ...
    
    @property
    def traceorder(self): # -> tuple[Any, ...] | Self | None:
        """
        Determines the order at which the legend items are displayed.
        If "normal", the items are displayed top-to-bottom in the same
        order as the input data. If "reversed", the items are displayed
        in the opposite order as "normal". If "grouped", the items are
        displayed in groups (when a trace `legendgroup` is provided).
        if "grouped+reversed", the items are displayed in the opposite
        order as "grouped".

        The 'traceorder' property is a flaglist and may be specified
        as a string containing:
          - Any combination of ['reversed', 'grouped'] joined with '+' characters
            (e.g. 'reversed+grouped')
            OR exactly one of ['normal'] (e.g. 'normal')

        Returns
        -------
        Any
        """
        ...
    
    @traceorder.setter
    def traceorder(self, val): # -> None:
        ...
    
    @property
    def uirevision(self): # -> tuple[Any, ...] | Self | None:
        """
        Controls persistence of legend-driven changes in trace and pie
        label visibility. Defaults to `layout.uirevision`.

        The 'uirevision' property accepts values of any type

        Returns
        -------
        Any
        """
        ...
    
    @uirevision.setter
    def uirevision(self, val): # -> None:
        ...
    
    @property
    def valign(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the vertical alignment of the symbols with respect to
        their associated text.

        The 'valign' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['top', 'middle', 'bottom']

        Returns
        -------
        Any
        """
        ...
    
    @valign.setter
    def valign(self, val): # -> None:
        ...
    
    @property
    def visible(self): # -> tuple[Any, ...] | Self | None:
        """
        Determines whether or not this legend is visible.

        The 'visible' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        ...
    
    @visible.setter
    def visible(self, val): # -> None:
        ...
    
    @property
    def x(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the x position with respect to `xref` (in normalized
        coordinates) of the legend. When `xref` is "paper", defaults to
        1.02 for vertical legends and defaults to 0 for horizontal
        legends. When `xref` is "container", defaults to 1 for vertical
        legends and defaults to 0 for horizontal legends. Must be
        between 0 and 1 if `xref` is "container". and between "-2" and
        3 if `xref` is "paper".

        The 'x' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        ...
    
    @x.setter
    def x(self, val): # -> None:
        ...
    
    @property
    def xanchor(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the legend's horizontal position anchor. This anchor binds
        the `x` position to the "left", "center" or "right" of the
        legend. Value "auto" anchors legends to the right for `x`
        values greater than or equal to 2/3, anchors legends to the
        left for `x` values less than or equal to 1/3 and anchors
        legends with respect to their center otherwise.

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
    def xref(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the container `x` refers to. "container" spans the entire
        `width` of the plot. "paper" refers to the width of the
        plotting area only.

        The 'xref' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['container', 'paper']

        Returns
        -------
        Any
        """
        ...
    
    @xref.setter
    def xref(self, val): # -> None:
        ...
    
    @property
    def y(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the y position with respect to `yref` (in normalized
        coordinates) of the legend. When `yref` is "paper", defaults to
        1 for vertical legends, defaults to "-0.1" for horizontal
        legends on graphs w/o range sliders and defaults to 1.1 for
        horizontal legends on graph with one or multiple range sliders.
        When `yref` is "container", defaults to 1. Must be between 0
        and 1 if `yref` is "container" and between "-2" and 3 if `yref`
        is "paper".

        The 'y' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        ...
    
    @y.setter
    def y(self, val): # -> None:
        ...
    
    @property
    def yanchor(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the legend's vertical position anchor This anchor binds
        the `y` position to the "top", "middle" or "bottom" of the
        legend. Value "auto" anchors legends at their bottom for `y`
        values less than or equal to 1/3, anchors legends to at their
        top for `y` values greater than or equal to 2/3 and anchors
        legends with respect to their middle otherwise.

        The 'yanchor' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['auto', 'top', 'middle', 'bottom']

        Returns
        -------
        Any
        """
        ...
    
    @yanchor.setter
    def yanchor(self, val): # -> None:
        ...
    
    @property
    def yref(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the container `y` refers to. "container" spans the entire
        `height` of the plot. "paper" refers to the height of the
        plotting area only.

        The 'yref' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['container', 'paper']

        Returns
        -------
        Any
        """
        ...
    
    @yref.setter
    def yref(self, val): # -> None:
        ...
    
    def __init__(self, arg=..., bgcolor=..., bordercolor=..., borderwidth=..., entrywidth=..., entrywidthmode=..., font=..., groupclick=..., grouptitlefont=..., itemclick=..., itemdoubleclick=..., itemsizing=..., itemwidth=..., orientation=..., title=..., tracegroupgap=..., traceorder=..., uirevision=..., valign=..., visible=..., x=..., xanchor=..., xref=..., y=..., yanchor=..., yref=..., **kwargs) -> None:
        """
        Construct a new Legend object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.layout.Legend`
        bgcolor
            Sets the legend background color. Defaults to
            `layout.paper_bgcolor`.
        bordercolor
            Sets the color of the border enclosing the legend.
        borderwidth
            Sets the width (in px) of the border enclosing the
            legend.
        entrywidth
            Sets the width (in px or fraction) of the legend. Use 0
            to size the entry based on the text width, when
            `entrywidthmode` is set to "pixels".
        entrywidthmode
            Determines what entrywidth means.
        font
            Sets the font used to text the legend items.
        groupclick
            Determines the behavior on legend group item click.
            "toggleitem" toggles the visibility of the individual
            item clicked on the graph. "togglegroup" toggles the
            visibility of all items in the same legendgroup as the
            item clicked on the graph.
        grouptitlefont
            Sets the font for group titles in legend. Defaults to
            `legend.font` with its size increased about 10%.
        itemclick
            Determines the behavior on legend item click. "toggle"
            toggles the visibility of the item clicked on the
            graph. "toggleothers" makes the clicked item the sole
            visible item on the graph. False disables legend item
            click interactions.
        itemdoubleclick
            Determines the behavior on legend item double-click.
            "toggle" toggles the visibility of the item clicked on
            the graph. "toggleothers" makes the clicked item the
            sole visible item on the graph. False disables legend
            item double-click interactions.
        itemsizing
            Determines if the legend items symbols scale with their
            corresponding "trace" attributes or remain "constant"
            independent of the symbol size on the graph.
        itemwidth
            Sets the width (in px) of the legend item symbols (the
            part other than the title.text).
        orientation
            Sets the orientation of the legend.
        title
            :class:`plotly.graph_objects.layout.legend.Title`
            instance or dict with compatible properties
        tracegroupgap
            Sets the amount of vertical space (in px) between
            legend groups.
        traceorder
            Determines the order at which the legend items are
            displayed. If "normal", the items are displayed top-to-
            bottom in the same order as the input data. If
            "reversed", the items are displayed in the opposite
            order as "normal". If "grouped", the items are
            displayed in groups (when a trace `legendgroup` is
            provided). if "grouped+reversed", the items are
            displayed in the opposite order as "grouped".
        uirevision
            Controls persistence of legend-driven changes in trace
            and pie label visibility. Defaults to
            `layout.uirevision`.
        valign
            Sets the vertical alignment of the symbols with respect
            to their associated text.
        visible
            Determines whether or not this legend is visible.
        x
            Sets the x position with respect to `xref` (in
            normalized coordinates) of the legend. When `xref` is
            "paper", defaults to 1.02 for vertical legends and
            defaults to 0 for horizontal legends. When `xref` is
            "container", defaults to 1 for vertical legends and
            defaults to 0 for horizontal legends. Must be between 0
            and 1 if `xref` is "container". and between "-2" and 3
            if `xref` is "paper".
        xanchor
            Sets the legend's horizontal position anchor. This
            anchor binds the `x` position to the "left", "center"
            or "right" of the legend. Value "auto" anchors legends
            to the right for `x` values greater than or equal to
            2/3, anchors legends to the left for `x` values less
            than or equal to 1/3 and anchors legends with respect
            to their center otherwise.
        xref
            Sets the container `x` refers to. "container" spans the
            entire `width` of the plot. "paper" refers to the width
            of the plotting area only.
        y
            Sets the y position with respect to `yref` (in
            normalized coordinates) of the legend. When `yref` is
            "paper", defaults to 1 for vertical legends, defaults
            to "-0.1" for horizontal legends on graphs w/o range
            sliders and defaults to 1.1 for horizontal legends on
            graph with one or multiple range sliders. When `yref`
            is "container", defaults to 1. Must be between 0 and 1
            if `yref` is "container" and between "-2" and 3 if
            `yref` is "paper".
        yanchor
            Sets the legend's vertical position anchor This anchor
            binds the `y` position to the "top", "middle" or
            "bottom" of the legend. Value "auto" anchors legends at
            their bottom for `y` values less than or equal to 1/3,
            anchors legends to at their top for `y` values greater
            than or equal to 2/3 and anchors legends with respect
            to their middle otherwise.
        yref
            Sets the container `y` refers to. "container" spans the
            entire `height` of the plot. "paper" refers to the
            height of the plotting area only.

        Returns
        -------
        Legend
        """
        ...
    



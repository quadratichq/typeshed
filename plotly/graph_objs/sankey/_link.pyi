"""
This type stub file was generated by pyright.
"""

from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType

class Link(_BaseTraceHierarchyType):
    _parent_path_str = ...
    _path_str = ...
    _valid_props = ...
    @property
    def arrowlen(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the length (in px) of the links arrow, if 0 no arrow will
        be drawn.

        The 'arrowlen' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        ...
    
    @arrowlen.setter
    def arrowlen(self, val): # -> None:
        ...
    
    @property
    def color(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the `link` color. It can be a single value, or an array
        for specifying color for each `link`. If `link.color` is
        omitted, then by default, a translucent grey link will be used.

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
          - A list or array of any of the above

        Returns
        -------
        str|numpy.ndarray
        """
        ...
    
    @color.setter
    def color(self, val): # -> None:
        ...
    
    @property
    def colorscales(self): # -> tuple[Any, ...] | Self | None:
        """
        The 'colorscales' property is a tuple of instances of
        Colorscale that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.sankey.link.Colorscale
          - A list or tuple of dicts of string/value properties that
            will be passed to the Colorscale constructor

            Supported dict properties:

                cmax
                    Sets the upper bound of the color domain.
                cmin
                    Sets the lower bound of the color domain.
                colorscale
                    Sets the colorscale. The colorscale must be an
                    array containing arrays mapping a normalized
                    value to an rgb, rgba, hex, hsl, hsv, or named
                    color string. At minimum, a mapping for the
                    lowest (0) and highest (1) values are required.
                    For example, `[[0, 'rgb(0,0,255)'], [1,
                    'rgb(255,0,0)']]`. To control the bounds of the
                    colorscale in color space, use `cmin` and
                    `cmax`. Alternatively, `colorscale` may be a
                    palette name string of the following list: Blac
                    kbody,Bluered,Blues,Cividis,Earth,Electric,Gree
                    ns,Greys,Hot,Jet,Picnic,Portland,Rainbow,RdBu,R
                    eds,Viridis,YlGnBu,YlOrRd.
                label
                    The label of the links to color based on their
                    concentration within a flow.
                name
                    When used in a template, named items are
                    created in the output figure in addition to any
                    items the figure already has in this array. You
                    can modify these items in the output figure by
                    making your own item with `templateitemname`
                    matching this `name` alongside your
                    modifications (including `visible: false` or
                    `enabled: false` to hide it). Has no effect
                    outside of a template.
                templateitemname
                    Used to refer to a named item in this array in
                    the template. Named items from the template
                    will be created even without a matching item in
                    the input figure, but you can modify one by
                    making an item with `templateitemname` matching
                    its `name`, alongside your modifications
                    (including `visible: false` or `enabled: false`
                    to hide it). If there is no template or no
                    matching item, this item will be hidden unless
                    you explicitly show it with `visible: true`.

        Returns
        -------
        tuple[plotly.graph_objs.sankey.link.Colorscale]
        """
        ...
    
    @colorscales.setter
    def colorscales(self, val): # -> None:
        ...
    
    @property
    def colorscaledefaults(self): # -> tuple[Any, ...] | Self | None:
        """
        When used in a template (as
        layout.template.data.sankey.link.colorscaledefaults), sets the
        default property values to use for elements of
        sankey.link.colorscales

        The 'colorscaledefaults' property is an instance of Colorscale
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.sankey.link.Colorscale`
          - A dict of string/value properties that will be passed
            to the Colorscale constructor

            Supported dict properties:

        Returns
        -------
        plotly.graph_objs.sankey.link.Colorscale
        """
        ...
    
    @colorscaledefaults.setter
    def colorscaledefaults(self, val): # -> None:
        ...
    
    @property
    def colorsrc(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the source reference on Chart Studio Cloud for `color`.

        The 'colorsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        ...
    
    @colorsrc.setter
    def colorsrc(self, val): # -> None:
        ...
    
    @property
    def customdata(self): # -> tuple[Any, ...] | Self | None:
        """
        Assigns extra data to each link.

        The 'customdata' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        ...
    
    @customdata.setter
    def customdata(self, val): # -> None:
        ...
    
    @property
    def customdatasrc(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the source reference on Chart Studio Cloud for
        `customdata`.

        The 'customdatasrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        ...
    
    @customdatasrc.setter
    def customdatasrc(self, val): # -> None:
        ...
    
    @property
    def hovercolor(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the `link` hover color. It can be a single value, or an
        array for specifying hover colors for each `link`. If
        `link.hovercolor` is omitted, then by default, links will
        become slightly more opaque when hovered over.

        The 'hovercolor' property is a color and may be specified as:
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
          - A list or array of any of the above

        Returns
        -------
        str|numpy.ndarray
        """
        ...
    
    @hovercolor.setter
    def hovercolor(self, val): # -> None:
        ...
    
    @property
    def hovercolorsrc(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the source reference on Chart Studio Cloud for
        `hovercolor`.

        The 'hovercolorsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        ...
    
    @hovercolorsrc.setter
    def hovercolorsrc(self, val): # -> None:
        ...
    
    @property
    def hoverinfo(self): # -> tuple[Any, ...] | Self | None:
        """
        Determines which trace information appear when hovering links.
        If `none` or `skip` are set, no information is displayed upon
        hovering. But, if `none` is set, click and hover events are
        still fired.

        The 'hoverinfo' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['all', 'none', 'skip']

        Returns
        -------
        Any
        """
        ...
    
    @hoverinfo.setter
    def hoverinfo(self, val): # -> None:
        ...
    
    @property
    def hoverlabel(self): # -> tuple[Any, ...] | Self | None:
        """
        The 'hoverlabel' property is an instance of Hoverlabel
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.sankey.link.Hoverlabel`
          - A dict of string/value properties that will be passed
            to the Hoverlabel constructor

            Supported dict properties:

                align
                    Sets the horizontal alignment of the text
                    content within hover label box. Has an effect
                    only if the hover label text spans more two or
                    more lines
                alignsrc
                    Sets the source reference on Chart Studio Cloud
                    for `align`.
                bgcolor
                    Sets the background color of the hover labels
                    for this trace
                bgcolorsrc
                    Sets the source reference on Chart Studio Cloud
                    for `bgcolor`.
                bordercolor
                    Sets the border color of the hover labels for
                    this trace.
                bordercolorsrc
                    Sets the source reference on Chart Studio Cloud
                    for `bordercolor`.
                font
                    Sets the font used in hover labels.
                namelength
                    Sets the default length (in number of
                    characters) of the trace name in the hover
                    labels for all traces. -1 shows the whole name
                    regardless of length. 0-3 shows the first 0-3
                    characters, and an integer >3 will show the
                    whole name if it is less than that many
                    characters, but if it is longer, will truncate
                    to `namelength - 3` characters and add an
                    ellipsis.
                namelengthsrc
                    Sets the source reference on Chart Studio Cloud
                    for `namelength`.

        Returns
        -------
        plotly.graph_objs.sankey.link.Hoverlabel
        """
        ...
    
    @hoverlabel.setter
    def hoverlabel(self, val): # -> None:
        ...
    
    @property
    def hovertemplate(self): # -> tuple[Any, ...] | Self | None:
        """
        Template string used for rendering the information that appear
        on hover box. Note that this will override `hoverinfo`.
        Variables are inserted using %{variable}, for example "y: %{y}"
        as well as %{xother}, {%_xother}, {%_xother_}, {%xother_}. When
        showing info for several points, "xother" will be added to
        those with different x positions from the first point. An
        underscore before or after "(x|y)other" will add a space on
        that side, only when this field is shown. Numbers are formatted
        using d3-format's syntax %{variable:d3-format}, for example
        "Price: %{y:$.2f}".
        https://github.com/d3/d3-format/tree/v1.4.5#d3-format for
        details on the formatting syntax. Dates are formatted using
        d3-time-format's syntax %{variable|d3-time-format}, for example
        "Day: %{2019-01-01|%A}". https://github.com/d3/d3-time-
        format/tree/v2.2.3#locale_format for details on the date
        formatting syntax. The variables available in `hovertemplate`
        are the ones emitted as event data described at this link
        https://plotly.com/javascript/plotlyjs-events/#event-data.
        Additionally, every attributes that can be specified per-point
        (the ones that are `arrayOk: true`) are available.  Variables
        `source` and `target` are node objects.Finally, the template
        string has access to variables `value` and `label`. Anything
        contained in tag `<extra>` is displayed in the secondary box,
        for example "<extra>{fullData.name}</extra>". To hide the
        secondary box completely, use an empty tag `<extra></extra>`.

        The 'hovertemplate' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        str|numpy.ndarray
        """
        ...
    
    @hovertemplate.setter
    def hovertemplate(self, val): # -> None:
        ...
    
    @property
    def hovertemplatesrc(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the source reference on Chart Studio Cloud for
        `hovertemplate`.

        The 'hovertemplatesrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        ...
    
    @hovertemplatesrc.setter
    def hovertemplatesrc(self, val): # -> None:
        ...
    
    @property
    def label(self): # -> tuple[Any, ...] | Self | None:
        """
        The shown name of the link.

        The 'label' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        ...
    
    @label.setter
    def label(self, val): # -> None:
        ...
    
    @property
    def labelsrc(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the source reference on Chart Studio Cloud for `label`.

        The 'labelsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        ...
    
    @labelsrc.setter
    def labelsrc(self, val): # -> None:
        ...
    
    @property
    def line(self): # -> tuple[Any, ...] | Self | None:
        """
        The 'line' property is an instance of Line
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.sankey.link.Line`
          - A dict of string/value properties that will be passed
            to the Line constructor

            Supported dict properties:

                color
                    Sets the color of the `line` around each
                    `link`.
                colorsrc
                    Sets the source reference on Chart Studio Cloud
                    for `color`.
                width
                    Sets the width (in px) of the `line` around
                    each `link`.
                widthsrc
                    Sets the source reference on Chart Studio Cloud
                    for `width`.

        Returns
        -------
        plotly.graph_objs.sankey.link.Line
        """
        ...
    
    @line.setter
    def line(self, val): # -> None:
        ...
    
    @property
    def source(self): # -> tuple[Any, ...] | Self | None:
        """
        An integer number `[0..nodes.length - 1]` that represents the
        source node.

        The 'source' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        ...
    
    @source.setter
    def source(self, val): # -> None:
        ...
    
    @property
    def sourcesrc(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the source reference on Chart Studio Cloud for `source`.

        The 'sourcesrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        ...
    
    @sourcesrc.setter
    def sourcesrc(self, val): # -> None:
        ...
    
    @property
    def target(self): # -> tuple[Any, ...] | Self | None:
        """
        An integer number `[0..nodes.length - 1]` that represents the
        target node.

        The 'target' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        ...
    
    @target.setter
    def target(self, val): # -> None:
        ...
    
    @property
    def targetsrc(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the source reference on Chart Studio Cloud for `target`.

        The 'targetsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        ...
    
    @targetsrc.setter
    def targetsrc(self, val): # -> None:
        ...
    
    @property
    def value(self): # -> tuple[Any, ...] | Self | None:
        """
        A numeric value representing the flow volume value.

        The 'value' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        ...
    
    @value.setter
    def value(self, val): # -> None:
        ...
    
    @property
    def valuesrc(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the source reference on Chart Studio Cloud for `value`.

        The 'valuesrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        ...
    
    @valuesrc.setter
    def valuesrc(self, val): # -> None:
        ...
    
    def __init__(self, arg=..., arrowlen=..., color=..., colorscales=..., colorscaledefaults=..., colorsrc=..., customdata=..., customdatasrc=..., hovercolor=..., hovercolorsrc=..., hoverinfo=..., hoverlabel=..., hovertemplate=..., hovertemplatesrc=..., label=..., labelsrc=..., line=..., source=..., sourcesrc=..., target=..., targetsrc=..., value=..., valuesrc=..., **kwargs) -> None:
        """
        Construct a new Link object

        The links of the Sankey plot.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.sankey.Link`
        arrowlen
            Sets the length (in px) of the links arrow, if 0 no
            arrow will be drawn.
        color
            Sets the `link` color. It can be a single value, or an
            array for specifying color for each `link`. If
            `link.color` is omitted, then by default, a translucent
            grey link will be used.
        colorscales
            A tuple of
            :class:`plotly.graph_objects.sankey.link.Colorscale`
            instances or dicts with compatible properties
        colorscaledefaults
            When used in a template (as
            layout.template.data.sankey.link.colorscaledefaults),
            sets the default property values to use for elements of
            sankey.link.colorscales
        colorsrc
            Sets the source reference on Chart Studio Cloud for
            `color`.
        customdata
            Assigns extra data to each link.
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            `customdata`.
        hovercolor
            Sets the `link` hover color. It can be a single value,
            or an array for specifying hover colors for each
            `link`. If `link.hovercolor` is omitted, then by
            default, links will become slightly more opaque when
            hovered over.
        hovercolorsrc
            Sets the source reference on Chart Studio Cloud for
            `hovercolor`.
        hoverinfo
            Determines which trace information appear when hovering
            links. If `none` or `skip` are set, no information is
            displayed upon hovering. But, if `none` is set, click
            and hover events are still fired.
        hoverlabel
            :class:`plotly.graph_objects.sankey.link.Hoverlabel`
            instance or dict with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}" as well as %{xother}, {%_xother},
            {%_xother_}, {%xother_}. When showing info for several
            points, "xother" will be added to those with different
            x positions from the first point. An underscore before
            or after "(x|y)other" will add a space on that side,
            only when this field is shown. Numbers are formatted
            using d3-format's syntax %{variable:d3-format}, for
            example "Price: %{y:$.2f}".
            https://github.com/d3/d3-format/tree/v1.4.5#d3-format
            for details on the formatting syntax. Dates are
            formatted using d3-time-format's syntax
            %{variable|d3-time-format}, for example "Day:
            %{2019-01-01|%A}". https://github.com/d3/d3-time-
            format/tree/v2.2.3#locale_format for details on the
            date formatting syntax. The variables available in
            `hovertemplate` are the ones emitted as event data
            described at this link
            https://plotly.com/javascript/plotlyjs-events/#event-
            data. Additionally, every attributes that can be
            specified per-point (the ones that are `arrayOk: true`)
            are available.  Variables `source` and `target` are
            node objects.Finally, the template string has access to
            variables `value` and `label`. Anything contained in
            tag `<extra>` is displayed in the secondary box, for
            example "<extra>{fullData.name}</extra>". To hide the
            secondary box completely, use an empty tag
            `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on Chart Studio Cloud for
            `hovertemplate`.
        label
            The shown name of the link.
        labelsrc
            Sets the source reference on Chart Studio Cloud for
            `label`.
        line
            :class:`plotly.graph_objects.sankey.link.Line` instance
            or dict with compatible properties
        source
            An integer number `[0..nodes.length - 1]` that
            represents the source node.
        sourcesrc
            Sets the source reference on Chart Studio Cloud for
            `source`.
        target
            An integer number `[0..nodes.length - 1]` that
            represents the target node.
        targetsrc
            Sets the source reference on Chart Studio Cloud for
            `target`.
        value
            A numeric value representing the flow volume value.
        valuesrc
            Sets the source reference on Chart Studio Cloud for
            `value`.

        Returns
        -------
        Link
        """
        ...
    



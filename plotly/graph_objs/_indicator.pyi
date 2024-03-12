"""
This type stub file was generated by pyright.
"""

from plotly.basedatatypes import BaseTraceType as _BaseTraceType

class Indicator(_BaseTraceType):
    _parent_path_str = ...
    _path_str = ...
    _valid_props = ...
    @property
    def align(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the horizontal alignment of the `text` within the box.
        Note that this attribute has no effect if an angular gauge is
        displayed: in this case, it is always centered

        The 'align' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['left', 'center', 'right']

        Returns
        -------
        Any
        """
        ...
    
    @align.setter
    def align(self, val): # -> None:
        ...
    
    @property
    def customdata(self): # -> tuple[Any, ...] | Self | None:
        """
        Assigns extra data each datum. This may be useful when
        listening to hover, click and selection events. Note that,
        "scatter" traces also appends customdata items in the markers
        DOM elements

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
    def delta(self): # -> tuple[Any, ...] | Self | None:
        """
        The 'delta' property is an instance of Delta
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.indicator.Delta`
          - A dict of string/value properties that will be passed
            to the Delta constructor

            Supported dict properties:

                decreasing
                    :class:`plotly.graph_objects.indicator.delta.De
                    creasing` instance or dict with compatible
                    properties
                font
                    Set the font used to display the delta
                increasing
                    :class:`plotly.graph_objects.indicator.delta.In
                    creasing` instance or dict with compatible
                    properties
                position
                    Sets the position of delta with respect to the
                    number.
                prefix
                    Sets a prefix appearing before the delta.
                reference
                    Sets the reference value to compute the delta.
                    By default, it is set to the current value.
                relative
                    Show relative change
                suffix
                    Sets a suffix appearing next to the delta.
                valueformat
                    Sets the value formatting rule using d3
                    formatting mini-languages which are very
                    similar to those in Python. For numbers, see: h
                    ttps://github.com/d3/d3-format/tree/v1.4.5#d3-
                    format.

        Returns
        -------
        plotly.graph_objs.indicator.Delta
        """
        ...
    
    @delta.setter
    def delta(self, val): # -> None:
        ...
    
    @property
    def domain(self): # -> tuple[Any, ...] | Self | None:
        """
        The 'domain' property is an instance of Domain
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.indicator.Domain`
          - A dict of string/value properties that will be passed
            to the Domain constructor

            Supported dict properties:

                column
                    If there is a layout grid, use the domain for
                    this column in the grid for this indicator
                    trace .
                row
                    If there is a layout grid, use the domain for
                    this row in the grid for this indicator trace .
                x
                    Sets the horizontal domain of this indicator
                    trace (in plot fraction).
                y
                    Sets the vertical domain of this indicator
                    trace (in plot fraction).

        Returns
        -------
        plotly.graph_objs.indicator.Domain
        """
        ...
    
    @domain.setter
    def domain(self, val): # -> None:
        ...
    
    @property
    def gauge(self): # -> tuple[Any, ...] | Self | None:
        """
        The gauge of the Indicator plot.

        The 'gauge' property is an instance of Gauge
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.indicator.Gauge`
          - A dict of string/value properties that will be passed
            to the Gauge constructor

            Supported dict properties:

                axis
                    :class:`plotly.graph_objects.indicator.gauge.Ax
                    is` instance or dict with compatible properties
                bar
                    Set the appearance of the gauge's value
                bgcolor
                    Sets the gauge background color.
                bordercolor
                    Sets the color of the border enclosing the
                    gauge.
                borderwidth
                    Sets the width (in px) of the border enclosing
                    the gauge.
                shape
                    Set the shape of the gauge
                steps
                    A tuple of :class:`plotly.graph_objects.indicat
                    or.gauge.Step` instances or dicts with
                    compatible properties
                stepdefaults
                    When used in a template (as layout.template.dat
                    a.indicator.gauge.stepdefaults), sets the
                    default property values to use for elements of
                    indicator.gauge.steps
                threshold
                    :class:`plotly.graph_objects.indicator.gauge.Th
                    reshold` instance or dict with compatible
                    properties

        Returns
        -------
        plotly.graph_objs.indicator.Gauge
        """
        ...
    
    @gauge.setter
    def gauge(self, val): # -> None:
        ...
    
    @property
    def ids(self): # -> tuple[Any, ...] | Self | None:
        """
        Assigns id labels to each datum. These ids for object constancy
        of data points during animation. Should be an array of strings,
        not numbers or any other type.

        The 'ids' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        ...
    
    @ids.setter
    def ids(self, val): # -> None:
        ...
    
    @property
    def idssrc(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the source reference on Chart Studio Cloud for `ids`.

        The 'idssrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        ...
    
    @idssrc.setter
    def idssrc(self, val): # -> None:
        ...
    
    @property
    def legend(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the reference to a legend to show this trace in.
        References to these legends are "legend", "legend2", "legend3",
        etc. Settings for these legends are set in the layout, under
        `layout.legend`, `layout.legend2`, etc.

        The 'legend' property is an identifier of a particular
        subplot, of type 'legend', that may be specified as the string 'legend'
        optionally followed by an integer >= 1
        (e.g. 'legend', 'legend1', 'legend2', 'legend3', etc.)

        Returns
        -------
        str
        """
        ...
    
    @legend.setter
    def legend(self, val): # -> None:
        ...
    
    @property
    def legendgrouptitle(self): # -> tuple[Any, ...] | Self | None:
        """
        The 'legendgrouptitle' property is an instance of Legendgrouptitle
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.indicator.Legendgrouptitle`
          - A dict of string/value properties that will be passed
            to the Legendgrouptitle constructor

            Supported dict properties:

                font
                    Sets this legend group's title font.
                text
                    Sets the title of the legend group.

        Returns
        -------
        plotly.graph_objs.indicator.Legendgrouptitle
        """
        ...
    
    @legendgrouptitle.setter
    def legendgrouptitle(self, val): # -> None:
        ...
    
    @property
    def legendrank(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the legend rank for this trace. Items and groups with
        smaller ranks are presented on top/left side while with
        "reversed" `legend.traceorder` they are on bottom/right side.
        The default legendrank is 1000, so that you can use ranks less
        than 1000 to place certain items before all unranked items, and
        ranks greater than 1000 to go after all unranked items. When
        having unranked or equal rank items shapes would be displayed
        after traces i.e. according to their order in data and layout.

        The 'legendrank' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        ...
    
    @legendrank.setter
    def legendrank(self, val): # -> None:
        ...
    
    @property
    def legendwidth(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the width (in px or fraction) of the legend for this
        trace.

        The 'legendwidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        ...
    
    @legendwidth.setter
    def legendwidth(self, val): # -> None:
        ...
    
    @property
    def meta(self): # -> tuple[Any, ...] | Self | None:
        """
        Assigns extra meta information associated with this trace that
        can be used in various text attributes. Attributes such as
        trace `name`, graph, axis and colorbar `title.text`, annotation
        `text` `rangeselector`, `updatemenues` and `sliders` `label`
        text all support `meta`. To access the trace `meta` values in
        an attribute in the same trace, simply use `%{meta[i]}` where
        `i` is the index or key of the `meta` item in question. To
        access trace `meta` in layout attributes, use
        `%{data[n[.meta[i]}` where `i` is the index or key of the
        `meta` and `n` is the trace index.

        The 'meta' property accepts values of any type

        Returns
        -------
        Any|numpy.ndarray
        """
        ...
    
    @meta.setter
    def meta(self, val): # -> None:
        ...
    
    @property
    def metasrc(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the source reference on Chart Studio Cloud for `meta`.

        The 'metasrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        ...
    
    @metasrc.setter
    def metasrc(self, val): # -> None:
        ...
    
    @property
    def mode(self): # -> tuple[Any, ...] | Self | None:
        """
        Determines how the value is displayed on the graph. `number`
        displays the value numerically in text. `delta` displays the
        difference to a reference value in text. Finally, `gauge`
        displays the value graphically on an axis.

        The 'mode' property is a flaglist and may be specified
        as a string containing:
          - Any combination of ['number', 'delta', 'gauge'] joined with '+' characters
            (e.g. 'number+delta')

        Returns
        -------
        Any
        """
        ...
    
    @mode.setter
    def mode(self, val): # -> None:
        ...
    
    @property
    def name(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the trace name. The trace name appears as the legend item
        and on hover.

        The 'name' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        ...
    
    @name.setter
    def name(self, val): # -> None:
        ...
    
    @property
    def number(self): # -> tuple[Any, ...] | Self | None:
        """
        The 'number' property is an instance of Number
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.indicator.Number`
          - A dict of string/value properties that will be passed
            to the Number constructor

            Supported dict properties:

                font
                    Set the font used to display main number
                prefix
                    Sets a prefix appearing before the number.
                suffix
                    Sets a suffix appearing next to the number.
                valueformat
                    Sets the value formatting rule using d3
                    formatting mini-languages which are very
                    similar to those in Python. For numbers, see: h
                    ttps://github.com/d3/d3-format/tree/v1.4.5#d3-
                    format.

        Returns
        -------
        plotly.graph_objs.indicator.Number
        """
        ...
    
    @number.setter
    def number(self, val): # -> None:
        ...
    
    @property
    def stream(self): # -> tuple[Any, ...] | Self | None:
        """
        The 'stream' property is an instance of Stream
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.indicator.Stream`
          - A dict of string/value properties that will be passed
            to the Stream constructor

            Supported dict properties:

                maxpoints
                    Sets the maximum number of points to keep on
                    the plots from an incoming stream. If
                    `maxpoints` is set to 50, only the newest 50
                    points will be displayed on the plot.
                token
                    The stream id number links a data trace on a
                    plot with a stream. See https://chart-
                    studio.plotly.com/settings for more details.

        Returns
        -------
        plotly.graph_objs.indicator.Stream
        """
        ...
    
    @stream.setter
    def stream(self, val): # -> None:
        ...
    
    @property
    def title(self): # -> tuple[Any, ...] | Self | None:
        """
        The 'title' property is an instance of Title
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.indicator.Title`
          - A dict of string/value properties that will be passed
            to the Title constructor

            Supported dict properties:

                align
                    Sets the horizontal alignment of the title. It
                    defaults to `center` except for bullet charts
                    for which it defaults to right.
                font
                    Set the font used to display the title
                text
                    Sets the title of this indicator.

        Returns
        -------
        plotly.graph_objs.indicator.Title
        """
        ...
    
    @title.setter
    def title(self, val): # -> None:
        ...
    
    @property
    def uid(self): # -> tuple[Any, ...] | Self | None:
        """
        Assign an id to this trace, Use this to provide object
        constancy between traces during animations and transitions.

        The 'uid' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        ...
    
    @uid.setter
    def uid(self, val): # -> None:
        ...
    
    @property
    def uirevision(self): # -> tuple[Any, ...] | Self | None:
        """
        Controls persistence of some user-driven changes to the trace:
        `constraintrange` in `parcoords` traces, as well as some
        `editable: true` modifications such as `name` and
        `colorbar.title`. Defaults to `layout.uirevision`. Note that
        other user-driven trace attribute changes are controlled by
        `layout` attributes: `trace.visible` is controlled by
        `layout.legend.uirevision`, `selectedpoints` is controlled by
        `layout.selectionrevision`, and `colorbar.(x|y)` (accessible
        with `config: {editable: true}`) is controlled by
        `layout.editrevision`. Trace changes are tracked by `uid`,
        which only falls back on trace index if no `uid` is provided.
        So if your app can add/remove traces before the end of the
        `data` array, such that the same trace has a different index,
        you can still preserve user-driven changes if you give each
        trace a `uid` that stays with it as it moves.

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
    def value(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the number to be displayed.

        The 'value' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        ...
    
    @value.setter
    def value(self, val): # -> None:
        ...
    
    @property
    def visible(self): # -> tuple[Any, ...] | Self | None:
        """
        Determines whether or not this trace is visible. If
        "legendonly", the trace is not drawn, but can appear as a
        legend item (provided that the legend itself is visible).

        The 'visible' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                [True, False, 'legendonly']

        Returns
        -------
        Any
        """
        ...
    
    @visible.setter
    def visible(self, val): # -> None:
        ...
    
    @property
    def type(self):
        ...
    
    def __init__(self, arg=..., align=..., customdata=..., customdatasrc=..., delta=..., domain=..., gauge=..., ids=..., idssrc=..., legend=..., legendgrouptitle=..., legendrank=..., legendwidth=..., meta=..., metasrc=..., mode=..., name=..., number=..., stream=..., title=..., uid=..., uirevision=..., value=..., visible=..., **kwargs) -> None:
        """
        Construct a new Indicator object

        An indicator is used to visualize a single `value` along with
        some contextual information such as `steps` or a `threshold`,
        using a combination of three visual elements: a number, a
        delta, and/or a gauge. Deltas are taken with respect to a
        `reference`. Gauges can be either angular or bullet (aka
        linear) gauges.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.Indicator`
        align
            Sets the horizontal alignment of the `text` within the
            box. Note that this attribute has no effect if an
            angular gauge is displayed: in this case, it is always
            centered
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            `customdata`.
        delta
            :class:`plotly.graph_objects.indicator.Delta` instance
            or dict with compatible properties
        domain
            :class:`plotly.graph_objects.indicator.Domain` instance
            or dict with compatible properties
        gauge
            The gauge of the Indicator plot.
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            `ids`.
        legend
            Sets the reference to a legend to show this trace in.
            References to these legends are "legend", "legend2",
            "legend3", etc. Settings for these legends are set in
            the layout, under `layout.legend`, `layout.legend2`,
            etc.
        legendgrouptitle
            :class:`plotly.graph_objects.indicator.Legendgrouptitle
            ` instance or dict with compatible properties
        legendrank
            Sets the legend rank for this trace. Items and groups
            with smaller ranks are presented on top/left side while
            with "reversed" `legend.traceorder` they are on
            bottom/right side. The default legendrank is 1000, so
            that you can use ranks less than 1000 to place certain
            items before all unranked items, and ranks greater than
            1000 to go after all unranked items. When having
            unranked or equal rank items shapes would be displayed
            after traces i.e. according to their order in data and
            layout.
        legendwidth
            Sets the width (in px or fraction) of the legend for
            this trace.
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            `meta`.
        mode
            Determines how the value is displayed on the graph.
            `number` displays the value numerically in text.
            `delta` displays the difference to a reference value in
            text. Finally, `gauge` displays the value graphically
            on an axis.
        name
            Sets the trace name. The trace name appears as the
            legend item and on hover.
        number
            :class:`plotly.graph_objects.indicator.Number` instance
            or dict with compatible properties
        stream
            :class:`plotly.graph_objects.indicator.Stream` instance
            or dict with compatible properties
        title
            :class:`plotly.graph_objects.indicator.Title` instance
            or dict with compatible properties
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        value
            Sets the number to be displayed.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).

        Returns
        -------
        Indicator
        """
        ...
    



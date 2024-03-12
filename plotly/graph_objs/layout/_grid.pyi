"""
This type stub file was generated by pyright.
"""

from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType

class Grid(_BaseLayoutHierarchyType):
    _parent_path_str = ...
    _path_str = ...
    _valid_props = ...
    @property
    def columns(self): # -> tuple[Any, ...] | Self | None:
        """
        The number of columns in the grid. If you provide a 2D
        `subplots` array, the length of its longest row is used as the
        default. If you give an `xaxes` array, its length is used as
        the default. But it's also possible to have a different length,
        if you want to leave a row at the end for non-cartesian
        subplots.

        The 'columns' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [1, 9223372036854775807]

        Returns
        -------
        int
        """
        ...
    
    @columns.setter
    def columns(self, val): # -> None:
        ...
    
    @property
    def domain(self): # -> tuple[Any, ...] | Self | None:
        """
        The 'domain' property is an instance of Domain
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.grid.Domain`
          - A dict of string/value properties that will be passed
            to the Domain constructor

            Supported dict properties:

                x
                    Sets the horizontal domain of this grid subplot
                    (in plot fraction). The first and last cells
                    end exactly at the domain edges, with no grout
                    around the edges.
                y
                    Sets the vertical domain of this grid subplot
                    (in plot fraction). The first and last cells
                    end exactly at the domain edges, with no grout
                    around the edges.

        Returns
        -------
        plotly.graph_objs.layout.grid.Domain
        """
        ...
    
    @domain.setter
    def domain(self, val): # -> None:
        ...
    
    @property
    def pattern(self): # -> tuple[Any, ...] | Self | None:
        """
        If no `subplots`, `xaxes`, or `yaxes` are given but we do have
        `rows` and `columns`, we can generate defaults using
        consecutive axis IDs, in two ways: "coupled" gives one x axis
        per column and one y axis per row. "independent" uses a new xy
        pair for each cell, left-to-right across each row then
        iterating rows according to `roworder`.

        The 'pattern' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['independent', 'coupled']

        Returns
        -------
        Any
        """
        ...
    
    @pattern.setter
    def pattern(self, val): # -> None:
        ...
    
    @property
    def roworder(self): # -> tuple[Any, ...] | Self | None:
        """
        Is the first row the top or the bottom? Note that columns are
        always enumerated from left to right.

        The 'roworder' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['top to bottom', 'bottom to top']

        Returns
        -------
        Any
        """
        ...
    
    @roworder.setter
    def roworder(self, val): # -> None:
        ...
    
    @property
    def rows(self): # -> tuple[Any, ...] | Self | None:
        """
        The number of rows in the grid. If you provide a 2D `subplots`
        array or a `yaxes` array, its length is used as the default.
        But it's also possible to have a different length, if you want
        to leave a row at the end for non-cartesian subplots.

        The 'rows' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [1, 9223372036854775807]

        Returns
        -------
        int
        """
        ...
    
    @rows.setter
    def rows(self, val): # -> None:
        ...
    
    @property
    def subplots(self): # -> tuple[Any, ...] | Self | None:
        """
        Used for freeform grids, where some axes may be shared across
        subplots but others are not. Each entry should be a cartesian
        subplot id, like "xy" or "x3y2", or "" to leave that cell
        empty. You may reuse x axes within the same column, and y axes
        within the same row. Non-cartesian subplots and traces that
        support `domain` can place themselves in this grid separately
        using the `gridcell` attribute.

        The 'subplots' property is an info array that may be specified as:
        * a 2D list where:
          The 'subplots[i][j]' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['']
          - A string that matches one of the following regular expressions:
                ['^x([2-9]|[1-9][0-9]+)?y([2-9]|[1-9][0-9]+)?$']

        Returns
        -------
        list
        """
        ...
    
    @subplots.setter
    def subplots(self, val): # -> None:
        ...
    
    @property
    def xaxes(self): # -> tuple[Any, ...] | Self | None:
        """
        Used with `yaxes` when the x and y axes are shared across
        columns and rows. Each entry should be an x axis id like "x",
        "x2", etc., or "" to not put an x axis in that column. Entries
        other than "" must be unique. Ignored if `subplots` is present.
        If missing but `yaxes` is present, will generate consecutive
        IDs.

        The 'xaxes' property is an info array that may be specified as:
        * a list of elements where:
          The 'xaxes[i]' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['']
          - A string that matches one of the following regular expressions:
                ['^x([2-9]|[1-9][0-9]+)?( domain)?$']

        Returns
        -------
        list
        """
        ...
    
    @xaxes.setter
    def xaxes(self, val): # -> None:
        ...
    
    @property
    def xgap(self): # -> tuple[Any, ...] | Self | None:
        """
        Horizontal space between grid cells, expressed as a fraction of
        the total width available to one cell. Defaults to 0.1 for
        coupled-axes grids and 0.2 for independent grids.

        The 'xgap' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        ...
    
    @xgap.setter
    def xgap(self, val): # -> None:
        ...
    
    @property
    def xside(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets where the x axis labels and titles go. "bottom" means the
        very bottom of the grid. "bottom plot" is the lowest plot that
        each x axis is used in. "top" and "top plot" are similar.

        The 'xside' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['bottom', 'bottom plot', 'top plot', 'top']

        Returns
        -------
        Any
        """
        ...
    
    @xside.setter
    def xside(self, val): # -> None:
        ...
    
    @property
    def yaxes(self): # -> tuple[Any, ...] | Self | None:
        """
        Used with `yaxes` when the x and y axes are shared across
        columns and rows. Each entry should be an y axis id like "y",
        "y2", etc., or "" to not put a y axis in that row. Entries
        other than "" must be unique. Ignored if `subplots` is present.
        If missing but `xaxes` is present, will generate consecutive
        IDs.

        The 'yaxes' property is an info array that may be specified as:
        * a list of elements where:
          The 'yaxes[i]' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['']
          - A string that matches one of the following regular expressions:
                ['^y([2-9]|[1-9][0-9]+)?( domain)?$']

        Returns
        -------
        list
        """
        ...
    
    @yaxes.setter
    def yaxes(self, val): # -> None:
        ...
    
    @property
    def ygap(self): # -> tuple[Any, ...] | Self | None:
        """
        Vertical space between grid cells, expressed as a fraction of
        the total height available to one cell. Defaults to 0.1 for
        coupled-axes grids and 0.3 for independent grids.

        The 'ygap' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        ...
    
    @ygap.setter
    def ygap(self, val): # -> None:
        ...
    
    @property
    def yside(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets where the y axis labels and titles go. "left" means the
        very left edge of the grid. *left plot* is the leftmost plot
        that each y axis is used in. "right" and *right plot* are
        similar.

        The 'yside' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['left', 'left plot', 'right plot', 'right']

        Returns
        -------
        Any
        """
        ...
    
    @yside.setter
    def yside(self, val): # -> None:
        ...
    
    def __init__(self, arg=..., columns=..., domain=..., pattern=..., roworder=..., rows=..., subplots=..., xaxes=..., xgap=..., xside=..., yaxes=..., ygap=..., yside=..., **kwargs) -> None:
        """
        Construct a new Grid object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.layout.Grid`
        columns
            The number of columns in the grid. If you provide a 2D
            `subplots` array, the length of its longest row is used
            as the default. If you give an `xaxes` array, its
            length is used as the default. But it's also possible
            to have a different length, if you want to leave a row
            at the end for non-cartesian subplots.
        domain
            :class:`plotly.graph_objects.layout.grid.Domain`
            instance or dict with compatible properties
        pattern
            If no `subplots`, `xaxes`, or `yaxes` are given but we
            do have `rows` and `columns`, we can generate defaults
            using consecutive axis IDs, in two ways: "coupled"
            gives one x axis per column and one y axis per row.
            "independent" uses a new xy pair for each cell, left-
            to-right across each row then iterating rows according
            to `roworder`.
        roworder
            Is the first row the top or the bottom? Note that
            columns are always enumerated from left to right.
        rows
            The number of rows in the grid. If you provide a 2D
            `subplots` array or a `yaxes` array, its length is used
            as the default. But it's also possible to have a
            different length, if you want to leave a row at the end
            for non-cartesian subplots.
        subplots
            Used for freeform grids, where some axes may be shared
            across subplots but others are not. Each entry should
            be a cartesian subplot id, like "xy" or "x3y2", or ""
            to leave that cell empty. You may reuse x axes within
            the same column, and y axes within the same row. Non-
            cartesian subplots and traces that support `domain` can
            place themselves in this grid separately using the
            `gridcell` attribute.
        xaxes
            Used with `yaxes` when the x and y axes are shared
            across columns and rows. Each entry should be an x axis
            id like "x", "x2", etc., or "" to not put an x axis in
            that column. Entries other than "" must be unique.
            Ignored if `subplots` is present. If missing but
            `yaxes` is present, will generate consecutive IDs.
        xgap
            Horizontal space between grid cells, expressed as a
            fraction of the total width available to one cell.
            Defaults to 0.1 for coupled-axes grids and 0.2 for
            independent grids.
        xside
            Sets where the x axis labels and titles go. "bottom"
            means the very bottom of the grid. "bottom plot" is the
            lowest plot that each x axis is used in. "top" and "top
            plot" are similar.
        yaxes
            Used with `yaxes` when the x and y axes are shared
            across columns and rows. Each entry should be an y axis
            id like "y", "y2", etc., or "" to not put a y axis in
            that row. Entries other than "" must be unique. Ignored
            if `subplots` is present. If missing but `xaxes` is
            present, will generate consecutive IDs.
        ygap
            Vertical space between grid cells, expressed as a
            fraction of the total height available to one cell.
            Defaults to 0.1 for coupled-axes grids and 0.3 for
            independent grids.
        yside
            Sets where the y axis labels and titles go. "left"
            means the very left edge of the grid. *left plot* is
            the leftmost plot that each y axis is used in. "right"
            and *right plot* are similar.

        Returns
        -------
        Grid
        """
        ...
    



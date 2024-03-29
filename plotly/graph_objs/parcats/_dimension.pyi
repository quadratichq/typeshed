"""
This type stub file was generated by pyright.
"""

from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType

class Dimension(_BaseTraceHierarchyType):
    _parent_path_str = ...
    _path_str = ...
    _valid_props = ...
    @property
    def categoryarray(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the order in which categories in this dimension appear.
        Only has an effect if `categoryorder` is set to "array". Used
        with `categoryorder`.

        The 'categoryarray' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        ...
    
    @categoryarray.setter
    def categoryarray(self, val): # -> None:
        ...
    
    @property
    def categoryarraysrc(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the source reference on Chart Studio Cloud for
        `categoryarray`.

        The 'categoryarraysrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        ...
    
    @categoryarraysrc.setter
    def categoryarraysrc(self, val): # -> None:
        ...
    
    @property
    def categoryorder(self): # -> tuple[Any, ...] | Self | None:
        """
        Specifies the ordering logic for the categories in the
        dimension. By default, plotly uses "trace", which specifies the
        order that is present in the data supplied. Set `categoryorder`
        to *category ascending* or *category descending* if order
        should be determined by the alphanumerical order of the
        category names. Set `categoryorder` to "array" to derive the
        ordering from the attribute `categoryarray`. If a category is
        not found in the `categoryarray` array, the sorting behavior
        for that attribute will be identical to the "trace" mode. The
        unspecified categories will follow the categories in
        `categoryarray`.

        The 'categoryorder' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['trace', 'category ascending', 'category descending',
                'array']

        Returns
        -------
        Any
        """
        ...
    
    @categoryorder.setter
    def categoryorder(self, val): # -> None:
        ...
    
    @property
    def displayindex(self): # -> tuple[Any, ...] | Self | None:
        """
        The display index of dimension, from left to right, zero
        indexed, defaults to dimension index.

        The 'displayindex' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)

        Returns
        -------
        int
        """
        ...
    
    @displayindex.setter
    def displayindex(self, val): # -> None:
        ...
    
    @property
    def label(self): # -> tuple[Any, ...] | Self | None:
        """
        The shown name of the dimension.

        The 'label' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        ...
    
    @label.setter
    def label(self, val): # -> None:
        ...
    
    @property
    def ticktext(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets alternative tick labels for the categories in this
        dimension. Only has an effect if `categoryorder` is set to
        "array". Should be an array the same length as `categoryarray`
        Used with `categoryorder`.

        The 'ticktext' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        ...
    
    @ticktext.setter
    def ticktext(self, val): # -> None:
        ...
    
    @property
    def ticktextsrc(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the source reference on Chart Studio Cloud for `ticktext`.

        The 'ticktextsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        ...
    
    @ticktextsrc.setter
    def ticktextsrc(self, val): # -> None:
        ...
    
    @property
    def values(self): # -> tuple[Any, ...] | Self | None:
        """
        Dimension values. `values[n]` represents the category value of
        the `n`th point in the dataset, therefore the `values` vector
        for all dimensions must be the same (longer vectors will be
        truncated).

        The 'values' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        ...
    
    @values.setter
    def values(self, val): # -> None:
        ...
    
    @property
    def valuessrc(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the source reference on Chart Studio Cloud for `values`.

        The 'valuessrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        ...
    
    @valuessrc.setter
    def valuessrc(self, val): # -> None:
        ...
    
    @property
    def visible(self): # -> tuple[Any, ...] | Self | None:
        """
        Shows the dimension when set to `true` (the default). Hides the
        dimension for `false`.

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
    
    def __init__(self, arg=..., categoryarray=..., categoryarraysrc=..., categoryorder=..., displayindex=..., label=..., ticktext=..., ticktextsrc=..., values=..., valuessrc=..., visible=..., **kwargs) -> None:
        """
        Construct a new Dimension object

        The dimensions (variables) of the parallel categories diagram.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.parcats.Dimension`
        categoryarray
            Sets the order in which categories in this dimension
            appear. Only has an effect if `categoryorder` is set to
            "array". Used with `categoryorder`.
        categoryarraysrc
            Sets the source reference on Chart Studio Cloud for
            `categoryarray`.
        categoryorder
            Specifies the ordering logic for the categories in the
            dimension. By default, plotly uses "trace", which
            specifies the order that is present in the data
            supplied. Set `categoryorder` to *category ascending*
            or *category descending* if order should be determined
            by the alphanumerical order of the category names. Set
            `categoryorder` to "array" to derive the ordering from
            the attribute `categoryarray`. If a category is not
            found in the `categoryarray` array, the sorting
            behavior for that attribute will be identical to the
            "trace" mode. The unspecified categories will follow
            the categories in `categoryarray`.
        displayindex
            The display index of dimension, from left to right,
            zero indexed, defaults to dimension index.
        label
            The shown name of the dimension.
        ticktext
            Sets alternative tick labels for the categories in this
            dimension. Only has an effect if `categoryorder` is set
            to "array". Should be an array the same length as
            `categoryarray` Used with `categoryorder`.
        ticktextsrc
            Sets the source reference on Chart Studio Cloud for
            `ticktext`.
        values
            Dimension values. `values[n]` represents the category
            value of the `n`th point in the dataset, therefore the
            `values` vector for all dimensions must be the same
            (longer vectors will be truncated).
        valuessrc
            Sets the source reference on Chart Studio Cloud for
            `values`.
        visible
            Shows the dimension when set to `true` (the default).
            Hides the dimension for `false`.

        Returns
        -------
        Dimension
        """
        ...
    



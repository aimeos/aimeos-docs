
# detail
## product/attribute/types

List of attribute type codes that should be displayed in the basket along with their product

```
client/html/common/summary/detail/product/attribute/types = Array
(
    [0] => variant
    [1] => config
    [2] => custom
)
```

* Default: `Array
(
    [0] => variant
    [1] => config
    [2] => custom
)
`
* Type: array - List of attribute type codes
* Since: 2014.09

The products in the basket can store attributes that exactly define an ordered
product or which are important for the back office. By default, the product
variant attributes are always displayed and the configurable product attributes
are displayed separately.

Additional attributes for each ordered product can be added by basket plugins.
Depending on the attribute types and if they should be shown to the customers,
you need to extend the list of displayed attribute types ab adding their codes
to the configurable list.

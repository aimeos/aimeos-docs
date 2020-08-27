
# detail
## download/payment-status

Minium payment status value for product download files

```
client/html/common/summary/detail/download/payment-status = 6
```

* Default: 6
* Type: integer - Order payment constant value
* Since: 2016.3

This setting specifies the payment status value of an order for which
links to bought product download files are shown on the "thank you"
page, in the "MyAccount" and in the e-mails sent to the customers.

The value is one of the payment constant values from [order item](https://github.com/aimeos/aimeos-core/blob/master/lib/mshoplib/src/MShop/Order/Item/Base.php#L105).
Most of the time, only two values are of interest:

* 5: payment authorized
* 6: payment received


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

* Default: Array
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

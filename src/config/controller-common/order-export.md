
# csv
## mapping

List of mappings between the position in the CSV file and item keys

```
controller/common/order/export/csv/mapping = Array
(
    [invoice] => Array
        (
            [2] => order.type
            [3] => order.datepayment
            [4] => order.statuspayment
            [5] => order.datedelivery
            [6] => order.statusdelivery
            [7] => order.relatedid
            [8] => order.base.customerid
            [9] => order.base.sitecode
            [10] => order.base.languageid
            [11] => order.base.currencyid
            [12] => order.base.price
            [13] => order.base.costs
            [14] => order.base.rebate
            [15] => order.base.taxvalue
            [16] => order.base.taxflag
            [17] => order.base.status
            [18] => order.base.comment
        )

    [address] => Array
        (
            [2] => order.base.address.type
            [3] => order.base.address.salutation
            [4] => order.base.address.company
            [5] => order.base.address.vatid
            [6] => order.base.address.title
            [7] => order.base.address.firstname
            [8] => order.base.address.lastname
            [9] => order.base.address.address1
            [10] => order.base.address.address2
            [11] => order.base.address.address3
            [12] => order.base.address.postal
            [13] => order.base.address.city
            [14] => order.base.address.state
            [15] => order.base.address.countryid
            [16] => order.base.address.languageid
            [17] => order.base.address.telephone
            [18] => order.base.address.telefax
            [19] => order.base.address.email
            [20] => order.base.address.website
            [21] => order.base.address.longitude
            [22] => order.base.address.latitude
        )

    [service] => Array
        (
            [2] => order.base.service.type
            [3] => order.base.service.code
            [4] => order.base.service.name
            [5] => order.base.service.mediaurl
            [6] => order.base.service.price
            [7] => order.base.service.costs
            [8] => order.base.service.rebate
            [9] => order.base.service.taxrate
            [10] => order.base.service.attribute.type
            [11] => order.base.service.attribute.code
            [12] => order.base.service.attribute.name
            [13] => order.base.service.attribute.value
        )

    [coupon] => Array
        (
            [2] => order.base.coupon.code
        )

    [product] => Array
        (
            [2] => order.base.product.type
            [3] => order.base.product.stocktype
            [4] => order.base.product.suppliercode
            [5] => order.base.product.prodcode
            [6] => order.base.product.productid
            [7] => order.base.product.quantity
            [8] => order.base.product.name
            [9] => order.base.product.mediaurl
            [10] => order.base.product.price
            [11] => order.base.product.costs
            [12] => order.base.product.rebate
            [13] => order.base.product.taxrate
            [14] => order.base.product.status
            [15] => order.base.product.position
            [16] => order.base.product.attribute.type
            [17] => order.base.product.attribute.code
            [18] => order.base.product.attribute.name
            [19] => order.base.product.attribute.value
        )

)
```

* Default: Array
* Type: array - Associative list of processor names and lists of key/position pairs
* Since: 2017.08

The exporter has to know which data is at which position in the CSV
file. Therefore, you need to specify a mapping between each position
and the MShop domain item key (e.g. "order.type") it represents.

These mappings are grouped together by their processor names, which
are responsible for exporting the data, e.g. all mappings in "invoice"
will be managed by the invoice processor while the mappings in
"product" will be exported by the product processor.

See also:

* controller/common/order/export/csv/max-size

## max-size

Maximum number of CSV rows to export at once

```
controller/common/order/export/csv/max-size = 1000
```

* Default: 1000
* Type: integer - Number of rows
* Since: 2017.08

It's more efficient to read and export more than one row at a time
to speed up the export. Usually, the bigger the chunk that is exported
at once, the less time the exporter will need. The downside is that
the amount of memory required by the export process will increase as
well. Therefore, it's a trade-off between memory consumption and
export speed.

See also:

* controller/common/order/export/csv/mapping

## processor/address/name

```
controller/common/order/export/csv/processor/address/name = Standard
```

* Default: Standard


## processor/coupon/name

```
controller/common/order/export/csv/processor/coupon/name = Standard
```

* Default: Standard


## processor/invoice/name

```
controller/common/order/export/csv/processor/invoice/name = Standard
```

* Default: Standard


## processor/product/name

```
controller/common/order/export/csv/processor/product/name = Standard
```

* Default: Standard


## processor/service/name

```
controller/common/order/export/csv/processor/service/name = Standard
```

* Default: Standard

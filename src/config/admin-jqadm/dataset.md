
# product

Predefined data sets for products

```
admin/jqadm/dataset/product = Array
(
)
```

* Default: `Array
(
)
`
* Type: array - Associative list of name/configuration pairs
* Since: 2019.10

To simplify creating new products by editors, Aimeos supports the defintion
of arbitrary product templates. Each template consists of a name and the
associated configuration template for that product type (e.g. a T-Shirt).
The template names will be listed in a select box in the product detail view.

A template definition may look like this in the PHP configuration:

```
 [
   'T-Shirt' => [
     'characteristic/variant' => [['attribute.type' => 'color'], ['attribute.type' => 'size']],
     'characteristic/default' => [['attribute.type' => 'material']],
     'characteristic/config' => [['attribute.type' => 'sticker']],
     'characteristic/custom' => [['attribute.type' => 'print']],
     'price' => [['price.currencyid' => 'EUR', 'price.taxrates' => ['' => '19.00']]],
     'stock' => [['stock.type' => 'default']],
   ],
 ]
```

That definition would add "T-Shirt" to the data set selection and if the editor
selects this data set defintion the following will appear:

* two variant attribute select boxes (type "color" and "size") in the "Characteristics" tab
* one default attribute select box (type "material") in the "Characteristics" tab
* one select box for configurable attributes (type: "sticker") in the "Characteristics" tab
* one select box for customizable attributes (type: "print") in the "Characteristics" tab
* a price item with currency "EUR" and tax rate pre-filled
* a stock item with of type "default" pre-filled

You can also define a template for a book with a totally different data set:

```
 [
   'Book' => [
     'catalog/default' => [[]],
     'catalog/promotion' => [[]],
     'characteristic/default' => [['attribute.type' => 'binding']],
     'characteristic/property' => [['product.property.type' => 'isbn']],
     'media' => [['media.type' => 'default'], ['media.type' => 'download']],
     'price' => [['price.currencyid' => 'EUR', 'price.taxrates' => ['' => '7.00']]],
     'related/bought-together' => [[]],
     'related/suggestion' => [[], []],
     'supplier/default' => [[]],
     'stock' => [['stock.type' => 'default']],
     'text' => [
       ['text.type' => 'name', 'text.languageid' => 'en'],
       ['text.type' => 'short', 'text.languageid' => 'en'],
       ['text.type' => 'long', 'text.languageid' => 'en'],
     ],
   ],
 ]
```

If an editor select the book dataset defintion, the following will appear:

* one select box for a default category in the "Categories" tab
* one select box for a promotion category in the "Categories" tab
* one attribute select box (type "binding") in the "Characteristics" tab
* one property line (type "isbn") in the "Characteristics" tab
* two media items ("default" image and "download" file)
* a price item with currency "EUR" and tax rate pre-filled
* one select boxe for products bought together in the "Related" tab
* two select boxes for suggested products in the "Related" tab
* one select box for a default supplier in the "Suppliers" tab
* a stock item with of type "default" pre-filled
* three text items for name, short and long texts and "English" language pre-selected

All types in a template that should be pre-selected must already exist. Make
sure you've created them first in the appropriate type panels.

Also, the data set template can contain definitions for other tabs as well,
e.g. for product variants and bundles.

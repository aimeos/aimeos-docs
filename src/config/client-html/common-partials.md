
# attribute

Relative path to the product attribute partial template file

```
client/html/common/partials/attribute = common/partials/attribute-standard
```

* Default: common/partials/attribute-standard
* Type: string - Relative path to the template file
* Since: 2016.01

Partials are templates which are reused in other templates and generate
reoccuring blocks filled with data from the assigned values. The attribute
partial creates an HTML block for a list of optional product attributes a
customer can select from.

The partial template files are usually stored in the templates/partials/ folder
of the core or the extensions. The configured path to the partial file must
be relative to the templates/ folder, e.g. "partials/attribute-standard.php".

See also:

* client/html/common/partials/selection

# group

Relative path to the group product partial template file

```
client/html/common/partials/group = 
```

* Default: 
* Type: string - Relative path to the template file
* Since: 2021.07

Partials are templates which are reused in other templates and generate
reoccuring blocks filled with data from the assigned values. The group
partial creates an HTML block for a list of sub-products assigned to a
group product a customer can select from.

The partial template files are usually stored in the templates/partials/ folder
of the core or the extensions. The configured path to the partial file must
be relative to the templates/ folder, e.g. "common/partials/selection-list".

See also:

* client/html/common/partials/attribute

# media

Relative path to the media partial template file

```
client/html/common/partials/media = common/partials/media-standard
```

* Default: common/partials/media-standard
* Type: string - Relative path to the template file
* Since: 2015.08

Partials are templates which are reused in other templates and generate
reoccuring blocks filled with data from the assigned values. The media
partial creates an HTML block of for images, video, audio or other documents.

The partial template files are usually stored in the templates/partials/ folder
of the core or the extensions. The configured path to the partial file must
be relative to the templates/ folder, e.g. "common/partials/media-standard.php".


# price

Relative path to the price partial template file

```
client/html/common/partials/price = common/partials/price-standard
```

* Default: common/partials/price-standard
* Type: string - Relative path to the template file
* Since: 2015.04

Partials are templates which are reused in other templates and generate
reoccuring blocks filled with data from the assigned values. The price
partial creates an HTML block for a list of price items.

The partial template files are usually stored in the templates/partials/ folder
of the core or the extensions. The configured path to the partial file must
be relative to the templates/ folder, e.g. "partials/price-standard.php".


# products

Relative path to the products partial template file

```
client/html/common/partials/products = common/partials/products-standard
```

* Default: common/partials/products-standard
* Type: string - Relative path to the template file
* Since: 2017.01

Partials are templates which are reused in other templates and generate
reoccuring blocks filled with data from the assigned values. The products
partial creates an HTML block for a product listing.


# selection

Relative path to the variant attribute partial template file

```
client/html/common/partials/selection = common/partials/selection-standard
```

* Default: common/partials/selection-standard
* Type: string - Relative path to the template file
* Since: 2015.04

Partials are templates which are reused in other templates and generate
reoccuring blocks filled with data from the assigned values. The selection
partial creates an HTML block for a list of variant product attributes
assigned to a selection product a customer must select from.

The partial template files are usually stored in the templates/partials/ folder
of the core or the extensions. The configured path to the partial file must
be relative to the templates/ folder, e.g. "common/partials/selection-standard".

See also:

* client/html/common/partials/attribute
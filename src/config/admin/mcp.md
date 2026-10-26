
# ai
## isolate/max-size

Maximum size of the images passed to the ai-isolate tool in bytes

```
admin/mcp/ai/isolate/max-size = 
```

* Type: integer - Number of bytes
* Since: 2026.10

The ai-isolate tool removes the background of images sent by the MCP
client as base64 encoded content. Larger images are rejected with
an error to limit the memory usage and the costs of the AI provider.
The default value is 10MB.

See also:

* admin/mcp/media/max-size

# lists-domains

Domains of the list items included in the items returned by the MCP tools

```
admin/mcp/lists-domains = Array
(
    [0] => attribute
    [1] => catalog
    [2] => customer
    [3] => group
    [4] => media
    [5] => price
    [6] => product
    [7] => service
    [8] => supplier
    [9] => text
)
```

* Default: 
```
Array
(
)
```
* Type: array - List of domain names
* Since: 2026.10

Items like products or catalogs can reference other items via list
items, e.g. texts, prices or media. Only referenced items of the
domains in this list are added to the "lists" section of the returned
items, so the MCP client can see and update them together with the
parent item. Remove domains to keep the responses small or add the
domains of your own extensions if their items should be returned too.

See also:

* admin/mcp/serialization/max-depth

# media
## max-size

Maximum size of the files uploaded by the media-save tool in bytes

```
admin/mcp/media/max-size = 
```

* Type: integer - Number of bytes
* Since: 2026.10

MCP clients upload media files and preview images as base64 encoded
content. Files larger than this value are rejected with an error.
The default value is 10MB.

See also:

* admin/mcp/ai/isolate/max-size

# resource
## ai/imagine

List of user groups that are allowed to generate images using the AI provider

```
admin/mcp/resource/ai/imagine = 
```

* Type: array - List of user group names
* Since: 2026.10

The "ai-imagine" MCP tool can only be executed by users who are members
of at least one of the configured groups.

See also:

* admin/mcp/resource/ai/write
* admin/mcp/resource/ai/translate
* admin/mcp/resource/ai/isolate
* admin/mcp/tools

## ai/isolate

List of user groups that are allowed to remove the background of images using the AI provider

```
admin/mcp/resource/ai/isolate = 
```

* Type: array - List of user group names
* Since: 2026.10

The "ai-isolate" MCP tool can only be executed by users who are members
of at least one of the configured groups.

See also:

* admin/mcp/resource/ai/write
* admin/mcp/resource/ai/translate
* admin/mcp/resource/ai/imagine
* admin/mcp/tools

## ai/translate

List of user groups that are allowed to translate texts using the AI provider

```
admin/mcp/resource/ai/translate = 
```

* Type: array - List of user group names
* Since: 2026.10

The "ai-translate" MCP tool can only be executed by users who are
members of at least one of the configured groups.

See also:

* admin/mcp/resource/ai/write
* admin/mcp/resource/ai/imagine
* admin/mcp/resource/ai/isolate
* admin/mcp/tools

## ai/write

List of user groups that are allowed to generate texts using the AI provider

```
admin/mcp/resource/ai/write = Array
(
    [0] => admin
    [1] => editor
    [2] => super
)
```

* Default: 
```
Array
(
)
```
* Type: array - List of user group names
* Since: 2026.10

The "ai-write" MCP tool can only be executed by users who are members of
at least one of the configured groups.

See also:

* admin/mcp/resource/ai/translate
* admin/mcp/resource/ai/imagine
* admin/mcp/resource/ai/isolate
* admin/mcp/tools

## attribute/delete

List of user groups that are allowed to delete attribute items

```
admin/mcp/resource/attribute/delete = 
```

* Type: array - List of user group names
* Since: 2026.10

The "attribute-delete" MCP tool can only be executed by users who are
members of at least one of the configured groups.

See also:

* admin/mcp/resource/attribute/get
* admin/mcp/resource/attribute/save
* admin/mcp/tools

## attribute/get

List of user groups that are allowed to view attribute items

```
admin/mcp/resource/attribute/get = 
```

* Type: array - List of user group names
* Since: 2026.10

The "attribute-get", "attribute-find" and "attribute-search" MCP tools
can only be executed by users who are members of at least one of the
configured groups.

See also:

* admin/mcp/resource/attribute/save
* admin/mcp/resource/attribute/delete
* admin/mcp/tools

## attribute/save

List of user groups that are allowed to create and update attribute items

```
admin/mcp/resource/attribute/save = 
```

* Type: array - List of user group names
* Since: 2026.10

The "attribute-save" MCP tool can only be executed by users who are
members of at least one of the configured groups.

See also:

* admin/mcp/resource/attribute/get
* admin/mcp/resource/attribute/delete
* admin/mcp/tools

## catalog/delete

List of user groups that are allowed to delete catalog items

```
admin/mcp/resource/catalog/delete = 
```

* Type: array - List of user group names
* Since: 2026.10

The "catalog-delete" MCP tool can only be executed by users who are
members of at least one of the configured groups.

See also:

* admin/mcp/resource/catalog/get
* admin/mcp/resource/catalog/save
* admin/mcp/tools

## catalog/get

List of user groups that are allowed to view catalog items

```
admin/mcp/resource/catalog/get = Array
(
    [0] => admin
    [1] => editor
    [2] => super
)
```

* Default: 
```
Array
(
)
```
* Type: array - List of user group names
* Since: 2026.10

The "catalog-get", "catalog-find", "catalog-search", "catalog-tree",
"catalog-path" and "catalog-search-tree" MCP tools can only be executed
by users who are members of at least one of the configured groups.

See also:

* admin/mcp/resource/catalog/save
* admin/mcp/resource/catalog/delete
* admin/mcp/tools

## catalog/save

List of user groups that are allowed to create and update catalog items

```
admin/mcp/resource/catalog/save = 
```

* Type: array - List of user group names
* Since: 2026.10

The "catalog-save", "catalog-insert" and "catalog-move" MCP tools can
only be executed by users who are members of at least one of the
configured groups.

See also:

* admin/mcp/resource/catalog/get
* admin/mcp/resource/catalog/delete
* admin/mcp/tools

## coupon/code/delete

List of user groups that are allowed to delete coupon code items

```
admin/mcp/resource/coupon/code/delete = 
```

* Type: array - List of user group names
* Since: 2026.10

The "coupon-code-delete" MCP tool can only be executed by users who are
members of at least one of the configured groups.

See also:

* admin/mcp/resource/coupon/code/get
* admin/mcp/resource/coupon/code/save
* admin/mcp/tools

## coupon/code/get

List of user groups that are allowed to view coupon code items

```
admin/mcp/resource/coupon/code/get = 
```

* Type: array - List of user group names
* Since: 2026.10

The "coupon-code-get" and "coupon-code-search" MCP tools can only be
executed by users who are members of at least one of the configured
groups.

See also:

* admin/mcp/resource/coupon/code/save
* admin/mcp/resource/coupon/code/delete
* admin/mcp/tools

## coupon/code/save

List of user groups that are allowed to create and update coupon code items

```
admin/mcp/resource/coupon/code/save = 
```

* Type: array - List of user group names
* Since: 2026.10

The "coupon-code-save" MCP tool can only be executed by users who are
members of at least one of the configured groups.

See also:

* admin/mcp/resource/coupon/code/get
* admin/mcp/resource/coupon/code/delete
* admin/mcp/tools

## coupon/delete

List of user groups that are allowed to delete coupon items

```
admin/mcp/resource/coupon/delete = 
```

* Type: array - List of user group names
* Since: 2026.10

The "coupon-delete" MCP tool can only be executed by users who are
members of at least one of the configured groups.

See also:

* admin/mcp/resource/coupon/get
* admin/mcp/resource/coupon/save
* admin/mcp/tools

## coupon/get

List of user groups that are allowed to view coupon items

```
admin/mcp/resource/coupon/get = 
```

* Type: array - List of user group names
* Since: 2026.10

The "coupon-get", "coupon-search" and "coupon-config" MCP tools can only
be executed by users who are members of at least one of the configured
groups.

See also:

* admin/mcp/resource/coupon/save
* admin/mcp/resource/coupon/delete
* admin/mcp/tools

## coupon/save

List of user groups that are allowed to create and update coupon items

```
admin/mcp/resource/coupon/save = 
```

* Type: array - List of user group names
* Since: 2026.10

The "coupon-save" MCP tool can only be executed by users who are members
of at least one of the configured groups.

See also:

* admin/mcp/resource/coupon/get
* admin/mcp/resource/coupon/delete
* admin/mcp/tools

## customer/delete

List of user groups that are allowed to delete customer items

```
admin/mcp/resource/customer/delete = 
```

* Type: array - List of user group names
* Since: 2026.10

The "customer-delete" MCP tool can only be executed by users who are
members of at least one of the configured groups.

See also:

* admin/mcp/resource/customer/get
* admin/mcp/resource/customer/save
* admin/mcp/tools

## customer/get

List of user groups that are allowed to view customer items

```
admin/mcp/resource/customer/get = Array
(
    [0] => admin
    [1] => editor
    [2] => super
)
```

* Default: 
```
Array
(
)
```
* Type: array - List of user group names
* Since: 2026.10

The "customer-get", "customer-find", "customer-search" and
"customer-aggregate" MCP tools can only be executed by users who are
members of at least one of the configured groups.

See also:

* admin/mcp/resource/customer/save
* admin/mcp/resource/customer/delete
* admin/mcp/tools

## customer/save

List of user groups that are allowed to create and update customer items

```
admin/mcp/resource/customer/save = 
```

* Type: array - List of user group names
* Since: 2026.10

The "customer-save" MCP tool can only be executed by users who are
members of at least one of the configured groups.

See also:

* admin/mcp/resource/customer/get
* admin/mcp/resource/customer/delete
* admin/mcp/tools

## group/delete

List of user groups that are allowed to delete group items

```
admin/mcp/resource/group/delete = Array
(
    [0] => admin
    [1] => super
)
```

* Default: 
```
Array
(
)
```
* Type: array - List of user group names
* Since: 2026.10

The "group-delete" MCP tool can only be executed by users who are
members of at least one of the configured groups.

See also:

* admin/mcp/resource/group/get
* admin/mcp/resource/group/save
* admin/mcp/tools

## group/get

List of user groups that are allowed to view group items

```
admin/mcp/resource/group/get = 
```

* Type: array - List of user group names
* Since: 2026.10

The "group-get" and "group-search" MCP tools can only be executed by
users who are members of at least one of the configured groups.

See also:

* admin/mcp/resource/group/save
* admin/mcp/resource/group/delete
* admin/mcp/tools

## group/save

List of user groups that are allowed to create and update group items

```
admin/mcp/resource/group/save = Array
(
    [0] => admin
    [1] => super
)
```

* Default: 
```
Array
(
)
```
* Type: array - List of user group names
* Since: 2026.10

The "group-save" MCP tool can only be executed by users who are members
of at least one of the configured groups.

See also:

* admin/mcp/resource/group/get
* admin/mcp/resource/group/delete
* admin/mcp/tools

## index/get

List of user groups that are allowed to view product index items

```
admin/mcp/resource/index/get = 
```

* Type: array - List of user group names
* Since: 2026.10

The "index-search" and "index-aggregate" MCP tools can only be executed
by users who are members of at least one of the configured groups.

See also:

* admin/mcp/tools

## locale/currency/delete

List of user groups that are allowed to delete currency items

```
admin/mcp/resource/locale/currency/delete = 
```

* Type: array - List of user group names
* Since: 2026.10

The "locale-currency-delete" MCP tool can only be executed by users who
are members of at least one of the configured groups.

See also:

* admin/mcp/resource/locale/currency/get
* admin/mcp/resource/locale/currency/save
* admin/mcp/tools

## locale/currency/get

List of user groups that are allowed to view currency items

```
admin/mcp/resource/locale/currency/get = 
```

* Type: array - List of user group names
* Since: 2026.10

The "locale-currency-get" and "locale-currency-search" MCP tools can
only be executed by users who are members of at least one of the
configured groups.

See also:

* admin/mcp/resource/locale/currency/save
* admin/mcp/resource/locale/currency/delete
* admin/mcp/tools

## locale/currency/save

List of user groups that are allowed to create and update currency items

```
admin/mcp/resource/locale/currency/save = 
```

* Type: array - List of user group names
* Since: 2026.10

The "locale-currency-save" MCP tool can only be executed by users who
are members of at least one of the configured groups.

See also:

* admin/mcp/resource/locale/currency/get
* admin/mcp/resource/locale/currency/delete
* admin/mcp/tools

## locale/delete

List of user groups that are allowed to delete locale items

```
admin/mcp/resource/locale/delete = 
```

* Type: array - List of user group names
* Since: 2026.10

The "locale-delete" MCP tool can only be executed by users who are
members of at least one of the configured groups.

See also:

* admin/mcp/resource/locale/get
* admin/mcp/resource/locale/save
* admin/mcp/tools

## locale/get

List of user groups that are allowed to view locale items

```
admin/mcp/resource/locale/get = 
```

* Type: array - List of user group names
* Since: 2026.10

The "locale-get" and "locale-search" MCP tools can only be executed by
users who are members of at least one of the configured groups.

See also:

* admin/mcp/resource/locale/save
* admin/mcp/resource/locale/delete
* admin/mcp/tools

## locale/language/delete

List of user groups that are allowed to delete language items

```
admin/mcp/resource/locale/language/delete = 
```

* Type: array - List of user group names
* Since: 2026.10

The "locale-language-delete" MCP tool can only be executed by users who
are members of at least one of the configured groups.

See also:

* admin/mcp/resource/locale/language/get
* admin/mcp/resource/locale/language/save
* admin/mcp/tools

## locale/language/get

List of user groups that are allowed to view language items

```
admin/mcp/resource/locale/language/get = 
```

* Type: array - List of user group names
* Since: 2026.10

The "locale-language-get" and "locale-language-search" MCP tools can
only be executed by users who are members of at least one of the
configured groups.

See also:

* admin/mcp/resource/locale/language/save
* admin/mcp/resource/locale/language/delete
* admin/mcp/tools

## locale/language/save

List of user groups that are allowed to create and update language items

```
admin/mcp/resource/locale/language/save = 
```

* Type: array - List of user group names
* Since: 2026.10

The "locale-language-save" MCP tool can only be executed by users who
are members of at least one of the configured groups.

See also:

* admin/mcp/resource/locale/language/get
* admin/mcp/resource/locale/language/delete
* admin/mcp/tools

## locale/save

List of user groups that are allowed to create and update locale items

```
admin/mcp/resource/locale/save = 
```

* Type: array - List of user group names
* Since: 2026.10

The "locale-save" MCP tool can only be executed by users who are members
of at least one of the configured groups.

See also:

* admin/mcp/resource/locale/get
* admin/mcp/resource/locale/delete
* admin/mcp/tools

## locale/site/delete

List of user groups that are allowed to delete site items

```
admin/mcp/resource/locale/site/delete = 
```

* Type: array - List of user group names
* Since: 2026.10

The "locale-site-delete" MCP tool can only be executed by users who are
members of at least one of the configured groups.

See also:

* admin/mcp/resource/locale/site/get
* admin/mcp/resource/locale/site/save
* admin/mcp/resource/locale/site/insert
* admin/mcp/resource/locale/site/move
* admin/mcp/tools

## locale/site/get

List of user groups that are allowed to view site items

```
admin/mcp/resource/locale/site/get = 
```

* Type: array - List of user group names
* Since: 2026.10

The "locale-site-get", "locale-site-find", "locale-site-search",
"locale-site-tree", "locale-site-path" and "locale-site-search-tree" MCP
tools can only be executed by users who are members of at least one of
the configured groups.

See also:

* admin/mcp/resource/locale/site/save
* admin/mcp/resource/locale/site/delete
* admin/mcp/resource/locale/site/insert
* admin/mcp/resource/locale/site/move
* admin/mcp/tools

## locale/site/insert

List of user groups that are allowed to create new site items in the site tree

```
admin/mcp/resource/locale/site/insert = 
```

* Type: array - List of user group names
* Since: 2026.10

The "locale-site-insert" MCP tool can only be executed by users who are
members of at least one of the configured groups.

See also:

* admin/mcp/resource/locale/site/get
* admin/mcp/resource/locale/site/save
* admin/mcp/resource/locale/site/delete
* admin/mcp/resource/locale/site/move
* admin/mcp/tools

## locale/site/move

List of user groups that are allowed to move site items within the site tree

```
admin/mcp/resource/locale/site/move = 
```

* Type: array - List of user group names
* Since: 2026.10

The "locale-site-move" MCP tool can only be executed by users who are
members of at least one of the configured groups.

See also:

* admin/mcp/resource/locale/site/get
* admin/mcp/resource/locale/site/save
* admin/mcp/resource/locale/site/delete
* admin/mcp/resource/locale/site/insert
* admin/mcp/tools

## locale/site/save

List of user groups that are allowed to create and update site items

```
admin/mcp/resource/locale/site/save = 
```

* Type: array - List of user group names
* Since: 2026.10

The "locale-site-save" MCP tool can only be executed by users who are
members of at least one of the configured groups.

See also:

* admin/mcp/resource/locale/site/get
* admin/mcp/resource/locale/site/delete
* admin/mcp/resource/locale/site/insert
* admin/mcp/resource/locale/site/move
* admin/mcp/tools

## media/delete

List of user groups that are allowed to delete media items

```
admin/mcp/resource/media/delete = 
```

* Type: array - List of user group names
* Since: 2026.10

The "media-delete" MCP tool can only be executed by users who are
members of at least one of the configured groups.

See also:

* admin/mcp/resource/media/get
* admin/mcp/resource/media/save
* admin/mcp/tools

## media/get

List of user groups that are allowed to view media items

```
admin/mcp/resource/media/get = 
```

* Type: array - List of user group names
* Since: 2026.10

The "media-get" and "media-search" MCP tools can only be executed by
users who are members of at least one of the configured groups.

See also:

* admin/mcp/resource/media/save
* admin/mcp/resource/media/delete
* admin/mcp/tools

## media/save

List of user groups that are allowed to create and update media items

```
admin/mcp/resource/media/save = 
```

* Type: array - List of user group names
* Since: 2026.10

The "media-save" MCP tool can only be executed by users who are members
of at least one of the configured groups.

See also:

* admin/mcp/resource/media/get
* admin/mcp/resource/media/delete
* admin/mcp/tools

## order/get

List of user groups that are allowed to view order items

```
admin/mcp/resource/order/get = 
```

* Type: array - List of user group names
* Since: 2026.10

The "order-get", "order-search" and "order-aggregate" MCP tools can only
be executed by users who are members of at least one of the configured
groups.

See also:

* admin/mcp/resource/order/save
* admin/mcp/tools

## order/save

List of user groups that are allowed to create and update order items

```
admin/mcp/resource/order/save = 
```

* Type: array - List of user group names
* Since: 2026.10

The "order-save" MCP tool can only be executed by users who are members
of at least one of the configured groups.

See also:

* admin/mcp/resource/order/get
* admin/mcp/tools

## plugin/delete

List of user groups that are allowed to delete plugin items

```
admin/mcp/resource/plugin/delete = 
```

* Type: array - List of user group names
* Since: 2026.10

The "plugin-delete" MCP tool can only be executed by users who are
members of at least one of the configured groups.

See also:

* admin/mcp/resource/plugin/get
* admin/mcp/resource/plugin/save
* admin/mcp/tools

## plugin/get

List of user groups that are allowed to view plugin items

```
admin/mcp/resource/plugin/get = Array
(
    [0] => admin
)
```

* Default: 
```
Array
(
)
```
* Type: array - List of user group names
* Since: 2026.10

The "plugin-get", "plugin-search" and "plugin-config" MCP tools can only
be executed by users who are members of at least one of the configured
groups.

See also:

* admin/mcp/resource/plugin/save
* admin/mcp/resource/plugin/delete
* admin/mcp/tools

## plugin/save

List of user groups that are allowed to create and update plugin items

```
admin/mcp/resource/plugin/save = Array
(
    [0] => editor
)
```

* Default: 
```
Array
(
)
```
* Type: array - List of user group names
* Since: 2026.10

The "plugin-save" MCP tool can only be executed by users who are members
of at least one of the configured groups.

See also:

* admin/mcp/resource/plugin/get
* admin/mcp/resource/plugin/delete
* admin/mcp/tools

## price/delete

List of user groups that are allowed to delete price items

```
admin/mcp/resource/price/delete = 
```

* Type: array - List of user group names
* Since: 2026.10

The "price-delete" MCP tool can only be executed by users who are
members of at least one of the configured groups.

See also:

* admin/mcp/resource/price/get
* admin/mcp/resource/price/save
* admin/mcp/tools

## price/get

List of user groups that are allowed to view price items

```
admin/mcp/resource/price/get = 
```

* Type: array - List of user group names
* Since: 2026.10

The "price-get" and "price-search" MCP tools can only be executed by
users who are members of at least one of the configured groups.

See also:

* admin/mcp/resource/price/save
* admin/mcp/resource/price/delete
* admin/mcp/tools

## price/save

List of user groups that are allowed to create and update price items

```
admin/mcp/resource/price/save = 
```

* Type: array - List of user group names
* Since: 2026.10

The "price-save" MCP tool can only be executed by users who are members
of at least one of the configured groups.

See also:

* admin/mcp/resource/price/get
* admin/mcp/resource/price/delete
* admin/mcp/tools

## product/delete

List of user groups that are allowed to delete product items

```
admin/mcp/resource/product/delete = Array
(
    [0] => admin
    [1] => editor
    [2] => super
)
```

* Default: 
```
Array
(
)
```
* Type: array - List of user group names
* Since: 2026.10

The "product-delete" MCP tool can only be executed by users who are
members of at least one of the configured groups.

See also:

* admin/mcp/resource/product/get
* admin/mcp/resource/product/save
* admin/mcp/tools

## product/get

List of user groups that are allowed to view product items

```
admin/mcp/resource/product/get = Array
(
    [0] => admin
    [1] => editor
    [2] => super
)
```

* Default: 
```
Array
(
)
```
* Type: array - List of user group names
* Since: 2026.10

The "product-get", "product-find" and "product-search" MCP tools can
only be executed by users who are members of at least one of the
configured groups.

See also:

* admin/mcp/resource/product/save
* admin/mcp/resource/product/delete
* admin/mcp/tools

## product/save

List of user groups that are allowed to create and update product items

```
admin/mcp/resource/product/save = Array
(
    [0] => admin
    [1] => editor
    [2] => super
)
```

* Default: 
```
Array
(
)
```
* Type: array - List of user group names
* Since: 2026.10

The "product-save" MCP tool can only be executed by users who are
members of at least one of the configured groups.

See also:

* admin/mcp/resource/product/get
* admin/mcp/resource/product/delete
* admin/mcp/tools

## review/delete

List of user groups that are allowed to delete review items

```
admin/mcp/resource/review/delete = 
```

* Type: array - List of user group names
* Since: 2026.10

The "review-delete" MCP tool can only be executed by users who are
members of at least one of the configured groups.

See also:

* admin/mcp/resource/review/get
* admin/mcp/resource/review/save
* admin/mcp/tools

## review/get

List of user groups that are allowed to view review items

```
admin/mcp/resource/review/get = 
```

* Type: array - List of user group names
* Since: 2026.10

The "review-get" and "review-search" MCP tools can only be executed by
users who are members of at least one of the configured groups.

See also:

* admin/mcp/resource/review/save
* admin/mcp/resource/review/delete
* admin/mcp/tools

## review/save

List of user groups that are allowed to create and update review items

```
admin/mcp/resource/review/save = 
```

* Type: array - List of user group names
* Since: 2026.10

The "review-save" MCP tool can only be executed by users who are members
of at least one of the configured groups.

See also:

* admin/mcp/resource/review/get
* admin/mcp/resource/review/delete
* admin/mcp/tools

## rule/delete

List of user groups that are allowed to delete rule items

```
admin/mcp/resource/rule/delete = 
```

* Type: array - List of user group names
* Since: 2026.10

The "rule-delete" MCP tool can only be executed by users who are members
of at least one of the configured groups.

See also:

* admin/mcp/resource/rule/get
* admin/mcp/resource/rule/save
* admin/mcp/tools

## rule/get

List of user groups that are allowed to view rule items

```
admin/mcp/resource/rule/get = 
```

* Type: array - List of user group names
* Since: 2026.10

The "rule-get", "rule-search" and "rule-config" MCP tools can only be
executed by users who are members of at least one of the configured
groups.

See also:

* admin/mcp/resource/rule/save
* admin/mcp/resource/rule/delete
* admin/mcp/tools

## rule/save

List of user groups that are allowed to create and update rule items

```
admin/mcp/resource/rule/save = 
```

* Type: array - List of user group names
* Since: 2026.10

The "rule-save" MCP tool can only be executed by users who are members
of at least one of the configured groups.

See also:

* admin/mcp/resource/rule/get
* admin/mcp/resource/rule/delete
* admin/mcp/tools

## service/delete

List of user groups that are allowed to delete service items

```
admin/mcp/resource/service/delete = 
```

* Type: array - List of user group names
* Since: 2026.10

The "service-delete" MCP tool can only be executed by users who are
members of at least one of the configured groups.

See also:

* admin/mcp/resource/service/get
* admin/mcp/resource/service/save
* admin/mcp/tools

## service/get

List of user groups that are allowed to view service items

```
admin/mcp/resource/service/get = 
```

* Type: array - List of user group names
* Since: 2026.10

The "service-get", "service-find", "service-search" and "service-config"
MCP tools can only be executed by users who are members of at least one
of the configured groups.

See also:

* admin/mcp/resource/service/save
* admin/mcp/resource/service/delete
* admin/mcp/tools

## service/save

List of user groups that are allowed to create and update service items

```
admin/mcp/resource/service/save = 
```

* Type: array - List of user group names
* Since: 2026.10

The "service-save" MCP tool can only be executed by users who are
members of at least one of the configured groups.

See also:

* admin/mcp/resource/service/get
* admin/mcp/resource/service/delete
* admin/mcp/tools

## stock/delete

List of user groups that are allowed to delete stock items

```
admin/mcp/resource/stock/delete = 
```

* Type: array - List of user group names
* Since: 2026.10

The "stock-delete" MCP tool can only be executed by users who are
members of at least one of the configured groups.

See also:

* admin/mcp/resource/stock/get
* admin/mcp/resource/stock/save
* admin/mcp/tools

## stock/get

List of user groups that are allowed to view stock items

```
admin/mcp/resource/stock/get = 
```

* Type: array - List of user group names
* Since: 2026.10

The "stock-get" and "stock-search" MCP tools can only be executed by
users who are members of at least one of the configured groups.

See also:

* admin/mcp/resource/stock/save
* admin/mcp/resource/stock/delete
* admin/mcp/tools

## stock/save

List of user groups that are allowed to create and update stock items

```
admin/mcp/resource/stock/save = 
```

* Type: array - List of user group names
* Since: 2026.10

The "stock-save" MCP tool can only be executed by users who are members
of at least one of the configured groups.

See also:

* admin/mcp/resource/stock/get
* admin/mcp/resource/stock/delete
* admin/mcp/tools

## subscription/delete

List of user groups that are allowed to delete subscription items

```
admin/mcp/resource/subscription/delete = 
```

* Type: array - List of user group names
* Since: 2026.10

The "subscription-delete" MCP tool can only be executed by users who are
members of at least one of the configured groups.

See also:

* admin/mcp/resource/subscription/get
* admin/mcp/resource/subscription/save
* admin/mcp/tools

## subscription/get

List of user groups that are allowed to view subscription items

```
admin/mcp/resource/subscription/get = 
```

* Type: array - List of user group names
* Since: 2026.10

The "subscription-get" and "subscription-search" MCP tools can only be
executed by users who are members of at least one of the configured
groups.

See also:

* admin/mcp/resource/subscription/save
* admin/mcp/resource/subscription/delete
* admin/mcp/tools

## subscription/save

List of user groups that are allowed to create and update subscription items

```
admin/mcp/resource/subscription/save = 
```

* Type: array - List of user group names
* Since: 2026.10

The "subscription-save" MCP tool can only be executed by users who are
members of at least one of the configured groups.

See also:

* admin/mcp/resource/subscription/get
* admin/mcp/resource/subscription/delete
* admin/mcp/tools

## supplier/delete

List of user groups that are allowed to delete supplier items

```
admin/mcp/resource/supplier/delete = 
```

* Type: array - List of user group names
* Since: 2026.10

The "supplier-delete" MCP tool can only be executed by users who are
members of at least one of the configured groups.

See also:

* admin/mcp/resource/supplier/get
* admin/mcp/resource/supplier/save
* admin/mcp/tools

## supplier/get

List of user groups that are allowed to view supplier items

```
admin/mcp/resource/supplier/get = 
```

* Type: array - List of user group names
* Since: 2026.10

The "supplier-get", "supplier-find" and "supplier-search" MCP tools can
only be executed by users who are members of at least one of the
configured groups.

See also:

* admin/mcp/resource/supplier/save
* admin/mcp/resource/supplier/delete
* admin/mcp/tools

## supplier/save

List of user groups that are allowed to create and update supplier items

```
admin/mcp/resource/supplier/save = 
```

* Type: array - List of user group names
* Since: 2026.10

The "supplier-save" MCP tool can only be executed by users who are
members of at least one of the configured groups.

See also:

* admin/mcp/resource/supplier/get
* admin/mcp/resource/supplier/delete
* admin/mcp/tools

## text/delete

List of user groups that are allowed to delete text items

```
admin/mcp/resource/text/delete = 
```

* Type: array - List of user group names
* Since: 2026.10

The "text-delete" MCP tool can only be executed by users who are members
of at least one of the configured groups.

See also:

* admin/mcp/resource/text/get
* admin/mcp/resource/text/save
* admin/mcp/tools

## text/get

List of user groups that are allowed to view text items

```
admin/mcp/resource/text/get = 
```

* Type: array - List of user group names
* Since: 2026.10

The "text-get" and "text-search" MCP tools can only be executed by users
who are members of at least one of the configured groups.

See also:

* admin/mcp/resource/text/save
* admin/mcp/resource/text/delete
* admin/mcp/tools

## text/save

List of user groups that are allowed to create and update text items

```
admin/mcp/resource/text/save = Array
(
    [0] => admin
    [1] => editor
    [2] => super
)
```

* Default: 
```
Array
(
)
```
* Type: array - List of user group names
* Since: 2026.10

The "text-save" MCP tool can only be executed by users who are members
of at least one of the configured groups.

See also:

* admin/mcp/resource/text/get
* admin/mcp/resource/text/delete
* admin/mcp/tools

# serialization
## max-depth

Maximum nesting level of referenced items returned by the MCP tools

```
admin/mcp/serialization/max-depth = 3
```

* Default: `3`
* Type: integer - Number of levels
* Since: 2026.10

Returned items contain their referenced items like list items,
addresses, properties, stock or child nodes, which can contain
referenced items themselves. This setting limits how deep these
references are followed to keep the responses small. A value of
"0" returns the items without any references.

See also:

* admin/mcp/lists-domains

# tools

List of tool classes offered to the MCP clients

```
admin/mcp/tools = Array
(
    [0] => Aimeos\Admin\Mcp\Tool\Ai\Write
    [1] => Aimeos\Admin\Mcp\Tool\Ai\Translate
    [2] => Aimeos\Admin\Mcp\Tool\Ai\Imagine
    [3] => Aimeos\Admin\Mcp\Tool\Ai\Isolate
    [4] => Aimeos\Admin\Mcp\Tool\Attribute\Get
    [5] => Aimeos\Admin\Mcp\Tool\Attribute\Find
    [6] => Aimeos\Admin\Mcp\Tool\Attribute\Search
    [7] => Aimeos\Admin\Mcp\Tool\Attribute\Save
    [8] => Aimeos\Admin\Mcp\Tool\Attribute\Delete
    [9] => Aimeos\Admin\Mcp\Tool\Catalog\Get
    [10] => Aimeos\Admin\Mcp\Tool\Catalog\Find
    [11] => Aimeos\Admin\Mcp\Tool\Catalog\Search
    [12] => Aimeos\Admin\Mcp\Tool\Catalog\Tree
    [13] => Aimeos\Admin\Mcp\Tool\Catalog\Path
    [14] => Aimeos\Admin\Mcp\Tool\Catalog\SearchTree
    [15] => Aimeos\Admin\Mcp\Tool\Catalog\Save
    [16] => Aimeos\Admin\Mcp\Tool\Catalog\Delete
    [17] => Aimeos\Admin\Mcp\Tool\Catalog\Insert
    [18] => Aimeos\Admin\Mcp\Tool\Catalog\Move
    [19] => Aimeos\Admin\Mcp\Tool\Coupon\Get
    [20] => Aimeos\Admin\Mcp\Tool\Coupon\Search
    [21] => Aimeos\Admin\Mcp\Tool\Coupon\Config
    [22] => Aimeos\Admin\Mcp\Tool\Coupon\Save
    [23] => Aimeos\Admin\Mcp\Tool\Coupon\Delete
    [24] => Aimeos\Admin\Mcp\Tool\Coupon\Code\Get
    [25] => Aimeos\Admin\Mcp\Tool\Coupon\Code\Search
    [26] => Aimeos\Admin\Mcp\Tool\Coupon\Code\Save
    [27] => Aimeos\Admin\Mcp\Tool\Coupon\Code\Delete
    [28] => Aimeos\Admin\Mcp\Tool\Customer\Get
    [29] => Aimeos\Admin\Mcp\Tool\Customer\Find
    [30] => Aimeos\Admin\Mcp\Tool\Customer\Search
    [31] => Aimeos\Admin\Mcp\Tool\Customer\Aggregate
    [32] => Aimeos\Admin\Mcp\Tool\Customer\Save
    [33] => Aimeos\Admin\Mcp\Tool\Customer\Delete
    [34] => Aimeos\Admin\Mcp\Tool\Group\Get
    [35] => Aimeos\Admin\Mcp\Tool\Group\Search
    [36] => Aimeos\Admin\Mcp\Tool\Group\Save
    [37] => Aimeos\Admin\Mcp\Tool\Group\Delete
    [38] => Aimeos\Admin\Mcp\Tool\Index\Search
    [39] => Aimeos\Admin\Mcp\Tool\Index\Aggregate
    [40] => Aimeos\Admin\Mcp\Tool\Locale\Get
    [41] => Aimeos\Admin\Mcp\Tool\Locale\Search
    [42] => Aimeos\Admin\Mcp\Tool\Locale\Save
    [43] => Aimeos\Admin\Mcp\Tool\Locale\Delete
    [44] => Aimeos\Admin\Mcp\Tool\Locale\Language\Get
    [45] => Aimeos\Admin\Mcp\Tool\Locale\Language\Search
    [46] => Aimeos\Admin\Mcp\Tool\Locale\Language\Save
    [47] => Aimeos\Admin\Mcp\Tool\Locale\Language\Delete
    [48] => Aimeos\Admin\Mcp\Tool\Locale\Currency\Get
    [49] => Aimeos\Admin\Mcp\Tool\Locale\Currency\Search
    [50] => Aimeos\Admin\Mcp\Tool\Locale\Currency\Save
    [51] => Aimeos\Admin\Mcp\Tool\Locale\Currency\Delete
    [52] => Aimeos\Admin\Mcp\Tool\Locale\Site\Get
    [53] => Aimeos\Admin\Mcp\Tool\Locale\Site\Find
    [54] => Aimeos\Admin\Mcp\Tool\Locale\Site\Search
    [55] => Aimeos\Admin\Mcp\Tool\Locale\Site\Tree
    [56] => Aimeos\Admin\Mcp\Tool\Locale\Site\Path
    [57] => Aimeos\Admin\Mcp\Tool\Locale\Site\SearchTree
    [58] => Aimeos\Admin\Mcp\Tool\Locale\Site\Save
    [59] => Aimeos\Admin\Mcp\Tool\Locale\Site\Delete
    [60] => Aimeos\Admin\Mcp\Tool\Locale\Site\Insert
    [61] => Aimeos\Admin\Mcp\Tool\Locale\Site\Move
    [62] => Aimeos\Admin\Mcp\Tool\Media\Get
    [63] => Aimeos\Admin\Mcp\Tool\Media\Search
    [64] => Aimeos\Admin\Mcp\Tool\Media\Save
    [65] => Aimeos\Admin\Mcp\Tool\Media\Delete
    [66] => Aimeos\Admin\Mcp\Tool\Order\Get
    [67] => Aimeos\Admin\Mcp\Tool\Order\Search
    [68] => Aimeos\Admin\Mcp\Tool\Order\Aggregate
    [69] => Aimeos\Admin\Mcp\Tool\Order\Save
    [70] => Aimeos\Admin\Mcp\Tool\Plugin\Get
    [71] => Aimeos\Admin\Mcp\Tool\Plugin\Search
    [72] => Aimeos\Admin\Mcp\Tool\Plugin\Config
    [73] => Aimeos\Admin\Mcp\Tool\Plugin\Save
    [74] => Aimeos\Admin\Mcp\Tool\Plugin\Delete
    [75] => Aimeos\Admin\Mcp\Tool\Price\Get
    [76] => Aimeos\Admin\Mcp\Tool\Price\Search
    [77] => Aimeos\Admin\Mcp\Tool\Price\Save
    [78] => Aimeos\Admin\Mcp\Tool\Price\Delete
    [79] => Aimeos\Admin\Mcp\Tool\Product\Get
    [80] => Aimeos\Admin\Mcp\Tool\Product\Find
    [81] => Aimeos\Admin\Mcp\Tool\Product\Search
    [82] => Aimeos\Admin\Mcp\Tool\Product\Save
    [83] => Aimeos\Admin\Mcp\Tool\Product\Delete
    [84] => Aimeos\Admin\Mcp\Tool\Review\Get
    [85] => Aimeos\Admin\Mcp\Tool\Review\Search
    [86] => Aimeos\Admin\Mcp\Tool\Review\Save
    [87] => Aimeos\Admin\Mcp\Tool\Review\Delete
    [88] => Aimeos\Admin\Mcp\Tool\Rule\Get
    [89] => Aimeos\Admin\Mcp\Tool\Rule\Search
    [90] => Aimeos\Admin\Mcp\Tool\Rule\Config
    [91] => Aimeos\Admin\Mcp\Tool\Rule\Save
    [92] => Aimeos\Admin\Mcp\Tool\Rule\Delete
    [93] => Aimeos\Admin\Mcp\Tool\Service\Get
    [94] => Aimeos\Admin\Mcp\Tool\Service\Find
    [95] => Aimeos\Admin\Mcp\Tool\Service\Search
    [96] => Aimeos\Admin\Mcp\Tool\Service\Config
    [97] => Aimeos\Admin\Mcp\Tool\Service\Save
    [98] => Aimeos\Admin\Mcp\Tool\Service\Delete
    [99] => Aimeos\Admin\Mcp\Tool\Stock\Get
    [100] => Aimeos\Admin\Mcp\Tool\Stock\Search
    [101] => Aimeos\Admin\Mcp\Tool\Stock\Save
    [102] => Aimeos\Admin\Mcp\Tool\Stock\Delete
    [103] => Aimeos\Admin\Mcp\Tool\Subscription\Get
    [104] => Aimeos\Admin\Mcp\Tool\Subscription\Search
    [105] => Aimeos\Admin\Mcp\Tool\Subscription\Save
    [106] => Aimeos\Admin\Mcp\Tool\Subscription\Delete
    [107] => Aimeos\Admin\Mcp\Tool\Supplier\Get
    [108] => Aimeos\Admin\Mcp\Tool\Supplier\Find
    [109] => Aimeos\Admin\Mcp\Tool\Supplier\Search
    [110] => Aimeos\Admin\Mcp\Tool\Supplier\Save
    [111] => Aimeos\Admin\Mcp\Tool\Supplier\Delete
    [112] => Aimeos\Admin\Mcp\Tool\Text\Get
    [113] => Aimeos\Admin\Mcp\Tool\Text\Search
    [114] => Aimeos\Admin\Mcp\Tool\Text\Save
    [115] => Aimeos\Admin\Mcp\Tool\Text\Delete
)
```

* Default: 
```
Array
(
    [0] => Aimeos\Admin\Mcp\Tool\Ai\Write
    [1] => Aimeos\Admin\Mcp\Tool\Ai\Translate
    [2] => Aimeos\Admin\Mcp\Tool\Ai\Imagine
    [3] => Aimeos\Admin\Mcp\Tool\Ai\Isolate
    [4] => Aimeos\Admin\Mcp\Tool\Attribute\Get
    [5] => Aimeos\Admin\Mcp\Tool\Attribute\Find
    [6] => Aimeos\Admin\Mcp\Tool\Attribute\Search
    [7] => Aimeos\Admin\Mcp\Tool\Attribute\Save
    [8] => Aimeos\Admin\Mcp\Tool\Attribute\Delete
    [9] => Aimeos\Admin\Mcp\Tool\Catalog\Get
    [10] => Aimeos\Admin\Mcp\Tool\Catalog\Find
    [11] => Aimeos\Admin\Mcp\Tool\Catalog\Search
    [12] => Aimeos\Admin\Mcp\Tool\Catalog\Tree
    [13] => Aimeos\Admin\Mcp\Tool\Catalog\Path
    [14] => Aimeos\Admin\Mcp\Tool\Catalog\SearchTree
    [15] => Aimeos\Admin\Mcp\Tool\Catalog\Save
    [16] => Aimeos\Admin\Mcp\Tool\Catalog\Delete
    [17] => Aimeos\Admin\Mcp\Tool\Catalog\Insert
    [18] => Aimeos\Admin\Mcp\Tool\Catalog\Move
    [19] => Aimeos\Admin\Mcp\Tool\Coupon\Get
    [20] => Aimeos\Admin\Mcp\Tool\Coupon\Search
    [21] => Aimeos\Admin\Mcp\Tool\Coupon\Config
    [22] => Aimeos\Admin\Mcp\Tool\Coupon\Save
    [23] => Aimeos\Admin\Mcp\Tool\Coupon\Delete
    [24] => Aimeos\Admin\Mcp\Tool\Coupon\Code\Get
    [25] => Aimeos\Admin\Mcp\Tool\Coupon\Code\Search
    [26] => Aimeos\Admin\Mcp\Tool\Coupon\Code\Save
    [27] => Aimeos\Admin\Mcp\Tool\Coupon\Code\Delete
    [28] => Aimeos\Admin\Mcp\Tool\Customer\Get
    [29] => Aimeos\Admin\Mcp\Tool\Customer\Find
    [30] => Aimeos\Admin\Mcp\Tool\Customer\Search
    [31] => Aimeos\Admin\Mcp\Tool\Customer\Aggregate
    [32] => Aimeos\Admin\Mcp\Tool\Customer\Save
    [33] => Aimeos\Admin\Mcp\Tool\Customer\Delete
    [34] => Aimeos\Admin\Mcp\Tool\Group\Get
    [35] => Aimeos\Admin\Mcp\Tool\Group\Search
    [36] => Aimeos\Admin\Mcp\Tool\Group\Save
    [37] => Aimeos\Admin\Mcp\Tool\Group\Delete
    [38] => Aimeos\Admin\Mcp\Tool\Index\Search
    [39] => Aimeos\Admin\Mcp\Tool\Index\Aggregate
    [40] => Aimeos\Admin\Mcp\Tool\Locale\Get
    [41] => Aimeos\Admin\Mcp\Tool\Locale\Search
    [42] => Aimeos\Admin\Mcp\Tool\Locale\Save
    [43] => Aimeos\Admin\Mcp\Tool\Locale\Delete
    [44] => Aimeos\Admin\Mcp\Tool\Locale\Language\Get
    [45] => Aimeos\Admin\Mcp\Tool\Locale\Language\Search
    [46] => Aimeos\Admin\Mcp\Tool\Locale\Language\Save
    [47] => Aimeos\Admin\Mcp\Tool\Locale\Language\Delete
    [48] => Aimeos\Admin\Mcp\Tool\Locale\Currency\Get
    [49] => Aimeos\Admin\Mcp\Tool\Locale\Currency\Search
    [50] => Aimeos\Admin\Mcp\Tool\Locale\Currency\Save
    [51] => Aimeos\Admin\Mcp\Tool\Locale\Currency\Delete
    [52] => Aimeos\Admin\Mcp\Tool\Locale\Site\Get
    [53] => Aimeos\Admin\Mcp\Tool\Locale\Site\Find
    [54] => Aimeos\Admin\Mcp\Tool\Locale\Site\Search
    [55] => Aimeos\Admin\Mcp\Tool\Locale\Site\Tree
    [56] => Aimeos\Admin\Mcp\Tool\Locale\Site\Path
    [57] => Aimeos\Admin\Mcp\Tool\Locale\Site\SearchTree
    [58] => Aimeos\Admin\Mcp\Tool\Locale\Site\Save
    [59] => Aimeos\Admin\Mcp\Tool\Locale\Site\Delete
    [60] => Aimeos\Admin\Mcp\Tool\Locale\Site\Insert
    [61] => Aimeos\Admin\Mcp\Tool\Locale\Site\Move
    [62] => Aimeos\Admin\Mcp\Tool\Media\Get
    [63] => Aimeos\Admin\Mcp\Tool\Media\Search
    [64] => Aimeos\Admin\Mcp\Tool\Media\Save
    [65] => Aimeos\Admin\Mcp\Tool\Media\Delete
    [66] => Aimeos\Admin\Mcp\Tool\Order\Get
    [67] => Aimeos\Admin\Mcp\Tool\Order\Search
    [68] => Aimeos\Admin\Mcp\Tool\Order\Aggregate
    [69] => Aimeos\Admin\Mcp\Tool\Order\Save
    [70] => Aimeos\Admin\Mcp\Tool\Plugin\Get
    [71] => Aimeos\Admin\Mcp\Tool\Plugin\Search
    [72] => Aimeos\Admin\Mcp\Tool\Plugin\Config
    [73] => Aimeos\Admin\Mcp\Tool\Plugin\Save
    [74] => Aimeos\Admin\Mcp\Tool\Plugin\Delete
    [75] => Aimeos\Admin\Mcp\Tool\Price\Get
    [76] => Aimeos\Admin\Mcp\Tool\Price\Search
    [77] => Aimeos\Admin\Mcp\Tool\Price\Save
    [78] => Aimeos\Admin\Mcp\Tool\Price\Delete
    [79] => Aimeos\Admin\Mcp\Tool\Product\Get
    [80] => Aimeos\Admin\Mcp\Tool\Product\Find
    [81] => Aimeos\Admin\Mcp\Tool\Product\Search
    [82] => Aimeos\Admin\Mcp\Tool\Product\Save
    [83] => Aimeos\Admin\Mcp\Tool\Product\Delete
    [84] => Aimeos\Admin\Mcp\Tool\Review\Get
    [85] => Aimeos\Admin\Mcp\Tool\Review\Search
    [86] => Aimeos\Admin\Mcp\Tool\Review\Save
    [87] => Aimeos\Admin\Mcp\Tool\Review\Delete
    [88] => Aimeos\Admin\Mcp\Tool\Rule\Get
    [89] => Aimeos\Admin\Mcp\Tool\Rule\Search
    [90] => Aimeos\Admin\Mcp\Tool\Rule\Config
    [91] => Aimeos\Admin\Mcp\Tool\Rule\Save
    [92] => Aimeos\Admin\Mcp\Tool\Rule\Delete
    [93] => Aimeos\Admin\Mcp\Tool\Service\Get
    [94] => Aimeos\Admin\Mcp\Tool\Service\Find
    [95] => Aimeos\Admin\Mcp\Tool\Service\Search
    [96] => Aimeos\Admin\Mcp\Tool\Service\Config
    [97] => Aimeos\Admin\Mcp\Tool\Service\Save
    [98] => Aimeos\Admin\Mcp\Tool\Service\Delete
    [99] => Aimeos\Admin\Mcp\Tool\Stock\Get
    [100] => Aimeos\Admin\Mcp\Tool\Stock\Search
    [101] => Aimeos\Admin\Mcp\Tool\Stock\Save
    [102] => Aimeos\Admin\Mcp\Tool\Stock\Delete
    [103] => Aimeos\Admin\Mcp\Tool\Subscription\Get
    [104] => Aimeos\Admin\Mcp\Tool\Subscription\Search
    [105] => Aimeos\Admin\Mcp\Tool\Subscription\Save
    [106] => Aimeos\Admin\Mcp\Tool\Subscription\Delete
    [107] => Aimeos\Admin\Mcp\Tool\Supplier\Get
    [108] => Aimeos\Admin\Mcp\Tool\Supplier\Find
    [109] => Aimeos\Admin\Mcp\Tool\Supplier\Search
    [110] => Aimeos\Admin\Mcp\Tool\Supplier\Save
    [111] => Aimeos\Admin\Mcp\Tool\Supplier\Delete
    [112] => Aimeos\Admin\Mcp\Tool\Text\Get
    [113] => Aimeos\Admin\Mcp\Tool\Text\Search
    [114] => Aimeos\Admin\Mcp\Tool\Text\Save
    [115] => Aimeos\Admin\Mcp\Tool\Text\Delete
)
```
* Type: array - List of fully qualified class names
* Since: 2026.10

By default, all built-in tools are available and the user groups
allowed to execute them are configured below "admin/mcp/resource".
If you set this option, your list replaces the built-in tools
completely. Use it to offer only a subset of the tools to the MCP
clients or to add your own tools, e.g.

```
 'admin/mcp/tools' => [
     \Aimeos\Admin\Mcp\Tool\Product\Get::class,
     \Aimeos\Admin\Mcp\Tool\Product\Search::class,
     \MyVendor\Admin\Mcp\Tool\Product\Import::class,
 ]
```

Each class must extend \Aimeos\Admin\Mcp\Tool and the tool names
must be unique.

See also:

* admin/mcp/resource/product/get

# debug

Send debug information withing responses to clients if an error occurrs

```
admin/graphql/debug = 1
```

* Default: ``
* Type: boolean - True to return the stack trace in response, false for error message only
* Since: 2022.10

By default, the Aimeos admin GraphQL API won't send any details
besides the error message to the client if an error occurred. This
prevents leaking sensitive information to attackers. For debugging
your requests it's helpful to see the stack strace. If you set this
configuration option to true, the stack trace will be returned too.


# domains

List of domains available via the GraphQL API

```
admin/graphql/domains = Array
(
    [ai] => ai
    [attribute] => attribute
    [attribute/type] => attribute/type
    [attribute/lists/type] => attribute/lists/type
    [attribute/property/type] => attribute/property/type
    [catalog] => catalog
    [catalog/lists/type] => catalog/lists/type
    [coupon] => coupon
    [coupon/code] => coupon/code
    [customer] => customer
    [customer/lists/type] => customer/lists/type
    [customer/property/type] => customer/property/type
    [group] => group
    [index] => index
    [locale] => locale
    [locale/currency] => locale/currency
    [locale/language] => locale/language
    [locale/site] => locale/site
    [media] => media
    [media/type] => media/type
    [media/lists/type] => media/lists/type
    [media/property/type] => media/property/type
    [order] => order
    [order/status] => order/status
    [plugin] => plugin
    [plugin/type] => plugin/type
    [price] => price
    [price/type] => price/type
    [price/lists/type] => price/lists/type
    [price/property/type] => price/property/type
    [product] => product
    [product/type] => product/type
    [product/lists/type] => product/lists/type
    [product/property/type] => product/property/type
    [review] => review
    [rule] => rule
    [rule/type] => rule/type
    [service] => service
    [service/type] => service/type
    [service/lists/type] => service/lists/type
    [stock] => stock
    [stock/type] => stock/type
    [subscription] => subscription
    [supplier] => supplier
    [supplier/lists/type] => supplier/lists/type
    [tag] => tag
    [tag/type] => tag/type
    [text] => text
    [text/type] => text/type
    [text/lists/type] => text/lists/type
    [type] => type
    [feed] => feed
)
```

* Default: 
```
Array
(
)
```
* Type: array - Associative list of domain names as keys and values
* Since: 2022.10

Queries and mutations are only available for the domains in this
list. Remove domains you don't want to manage via GraphQL or add the
domains of your own extensions. The class used for each domain is
configured by "admin/graphql/<domain>/name" and users also need the
permissions configured below "admin/graphql/resource".

See also:

* admin/graphql/name
* admin/graphql/lists-domains

# lists-domains

Domains of the referenced items available via list items

```
admin/graphql/lists-domains = Array
(
    [attribute] => attribute
    [catalog] => catalog
    [customer] => customer
    [group] => group
    [media] => media
    [price] => price
    [product] => product
    [service] => service
    [supplier] => supplier
    [tag] => tag
    [text] => text
)
```

* Default: 
```
Array
(
)
```
* Type: array - Associative list of domain names as keys and values
* Since: 2022.10

Items like products or catalogs can reference other items via list
items, e.g. texts, prices or media. GraphQL clients can only fetch
and save referenced items of the domains in this list together with
the parent item. Add the domains of your own extensions if their
items should be available as references too.

See also:

* admin/graphql/domains

# max-query-complexity

Maximum complexity of GraphQL queries

```
admin/graphql/max-query-complexity = 500
```

* Default: `500`
* Type: integer - Maximum complexity score
* Since: 2026.04

The complexity of a query is the number of fields it requests,
including all fields of nested items. Requests with queries more
complex than this value are rejected with an error to protect the
server against expensive requests.

See also:

* admin/graphql/max-query-depth

# max-query-depth

Maximum nesting level of the fields in GraphQL queries

```
admin/graphql/max-query-depth = 10
```

* Default: `10`
* Type: integer - Number of levels
* Since: 2026.04

Deeply nested queries can be very expensive to resolve and may be
used to overload the server. Requests with queries nested deeper
than this value are rejected with an error. Increase the value if
your clients need to fetch more levels of referenced items.

See also:

* admin/graphql/max-query-complexity

# name

Class name of the GraphQL implementation used for all domains

```
admin/graphql/name = Standard
```

* Default: `Standard`
* Type: string - Last part of the class name
* Since: 2022.10

The GraphQL queries and mutations of each domain are provided by the
class configured in "admin/graphql/<domain>/name", e.g.

```
 admin/graphql/product/name = Myproduct
```

uses \Aimeos\Admin\Graphql\Product\Myproduct. For sub-domains like
"product/lists/type", the class is \Aimeos\Admin\Graphql\Product\Lists\Type\...
If no such class exists, the class configured by this setting is used
instead, which is \Aimeos\Admin\Graphql\Standard by default.

The value is the last part of your own class name and it's case
sensitive, so take care that the configuration value is exactly named
like the last part of the class name.

See also:

* admin/graphql/domains
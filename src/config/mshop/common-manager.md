
# aggregate
## limit

Limits the number of records that are used when aggregating items

```
mshop/common/manager/aggregate/limit = 10000
```

* Default: 10000
* Type: integer - Number of records
* Since: 2021.04

As counting huge amount of records (several 10 000 records) takes a long time,
the limit can cut down response times so the counts are available more quickly
in the front-end and the server load is reduced.

Using a low limit can lead to incorrect numbers if the amount of found items
is very high. Approximate item counts are normally not a problem but it can
lead to the situation that visitors see that no items are available despite
the fact that there would be at least one.


# decorators
## default

Configures the list of decorators applied to all shop managers

```
mshop/common/manager/decorators/default = Array
(
    [Depth] => Depth
    [Lazy] => Lazy
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to configure a list of decorator names that should
be wrapped around the original instances of all created managers:

```
 mshop/common/manager/decorators/default = array( 'decorator1', 'decorator2' )
```

This would wrap the decorators named "decorator1" and "decorator2" around
all controller instances in that order. The decorator classes would be
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" and
"\Aimeos\MShop\Common\Manager\Decorator\Decorator2".


# maxdepth

Maximum level of recursion for retrieving referenced items

```
mshop/common/manager/maxdepth = 2
```

* Default: 2
* Type: int - Number of levels
* Since: 2019.04

Searching for items also fetches the associated items referenced in the
list tables if the domain names are passed to the second parameter of e.g. the
search() method. To avoid infinite recursion because two items reference
each other, the maximum level must be limited.

The default setting (two levels) means that retrieving a product item with
sub-products will retrieve the directly associated products but not the
products referenced by the associated product for example.

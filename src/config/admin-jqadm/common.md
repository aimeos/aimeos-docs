
# decorators
## default

Configures the list of decorators applied to all jqadm clients

```
admin/jqadm/common/decorators/default = Array
(
    [0] => Page
)
```

* Default: 
```
Array
(
)
```
* Type: array - List of decorator names
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to configure a list of decorator names that should
be wrapped around the original instance of all created clients:

```
 admin/jqadm/common/decorators/default = array( 'decorator1', 'decorator2' )
```

This would wrap the decorators named "decorator1" and "decorator2" around
all client instances in that order. The decorator classes would be
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" and
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator2".


# navbar

List of JQAdm client names shown in the navigation bar of the admin interface

```
admin/jqadm/navbar = Array
(
    [0] => dashboard
    [10] => Array
        (
            [_] => sales
            [10] => order
            [20] => subscription
            [30] => basket
        )

    [20] => Array
        (
            [_] => goods
            [10] => product
            [20] => catalog
            [30] => attribute
            [40] => supplier
        )

    [30] => Array
        (
            [_] => users
            [10] => customer
            [20] => group
        )

    [40] => Array
        (
            [_] => marketing
            [10] => coupon
            [20] => rule
            [30] => review
            [95] => feed
        )

    [50] => settings
    [60] => Array
        (
            [_] => setup
            [20] => service
            [30] => plugin
        )

    [70] => Array
        (
            [_] => locale
            [10] => locale
            [20] => locale/site
            [30] => locale/language
            [40] => locale/currency
        )

    [80] => type
    [90] => log
    [45] => cms
)
```

* Default: 
```
Array
(
)
```
* Type: array - List of resource client names
* Since: 2017.10

You can add, remove or reorder the links in the navigation bar by
setting a new list of client resource names.
In the configuration files of extensions, you should only add entries using
one of these lines:

```
 'myclient' => 'myclient',
 'myclient-subclient' => 'myclient/subclient',
```

The key of the new client must be unique in the extension configuration so
it's not overwritten by other extensions. Don't use slashes in keys (/)
because they are interpreted as keys of sub-arrays in the configuration.

See also:

* admin/jqadm/navbar-limit
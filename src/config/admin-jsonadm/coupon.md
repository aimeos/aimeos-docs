
# config
## decorators/excludes

Excludes decorators added by the "common" option from the JSON API clients

```
admin/jsonadm/coupon/config/decorators/excludes = Array
(
)
```

* Default: 
```
Array
(
)
```
* Type: array - List of decorator names
* Since: 2017.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"admin/jsonadm/common/decorators/default" before they are wrapped
around the Jsonadm client.

```
 admin/jsonadm/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JsonAdm\Common\Decorator\*") added via
"admin/jsonadm/common/decorators/default" for the JSON API client.

See also:

* admin/jsonadm/common/decorators/default
* admin/jsonadm/coupon/config/decorators/global
* admin/jsonadm/coupon/config/decorators/local

## decorators/global

Adds a list of globally available decorators only to the Jsonadm client

```
admin/jsonadm/coupon/config/decorators/global = Array
(
)
```

* Default: 
```
Array
(
)
```
* Type: array - List of decorator names
* Since: 2017.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\Jsonadm\Common\Decorator\*") around the Jsonadm
client.

```
 admin/jsonadm/coupon/config/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\Jsonadm\Common\Decorator\Decorator1" only to the
"coupon/config" Jsonadm client.

See also:

* admin/jsonadm/common/decorators/default
* admin/jsonadm/coupon/config/decorators/excludes
* admin/jsonadm/coupon/config/decorators/local

## decorators/local

Adds a list of local decorators only to the Jsonadm client

```
admin/jsonadm/coupon/config/decorators/local = Array
(
)
```

* Default: 
```
Array
(
)
```
* Type: array - List of decorator names
* Since: 2017.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\Jsonadm\Coupon\Config\Decorator\*") around the Jsonadm
client.

```
 admin/jsonadm/coupon/config/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\Jsonadm\Coupon\Config\Decorator\Decorator2" only to the
"coupon/config" Jsonadm client.

See also:

* admin/jsonadm/common/decorators/default
* admin/jsonadm/coupon/config/decorators/excludes
* admin/jsonadm/coupon/config/decorators/global

## name

```
admin/jsonadm/coupon/config/name = Standard
```

* Default: `Standard`


## template-get

Relative path to the JSON API template for GET requests

```
admin/jsonadm/coupon/config/template-get = config
```

* Default: `config`
* Type: string - Relative path to the template creating the body for the GET method of the JSON API
* Since: 2017.07

The template file contains the code and processing instructions
to generate the result shown in the JSON API body. The
configuration string is the path to the template file relative
to the templates directory (usually in templates/admin/jsonadm).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "standard" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "standard"
should be replaced by the name of the new class.


# decorators
## excludes

Excludes decorators added by the "common" option from the JSON API clients

```
admin/jsonadm/coupon/decorators/excludes = 
```

* Type: array - List of decorator names
* Since: 2016.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"admin/jsonadm/common/decorators/default" before they are wrapped
around the Jsonadm client.

```
 admin/jsonadm/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JsonAdm\Common\Decorator\*") added via
"admin/jsonadm/common/decorators/default" for the JSON API client.

See also:

* admin/jsonadm/common/decorators/default
* admin/jsonadm/coupon/decorators/global
* admin/jsonadm/coupon/decorators/local

## global

Adds a list of globally available decorators only to the Jsonadm client

```
admin/jsonadm/coupon/decorators/global = 
```

* Type: array - List of decorator names
* Since: 2016.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\Jsonadm\Common\Decorator\*") around the Jsonadm
client.

```
 admin/jsonadm/coupon/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\Jsonadm\Common\Decorator\Decorator1" only to the
"coupon" Jsonadm client.

See also:

* admin/jsonadm/common/decorators/default
* admin/jsonadm/coupon/decorators/excludes
* admin/jsonadm/coupon/decorators/local

## local

Adds a list of local decorators only to the Jsonadm client

```
admin/jsonadm/coupon/decorators/local = 
```

* Type: array - List of decorator names
* Since: 2016.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\Jsonadm\Coupon\Decorator\*") around the Jsonadm
client.

```
 admin/jsonadm/coupon/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\Jsonadm\Coupon\Decorator\Decorator2" only to the
"coupon" Jsonadm client.

See also:

* admin/jsonadm/common/decorators/default
* admin/jsonadm/coupon/decorators/excludes
* admin/jsonadm/coupon/decorators/global
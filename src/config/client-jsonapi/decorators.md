
# excludes

Excludes decorators added by the "common" option from the JSON API clients

```
client/jsonapi/decorators/excludes = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2016.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"client/jsonapi/common/decorators/default" before they are wrapped
around the Jsonadm client.

```
 client/jsonapi/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Client\JsonApi\Common\Decorator\*") added via
"client/jsonapi/common/decorators/default" for the JSON API client.

See also:

* client/jsonapi/common/decorators/default
* client/jsonapi/decorators/global
* client/jsonapi/decorators/local

# global

Adds a list of globally available decorators only to the Jsonadm client

```
client/jsonapi/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2016.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Client\Jsonadm\Common\Decorator\*") around the Jsonadm
client.

```
 client/jsonapi/product/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Client\Jsonadm\Common\Decorator\Decorator1" only to the
"product" Jsonadm client.

See also:

* client/jsonapi/common/decorators/default
* client/jsonapi/decorators/excludes
* client/jsonapi/decorators/local

# local

Adds a list of local decorators only to the Jsonadm client

```
client/jsonapi/decorators/local = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2016.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Client\Jsonadm\Product\Decorator\*") around the Jsonadm
client.

```
 client/jsonapi/product/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Client\Jsonadm\Product\Decorator\Decorator2" only to the
"product" Jsonadm client.

See also:

* client/jsonapi/common/decorators/default
* client/jsonapi/decorators/excludes
* client/jsonapi/decorators/global
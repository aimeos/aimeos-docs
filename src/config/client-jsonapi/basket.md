
# address
## decorators/excludes

Excludes decorators added by the "common" option from the JSON API clients

```
client/jsonapi/basket/address/decorators/excludes = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2017.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"client/jsonapi/common/decorators/default" before they are wrapped
around the JsonApi client.

```
 client/jsonapi/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Client\JsonApi\Common\Decorator\*") added via
"client/jsonapi/common/decorators/default" for the JSON API client.

See also:

* client/jsonapi/common/decorators/default
* client/jsonapi/basket/address/decorators/global
* client/jsonapi/basket/address/decorators/local

## decorators/global

Adds a list of globally available decorators only to the JsonApi client

```
client/jsonapi/basket/address/decorators/global = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2017.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Client\JsonApi\Common\Decorator\*") around the JsonApi
client.

```
 client/jsonapi/basket/address/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Client\JsonApi\Common\Decorator\Decorator1" only to the
"basket" JsonApi client.

See also:

* client/jsonapi/common/decorators/default
* client/jsonapi/basket/address/decorators/excludes
* client/jsonapi/basket/address/decorators/local

## decorators/local

Adds a list of local decorators only to the JsonApi client

```
client/jsonapi/basket/address/decorators/local = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2017.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Client\JsonApi\Basket\Address\Decorator\*") around the JsonApi
client.

```
 client/jsonapi/basket/address/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Client\JsonApi\Basket\Address\Decorator\Decorator2" only to the
"basket address" JsonApi client.

See also:

* client/jsonapi/common/decorators/default
* client/jsonapi/basket/address/decorators/excludes
* client/jsonapi/basket/address/decorators/global

## name

Class name of the used basket/address client implementation

```
client/jsonapi/basket/address/name = 
```

* Default: 
* Type: string - Last part of the class name
* Since: 2017.03

Each default JSON API client can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the client factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Client\JsonApi\Basket\Address\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Client\JsonApi\Basket\Address\Mybasket/address
```

then you have to set the this configuration option:

```
 client/jsonapi/basket/address/name = Mybasket/address
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyAddress"!


# coupon
## decorators/excludes

Excludes decorators added by the "common" option from the JSON API clients

```
client/jsonapi/basket/coupon/decorators/excludes = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2017.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"client/jsonapi/common/decorators/default" before they are wrapped
around the JsonApi client.

```
 client/jsonapi/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Client\JsonApi\Common\Decorator\*") added via
"client/jsonapi/common/decorators/default" for the JSON API client.

See also:

* client/jsonapi/common/decorators/default
* client/jsonapi/basket/coupon/decorators/global
* client/jsonapi/basket/coupon/decorators/local

## decorators/global

Adds a list of globally available decorators only to the JsonApi client

```
client/jsonapi/basket/coupon/decorators/global = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2017.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Client\JsonApi\Common\Decorator\*") around the JsonApi
client.

```
 client/jsonapi/basket/coupon/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Client\JsonApi\Common\Decorator\Decorator1" only to the
"basket" JsonApi client.

See also:

* client/jsonapi/common/decorators/default
* client/jsonapi/basket/coupon/decorators/excludes
* client/jsonapi/basket/coupon/decorators/local

## decorators/local

Adds a list of local decorators only to the JsonApi client

```
client/jsonapi/basket/coupon/decorators/local = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2017.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Client\JsonApi\Basket\Coupon\Decorator\*") around the JsonApi
client.

```
 client/jsonapi/basket/coupon/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Client\JsonApi\Basket\Coupon\Decorator\Decorator2" only to the
"basket coupon" JsonApi client.

See also:

* client/jsonapi/common/decorators/default
* client/jsonapi/basket/coupon/decorators/excludes
* client/jsonapi/basket/coupon/decorators/global

## name

Class name of the used basket/coupon client implementation

```
client/jsonapi/basket/coupon/name = 
```

* Default: 
* Type: string - Last part of the class name
* Since: 2017.03

Each default JSON API client can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the client factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Client\JsonApi\Basket\Coupon\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Client\JsonApi\Basket\Coupon\Mybasket/coupon
```

then you have to set the this configuration option:

```
 client/jsonapi/basket/coupon/name = Mybasket/coupon
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyCoupon"!


# decorators
## excludes

Excludes decorators added by the "common" option from the JSON API clients

```
client/jsonapi/basket/decorators/excludes = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2017.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"client/jsonapi/common/decorators/default" before they are wrapped
around the JsonApi client.

```
 client/jsonapi/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Client\JsonApi\Common\Decorator\*") added via
"client/jsonapi/common/decorators/default" for the JSON API client.

See also:

* client/jsonapi/common/decorators/default
* client/jsonapi/basket/decorators/global
* client/jsonapi/basket/decorators/local

## global

Adds a list of globally available decorators only to the JsonApi client

```
client/jsonapi/basket/decorators/global = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2017.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Client\JsonApi\Common\Decorator\*") around the JsonApi
client.

```
 client/jsonapi/basket/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Client\JsonApi\Common\Decorator\Decorator1" only to the
"basket" JsonApi client.

See also:

* client/jsonapi/common/decorators/default
* client/jsonapi/basket/decorators/excludes
* client/jsonapi/basket/decorators/local

## local

Adds a list of local decorators only to the JsonApi client

```
client/jsonapi/basket/decorators/local = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2017.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Client\JsonApi\Basket\Decorator\*") around the JsonApi
client.

```
 client/jsonapi/basket/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Client\JsonApi\Basket\Decorator\Decorator2" only to the
"basket" JsonApi client.

See also:

* client/jsonapi/common/decorators/default
* client/jsonapi/basket/decorators/excludes
* client/jsonapi/basket/decorators/global

# name

Class name of the used basket client implementation

```
client/jsonapi/basket/name = 
```

* Default: 
* Type: string - Last part of the class name
* Since: 2017.03

Each default JSON API client can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the client factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Client\JsonApi\Basket\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Client\JsonApi\Basket\Mybasket
```

then you have to set the this configuration option:

```
 client/jsonapi/basket/name = Mybasket
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyBasket"!


# product
## decorators/excludes

Excludes decorators added by the "common" option from the JSON API clients

```
client/jsonapi/basket/product/decorators/excludes = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2017.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"client/jsonapi/common/decorators/default" before they are wrapped
around the JsonApi client.

```
 client/jsonapi/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Client\JsonApi\Common\Decorator\*") added via
"client/jsonapi/common/decorators/default" for the JSON API client.

See also:

* client/jsonapi/common/decorators/default
* client/jsonapi/basket/product/decorators/global
* client/jsonapi/basket/product/decorators/local

## decorators/global

Adds a list of globally available decorators only to the JsonApi client

```
client/jsonapi/basket/product/decorators/global = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2017.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Client\JsonApi\Common\Decorator\*") around the JsonApi
client.

```
 client/jsonapi/basket/product/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Client\JsonApi\Common\Decorator\Decorator1" only to the
"basket" JsonApi client.

See also:

* client/jsonapi/common/decorators/default
* client/jsonapi/basket/product/decorators/excludes
* client/jsonapi/basket/product/decorators/local

## decorators/local

Adds a list of local decorators only to the JsonApi client

```
client/jsonapi/basket/product/decorators/local = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2017.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Client\JsonApi\Basket\Product\Decorator\*") around the JsonApi
client.

```
 client/jsonapi/basket/product/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Client\JsonApi\Basket\Product\Decorator\Decorator2" only to the
"basket product" JsonApi client.

See also:

* client/jsonapi/common/decorators/default
* client/jsonapi/basket/product/decorators/excludes
* client/jsonapi/basket/product/decorators/global

## name

Class name of the used basket/product client implementation

```
client/jsonapi/basket/product/name = 
```

* Default: 
* Type: string - Last part of the class name
* Since: 2017.03

Each default JSON API client can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the client factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Client\JsonApi\Basket\Product\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Client\JsonApi\Basket\Product\Mybasket/product
```

then you have to set the this configuration option:

```
 client/jsonapi/basket/product/name = Mybasket/product
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyProduct"!


# service
## decorators/excludes

Excludes decorators added by the "common" option from the JSON API clients

```
client/jsonapi/basket/service/decorators/excludes = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2017.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"client/jsonapi/common/decorators/default" before they are wrapped
around the JsonApi client.

```
 client/jsonapi/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Client\JsonApi\Common\Decorator\*") added via
"client/jsonapi/common/decorators/default" for the JSON API client.

See also:

* client/jsonapi/common/decorators/default
* client/jsonapi/basket/service/decorators/global
* client/jsonapi/basket/service/decorators/local

## decorators/global

Adds a list of globally available decorators only to the JsonApi client

```
client/jsonapi/basket/service/decorators/global = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2017.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Client\JsonApi\Common\Decorator\*") around the JsonApi
client.

```
 client/jsonapi/basket/service/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Client\JsonApi\Common\Decorator\Decorator1" only to the
"basket" JsonApi client.

See also:

* client/jsonapi/common/decorators/default
* client/jsonapi/basket/service/decorators/excludes
* client/jsonapi/basket/service/decorators/local

## decorators/local

Adds a list of local decorators only to the JsonApi client

```
client/jsonapi/basket/service/decorators/local = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2017.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Client\JsonApi\Basket\Service\Decorator\*") around the JsonApi
client.

```
 client/jsonapi/basket/service/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Client\JsonApi\Basket\Service\Decorator\Decorator2" only to the
"basket service" JsonApi client.

See also:

* client/jsonapi/common/decorators/default
* client/jsonapi/basket/service/decorators/excludes
* client/jsonapi/basket/service/decorators/global

## name

Class name of the used basket/service client implementation

```
client/jsonapi/basket/service/name = 
```

* Default: 
* Type: string - Last part of the class name
* Since: 2017.03

Each default JSON API client can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the client factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Client\JsonApi\Basket\Service\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Client\JsonApi\Basket\Service\Mybasket/service
```

then you have to set the this configuration option:

```
 client/jsonapi/basket/service/name = Mybasket/service
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyService"!


# template

Relative path to the basket JSON API template

```
client/jsonapi/basket/template = basket/standard
```

* Default: basket/standard
* Type: string - Relative path to the template creating the body for the JSON API
* Since: 2017.04

The template file contains the code and processing instructions
to generate the result shown in the JSON API body. The
configuration string is the path to the template file relative
to the templates directory (usually in templates/client/jsonapi).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "standard" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "standard"
should be replaced by the name of the new class.

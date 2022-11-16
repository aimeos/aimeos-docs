
# address
## decorators/excludes

Excludes decorators added by the "common" option from the JSON API clients

```
client/jsonapi/customer/address/decorators/excludes = 
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
* client/jsonapi/customer/address/decorators/global
* client/jsonapi/customer/address/decorators/local

## decorators/global

Adds a list of globally available decorators only to the JsonApi client

```
client/jsonapi/customer/address/decorators/global = 
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
 client/jsonapi/customer/address/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Client\JsonApi\Common\Decorator\Decorator1" only to the
"customer" JsonApi client.

See also:

* client/jsonapi/common/decorators/default
* client/jsonapi/customer/address/decorators/excludes
* client/jsonapi/customer/address/decorators/local

## decorators/local

Adds a list of local decorators only to the JsonApi client

```
client/jsonapi/customer/address/decorators/local = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2017.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Client\JsonApi\Customer\Address\Decorator\*") around the JsonApi
client.

```
 client/jsonapi/customer/address/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Client\JsonApi\Customer\Address\Decorator\Decorator2" only to the
"customer address" JsonApi client.

See also:

* client/jsonapi/common/decorators/default
* client/jsonapi/customer/address/decorators/excludes
* client/jsonapi/customer/address/decorators/global

## name

Class name of the used customer/address client implementation

```
client/jsonapi/customer/address/name = 
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
 \Aimeos\Client\JsonApi\Customer\Address\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Client\JsonApi\Customer\Address\Mycustomer/address
```

then you have to set the this configuration option:

```
 client/jsonapi/customer/address/name = Mycustomer/address
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyAddress"!


## template

Relative path to the customer address JSON API template

```
client/jsonapi/customer/address/template = customer/address/standard
```

* Default: customer/address/standard
* Type: string - Relative path to the template creating the body for the JSON API
* Since: 2017.07

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


# decorators
## excludes

Excludes decorators added by the "common" option from the JSON API clients

```
client/jsonapi/customer/decorators/excludes = 
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
* client/jsonapi/customer/decorators/global
* client/jsonapi/customer/decorators/local

## global

Adds a list of globally available decorators only to the JsonApi client

```
client/jsonapi/customer/decorators/global = 
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
 client/jsonapi/customer/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Client\JsonApi\Common\Decorator\Decorator1" only to the
"customer" JsonApi client.

See also:

* client/jsonapi/common/decorators/default
* client/jsonapi/customer/decorators/excludes
* client/jsonapi/customer/decorators/local

## local

Adds a list of local decorators only to the JsonApi client

```
client/jsonapi/customer/decorators/local = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2017.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Client\JsonApi\Customer\Decorator\*") around the JsonApi
client.

```
 client/jsonapi/customer/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Client\JsonApi\Customer\Decorator\Decorator2" only to the
"customer" JsonApi client.

See also:

* client/jsonapi/common/decorators/default
* client/jsonapi/customer/decorators/excludes
* client/jsonapi/customer/decorators/global

# name

Class name of the used customer client implementation

```
client/jsonapi/customer/name = 
```

* Default: 
* Type: string - Last part of the class name
* Since: 2017.04

Each default JSON API client can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the client factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Client\JsonApi\Customer\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Client\JsonApi\Customer\Mycustomer
```

then you have to set the this configuration option:

```
 client/jsonapi/customer/name = Mycustomer
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyCustomer"!


# property
## decorators/excludes

Excludes decorators added by the "common" option from the JSON API clients

```
client/jsonapi/customer/property/decorators/excludes = 
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
* client/jsonapi/customer/property/decorators/global
* client/jsonapi/customer/property/decorators/local

## decorators/global

Adds a list of globally available decorators only to the JsonApi client

```
client/jsonapi/customer/property/decorators/global = 
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
 client/jsonapi/customer/property/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Client\JsonApi\Common\Decorator\Decorator1" only to the
"customer" JsonApi client.

See also:

* client/jsonapi/common/decorators/default
* client/jsonapi/customer/property/decorators/excludes
* client/jsonapi/customer/property/decorators/local

## decorators/local

Adds a list of local decorators only to the JsonApi client

```
client/jsonapi/customer/property/decorators/local = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2017.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Client\JsonApi\Customer\Property\Decorator\*") around the JsonApi
client.

```
 client/jsonapi/customer/property/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Client\JsonApi\Customer\Property\Decorator\Decorator2" only to the
"customer property" JsonApi client.

See also:

* client/jsonapi/common/decorators/default
* client/jsonapi/customer/property/decorators/excludes
* client/jsonapi/customer/property/decorators/global

## name

Class name of the used customer/property client implementation

```
client/jsonapi/customer/property/name = 
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
 \Aimeos\Client\JsonApi\Customer\Property\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Client\JsonApi\Customer\Property\Mycustomer/property
```

then you have to set the this configuration option:

```
 client/jsonapi/customer/property/name = Mycustomer/property
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyProperty"!


## template

Relative path to the customer property JSON API template

```
client/jsonapi/customer/property/template = customer/property/standard
```

* Default: customer/property/standard
* Type: string - Relative path to the template creating the body for the JSON API
* Since: 2017.07

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


# relationships
## decorators/excludes

Excludes decorators added by the "common" option from the JSON API clients

```
client/jsonapi/customer/relationships/decorators/excludes = 
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
* client/jsonapi/customer/relationships/decorators/global
* client/jsonapi/customer/relationships/decorators/local

## decorators/global

Adds a list of globally available decorators only to the JsonApi client

```
client/jsonapi/customer/relationships/decorators/global = 
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
 client/jsonapi/customer/relationships/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Client\JsonApi\Common\Decorator\Decorator1" only to the
"customer" JsonApi client.

See also:

* client/jsonapi/common/decorators/default
* client/jsonapi/customer/relationships/decorators/excludes
* client/jsonapi/customer/relationships/decorators/local

## decorators/local

Adds a list of local decorators only to the JsonApi client

```
client/jsonapi/customer/relationships/decorators/local = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2017.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Client\JsonApi\Customer\Relationships\Decorator\*") around the JsonApi
client.

```
 client/jsonapi/customer/relationships/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Client\JsonApi\Customer\Relationships\Decorator\Decorator2" only to the
"customer relationships" JsonApi client.

See also:

* client/jsonapi/common/decorators/default
* client/jsonapi/customer/relationships/decorators/excludes
* client/jsonapi/customer/relationships/decorators/global

## name

Class name of the used customer/relationships client implementation

```
client/jsonapi/customer/relationships/name = 
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
 \Aimeos\Client\JsonApi\Customer\Relationships\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Client\JsonApi\Customer\Relationships\Mycustomer/relationships
```

then you have to set the this configuration option:

```
 client/jsonapi/customer/relationships/name = Mycustomer/relationships
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyRelationships"!


## template

Relative path to the customer relationships JSON API template

```
client/jsonapi/customer/relationships/template = customer/relationships/standard
```

* Default: customer/relationships/standard
* Type: string - Relative path to the template creating the body for the JSON API
* Since: 2017.07

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


# review
## decorators/excludes

Excludes decorators added by the "common" option from the JSON API clients

```
client/jsonapi/customer/review/decorators/excludes = 
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
* client/jsonapi/customer/review/decorators/global
* client/jsonapi/customer/review/decorators/local

## decorators/global

Adds a list of globally available decorators only to the JsonApi client

```
client/jsonapi/customer/review/decorators/global = 
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
 client/jsonapi/customer/review/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Client\JsonApi\Common\Decorator\Decorator1" only to the
"customer" JsonApi client.

See also:

* client/jsonapi/common/decorators/default
* client/jsonapi/customer/review/decorators/excludes
* client/jsonapi/customer/review/decorators/local

## decorators/local

Adds a list of local decorators only to the JsonApi client

```
client/jsonapi/customer/review/decorators/local = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2017.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Client\JsonApi\Customer\Review\Decorator\*") around the JsonApi
client.

```
 client/jsonapi/customer/review/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Client\JsonApi\Customer\Review\Decorator\Decorator2" only to the
"customer review" JsonApi client.

See also:

* client/jsonapi/common/decorators/default
* client/jsonapi/customer/review/decorators/excludes
* client/jsonapi/customer/review/decorators/global

## name

Class name of the used customer/review client implementation

```
client/jsonapi/customer/review/name = 
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
 \Aimeos\Client\JsonApi\Customer\Review\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Client\JsonApi\Customer\Review\Mycustomer/review
```

then you have to set the this configuration option:

```
 client/jsonapi/customer/review/name = Mycustomer/review
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyReview"!


## template

Relative path to the customer review JSON API template

```
client/jsonapi/customer/review/template = customer/review/standard
```

* Default: customer/review/standard
* Type: string - Relative path to the template creating the body for the JSON API
* Since: 2017.07

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


# template

Relative path to the customer JSON API template

```
client/jsonapi/customer/template = customer/standard
```

* Default: customer/standard
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

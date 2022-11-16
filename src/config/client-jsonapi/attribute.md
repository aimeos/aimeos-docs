
# decorators
## excludes

Excludes decorators added by the "common" option from the JSON API clients

```
client/jsonapi/attribute/decorators/excludes = 
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
* client/jsonapi/attribute/decorators/global
* client/jsonapi/attribute/decorators/local

## global

Adds a list of globally available decorators only to the JsonApi client

```
client/jsonapi/attribute/decorators/global = 
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
 client/jsonapi/attribute/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Client\JsonApi\Common\Decorator\Decorator1" only to the
"attribute" JsonApi client.

See also:

* client/jsonapi/common/decorators/default
* client/jsonapi/attribute/decorators/excludes
* client/jsonapi/attribute/decorators/local

## local

Adds a list of local decorators only to the JsonApi client

```
client/jsonapi/attribute/decorators/local = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2017.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Client\JsonApi\Attribute\Decorator\*") around the JsonApi
client.

```
 client/jsonapi/attribute/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Client\JsonApi\Attribute\Decorator\Decorator2" only to the
"attribute" JsonApi client.

See also:

* client/jsonapi/common/decorators/default
* client/jsonapi/attribute/decorators/excludes
* client/jsonapi/attribute/decorators/global

# name

Class name of the used attribute client implementation

```
client/jsonapi/attribute/name = 
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
 \Aimeos\Client\JsonApi\Attribute\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Client\JsonApi\Attribute\Myattribute
```

then you have to set the this configuration option:

```
 client/jsonapi/attribute/name = Myattribute
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyAttribute"!


# template

Relative path to the attribute lists JSON API template

```
client/jsonapi/attribute/template = attribute/standard
```

* Default: attribute/standard
* Type: string - Relative path to the template creating the body for the GET method of the JSON API
* Since: 2017.03

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


# types

List of attribute types that should be displayed in this order in the catalog filter

```
client/jsonapi/attribute/types = Array
(
)
```

* Default: Array
(
)

* Type: array - List of attribute type codes
* Since: 2017.03

The attribute section in the catalog filter component can display
all attributes a visitor can use to reduce the listed products
to those that contains one or more attributes. By default, all
available attributes will be displayed and ordered by their
attribute type.

With this setting, you can limit the attribute types to only thoses
whose names are part of the setting value. Furthermore, a particular
order for the attribute types can be enforced that is different
from the standard order.


# decorators
## excludes

Excludes decorators added by the "common" option from the JSON API clients

```
client/jsonapi/product/decorators/excludes = Array
(
)
```

* Default: Array
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
* client/jsonapi/product/decorators/global
* client/jsonapi/product/decorators/local

## global

Adds a list of globally available decorators only to the JsonApi client

```
client/jsonapi/product/decorators/global = Array
(
)
```

* Default: Array
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
 client/jsonapi/product/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Client\JsonApi\Common\Decorator\Decorator1" only to the
"product" JsonApi client.

See also:

* client/jsonapi/common/decorators/default
* client/jsonapi/product/decorators/excludes
* client/jsonapi/product/decorators/local

## local

Adds a list of local decorators only to the JsonApi client

```
client/jsonapi/product/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Client\JsonApi\Product\Decorator\*") around the JsonApi
client.

```
 client/jsonapi/product/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Client\JsonApi\Product\Decorator\Decorator2" only to the
"product" JsonApi client.

See also:

* client/jsonapi/common/decorators/default
* client/jsonapi/product/decorators/excludes
* client/jsonapi/product/decorators/global

# levels

Include products of sub-categories in the product list of the current category

```
client/jsonapi/product/levels = 1
```

* Default: 1
* Type: integer - Tree level constant
* Since: 2017.03

Sometimes it may be useful to show products of sub-categories in the
current category product list, e.g. if the current category contains
no products at all or if there are only a few products in all categories.

Possible constant values for this setting are:
* 1 : Only products from the current category
* 2 : Products from the current category and the direct child categories
* 3 : Products from the current category and the whole category sub-tree

Caution: Please keep in mind that displaying products of sub-categories
can slow down your shop, especially if it contains more than a few
products! You have no real control over the positions of the products
in the result list too because all products from different categories
with the same position value are placed randomly.

Usually, a better way is to associate products to all categories they
should be listed in. This can be done manually if there are only a few
ones or during the product import automatically.


# name

Class name of the used product client implementation

```
client/jsonapi/product/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2017.03

Each default JSON API client can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the client factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Client\JsonApi\Product\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Client\JsonApi\Product\Myproduct
```

then you have to set the this configuration option:

```
 client/jsonapi/product/name = Myproduct
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyProduct"!


# standard
## template

Relative path to the product JSON API template

```
client/jsonapi/product/standard/template = product/standard
```

* Default: product/standard
* Type: string - Relative path to the template creating the body for the GET method of the JSON API
* Since: 2017.03

The template file contains the code and processing instructions
to generate the result shown in the JSON API body. The
configuration string is the path to the template file relative
to the templates directory (usually in client/jsonapi/templates).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "standard" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "standard"
should be replaced by the name of the new class.


## template-aggregate

Relative path to the product aggregate JSON API template

```
client/jsonapi/product/standard/template-aggregate = aggregate-standard
```

* Default: aggregate-standard
* Type: string - Relative path to the template creating the list of aggregated product counts
* Since: 2017.03

The template file contains the code and processing instructions
to generate the result shown in the JSON API body. The
configuration string is the path to the template file relative
to the templates directory (usually in client/jsonapi/templates).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "standard" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "standard"
should be replaced by the name of the new class.

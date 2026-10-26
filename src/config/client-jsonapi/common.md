
# decorators
## default

Configures the list of decorators applied to all JSON API clients

```
client/jsonapi/common/decorators/default = Array
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
* Since: 2015.12

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to configure a list of decorator names that should
be wrapped around the original instance of all created clients:

```
 client/jsonapi/common/decorators/default = array( 'decorator1', 'decorator2' )
```

This would wrap the decorators named "decorator1" and "decorator2" around
all client instances in that order. The decorator classes would be
"\Aimeos\Client\JsonApi\Common\Decorator\Decorator1" and
"\Aimeos\Client\JsonApi\Common\Decorator\Decorator2".


# debug

Send debug information withing responses to clients if an error occurrs

```
client/jsonapi/debug = 1
```

* Default: ``
* Type: boolean - True to return the stack trace in JSON response, false for error message only
* Since: 2017.07

By default, the Aimeos client JSON REST API won't send any details
besides the error message to the client if an error occurred. This
prevents leaking sensitive information to attackers. For debugging
your requests it's helpful to see the stack strace. If you set this
configuration option to true, the stack trace will be returned too.


# name

Class name of the used JSON API client implementation

```
client/jsonapi/name = Standard
```

* Default: `Standard`
* Type: string - Last part of the class name
* Since: 2015.12

Each default JSON API client can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the client factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Client\JsonApi\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Client\JsonApi\Mycntl
```

then you have to set the this configuration option:

```
 client/jsonapi/name = Mycntl
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyCntl"!


# resources

A list of resource names whose clients are available for the JSON API

```
client/jsonapi/resources = Array
(
    [attribute] => attribute
    [basket] => basket
    [catalog] => catalog
    [customer] => customer
    [locale] => locale
    [order] => order
    [product] => product
    [review] => review
    [service] => service
    [site] => site
    [stock] => stock
    [subscription] => subscription
    [supplier] => supplier
)
```

* Default: 
```
Array
(
)
```
* Type: array - List of resource names
* Since: 2017.03

The HTTP OPTIONS method returns a list of resources known by the
JSON API including their URLs. The list of available resources
can be exteded dynamically be implementing a new Jsonadm client
class handling request for this new domain.

To add the new domain client to the list of resources returned
by the HTTP OPTIONS method, you have to add its name in lower case
to the existing configuration.


# template-error

Relative path to the default JSON API template

```
client/jsonapi/template-error = error-standard
```

* Default: `error-standard`
* Type: string - Relative path to the template creating the body for the JSON API response
* Since: 2017.02

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

See also:

* client/jsonapi/template-delete
* client/jsonapi/template-patch
* client/jsonapi/template-post
* client/jsonapi/template-get
* client/jsonapi/template-options

# template-get

Relative path to the default JSON API template for unknown GET request

```
client/jsonapi/template-get = get-standard
```

* Default: `get-standard`
* Type: string - Relative path to the template creating the body for the JSON API GET response
* Since: 2017.05

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

See also:

* client/jsonapi/template-options

# template-options

Relative path to the JSON API template for OPTIONS requests

```
client/jsonapi/template-options = options-standard
```

* Default: `options-standard`
* Type: string - Relative path to the template creating the body for the OPTIONS method of the JSON API
* Since: 2017.02

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

See also:

* client/jsonapi/template-get
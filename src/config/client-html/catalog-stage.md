
# cache

Enables or disables caching only for the catalog stage component

```
client/html/catalog/stage/cache = 1
```

* Default: `1`
* Type: boolean - True to enable caching, false to disable

Disable caching for components can be useful if you would have too much
entries to cache or if the component contains non-cacheable parts that
can't be replaced using the modify() method.

See also:

* client/html/catalog/detail/cache
* client/html/catalog/filter/cache
* client/html/catalog/lists/cache

# decorators
## excludes

Excludes decorators added by the "common" option from the catalog stage html client

```
client/html/catalog/stage/decorators/excludes = 
```

* Type: array - List of decorator names

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"client/html/common/decorators/default" before they are wrapped
around the html client.

```
 client/html/catalog/stage/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Client\Html\Common\Decorator\*") added via
"client/html/common/decorators/default" to the html client.

See also:

* client/html/common/decorators/default
* client/html/catalog/stage/decorators/global
* client/html/catalog/stage/decorators/local

## global

Adds a list of globally available decorators only to the catalog stage html client

```
client/html/catalog/stage/decorators/global = 
```

* Type: array - List of decorator names

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Client\Html\Common\Decorator\*") around the html client.

```
 client/html/catalog/stage/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Client\Html\Common\Decorator\Decorator1" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/catalog/stage/decorators/excludes
* client/html/catalog/stage/decorators/local

## local

Adds a list of local decorators only to the catalog stage html client

```
client/html/catalog/stage/decorators/local = 
```

* Type: array - List of decorator names

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Client\Html\Catalog\Decorator\*") around the html client.

```
 client/html/catalog/stage/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Client\Html\Catalog\Decorator\Decorator2" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/catalog/stage/decorators/excludes
* client/html/catalog/stage/decorators/global

# domains

A list of domain names whose items should be available in the catalog stage view template

```
client/html/catalog/stage/domains = Array
(
    [0] => attribute
    [1] => media
    [2] => media/property
    [3] => text
)
```

* Default: 
```
Array
(
    [0] => attribute
    [1] => media
    [2] => media/property
    [3] => text
)
```
* Type: array - List of domain names
* Since: 2014.03

The templates rendering the catalog stage section use the texts and
maybe images and attributes associated to the categories. You can
configure your own list of domains (attribute, media, price, product,
text, etc. are domains) whose items are fetched from the storage.
Please keep in mind that the more domains you add to the configuration,
the more time is required for fetching the content!

This configuration option overwrites the "client/html/catalog/domains"
option that allows to configure the domain names of the items fetched
for all catalog related data.

See also:

* client/html/catalog/domains
* client/html/catalog/detail/domains
* client/html/catalog/lists/domains

# name

Class name of the used catalog stage client implementation

```
client/html/catalog/stage/name = 
```

* Type: string - Last part of the class name
* Since: 2014.03

Each default HTML client can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the client factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Client\Html\Catalog\Stage\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Client\Html\Catalog\Stage\Mystage
```

then you have to set the this configuration option:

```
 client/html/catalog/stage/name = Mystage
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyStage"!


# template-body

Relative path to the HTML body template of the catalog stage client.

```
client/html/catalog/stage/template-body = catalog/stage/body
```

* Default: `catalog/stage/body`
* Type: string - Relative path to the template creating code for the HTML page body
* Since: 2014.03

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in templates/client/html).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but suffixed by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, it
should be suffixed by the name of the new class.

See also:

* client/html/catalog/stage/template-header

# template-header

Relative path to the HTML header template of the catalog stage client.

```
client/html/catalog/stage/template-header = catalog/stage/header
```

* Default: `catalog/stage/header`
* Type: string - Relative path to the template creating code for the HTML page head
* Since: 2014.03

The template file contains the HTML code and processing instructions
to generate the HTML code that is inserted into the HTML page header
of the rendered page in the frontend. The configuration string is the
path to the template file relative to the templates directory (usually
in templates/client/html).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but suffixed by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, it
should be suffixed by the name of the new class.

See also:

* client/html/catalog/stage/template-body

# cache

Enables or disables caching only for the supplier detail component

```
client/html/supplier/detail/cache = 1
```

* Default: 1
* Type: boolean - True to enable caching, false to disable

Disable caching for components can be useful if you would have too much
entries to cache or if the component contains non-cacheable parts that
can't be replaced using the modify() method.

See also:

* client/html/supplier/detail/cache
* client/html/supplier/filter/cache
* client/html/supplier/lists/cache

# domains

A list of domain names whose items should be available in the supplier detail view template

```
client/html/supplier/detail/domains = Array
(
    [0] => supplier/address
    [1] => media
    [2] => text
)
```

* Default: Array
(
    [0] => supplier/address
    [1] => media
    [2] => text
)

* Type: array - List of domain names
* Since: 2020.10

The templates rendering the supplier detail section use the texts and
maybe images and attributes associated to the categories. You can
configure your own list of domains (attribute, media, price, product,
text, etc. are domains) whose items are fetched from the storage.
Please keep in mind that the more domains you add to the configuration,
the more time is required for fetching the content!


# metatags

Adds the title, meta and link tags to the HTML header

```
client/html/supplier/detail/metatags = 1
```

* Default: 1
* Type: boolean - True to display the meta tags, false to hide it
* Since: 2021.01

By default, each instance of the supplier list component adds some HTML meta
tags to the page head section, like page title, meta keywords and description
as well as some link tags to support browser navigation. If several instances
are placed on one page, this leads to adding several title and meta tags used
by search engine. This setting enables you to suppress these tags in the page
header and maybe add your own to the page manually.

See also:

* client/html/supplier/lists/metatags

# name

Class name of the used supplier detail client implementation

```
client/html/supplier/detail/name = 
```

* Default: 
* Type: string - Last part of the class name
* Since: 2020.10

Each default HTML client can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the client factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Client\Html\Supplier\Detail\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Client\Html\Supplier\Detail\Mydetail
```

then you have to set the this configuration option:

```
 client/html/supplier/detail/name = Mydetail
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyDetail"!


# supid-default

The default supplier ID used if none is given as parameter

```
client/html/supplier/detail/supid-default = 99
```

* Default: 
* Type: string - Supplier ID
* Since: 2021.01

You can configure the default supplier ID if no ID is passed in the
URL using this configuration.

See also:

* client/html/catalog/lists/catid-default

# template-body

Relative path to the HTML body template of the supplier detail client.

```
client/html/supplier/detail/template-body = supplier/detail/body
```

* Default: supplier/detail/body
* Type: string - Relative path to the template creating code for the HTML page body
* Since: 2020.10

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

* client/html/supplier/detail/template-header

# template-header

Relative path to the HTML header template of the supplier detail client.

```
client/html/supplier/detail/template-header = supplier/detail/header
```

* Default: supplier/detail/header
* Type: string - Relative path to the template creating code for the HTML page head
* Since: 2020.10

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

* client/html/supplier/detail/template-body

# url
## action

```
client/html/supplier/detail/url/action = detail
```

* Default: detail


## config

```
client/html/supplier/detail/url/config = Array
(
)
```

* Default: Array
(
)



## controller

```
client/html/supplier/detail/url/controller = supplier
```

* Default: supplier


## filter

```
client/html/supplier/detail/url/filter = Array
(
)
```

* Default: Array
(
)



## target

```
client/html/supplier/detail/url/target = 
```

* Default: 

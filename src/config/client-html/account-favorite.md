
# decorators
## excludes

```
client/html/account/favorite/decorators/excludes = Array
(
)
```

* Default: Array
(
)



## global

```
client/html/account/favorite/decorators/global = Array
(
)
```

* Default: Array
(
)



## local

```
client/html/account/favorite/decorators/local = Array
(
)
```

* Default: Array
(
)



# domains

A list of domain names whose items should be available in the account favorite view template

```
client/html/account/favorite/domains = Array
(
    [0] => catalog
    [1] => text
    [2] => price
    [3] => media
)
```

* Default: Array
(
    [0] => catalog
    [1] => text
    [2] => price
    [3] => media
)

* Type: array - List of domain names
* Since: 2014.09

The templates rendering product details usually add the images,
prices and texts associated to the product item. If you want to
display additional or less content, you can configure your own
list of domains (attribute, media, price, product, text, etc. are
domains) whose items are fetched from the storage. Please keep
in mind that the more domains you add to the configuration, the
more time is required for fetching the content!

See also:

* client/html/catalog/domains

# maxitems

Maximum number of products that can be favorites

```
client/html/account/favorite/maxitems = 100
```

* Default: 100
* Type: integer - Number of products
* Since: 2019.04

This option limits the number of products users can add to their
favorite list. It must be a positive integer value greater than 0.


# name

Class name of the used account favorite client implementation

```
client/html/account/favorite/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2014.03

Each default HTML client can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the client factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Client\Html\Account\Favorite\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Client\Html\Account\Favorite\Myfavorite
```

then you have to set the this configuration option:

```
 client/html/account/favorite/name = Myfavorite
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyFavorite"!


# size

The number of products shown in a list page for favorite products

```
client/html/account/favorite/size = 48
```

* Default: 48
* Type: integer - Number of products
* Since: 2014.09

Limits the number of products that is shown in the list pages to the
given value. If more products are available, the products are split
into bunches which will be shown on their own list page. The user is
able to move to the next page (or previous one if it's not the first)
to display the next (or previous) products.

The value must be an integer number from 1 to 100. Negative values as
well as values above 100 are not allowed. The value can be overwritten
per request if the "l_size" parameter is part of the URL.

See also:

* client/html/catalog/lists/size

# template-body

Relative path to the HTML body template of the account favorite client.

```
client/html/account/favorite/template-body = account/favorite/body
```

* Default: account/favorite/body
* Type: string - Relative path to the template creating code for the HTML page body
* Since: 2015.10

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

* client/html/account/favorite/template-header

# template-header

Relative path to the HTML header template of the account favorite client.

```
client/html/account/favorite/template-header = account/favorite/header
```

* Default: account/favorite/header
* Type: string - Relative path to the template creating code for the HTML page head
* Since: 2015.10

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

* client/html/account/favorite/template-body

# url
## action

Name of the action that should create the output

```
client/html/account/favorite/url/action = favorite
```

* Default: favorite
* Type: string - Name of the action
* Since: 2014.09

In Model-View-Controller (MVC) applications, actions are the methods of a
controller that create parts of the output displayed in the generated HTML page.
Action names are usually alpha-numeric.

See also:

* client/html/account/favorite/url/target
* client/html/account/favorite/url/controller
* client/html/account/favorite/url/config
* client/html/account/favorite/url/filter

## config

Associative list of configuration options used for generating the URL

```
client/html/account/favorite/url/config = Array
(
)
```

* Default: Array
(
)

* Type: string - Associative list of configuration options
* Since: 2014.09

You can specify additional options as key/value pairs used when generating
the URLs, like

```
 client/html/<clientname>/url/config = array( 'absoluteUri' => true )
```

The available key/value pairs depend on the application that embeds the e-commerce
framework. This is because the infrastructure of the application is used for
generating the URLs. The full list of available config options is referenced
in the "see also" section of this page.

See also:

* client/html/account/favorite/url/target
* client/html/account/favorite/url/controller
* client/html/account/favorite/url/action
* client/html/account/favorite/url/filter

## controller

Name of the controller whose action should be called

```
client/html/account/favorite/url/controller = Account
```

* Default: Account
* Type: string - Name of the controller
* Since: 2014.09

In Model-View-Controller (MVC) applications, the controller contains the methods
that create parts of the output displayed in the generated HTML page. Controller
names are usually alpha-numeric.

See also:

* client/html/account/favorite/url/target
* client/html/account/favorite/url/action
* client/html/account/favorite/url/config
* client/html/account/favorite/url/filter

## filter

Removes parameters for the detail page before generating the URL

```
client/html/account/favorite/url/filter = Array
(
)
```

* Default: Array
(
)

* Type: array - List of parameter names to remove
* Since: 2022.10

This setting removes the listed parameters from the URLs. Keep care to
remove no required parameters!

See also:

* client/html/account/favorite/url/target
* client/html/account/favorite/url/controller
* client/html/account/favorite/url/action
* client/html/account/favorite/url/config

## target

Destination of the URL where the controller specified in the URL is known

```
client/html/account/favorite/url/target = 
```

* Default: 
* Type: string - Destination of the URL
* Since: 2014.09

The destination can be a page ID like in a content management system or the
module of a software development framework. This "target" must contain or know
the controller that should be called by the generated URL.

See also:

* client/html/account/favorite/url/controller
* client/html/account/favorite/url/action
* client/html/account/favorite/url/config
* client/html/account/favorite/url/filter

# error
## url/target

Destination of the URL to redirect the customer if the file download isn't allowed

```
client/html/account/download/error/url/target = 
```

* Default: 
* Type: string - Destination of the URL
* Since: 2019.04

The destination can be a page ID like in a content management system or the
module of a software development framework. This "target" must contain or know
the controller that should be called by the generated URL.


# maxcount

Maximum number of file downloads allowed for an ordered product

```
client/html/account/download/maxcount = 0
```

* Default: 
* Type: integer - Maximum number of downloads
* Since: 2016.02

This configuration setting enables you to limit the number of downloads
of a product download file. The count is the maximum number for each
bought product and customer, i.e. setting the count to "3" allows
a customer to download the bought product file up to three times.

The default value of null enforces no limit.


# name

Class name of the used account download client implementation

```
client/html/account/download/name = 
```

* Default: 
* Type: string - Last part of the class name
* Since: 2014.03

Each default HTML client can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the client factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Client\Html\Account\Download\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Client\Html\Account\Download\Mydownload
```

then you have to set the this configuration option:

```
 client/html/account/download/name = Mydownload
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyDownload"!


# url
## action

Name of the action that should create the output

```
client/html/account/download/url/action = 
```

* Default: 
* Type: string - Name of the action
* Since: 2016.02

In Model-View-Controller (MVC) applications, actions are the methods of a
controller that create parts of the output displayed in the generated HTML page.
Action names are usually alpha-numeric.

See also:

* client/html/account/download/url/target
* client/html/account/download/url/controller
* client/html/account/download/url/config

## config

Associative list of configuration options used for generating the URL

```
client/html/account/download/url/config = 
```

* Default: 
* Type: string - Associative list of configuration options
* Since: 2016.02

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

* client/html/account/download/url/target
* client/html/account/download/url/controller
* client/html/account/download/url/action

## controller

Name of the controller whose action should be called

```
client/html/account/download/url/controller = 
```

* Default: 
* Type: string - Name of the controller
* Since: 2016.02

In Model-View-Controller (MVC) applications, the controller contains the methods
that create parts of the output displayed in the generated HTML page. Controller
names are usually alpha-numeric.

See also:

* client/html/account/download/url/target
* client/html/account/download/url/action
* client/html/account/download/url/config

## target

Destination of the URL where the controller specified in the URL is known

```
client/html/account/download/url/target = 
```

* Default: 
* Type: string - Destination of the URL
* Since: 2016.02

The destination can be a page ID like in a content management system or the
module of a software development framework. This "target" must contain or know
the controller that should be called by the generated URL.

See also:

* client/html/account/download/url/controller
* client/html/account/download/url/action
* client/html/account/download/url/config
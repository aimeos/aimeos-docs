
# decorators
## excludes

Excludes decorators added by the "common" option from the account download html client

```
client/html/account/download/decorators/excludes = 
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
 client/html/account/download/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Client\Html\Common\Decorator\*") added via
"client/html/common/decorators/default" to the html client.

See also:

* client/html/common/decorators/default
* client/html/account/download/decorators/global
* client/html/account/download/decorators/local

## global

Adds a list of globally available decorators only to the account download html client

```
client/html/account/download/decorators/global = 
```

* Type: array - List of decorator names

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Client\Html\Common\Decorator\*") around the html client.

```
 client/html/account/download/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Client\Html\Common\Decorator\Decorator1" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/account/download/decorators/excludes
* client/html/account/download/decorators/local

## local

Adds a list of local decorators only to the account download html client

```
client/html/account/download/decorators/local = 
```

* Type: array - List of decorator names

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Client\Html\Account\Decorator\*") around the html client.

```
 client/html/account/download/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Client\Html\Account\Decorator\Decorator2" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/account/download/decorators/excludes
* client/html/account/download/decorators/global

# error
## url/target

Destination of the URL to redirect the customer if the file download isn't allowed

```
client/html/account/download/error/url/target = 
```

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

* Type: string - Destination of the URL
* Since: 2016.02

The destination can be a page ID like in a content management system or the
module of a software development framework. This "target" must contain or know
the controller that should be called by the generated URL.

See also:

* client/html/account/download/url/controller
* client/html/account/download/url/action
* client/html/account/download/url/config
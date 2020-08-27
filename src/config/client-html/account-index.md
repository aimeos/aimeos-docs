
# url
## action

Name of the action that should create the output

```
client/html/account/index/url/action = index
```

* Default: index
* Type: string - Name of the action
* Since: 2019.07

In Model-View-Controller (MVC) applications, actions are the methods of a
controller that create parts of the output displayed in the generated HTML page.
Action names are usually alpha-numeric.

See also:

* client/html/account/index/url/target
* client/html/account/index/url/controller
* client/html/account/index/url/config

## config

Associative list of configuration options used for generating the URL

```
client/html/account/index/url/config = Array
(
    [absoluteUri] => 1
)
```

* Default: Array
* Type: string - Associative list of configuration options
* Since: 2019.07

You can specify additional options as key/value pairs used when generating
the URLs, like

```
 client/html/account/index/url/config = ['absoluteUri' => true]
```

The available key/value pairs depend on the application that embeds the e-commerce
framework. This is because the infrastructure of the application is used for
generating the URLs. The full list of available config options is referenced
in the "see also" section of this page.

See also:

* client/html/account/index/url/target
* client/html/account/index/url/controller
* client/html/account/index/url/action

## controller

Name of the controller whose action should be called

```
client/html/account/index/url/controller = account
```

* Default: account
* Type: string - Name of the controller
* Since: 2019.07

In Model-View-Controller (MVC) applications, the controller contains the methods
that create parts of the output displayed in the generated HTML page. Controller
names are usually alpha-numeric.

See also:

* client/html/account/index/url/target
* client/html/account/index/url/action
* client/html/account/index/url/config

## target

Destination of the URL where the controller specified in the URL is known

```
client/html/account/index/url/target = 
```

* Default: 
* Type: string - Destination of the URL
* Since: 2019.07

The destination can be a page ID like in a content management system or the
module of a software development framework. This "target" must contain or know
the controller that should be called by the generated URL.

See also:

* client/html/account/index/url/controller
* client/html/account/index/url/action
* client/html/account/index/url/config
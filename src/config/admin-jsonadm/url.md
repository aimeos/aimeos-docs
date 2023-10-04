
# action

Name of the action that should create the output

```
admin/jsonadm/url/action = get
```

* Default: get
* Type: string - Name of the action
* Since: 2016.01

In Model-View-Controller (MVC) applications, actions are the methods of a
client that create parts of the output displayed in the generated HTML page.
Action names are usually alpha-numeric.

See also:

* admin/jsonadm/url/target
* admin/jsonadm/url/controller
* admin/jsonadm/url/config

# config

Associative list of configuration options used for generating the URL

```
admin/jsonadm/url/config = Array
(
)
```

* Default: Array
(
)

* Type: string - Associative list of configuration options
* Since: 2016.01

You can specify additional options as key/value pairs used when generating
the URLs, like

```
 admin/jsonadm/url/config = array( 'absoluteUri' => true )
```

The available key/value pairs depend on the application that embeds the e-commerce
framework. This is because the infrastructure of the application is used for
generating the URLs. The full list of available config options is referenced
in the "see also" section of this page.

See also:

* admin/jsonadm/url/target
* admin/jsonadm/url/controller
* admin/jsonadm/url/action

# controller

Name of the client whose action should be called

```
admin/jsonadm/url/controller = jsonadm
```

* Default: jsonadm
* Type: string - Name of the client
* Since: 2016.01

In Model-View-Controller (MVC) applications, the client contains the methods
that create parts of the output displayed in the generated HTML page. Controller
names are usually alpha-numeric.

See also:

* admin/jsonadm/url/target
* admin/jsonadm/url/action
* admin/jsonadm/url/config

# target

Destination of the URL where the client specified in the URL is known

```
admin/jsonadm/url/target = 
```

* Type: string - Destination of the URL
* Since: 2016.01

The destination can be a page ID like in a content management system or the
module of a software development framework. This "target" must contain or know
the client that should be called by the generated URL.

See also:

* admin/jsonadm/url/controller
* admin/jsonadm/url/action
* admin/jsonadm/url/config
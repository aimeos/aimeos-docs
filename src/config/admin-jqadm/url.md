
# batch
## action

Name of the action that should create the output

```
admin/jqadm/url/batch/action = batch
```

* Default: batch
* Type: string - Name of the action
* Since: 2022.10

In Model-View-Controller (MVC) applications, actions are the methods of a
controller that create parts of the output displayed in the generated HTML page.
Action names are usually alpha-numeric.

See also:

* admin/jqadm/url/batch/target
* admin/jqadm/url/batch/controller
* admin/jqadm/url/batch/config
* admin/jqadm/url/batch/filter

## config

Associative list of configuration options used for generating the URL

```
admin/jqadm/url/batch/config = Array
(
)
```

* Default: Array
(
)

* Type: string - Associative list of configuration options
* Since: 2022.10

You can specify additional options as key/value pairs used when generating
the URLs, like

```
 admin/jqadm/url/batch/config = ['absoluteUri' => true]
```

The available key/value pairs depend on the application that embeds the e-commerce
framework. This is because the infrastructure of the application is used for
generating the URLs. The full list of available config options is referenced
in the "see also" section of this page.

See also:

* admin/jqadm/url/batch/target
* admin/jqadm/url/batch/controller
* admin/jqadm/url/batch/action
* admin/jqadm/url/batch/filter

## controller

Name of the controller whose action should be called

```
admin/jqadm/url/batch/controller = Url
```

* Default: Url
* Type: string - Name of the controller
* Since: 2022.10

In Model-View-Controller (MVC) applications, the controller contains the methods
that create parts of the output displayed in the generated HTML page. Controller
names are usually alpha-numeric.

See also:

* admin/jqadm/url/batch/target
* admin/jqadm/url/batch/action
* admin/jqadm/url/batch/config
* admin/jqadm/url/batch/filter

## filter

Removes parameters for the detail page before generating the URL

```
admin/jqadm/url/batch/filter = Array
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

* admin/jqadm/url/batch/target
* admin/jqadm/url/batch/controller
* admin/jqadm/url/batch/action
* admin/jqadm/url/batch/config

## target

Destination of the URL where the controller specified in the URL is known

```
admin/jqadm/url/batch/target = 
```

* Default: 
* Type: string - Destination of the URL
* Since: 2022.10

The destination can be a page ID like in a content management system or the
module of a software development framework. This "target" must contain or know
the controller that should be called by the generated URL.

See also:

* admin/jqadm/url/batch/controller
* admin/jqadm/url/batch/action
* admin/jqadm/url/batch/config
* admin/jqadm/url/batch/filter

# copy
## action

Name of the action that should create the output

```
admin/jqadm/url/copy/action = copy
```

* Default: copy
* Type: string - Name of the action
* Since: 2016.04

In Model-View-Controller (MVC) applications, actions are the methods of a
controller that create parts of the output displayed in the generated HTML page.
Action names are usually alpha-numeric.

See also:

* admin/jqadm/url/copy/target
* admin/jqadm/url/copy/controller
* admin/jqadm/url/copy/config
* admin/jqadm/url/copy/filter

## config

Associative list of configuration options used for generating the URL

```
admin/jqadm/url/copy/config = Array
(
)
```

* Default: Array
(
)

* Type: string - Associative list of configuration options
* Since: 2016.04

You can specify additional options as key/value pairs used when generating
the URLs, like

```
 admin/jqadm/url/copy/config = ['absoluteUri' => true]
```

The available key/value pairs depend on the application that embeds the e-commerce
framework. This is because the infrastructure of the application is used for
generating the URLs. The full list of available config options is referenced
in the "see also" section of this page.

See also:

* admin/jqadm/url/copy/target
* admin/jqadm/url/copy/controller
* admin/jqadm/url/copy/action
* admin/jqadm/url/copy/filter

## controller

Name of the controller whose action should be called

```
admin/jqadm/url/copy/controller = Url
```

* Default: Url
* Type: string - Name of the controller
* Since: 2016.04

In Model-View-Controller (MVC) applications, the controller contains the methods
that create parts of the output displayed in the generated HTML page. Controller
names are usually alpha-numeric.

See also:

* admin/jqadm/url/copy/target
* admin/jqadm/url/copy/action
* admin/jqadm/url/copy/config
* admin/jqadm/url/copy/filter

## filter

Removes parameters for the detail page before generating the URL

```
admin/jqadm/url/copy/filter = Array
(
)
```

* Default: Array
(
)

* Type: array - List of parameter names to remove
* Since: 2016.04

This setting removes the listed parameters from the URLs. Keep care to
remove no required parameters!

See also:

* admin/jqadm/url/copy/target
* admin/jqadm/url/copy/controller
* admin/jqadm/url/copy/action
* admin/jqadm/url/copy/config

## target

Destination of the URL where the controller specified in the URL is known

```
admin/jqadm/url/copy/target = 
```

* Default: 
* Type: string - Destination of the URL
* Since: 2016.04

The destination can be a page ID like in a content management system or the
module of a software development framework. This "target" must contain or know
the controller that should be called by the generated URL.

See also:

* admin/jqadm/url/copy/controller
* admin/jqadm/url/copy/action
* admin/jqadm/url/copy/config
* admin/jqadm/url/copy/filter

# create
## action

Name of the action that should create the output

```
admin/jqadm/url/create/action = create
```

* Default: create
* Type: string - Name of the action
* Since: 2016.04

In Model-View-Controller (MVC) applications, actions are the methods of a
controller that create parts of the output displayed in the generated HTML page.
Action names are usually alpha-numeric.

See also:

* admin/jqadm/url/create/target
* admin/jqadm/url/create/controller
* admin/jqadm/url/create/config
* admin/jqadm/url/create/filter

## config

Associative list of configuration options used for generating the URL

```
admin/jqadm/url/create/config = Array
(
)
```

* Default: Array
(
)

* Type: string - Associative list of configuration options
* Since: 2016.04

You can specify additional options as key/value pairs used when generating
the URLs, like

```
 admin/jqadm/url/create/config = ['absoluteUri' => true]
```

The available key/value pairs depend on the application that embeds the e-commerce
framework. This is because the infrastructure of the application is used for
generating the URLs. The full list of available config options is referenced
in the "see also" section of this page.

See also:

* admin/jqadm/url/create/target
* admin/jqadm/url/create/controller
* admin/jqadm/url/create/action
* admin/jqadm/url/create/filter

## controller

Name of the controller whose action should be called

```
admin/jqadm/url/create/controller = Url
```

* Default: Url
* Type: string - Name of the controller
* Since: 2016.04

In Model-View-Controller (MVC) applications, the controller contains the methods
that create parts of the output displayed in the generated HTML page. Controller
names are usually alpha-numeric.

See also:

* admin/jqadm/url/create/target
* admin/jqadm/url/create/action
* admin/jqadm/url/create/config
* admin/jqadm/url/create/filter

## filter

Removes parameters for the detail page before generating the URL

```
admin/jqadm/url/create/filter = Array
(
)
```

* Default: Array
(
)

* Type: array - List of parameter names to remove
* Since: 2016.04

This setting removes the listed parameters from the URLs. Keep care to
remove no required parameters!

See also:

* admin/jqadm/url/create/target
* admin/jqadm/url/create/controller
* admin/jqadm/url/create/action
* admin/jqadm/url/create/config

## target

Destination of the URL where the controller specified in the URL is known

```
admin/jqadm/url/create/target = 
```

* Default: 
* Type: string - Destination of the URL
* Since: 2016.04

The destination can be a page ID like in a content management system or the
module of a software development framework. This "target" must contain or know
the controller that should be called by the generated URL.

See also:

* admin/jqadm/url/create/controller
* admin/jqadm/url/create/action
* admin/jqadm/url/create/config
* admin/jqadm/url/create/filter

# delete
## action

Name of the action that should create the output

```
admin/jqadm/url/delete/action = delete
```

* Default: delete
* Type: string - Name of the action
* Since: 2016.04

In Model-View-Controller (MVC) applications, actions are the methods of a
controller that create parts of the output displayed in the generated HTML page.
Action names are usually alpha-numeric.

See also:

* admin/jqadm/url/delete/target
* admin/jqadm/url/delete/controller
* admin/jqadm/url/delete/config
* admin/jqadm/url/delete/filter

## config

Associative list of configuration options used for generating the URL

```
admin/jqadm/url/delete/config = Array
(
)
```

* Default: Array
(
)

* Type: string - Associative list of configuration options
* Since: 2016.04

You can specify additional options as key/value pairs used when generating
the URLs, like

```
 admin/jqadm/url/delete/config = ['absoluteUri' => true]
```

The available key/value pairs depend on the application that embeds the e-commerce
framework. This is because the infrastructure of the application is used for
generating the URLs. The full list of available config options is referenced
in the "see also" section of this page.

See also:

* admin/jqadm/url/delete/target
* admin/jqadm/url/delete/controller
* admin/jqadm/url/delete/action
* admin/jqadm/url/delete/filter

## controller

Name of the controller whose action should be called

```
admin/jqadm/url/delete/controller = Url
```

* Default: Url
* Type: string - Name of the controller
* Since: 2016.04

In Model-View-Controller (MVC) applications, the controller contains the methods
that create parts of the output displayed in the generated HTML page. Controller
names are usually alpha-numeric.

See also:

* admin/jqadm/url/delete/target
* admin/jqadm/url/delete/action
* admin/jqadm/url/delete/config
* admin/jqadm/url/delete/filter

## filter

Removes parameters for the detail page before generating the URL

```
admin/jqadm/url/delete/filter = Array
(
)
```

* Default: Array
(
)

* Type: array - List of parameter names to remove
* Since: 2016.04

This setting removes the listed parameters from the URLs. Keep care to
remove no required parameters!

See also:

* admin/jqadm/url/delete/target
* admin/jqadm/url/delete/controller
* admin/jqadm/url/delete/action
* admin/jqadm/url/delete/config

## target

Destination of the URL where the controller specified in the URL is known

```
admin/jqadm/url/delete/target = 
```

* Default: 
* Type: string - Destination of the URL
* Since: 2016.04

The destination can be a page ID like in a content management system or the
module of a software development framework. This "target" must contain or know
the controller that should be called by the generated URL.

See also:

* admin/jqadm/url/delete/controller
* admin/jqadm/url/delete/action
* admin/jqadm/url/delete/config
* admin/jqadm/url/delete/filter

# export
## action

Name of the action that should create the output

```
admin/jqadm/url/export/action = export
```

* Default: export
* Type: string - Name of the action
* Since: 2016.04

In Model-View-Controller (MVC) applications, actions are the methods of a
controller that create parts of the output displayed in the generated HTML page.
Action names are usually alpha-numeric.

See also:

* admin/jqadm/url/export/target
* admin/jqadm/url/export/controller
* admin/jqadm/url/export/config

## config

Associative list of configuration options used for generating the URL

```
admin/jqadm/url/export/config = Array
(
)
```

* Default: Array
(
)

* Type: string - Associative list of configuration options
* Since: 2016.04

You can specify additional options as key/value pairs used when generating
the URLs, like

```
 admin/jqadm/url/export/config = ['absoluteUri' => true )
```

The available key/value pairs depend on the application that embeds the e-commerce
framework. This is because the infrastructure of the application is used for
generating the URLs. The full list of available config options is referenced
in the "see also" section of this page.

See also:

* admin/jqadm/url/export/target
* admin/jqadm/url/export/controller
* admin/jqadm/url/export/action

## controller

Name of the controller whose action should be called

```
admin/jqadm/url/export/controller = Url
```

* Default: Url
* Type: string - Name of the controller
* Since: 2016.04

In Model-View-Controller (MVC) applications, the controller contains the methods
that create parts of the output displayed in the generated HTML page. Controller
names are usually alpha-numeric.

See also:

* admin/jqadm/url/export/target
* admin/jqadm/url/export/action
* admin/jqadm/url/export/config

## filter

Removes parameters for the detail page before generating the URL

```
admin/jqadm/url/export/filter = Array
(
)
```

* Default: Array
(
)

* Type: array - List of parameter names to remove
* Since: 2016.04

This setting removes the listed parameters from the URLs. Keep care to
remove no required parameters!

See also:

* admin/jqadm/url/export/target
* admin/jqadm/url/export/controller
* admin/jqadm/url/export/action
* admin/jqadm/url/export/config

## target

Destination of the URL where the controller specified in the URL is known

```
admin/jqadm/url/export/target = 
```

* Default: 
* Type: string - Destination of the URL
* Since: 2017.10

The destination can be a page ID like in a content management system or the
module of a software development framework. This "target" must contain or know
the controller that should be called by the generated URL.

See also:

* admin/jqadm/url/export/controller
* admin/jqadm/url/export/action
* admin/jqadm/url/export/config

# get
## action

Name of the action that should create the output

```
admin/jqadm/url/get/action = get
```

* Default: get
* Type: string - Name of the action
* Since: 2016.04

In Model-View-Controller (MVC) applications, actions are the methods of a
controller that create parts of the output displayed in the generated HTML page.
Action names are usually alpha-numeric.

See also:

* admin/jqadm/url/get/target
* admin/jqadm/url/get/controller
* admin/jqadm/url/get/config
* admin/jqadm/url/get/filter

## config

Associative list of configuration options used for generating the URL

```
admin/jqadm/url/get/config = Array
(
)
```

* Default: Array
(
)

* Type: string - Associative list of configuration options
* Since: 2016.04

You can specify additional options as key/value pairs used when generating
the URLs, like

```
 admin/jqadm/url/get/config = ['absoluteUri' => true]
```

The available key/value pairs depend on the application that embeds the e-commerce
framework. This is because the infrastructure of the application is used for
generating the URLs. The full list of available config options is referenced
in the "see also" section of this page.

See also:

* admin/jqadm/url/get/target
* admin/jqadm/url/get/controller
* admin/jqadm/url/get/action
* admin/jqadm/url/get/filter

## controller

Name of the controller whose action should be called

```
admin/jqadm/url/get/controller = Url
```

* Default: Url
* Type: string - Name of the controller
* Since: 2016.04

In Model-View-Controller (MVC) applications, the controller contains the methods
that create parts of the output displayed in the generated HTML page. Controller
names are usually alpha-numeric.

See also:

* admin/jqadm/url/get/target
* admin/jqadm/url/get/action
* admin/jqadm/url/get/config
* admin/jqadm/url/get/filter

## filter

Removes parameters for the detail page before generating the URL

```
admin/jqadm/url/get/filter = Array
(
)
```

* Default: Array
(
)

* Type: array - List of parameter names to remove
* Since: 2016.04

This setting removes the listed parameters from the URLs. Keep care to
remove no required parameters!

See also:

* admin/jqadm/url/get/target
* admin/jqadm/url/get/controller
* admin/jqadm/url/get/action
* admin/jqadm/url/get/config

## target

Destination of the URL where the controller specified in the URL is known

```
admin/jqadm/url/get/target = 
```

* Default: 
* Type: string - Destination of the URL
* Since: 2016.04

The destination can be a page ID like in a content management system or the
module of a software development framework. This "target" must contain or know
the controller that should be called by the generated URL.

See also:

* admin/jqadm/url/get/controller
* admin/jqadm/url/get/action
* admin/jqadm/url/get/config
* admin/jqadm/url/get/filter

# save
## action

Name of the action that should create the output

```
admin/jqadm/url/save/action = save
```

* Default: save
* Type: string - Name of the action
* Since: 2016.04

In Model-View-Controller (MVC) applications, actions are the methods of a
controller that create parts of the output displayed in the generated HTML page.
Action names are usually alpha-numeric.

See also:

* admin/jqadm/url/save/target
* admin/jqadm/url/save/controller
* admin/jqadm/url/save/config

## config

Associative list of configuration options used for generating the URL

```
admin/jqadm/url/save/config = Array
(
)
```

* Default: Array
(
)

* Type: string - Associative list of configuration options
* Since: 2016.04

You can specify additional options as key/value pairs used when generating
the URLs, like

```
 admin/jqadm/url/save/config = array( 'absoluteUri' => true )
```

The available key/value pairs depend on the application that embeds the e-commerce
framework. This is because the infrastructure of the application is used for
generating the URLs. The full list of available config options is referenced
in the "see also" section of this page.

See also:

* admin/jqadm/url/save/target
* admin/jqadm/url/save/controller
* admin/jqadm/url/save/action

## controller

Name of the controller whose action should be called

```
admin/jqadm/url/save/controller = Url
```

* Default: Url
* Type: string - Name of the controller
* Since: 2016.04

In Model-View-Controller (MVC) applications, the controller contains the methods
that create parts of the output displayed in the generated HTML page. Controller
names are usually alpha-numeric.

See also:

* admin/jqadm/url/save/target
* admin/jqadm/url/save/action
* admin/jqadm/url/save/config

## filter

Removes parameters for the detail page before generating the URL

```
admin/jqadm/url/save/filter = Array
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

* admin/jqadm/url/save/target
* admin/jqadm/url/save/controller
* admin/jqadm/url/save/action
* admin/jqadm/url/save/config

## target

Destination of the URL where the controller specified in the URL is known

```
admin/jqadm/url/save/target = 
```

* Default: 
* Type: string - Destination of the URL
* Since: 2016.04

The destination can be a page ID like in a content management system or the
module of a software development framework. This "target" must contain or know
the controller that should be called by the generated URL.

See also:

* admin/jqadm/url/save/controller
* admin/jqadm/url/save/action
* admin/jqadm/url/save/config

# search
## action

Name of the action that should create the output

```
admin/jqadm/url/search/action = search
```

* Default: search
* Type: string - Name of the action
* Since: 2016.04

In Model-View-Controller (MVC) applications, actions are the methods of a
controller that create parts of the output displayed in the generated HTML page.
Action names are usually alpha-numeric.

See also:

* admin/jqadm/url/search/target
* admin/jqadm/url/search/controller
* admin/jqadm/url/search/config
* admin/jqadm/url/search/filter

## config

Associative list of configuration options used for generating the URL

```
admin/jqadm/url/search/config = Array
(
)
```

* Default: Array
(
)

* Type: string - Associative list of configuration options
* Since: 2016.04

You can specify additional options as key/value pairs used when generating
the URLs, like

```
 admin/jqadm/url/search/config = ['absoluteUri' => true )
```

The available key/value pairs depend on the application that embeds the e-commerce
framework. This is because the infrastructure of the application is used for
generating the URLs. The full list of available config options is referenced
in the "see also" section of this page.

See also:

* admin/jqadm/url/search/target
* admin/jqadm/url/search/controller
* admin/jqadm/url/search/action
* admin/jqadm/url/search/filter

## controller

Name of the controller whose action should be called

```
admin/jqadm/url/search/controller = Url
```

* Default: Url
* Type: string - Name of the controller
* Since: 2016.04

In Model-View-Controller (MVC) applications, the controller contains the methods
that create parts of the output displayed in the generated HTML page. Controller
names are usually alpha-numeric.

See also:

* admin/jqadm/url/search/target
* admin/jqadm/url/search/action
* admin/jqadm/url/search/config
* admin/jqadm/url/search/filter

## filter

Removes parameters for the detail page before generating the URL

```
admin/jqadm/url/search/filter = Array
(
)
```

* Default: Array
(
)

* Type: array - List of parameter names to remove
* Since: 2016.04

This setting removes the listed parameters from the URLs. Keep care to
remove no required parameters!

See also:

* admin/jqadm/url/search/target
* admin/jqadm/url/search/controller
* admin/jqadm/url/search/action
* admin/jqadm/url/search/config

## target

Destination of the URL where the controller specified in the URL is known

```
admin/jqadm/url/search/target = 
```

* Default: 
* Type: string - Destination of the URL
* Since: 2016.04

The destination can be a page ID like in a content management system or the
module of a software development framework. This "target" must contain or know
the controller that should be called by the generated URL.

See also:

* admin/jqadm/url/search/controller
* admin/jqadm/url/search/action
* admin/jqadm/url/search/config
* admin/jqadm/url/search/filter
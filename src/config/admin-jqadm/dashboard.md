
# decorators
## excludes

Excludes decorators added by the "common" option from the dashboard JQAdm client

```
admin/jqadm/dashboard/decorators/excludes = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2016.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"client/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/dashboard/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"client/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/decorators/global
* admin/jqadm/dashboard/decorators/local

## global

Adds a list of globally available decorators only to the dashboard JQAdm client

```
admin/jqadm/dashboard/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2016.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/dashboard/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/decorators/excludes
* admin/jqadm/dashboard/decorators/local

## local

Adds a list of local decorators only to the dashboard JQAdm client

```
admin/jqadm/dashboard/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2016.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Dashboard\Decorator\*") around the JQAdm client.

```
 admin/jqadm/dashboard/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Dashboard\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/decorators/excludes
* admin/jqadm/dashboard/decorators/global

# job
## decorators/excludes

Excludes decorators added by the "common" option from the dashboard JQAdm client

```
admin/jqadm/dashboard/job/decorators/excludes = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2017.08

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"admin/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/dashboard/job/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"admin/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/job/decorators/global
* admin/jqadm/dashboard/job/decorators/local

## decorators/global

Adds a list of globally available decorators only to the dashboard JQAdm client

```
admin/jqadm/dashboard/job/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.08

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/dashboard/job/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/job/decorators/excludes
* admin/jqadm/dashboard/job/decorators/local

## decorators/local

Adds a list of local decorators only to the dashboard JQAdm client

```
admin/jqadm/dashboard/job/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.08

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Dashboard\Decorator\*") around the JQAdm client.

```
 admin/jqadm/dashboard/job/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Dashboard\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/job/decorators/excludes
* admin/jqadm/dashboard/job/decorators/global

## name

Name of the job subpart used by the JQAdm dashboard implementation

```
admin/jqadm/dashboard/job/name = Standard
```

* Default: Standard
* Type: string - Last part of the JQAdm class name
* Since: 2017.08

Use "Myname" if your class is named "\Aimeos\Admin\Jqadm\Dashboard\Job\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## standard/subparts

List of JQAdm sub-clients rendered within the dashboard job section

```
admin/jqadm/dashboard/job/standard/subparts = Array
(
)
```

* Default: Array
* Type: array - List of sub-client names
* Since: 2017.08

The output of the frontend is composed of the code generated by the JQAdm
clients. Each JQAdm client can consist of serveral (or none) sub-clients
that are responsible for rendering certain sub-parts of the output. The
sub-clients can contain JQAdm clients themselves and therefore a
hierarchical tree of JQAdm clients is composed. Each JQAdm client creates
the output that is placed inside the container of its parent.

At first, always the JQAdm code generated by the parent is printed, then
the JQAdm code of its sub-clients. The job of the JQAdm sub-clients
determines the job of the output of these sub-clients inside the parent
container. If the configured list of clients is

```
 array( "subclient1", "subclient2" )
```

you can easily change the job of the output by reordering the subparts:

```
 admin/jqadm/<clients>/subparts = array( "subclient1", "subclient2" )
```

You can also remove one or more parts if they shouldn't be rendered:

```
 admin/jqadm/<clients>/subparts = array( "subclient1" )
```

As the clients only generates structural JQAdm, the layout defined via CSS
should support adding, removing or reordering content by a fluid like
design.


## template-list

Relative path to the HTML body template of the job subpart for the dashboard.

```
admin/jqadm/dashboard/job/template-list = dashboard/list-job-standard
```

* Default: dashboard/list-job-standard
* Type: string - Relative path to the template creating the HTML code
* Since: 2017.08

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in admin/jqadm/templates).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "default" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "default"
should be replaced by the name of the new class.


# name

Class name of the used account favorite client implementation

```
admin/jqadm/dashboard/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2016.07

Each default admin client can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the client factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Admin\JQAdm\Dashboard\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Admin\JQAdm\Dashboard\Myfavorite
```

then you have to set the this configuration option:

```
 admin/jqadm/dashboard/name = Myfavorite
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyFavorite"!


# order
## countday/decorators/excludes

Excludes decorators added by the "common" option from the dashboard JQAdm client

```
admin/jqadm/dashboard/order/countday/decorators/excludes = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2018.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"admin/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/dashboard/order/countday/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"admin/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/order/countday/decorators/global
* admin/jqadm/dashboard/order/countday/decorators/local

## countday/decorators/global

Adds a list of globally available decorators only to the dashboard JQAdm client

```
admin/jqadm/dashboard/order/countday/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2018.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/dashboard/order/countday/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/order/countday/decorators/excludes
* admin/jqadm/dashboard/order/countday/decorators/local

## countday/decorators/local

Adds a list of local decorators only to the dashboard JQAdm client

```
admin/jqadm/dashboard/order/countday/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2018.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Dashboard\Decorator\*") around the JQAdm client.

```
 admin/jqadm/dashboard/order/countday/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Dashboard\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/order/countday/decorators/excludes
* admin/jqadm/dashboard/order/countday/decorators/global

## countday/name

Name of the order countday subpart used by the JQAdm dashboard implementation

```
admin/jqadm/dashboard/order/countday/name = Standard
```

* Default: Standard
* Type: string - Last part of the JQAdm class name
* Since: 2018.01

Use "Myname" if your class is named "\Aimeos\Admin\Jqadm\Dashboard\Order\Countday\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## countday/standard/subparts

List of JQAdm sub-clients rendered within the dashboard countday section

```
admin/jqadm/dashboard/order/countday/standard/subparts = Array
(
)
```

* Default: Array
* Type: array - List of sub-client names
* Since: 2018.01

The output of the frontend is composed of the code generated by the JQAdm
clients. Each JQAdm client can consist of serveral (or none) sub-clients
that are responsible for rendering certain sub-parts of the output. The
sub-clients can contain JQAdm clients themselves and therefore a
hierarchical tree of JQAdm clients is composed. Each JQAdm client creates
the output that is placed inside the container of its parent.

At first, always the JQAdm code generated by the parent is printed, then
the JQAdm code of its sub-clients. The order of the JQAdm sub-clients
determines the order of the output of these sub-clients inside the parent
container. If the configured list of clients is

```
 array( "subclient1", "subclient2" )
```

you can easily change the order of the output by reordering the subparts:

```
 admin/jqadm/<clients>/subparts = array( "subclient1", "subclient2" )
```

You can also remove one or more parts if they shouldn't be rendered:

```
 admin/jqadm/<clients>/subparts = array( "subclient1" )
```

As the clients only generates structural JQAdm, the layout defined via CSS
should support adding, removing or reordering content by a fluid like
design.


## countday/template-item

Relative path to the HTML body template of the order per countday subpart for the dashboard.

```
admin/jqadm/dashboard/order/countday/template-item = dashboard/item-order-countday-standard
```

* Default: dashboard/item-order-countday-standard
* Type: string - Relative path to the template creating the HTML code
* Since: 2016.04

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in admin/jqadm/templates).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "default" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "default"
should be replaced by the name of the new class.


## counthour/decorators/excludes

Excludes decorators added by the "common" option from the dashboard JQAdm client

```
admin/jqadm/dashboard/order/counthour/decorators/excludes = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2018.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"admin/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/dashboard/order/counthour/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"admin/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/order/counthour/decorators/global
* admin/jqadm/dashboard/order/counthour/decorators/local

## counthour/decorators/global

Adds a list of globally available decorators only to the dashboard JQAdm client

```
admin/jqadm/dashboard/order/counthour/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2018.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/dashboard/order/counthour/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/order/counthour/decorators/excludes
* admin/jqadm/dashboard/order/counthour/decorators/local

## counthour/decorators/local

Adds a list of local decorators only to the dashboard JQAdm client

```
admin/jqadm/dashboard/order/counthour/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2018.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Dashboard\Decorator\*") around the JQAdm client.

```
 admin/jqadm/dashboard/order/counthour/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Dashboard\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/order/counthour/decorators/excludes
* admin/jqadm/dashboard/order/counthour/decorators/global

## counthour/name

Name of the order counthour subpart used by the JQAdm dashboard implementation

```
admin/jqadm/dashboard/order/counthour/name = Standard
```

* Default: Standard
* Type: string - Last part of the JQAdm class name
* Since: 2018.01

Use "Myname" if your class is named "\Aimeos\Admin\Jqadm\Dashboard\Order\Counthour\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## counthour/standard/subparts

List of JQAdm sub-clients rendered within the dashboard counthour section

```
admin/jqadm/dashboard/order/counthour/standard/subparts = Array
(
)
```

* Default: Array
* Type: array - List of sub-client names
* Since: 2018.01

The output of the frontend is composed of the code generated by the JQAdm
clients. Each JQAdm client can consist of serveral (or none) sub-clients
that are responsible for rendering certain sub-parts of the output. The
sub-clients can contain JQAdm clients themselves and therefore a
hierarchical tree of JQAdm clients is composed. Each JQAdm client creates
the output that is placed inside the container of its parent.

At first, always the JQAdm code generated by the parent is printed, then
the JQAdm code of its sub-clients. The order of the JQAdm sub-clients
determines the order of the output of these sub-clients inside the parent
container. If the configured list of clients is

```
 array( "subclient1", "subclient2" )
```

you can easily change the order of the output by reordering the subparts:

```
 admin/jqadm/<clients>/subparts = array( "subclient1", "subclient2" )
```

You can also remove one or more parts if they shouldn't be rendered:

```
 admin/jqadm/<clients>/subparts = array( "subclient1" )
```

As the clients only generates structural JQAdm, the layout defined via CSS
should support adding, removing or reordering content by a fluid like
design.


## counthour/template-item

Relative path to the HTML body template of the order per counthour subpart for the dashboard.

```
admin/jqadm/dashboard/order/counthour/template-item = dashboard/item-order-counthour-standard
```

* Default: dashboard/item-order-counthour-standard
* Type: string - Relative path to the template creating the HTML code
* Since: 2016.04

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in admin/jqadm/templates).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "default" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "default"
should be replaced by the name of the new class.


## countpaystatus/decorators/excludes

Excludes decorators added by the "common" option from the dashboard JQAdm client

```
admin/jqadm/dashboard/order/countpaystatus/decorators/excludes = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2018.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"admin/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/dashboard/order/countpaystatus/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"admin/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/order/countpaystatus/decorators/global
* admin/jqadm/dashboard/order/countpaystatus/decorators/local

## countpaystatus/decorators/global

Adds a list of globally available decorators only to the dashboard JQAdm client

```
admin/jqadm/dashboard/order/countpaystatus/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2018.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/dashboard/order/countpaystatus/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/order/countpaystatus/decorators/excludes
* admin/jqadm/dashboard/order/countpaystatus/decorators/local

## countpaystatus/decorators/local

Adds a list of local decorators only to the dashboard JQAdm client

```
admin/jqadm/dashboard/order/countpaystatus/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2018.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Dashboard\Decorator\*") around the JQAdm client.

```
 admin/jqadm/dashboard/order/countpaystatus/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Dashboard\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/order/countpaystatus/decorators/excludes
* admin/jqadm/dashboard/order/countpaystatus/decorators/global

## countpaystatus/name

Name of the order countpaystatus subpart used by the JQAdm dashboard implementation

```
admin/jqadm/dashboard/order/countpaystatus/name = Standard
```

* Default: Standard
* Type: string - Last part of the JQAdm class name
* Since: 2018.01

Use "Myname" if your class is named "\Aimeos\Admin\Jqadm\Dashboard\Order\Countpaystatus\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## countpaystatus/standard/subparts

List of JQAdm sub-clients rendered within the dashboard countpaystatus section

```
admin/jqadm/dashboard/order/countpaystatus/standard/subparts = Array
(
)
```

* Default: Array
* Type: array - List of sub-client names
* Since: 2018.01

The output of the frontend is composed of the code generated by the JQAdm
clients. Each JQAdm client can consist of serveral (or none) sub-clients
that are responsible for rendering certain sub-parts of the output. The
sub-clients can contain JQAdm clients themselves and therefore a
hierarchical tree of JQAdm clients is composed. Each JQAdm client creates
the output that is placed inside the container of its parent.

At first, always the JQAdm code generated by the parent is printed, then
the JQAdm code of its sub-clients. The order of the JQAdm sub-clients
determines the order of the output of these sub-clients inside the parent
container. If the configured list of clients is

```
 array( "subclient1", "subclient2" )
```

you can easily change the order of the output by reordering the subparts:

```
 admin/jqadm/<clients>/subparts = array( "subclient1", "subclient2" )
```

You can also remove one or more parts if they shouldn't be rendered:

```
 admin/jqadm/<clients>/subparts = array( "subclient1" )
```

As the clients only generates structural JQAdm, the layout defined via CSS
should support adding, removing or reordering content by a fluid like
design.


## countpaystatus/template-item

Relative path to the HTML body template of the order per countpaystatus subpart for the dashboard.

```
admin/jqadm/dashboard/order/countpaystatus/template-item = dashboard/item-order-countpaystatus-standard
```

* Default: dashboard/item-order-countpaystatus-standard
* Type: string - Relative path to the template creating the HTML code
* Since: 2016.04

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in admin/jqadm/templates).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "default" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "default"
should be replaced by the name of the new class.


## decorators/excludes

Excludes decorators added by the "common" option from the dashboard JQAdm client

```
admin/jqadm/dashboard/order/decorators/excludes = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2018.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"admin/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/dashboard/order/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"admin/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/order/decorators/global
* admin/jqadm/dashboard/order/decorators/local

## decorators/global

Adds a list of globally available decorators only to the dashboard JQAdm client

```
admin/jqadm/dashboard/order/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2018.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/dashboard/order/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/order/decorators/excludes
* admin/jqadm/dashboard/order/decorators/local

## decorators/local

Adds a list of local decorators only to the dashboard JQAdm client

```
admin/jqadm/dashboard/order/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2018.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Dashboard\Decorator\*") around the JQAdm client.

```
 admin/jqadm/dashboard/order/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Dashboard\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/order/decorators/excludes
* admin/jqadm/dashboard/order/decorators/global

## latest/decorators/excludes

Excludes decorators added by the "common" option from the dashboard JQAdm client

```
admin/jqadm/dashboard/order/latest/decorators/excludes = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2016.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"admin/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/dashboard/order/latest/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"admin/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/order/latest/decorators/global
* admin/jqadm/dashboard/order/latest/decorators/local

## latest/decorators/global

Adds a list of globally available decorators only to the dashboard JQAdm client

```
admin/jqadm/dashboard/order/latest/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2016.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/dashboard/order/latest/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/order/latest/decorators/excludes
* admin/jqadm/dashboard/order/latest/decorators/local

## latest/decorators/local

Adds a list of local decorators only to the dashboard JQAdm client

```
admin/jqadm/dashboard/order/latest/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2016.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Dashboard\Decorator\*") around the JQAdm client.

```
 admin/jqadm/dashboard/order/latest/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Dashboard\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/order/latest/decorators/excludes
* admin/jqadm/dashboard/order/latest/decorators/global

## latest/name

Name of the order latest subpart used by the JQAdm dashboard implementation

```
admin/jqadm/dashboard/order/latest/name = Standard
```

* Default: Standard
* Type: string - Last part of the JQAdm class name
* Since: 2018.01

Use "Myname" if your class is named "\Aimeos\Admin\Jqadm\Dashboard\Order\Latest\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## latest/standard/subparts

List of JQAdm sub-clients rendered within the dashboard latest section

```
admin/jqadm/dashboard/order/latest/standard/subparts = Array
(
)
```

* Default: Array
* Type: array - List of sub-client names
* Since: 2016.07

The output of the frontend is composed of the code generated by the JQAdm
clients. Each JQAdm client can consist of serveral (or none) sub-clients
that are responsible for rendering certain sub-parts of the output. The
sub-clients can contain JQAdm clients themselves and therefore a
hierarchical tree of JQAdm clients is composed. Each JQAdm client creates
the output that is placed inside the container of its parent.

At first, always the JQAdm code generated by the parent is printed, then
the JQAdm code of its sub-clients. The order of the JQAdm sub-clients
determines the order of the output of these sub-clients inside the parent
container. If the configured list of clients is

```
 array( "subclient1", "subclient2" )
```

you can easily change the order of the output by reordering the subparts:

```
 admin/jqadm/<clients>/subparts = array( "subclient1", "subclient2" )
```

You can also remove one or more parts if they shouldn't be rendered:

```
 admin/jqadm/<clients>/subparts = array( "subclient1" )
```

As the clients only generates structural JQAdm, the layout defined via CSS
should support adding, removing or reordering content by a fluid like
design.


## latest/template-item

Relative path to the HTML body template of the latest orders subpart for the dashboard.

```
admin/jqadm/dashboard/order/latest/template-item = dashboard/item-order-latest-standard
```

* Default: dashboard/item-order-latest-standard
* Type: string - Relative path to the template creating the HTML code
* Since: 2016.04

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in admin/jqadm/templates).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "default" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "default"
should be replaced by the name of the new class.


## name

Name of the order subpart used by the JQAdm dashboard implementation

```
admin/jqadm/dashboard/order/name = Standard
```

* Default: Standard
* Type: string - Last part of the JQAdm class name
* Since: 2016.07

Use "Myname" if your class is named "\Aimeos\Admin\Jqadm\Dashboard\Order\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## salesday/decorators/excludes

Excludes decorators added by the "common" option from the dashboard JQAdm client

```
admin/jqadm/dashboard/order/salesday/decorators/excludes = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2018.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"admin/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/dashboard/order/salesday/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"admin/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/order/salesday/decorators/global
* admin/jqadm/dashboard/order/salesday/decorators/local

## salesday/decorators/global

Adds a list of globally available decorators only to the dashboard JQAdm client

```
admin/jqadm/dashboard/order/salesday/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2018.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/dashboard/order/salesday/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/order/salesday/decorators/excludes
* admin/jqadm/dashboard/order/salesday/decorators/local

## salesday/decorators/local

Adds a list of local decorators only to the dashboard JQAdm client

```
admin/jqadm/dashboard/order/salesday/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2018.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Dashboard\Decorator\*") around the JQAdm client.

```
 admin/jqadm/dashboard/order/salesday/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Dashboard\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/order/salesday/decorators/excludes
* admin/jqadm/dashboard/order/salesday/decorators/global

## salesday/name

Name of the order salesday subpart used by the JQAdm dashboard implementation

```
admin/jqadm/dashboard/order/salesday/name = Standard
```

* Default: Standard
* Type: string - Last part of the JQAdm class name
* Since: 2018.01

Use "Myname" if your class is named "\Aimeos\Admin\Jqadm\Dashboard\Order\Salesday\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## salesday/standard/subparts

List of JQAdm sub-clients rendered within the dashboard salesday section

```
admin/jqadm/dashboard/order/salesday/standard/subparts = Array
(
)
```

* Default: Array
* Type: array - List of sub-client names
* Since: 2018.01

The output of the frontend is composed of the code generated by the JQAdm
clients. Each JQAdm client can consist of serveral (or none) sub-clients
that are responsible for rendering certain sub-parts of the output. The
sub-clients can contain JQAdm clients themselves and therefore a
hierarchical tree of JQAdm clients is composed. Each JQAdm client creates
the output that is placed inside the container of its parent.

At first, always the JQAdm code generated by the parent is printed, then
the JQAdm code of its sub-clients. The order of the JQAdm sub-clients
determines the order of the output of these sub-clients inside the parent
container. If the configured list of clients is

```
 array( "subclient1", "subclient2" )
```

you can easily change the order of the output by reordering the subparts:

```
 admin/jqadm/<clients>/subparts = array( "subclient1", "subclient2" )
```

You can also remove one or more parts if they shouldn't be rendered:

```
 admin/jqadm/<clients>/subparts = array( "subclient1" )
```

As the clients only generates structural JQAdm, the layout defined via CSS
should support adding, removing or reordering content by a fluid like
design.


## salesday/template-item

Relative path to the HTML body template of the order per salesday subpart for the dashboard.

```
admin/jqadm/dashboard/order/salesday/template-item = dashboard/item-order-salesday-standard
```

* Default: dashboard/item-order-salesday-standard
* Type: string - Relative path to the template creating the HTML code
* Since: 2018.01

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in admin/jqadm/templates).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "default" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "default"
should be replaced by the name of the new class.


## salesmonth/decorators/excludes

Excludes decorators added by the "common" option from the dashboard JQAdm client

```
admin/jqadm/dashboard/order/salesmonth/decorators/excludes = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2018.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"admin/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/dashboard/order/salesmonth/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"admin/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/order/salesmonth/decorators/global
* admin/jqadm/dashboard/order/salesmonth/decorators/local

## salesmonth/decorators/global

Adds a list of globally available decorators only to the dashboard JQAdm client

```
admin/jqadm/dashboard/order/salesmonth/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2018.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/dashboard/order/salesmonth/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/order/salesmonth/decorators/excludes
* admin/jqadm/dashboard/order/salesmonth/decorators/local

## salesmonth/decorators/local

Adds a list of local decorators only to the dashboard JQAdm client

```
admin/jqadm/dashboard/order/salesmonth/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2018.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Dashboard\Decorator\*") around the JQAdm client.

```
 admin/jqadm/dashboard/order/salesmonth/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Dashboard\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/order/salesmonth/decorators/excludes
* admin/jqadm/dashboard/order/salesmonth/decorators/global

## salesmonth/name

Name of the order salesmonth subpart used by the JQAdm dashboard implementation

```
admin/jqadm/dashboard/order/salesmonth/name = Standard
```

* Default: Standard
* Type: string - Last part of the JQAdm class name
* Since: 2018.01

Use "Myname" if your class is named "\Aimeos\Admin\Jqadm\Dashboard\Order\Salesmonth\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## salesmonth/standard/subparts

List of JQAdm sub-clients rendered within the dashboard salesmonth section

```
admin/jqadm/dashboard/order/salesmonth/standard/subparts = Array
(
)
```

* Default: Array
* Type: array - List of sub-client names
* Since: 2018.01

The output of the frontend is composed of the code generated by the JQAdm
clients. Each JQAdm client can consist of serveral (or none) sub-clients
that are responsible for rendering certain sub-parts of the output. The
sub-clients can contain JQAdm clients themselves and therefore a
hierarchical tree of JQAdm clients is composed. Each JQAdm client creates
the output that is placed inside the container of its parent.

At first, always the JQAdm code generated by the parent is printed, then
the JQAdm code of its sub-clients. The order of the JQAdm sub-clients
determines the order of the output of these sub-clients inside the parent
container. If the configured list of clients is

```
 array( "subclient1", "subclient2" )
```

you can easily change the order of the output by reordering the subparts:

```
 admin/jqadm/<clients>/subparts = array( "subclient1", "subclient2" )
```

You can also remove one or more parts if they shouldn't be rendered:

```
 admin/jqadm/<clients>/subparts = array( "subclient1" )
```

As the clients only generates structural JQAdm, the layout defined via CSS
should support adding, removing or reordering content by a fluid like
design.


## salesmonth/template-item

Relative path to the HTML body template of the order per salesmonth subpart for the dashboard.

```
admin/jqadm/dashboard/order/salesmonth/template-item = dashboard/item-order-salesmonth-standard
```

* Default: dashboard/item-order-salesmonth-standard
* Type: string - Relative path to the template creating the HTML code
* Since: 2018.01

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in admin/jqadm/templates).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "default" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "default"
should be replaced by the name of the new class.


## salesweekday/decorators/excludes

Excludes decorators added by the "common" option from the dashboard JQAdm client

```
admin/jqadm/dashboard/order/salesweekday/decorators/excludes = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2018.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"admin/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/dashboard/order/salesweekday/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"admin/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/order/salesweekday/decorators/global
* admin/jqadm/dashboard/order/salesweekday/decorators/local

## salesweekday/decorators/global

Adds a list of globally available decorators only to the dashboard JQAdm client

```
admin/jqadm/dashboard/order/salesweekday/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2018.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/dashboard/order/salesweekday/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/order/salesweekday/decorators/excludes
* admin/jqadm/dashboard/order/salesweekday/decorators/local

## salesweekday/decorators/local

Adds a list of local decorators only to the dashboard JQAdm client

```
admin/jqadm/dashboard/order/salesweekday/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2018.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Dashboard\Decorator\*") around the JQAdm client.

```
 admin/jqadm/dashboard/order/salesweekday/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Dashboard\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/order/salesweekday/decorators/excludes
* admin/jqadm/dashboard/order/salesweekday/decorators/global

## salesweekday/name

Name of the order salesweekday subpart used by the JQAdm dashboard implementation

```
admin/jqadm/dashboard/order/salesweekday/name = Standard
```

* Default: Standard
* Type: string - Last part of the JQAdm class name
* Since: 2018.01

Use "Myname" if your class is named "\Aimeos\Admin\Jqadm\Dashboard\Order\Salesweekday\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## salesweekday/standard/subparts

List of JQAdm sub-clients rendered within the dashboard salesweekday section

```
admin/jqadm/dashboard/order/salesweekday/standard/subparts = Array
(
)
```

* Default: Array
* Type: array - List of sub-client names
* Since: 2018.01

The output of the frontend is composed of the code generated by the JQAdm
clients. Each JQAdm client can consist of serveral (or none) sub-clients
that are responsible for rendering certain sub-parts of the output. The
sub-clients can contain JQAdm clients themselves and therefore a
hierarchical tree of JQAdm clients is composed. Each JQAdm client creates
the output that is placed inside the container of its parent.

At first, always the JQAdm code generated by the parent is printed, then
the JQAdm code of its sub-clients. The order of the JQAdm sub-clients
determines the order of the output of these sub-clients inside the parent
container. If the configured list of clients is

```
 array( "subclient1", "subclient2" )
```

you can easily change the order of the output by reordering the subparts:

```
 admin/jqadm/<clients>/subparts = array( "subclient1", "subclient2" )
```

You can also remove one or more parts if they shouldn't be rendered:

```
 admin/jqadm/<clients>/subparts = array( "subclient1" )
```

As the clients only generates structural JQAdm, the layout defined via CSS
should support adding, removing or reordering content by a fluid like
design.


## salesweekday/template-item

Relative path to the HTML body template of the order per salesweekday subpart for the dashboard.

```
admin/jqadm/dashboard/order/salesweekday/template-item = dashboard/item-order-salesweekday-standard
```

* Default: dashboard/item-order-salesweekday-standard
* Type: string - Relative path to the template creating the HTML code
* Since: 2016.04

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in admin/jqadm/templates).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "default" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "default"
should be replaced by the name of the new class.


## servicedelivery/decorators/excludes

Excludes decorators added by the "common" option from the dashboard JQAdm client

```
admin/jqadm/dashboard/order/servicedelivery/decorators/excludes = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2018.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"admin/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/dashboard/order/servicedelivery/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"admin/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/order/servicedelivery/decorators/global
* admin/jqadm/dashboard/order/servicedelivery/decorators/local

## servicedelivery/decorators/global

Adds a list of globally available decorators only to the dashboard JQAdm client

```
admin/jqadm/dashboard/order/servicedelivery/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2018.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/dashboard/order/servicedelivery/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/order/servicedelivery/decorators/excludes
* admin/jqadm/dashboard/order/servicedelivery/decorators/local

## servicedelivery/decorators/local

Adds a list of local decorators only to the dashboard JQAdm client

```
admin/jqadm/dashboard/order/servicedelivery/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2018.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Dashboard\Decorator\*") around the JQAdm client.

```
 admin/jqadm/dashboard/order/servicedelivery/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Dashboard\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/order/servicedelivery/decorators/excludes
* admin/jqadm/dashboard/order/servicedelivery/decorators/global

## servicedelivery/name

Name of the order deliverytype subpart used by the JQAdm dashboard implementation

```
admin/jqadm/dashboard/order/servicedelivery/name = Standard
```

* Default: Standard
* Type: string - Last part of the JQAdm class name
* Since: 2018.01

Use "Myname" if your class is named "\Aimeos\Admin\Jqadm\Dashboard\Order\Servicedelivery\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## servicedelivery/standard/subparts

List of JQAdm sub-clients rendered within the dashboard servicedelivery section

```
admin/jqadm/dashboard/order/servicedelivery/standard/subparts = Array
(
)
```

* Default: Array
* Type: array - List of sub-client names
* Since: 2018.01

The output of the frontend is composed of the code generated by the JQAdm
clients. Each JQAdm client can consist of serveral (or none) sub-clients
that are responsible for rendering certain sub-parts of the output. The
sub-clients can contain JQAdm clients themselves and therefore a
hierarchical tree of JQAdm clients is composed. Each JQAdm client creates
the output that is placed inside the container of its parent.

At first, always the JQAdm code generated by the parent is printed, then
the JQAdm code of its sub-clients. The order of the JQAdm sub-clients
determines the order of the output of these sub-clients inside the parent
container. If the configured list of clients is

```
 array( "subclient1", "subclient2" )
```

you can easily change the order of the output by reordering the subparts:

```
 admin/jqadm/<clients>/subparts = array( "subclient1", "subclient2" )
```

You can also remove one or more parts if they shouldn't be rendered:

```
 admin/jqadm/<clients>/subparts = array( "subclient1" )
```

As the clients only generates structural JQAdm, the layout defined via CSS
should support adding, removing or reordering content by a fluid like
design.


## servicedelivery/template-item

Relative path to the HTML body template of the order per servicedelivery subpart for the dashboard.

```
admin/jqadm/dashboard/order/servicedelivery/template-item = dashboard/item-order-servicedelivery-standard
```

* Default: dashboard/item-order-servicedelivery-standard
* Type: string - Relative path to the template creating the HTML code
* Since: 2016.04

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in admin/jqadm/templates).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "default" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "default"
should be replaced by the name of the new class.


## servicepayment/decorators/excludes

Excludes decorators added by the "common" option from the dashboard JQAdm client

```
admin/jqadm/dashboard/order/servicepayment/decorators/excludes = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2018.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"admin/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/dashboard/order/servicepayment/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"admin/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/order/servicepayment/decorators/global
* admin/jqadm/dashboard/order/servicepayment/decorators/local

## servicepayment/decorators/global

Adds a list of globally available decorators only to the dashboard JQAdm client

```
admin/jqadm/dashboard/order/servicepayment/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2018.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/dashboard/order/servicepayment/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/order/servicepayment/decorators/excludes
* admin/jqadm/dashboard/order/servicepayment/decorators/local

## servicepayment/decorators/local

Adds a list of local decorators only to the dashboard JQAdm client

```
admin/jqadm/dashboard/order/servicepayment/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2018.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Dashboard\Decorator\*") around the JQAdm client.

```
 admin/jqadm/dashboard/order/servicepayment/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Dashboard\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/order/servicepayment/decorators/excludes
* admin/jqadm/dashboard/order/servicepayment/decorators/global

## servicepayment/name

Name of the order servicepayment subpart used by the JQAdm dashboard implementation

```
admin/jqadm/dashboard/order/servicepayment/name = Standard
```

* Default: Standard
* Type: string - Last part of the JQAdm class name
* Since: 2018.01

Use "Myname" if your class is named "\Aimeos\Admin\Jqadm\Dashboard\Order\Servicepayment\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## servicepayment/standard/subparts

List of JQAdm sub-clients rendered within the dashboard servicepayment section

```
admin/jqadm/dashboard/order/servicepayment/standard/subparts = Array
(
)
```

* Default: Array
* Type: array - List of sub-client names
* Since: 2018.01

The output of the frontend is composed of the code generated by the JQAdm
clients. Each JQAdm client can consist of serveral (or none) sub-clients
that are responsible for rendering certain sub-parts of the output. The
sub-clients can contain JQAdm clients themselves and therefore a
hierarchical tree of JQAdm clients is composed. Each JQAdm client creates
the output that is placed inside the container of its parent.

At first, always the JQAdm code generated by the parent is printed, then
the JQAdm code of its sub-clients. The order of the JQAdm sub-clients
determines the order of the output of these sub-clients inside the parent
container. If the configured list of clients is

```
 array( "subclient1", "subclient2" )
```

you can easily change the order of the output by reordering the subparts:

```
 admin/jqadm/<clients>/subparts = array( "subclient1", "subclient2" )
```

You can also remove one or more parts if they shouldn't be rendered:

```
 admin/jqadm/<clients>/subparts = array( "subclient1" )
```

As the clients only generates structural JQAdm, the layout defined via CSS
should support adding, removing or reordering content by a fluid like
design.


## servicepayment/template-item

Relative path to the HTML body template of the order per servicepayment subpart for the dashboard.

```
admin/jqadm/dashboard/order/servicepayment/template-item = dashboard/item-order-servicepayment-standard
```

* Default: dashboard/item-order-servicepayment-standard
* Type: string - Relative path to the template creating the HTML code
* Since: 2016.04

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in admin/jqadm/templates).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "default" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "default"
should be replaced by the name of the new class.


## standard/subparts

List of JQAdm sub-clients rendered within the dashboard order section

```
admin/jqadm/dashboard/order/standard/subparts = Array
(
    [latest] => latest
    [salesday] => salesday
    [salesmonth] => salesmonth
    [salesweekday] => salesweekday
    [countday] => countday
    [countpaystatus] => countpaystatus
    [counthour] => counthour
    [servicepayment] => servicepayment
    [servicedelivery] => servicedelivery
)
```

* Default: Array
* Type: array - List of sub-client names
* Since: 2018.01

The output of the frontend is composed of the code generated by the JQAdm
clients. Each JQAdm client can consist of serveral (or none) sub-clients
that are responsible for rendering certain sub-parts of the output. The
sub-clients can contain JQAdm clients themselves and therefore a
hierarchical tree of JQAdm clients is composed. Each JQAdm client creates
the output that is placed inside the container of its parent.

At first, always the JQAdm code generated by the parent is printed, then
the JQAdm code of its sub-clients. The order of the JQAdm sub-clients
determines the order of the output of these sub-clients inside the parent
container. If the configured list of clients is

```
 array( "subclient1", "subclient2" )
```

you can easily change the order of the output by reordering the subparts:

```
 admin/jqadm/<clients>/subparts = array( "subclient1", "subclient2" )
```

You can also remove one or more parts if they shouldn't be rendered:

```
 admin/jqadm/<clients>/subparts = array( "subclient1" )
```

As the clients only generates structural JQAdm, the layout defined via CSS
should support adding, removing or reordering content by a fluid like
design.


## template-list

Relative path to the HTML body template of the order subpart for the dashboard.

```
admin/jqadm/dashboard/order/template-list = dashboard/list-order-standard
```

* Default: dashboard/list-order-standard
* Type: string - Relative path to the template creating the HTML code
* Since: 2018.01

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in admin/jqadm/templates).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "default" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "default"
should be replaced by the name of the new class.


# setting
## decorators/excludes

Excludes decorators added by the "common" option from the dashboard JQAdm client

```
admin/jqadm/dashboard/setting/decorators/excludes = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2020.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"admin/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/dashboard/setting/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"admin/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/setting/decorators/global
* admin/jqadm/dashboard/setting/decorators/local

## decorators/global

Adds a list of globally available decorators only to the dashboard JQAdm client

```
admin/jqadm/dashboard/setting/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2020.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/dashboard/setting/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/setting/decorators/excludes
* admin/jqadm/dashboard/setting/decorators/local

## decorators/local

Adds a list of local decorators only to the dashboard JQAdm client

```
admin/jqadm/dashboard/setting/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2020.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Dashboard\Decorator\*") around the JQAdm client.

```
 admin/jqadm/dashboard/setting/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Dashboard\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/setting/decorators/excludes
* admin/jqadm/dashboard/setting/decorators/global

## name

Name of the setting subpart used by the JQAdm dashboard implementation

```
admin/jqadm/dashboard/setting/name = Standard
```

* Default: Standard
* Type: string - Last part of the JQAdm class name
* Since: 2020.01

Use "Myname" if your class is named "\Aimeos\Admin\Jqadm\Dashboard\Setting\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## standard/subparts

List of JQAdm sub-clients rendered within the dashboard setting section

```
admin/jqadm/dashboard/setting/standard/subparts = Array
(
)
```

* Default: Array
* Type: array - List of sub-client names
* Since: 2020.01

The output of the frontend is composed of the code generated by the JQAdm
clients. Each JQAdm client can consist of serveral (or none) sub-clients
that are responsible for rendering certain sub-parts of the output. The
sub-clients can contain JQAdm clients themselves and therefore a
hierarchical tree of JQAdm clients is composed. Each JQAdm client creates
the output that is placed inside the container of its parent.

At first, always the JQAdm code generated by the parent is printed, then
the JQAdm code of its sub-clients. The setting of the JQAdm sub-clients
determines the setting of the output of these sub-clients inside the parent
container. If the configured list of clients is

```
 array( "subclient1", "subclient2" )
```

you can easily change the setting of the output by reordering the subparts:

```
 admin/jqadm/<clients>/subparts = array( "subclient1", "subclient2" )
```

You can also remove one or more parts if they shouldn't be rendered:

```
 admin/jqadm/<clients>/subparts = array( "subclient1" )
```

As the clients only generates structural JQAdm, the layout defined via CSS
should support adding, removing or reordering content by a fluid like
design.


## template-list

Relative path to the HTML body template of the setting subpart for the dashboard.

```
admin/jqadm/dashboard/setting/template-list = dashboard/list-setting-standard
```

* Default: dashboard/list-setting-standard
* Type: string - Relative path to the template creating the HTML code
* Since: 2020.01

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in admin/jqadm/templates).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "default" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "default"
should be replaced by the name of the new class.


# standard
## subparts

List of JQAdm sub-clients rendered within the dashboard section

```
admin/jqadm/dashboard/standard/subparts = Array
(
    [setting] => setting
    [job] => job
    [order] => order
)
```

* Default: Array
* Type: array - List of sub-client names
* Since: 2016.07

The output of the frontend is composed of the code generated by the JQAdm
clients. Each JQAdm client can consist of serveral (or none) sub-clients
that are responsible for rendering certain sub-parts of the output. The
sub-clients can contain JQAdm clients themselves and therefore a
hierarchical tree of JQAdm clients is composed. Each JQAdm client creates
the output that is placed inside the container of its parent.

At first, always the JQAdm code generated by the parent is printed, then
the JQAdm code of its sub-clients. The order of the JQAdm sub-clients
determines the order of the output of these sub-clients inside the parent
container. If the configured list of clients is

```
 array( "subclient1", "subclient2" )
```

you can easily change the order of the output by reordering the subparts:

```
 admin/jqadm/<clients>/subparts = array( "subclient1", "subclient2" )
```

You can also remove one or more parts if they shouldn't be rendered:

```
 admin/jqadm/<clients>/subparts = array( "subclient1" )
```

As the clients only generates structural JQAdm, the layout defined via CSS
should support adding, removing or reordering content by a fluid like
design.


# template-list

Relative path to the HTML body template of the dashboard.

```
admin/jqadm/dashboard/template-list = dashboard/list-standard
```

* Default: dashboard/list-standard
* Type: string - Relative path to the template creating the HTML code
* Since: 2016.04

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in admin/jqadm/templates).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "default" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "default"
should be replaced by the name of the new class.

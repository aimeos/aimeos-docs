
# decorators
## excludes

Excludes decorators added by the "common" option from the dashboard JQAdm client

```
admin/jqadm/dashboard/decorators/excludes = 
```

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
admin/jqadm/dashboard/decorators/global = 
```

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
admin/jqadm/dashboard/decorators/local = 
```

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
(
)

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
(
)

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


## subparts

List of JQAdm sub-clients rendered within the dashboard job section

```
admin/jqadm/dashboard/job/subparts = Array
(
)
```

* Default: Array
(
)

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
admin/jqadm/dashboard/job/template-list = dashboard/list-job
```

* Default: dashboard/list-job
* Type: string - Relative path to the template creating the HTML code
* Since: 2017.08

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in templates/admin/jqadm).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "default" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "default"
should be replaced by the name of the new class.


# name

Class name of the used account favorite client implementation

```
admin/jqadm/dashboard/name = 
```

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


# notify
## decorators/excludes

Excludes decorators added by the "common" option from the dashboard JQAdm client

```
admin/jqadm/dashboard/notify/decorators/excludes = 
```

* Type: array - List of decorator names
* Since: 2022.04

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"admin/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/dashboard/notify/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"admin/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/notify/decorators/global
* admin/jqadm/dashboard/notify/decorators/local

## decorators/global

Adds a list of globally available decorators only to the dashboard JQAdm client

```
admin/jqadm/dashboard/notify/decorators/global = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2022.04

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/dashboard/notify/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/notify/decorators/excludes
* admin/jqadm/dashboard/notify/decorators/local

## decorators/local

Adds a list of local decorators only to the dashboard JQAdm client

```
admin/jqadm/dashboard/notify/decorators/local = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2022.04

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Dashboard\Decorator\*") around the JQAdm client.

```
 admin/jqadm/dashboard/notify/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Dashboard\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/notify/decorators/excludes
* admin/jqadm/dashboard/notify/decorators/global

## name

Name of the notify subpart used by the JQAdm dashboard implementation

```
admin/jqadm/dashboard/notify/name = Standard
```

* Default: Standard
* Type: string - Last part of the JQAdm class name
* Since: 2022.04

Use "Myname" if your class is named "\Aimeos\Admin\Jqadm\Dashboard\Notify\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## subparts

List of JQAdm sub-clients rendered within the dashboard notify section

```
admin/jqadm/dashboard/notify/subparts = Array
(
)
```

* Default: Array
(
)

* Type: array - List of sub-client names
* Since: 2022.04

The output of the frontend is composed of the code generated by the JQAdm
clients. Each JQAdm client can consist of serveral (or none) sub-clients
that are responsible for rendering certain sub-parts of the output. The
sub-clients can contain JQAdm clients themselves and therefore a
hierarchical tree of JQAdm clients is composed. Each JQAdm client creates
the output that is placed inside the container of its parent.

At first, always the JQAdm code generated by the parent is printed, then
the JQAdm code of its sub-clients. The notify of the JQAdm sub-clients
determines the notify of the output of these sub-clients inside the parent
container. If the configured list of clients is

```
 array( "subclient1", "subclient2" )
```

you can easily change the notify of the output by reordering the subparts:

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

Relative path to the HTML body template of the notify subpart for the dashboard.

```
admin/jqadm/dashboard/notify/template-list = dashboard/list-notify
```

* Default: dashboard/list-notify
* Type: string - Relative path to the template creating the HTML code
* Since: 2022.04

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in templates/admin/jqadm).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "default" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "default"
should be replaced by the name of the new class.


# order
## countcountry/decorators/excludes

Excludes decorators added by the "common" option from the dashboard JQAdm client

```
admin/jqadm/dashboard/order/countcountry/decorators/excludes = 
```

* Type: array - List of decorator names
* Since: 2021.04

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"admin/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/dashboard/order/countcountry/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"admin/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/order/countcountry/decorators/global
* admin/jqadm/dashboard/order/countcountry/decorators/local

## countcountry/decorators/global

Adds a list of globally available decorators only to the dashboard JQAdm client

```
admin/jqadm/dashboard/order/countcountry/decorators/global = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2021.04

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/dashboard/order/countcountry/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/order/countcountry/decorators/excludes
* admin/jqadm/dashboard/order/countcountry/decorators/local

## countcountry/decorators/local

Adds a list of local decorators only to the dashboard JQAdm client

```
admin/jqadm/dashboard/order/countcountry/decorators/local = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2021.04

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Dashboard\Decorator\*") around the JQAdm client.

```
 admin/jqadm/dashboard/order/countcountry/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Dashboard\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/order/countcountry/decorators/excludes
* admin/jqadm/dashboard/order/countcountry/decorators/global

## countcountry/name

Name of the order countcountry subpart used by the JQAdm dashboard implementation

```
admin/jqadm/dashboard/order/countcountry/name = Standard
```

* Default: Standard
* Type: string - Last part of the JQAdm class name
* Since: 2021.04

Use "Myname" if your class is named "\Aimeos\Admin\Jqadm\Dashboard\Order\Countcountry\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## countcountry/subparts

List of JQAdm sub-clients rendered within the dashboard countcountry section

```
admin/jqadm/dashboard/order/countcountry/subparts = Array
(
)
```

* Default: Array
(
)

* Type: array - List of sub-client names
* Since: 2021.04

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


## countcountry/template-item

Relative path to the HTML body template of the order per countcountry subpart for the dashboard.

```
admin/jqadm/dashboard/order/countcountry/template-item = dashboard/item-order-countcountry
```

* Default: dashboard/item-order-countcountry
* Type: string - Relative path to the template creating the HTML code
* Since: 2021.04

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in templates/admin/jqadm).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "default" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "default"
should be replaced by the name of the new class.


## countday/decorators/excludes

Excludes decorators added by the "common" option from the dashboard JQAdm client

```
admin/jqadm/dashboard/order/countday/decorators/excludes = 
```

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
(
)

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
(
)

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


## countday/subparts

List of JQAdm sub-clients rendered within the dashboard countday section

```
admin/jqadm/dashboard/order/countday/subparts = Array
(
)
```

* Default: Array
(
)

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
admin/jqadm/dashboard/order/countday/template-item = dashboard/item-order-countday
```

* Default: dashboard/item-order-countday
* Type: string - Relative path to the template creating the HTML code
* Since: 2016.04

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in templates/admin/jqadm).

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
(
)

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
(
)

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


## counthour/subparts

List of JQAdm sub-clients rendered within the dashboard counthour section

```
admin/jqadm/dashboard/order/counthour/subparts = Array
(
)
```

* Default: Array
(
)

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
admin/jqadm/dashboard/order/counthour/template-item = dashboard/item-order-counthour
```

* Default: dashboard/item-order-counthour
* Type: string - Relative path to the template creating the HTML code
* Since: 2016.04

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in templates/admin/jqadm).

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
(
)

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
(
)

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


## countpaystatus/subparts

List of JQAdm sub-clients rendered within the dashboard countpaystatus section

```
admin/jqadm/dashboard/order/countpaystatus/subparts = Array
(
)
```

* Default: Array
(
)

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
admin/jqadm/dashboard/order/countpaystatus/template-item = dashboard/item-order-countpaystatus
```

* Default: dashboard/item-order-countpaystatus
* Type: string - Relative path to the template creating the HTML code
* Since: 2016.04

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in templates/admin/jqadm).

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
(
)

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
(
)

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
(
)

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
(
)

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


## latest/subparts

List of JQAdm sub-clients rendered within the dashboard latest section

```
admin/jqadm/dashboard/order/latest/subparts = Array
(
)
```

* Default: Array
(
)

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
admin/jqadm/dashboard/order/latest/template-item = dashboard/item-order-latest
```

* Default: dashboard/item-order-latest
* Type: string - Relative path to the template creating the HTML code
* Since: 2016.04

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in templates/admin/jqadm).

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


## quick/countcompleted/decorators/excludes

Excludes decorators added by the "common" option from the dashboard JQAdm client

```
admin/jqadm/dashboard/order/quick/countcompleted/decorators/excludes = 
```

* Type: array - List of decorator names
* Since: 2021.04

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"admin/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/dashboard/order/quick/countcompleted/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"admin/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/order/quick/countcompleted/decorators/global
* admin/jqadm/dashboard/order/quick/countcompleted/decorators/local

## quick/countcompleted/decorators/global

Adds a list of globally available decorators only to the dashboard JQAdm client

```
admin/jqadm/dashboard/order/quick/countcompleted/decorators/global = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2021.04

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/dashboard/order/quick/countcompleted/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/order/quick/countcompleted/decorators/excludes
* admin/jqadm/dashboard/order/quick/countcompleted/decorators/local

## quick/countcompleted/decorators/local

Adds a list of local decorators only to the dashboard JQAdm client

```
admin/jqadm/dashboard/order/quick/countcompleted/decorators/local = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2021.04

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Dashboard\Decorator\*") around the JQAdm client.

```
 admin/jqadm/dashboard/order/quick/countcompleted/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Dashboard\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/order/quick/countcompleted/decorators/excludes
* admin/jqadm/dashboard/order/quick/countcompleted/decorators/global

## quick/countcompleted/name

Name of the order quick/countcompleted subpart used by the JQAdm dashboard implementation

```
admin/jqadm/dashboard/order/quick/countcompleted/name = Standard
```

* Default: Standard
* Type: string - Last part of the JQAdm class name
* Since: 2021.04

Use "Myname" if your class is named "\Aimeos\Admin\Jqadm\Dashboard\Order\Quick\Countorder\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## quick/countcompleted/subparts

List of JQAdm sub-clients rendered within the dashboard quick/countcompleted section

```
admin/jqadm/dashboard/order/quick/countcompleted/subparts = Array
(
)
```

* Default: Array
(
)

* Type: array - List of sub-client names
* Since: 2021.04

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


## quick/countcompleted/template-item

Relative path to the HTML body template of the order per quick/countcompleted subpart for the dashboard.

```
admin/jqadm/dashboard/order/quick/countcompleted/template-item = dashboard/item-order-quick-countcompleted
```

* Default: dashboard/item-order-quick-countcompleted
* Type: string - Relative path to the template creating the HTML code
* Since: 2021.04

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in templates/admin/jqadm).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "default" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "default"
should be replaced by the name of the new class.


## quick/countcustomer/decorators/excludes

Excludes decorators added by the "common" option from the dashboard JQAdm client

```
admin/jqadm/dashboard/order/quick/countcustomer/decorators/excludes = 
```

* Type: array - List of decorator names
* Since: 2021.04

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"admin/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/dashboard/order/quick/countcustomer/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"admin/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/order/quick/countcustomer/decorators/global
* admin/jqadm/dashboard/order/quick/countcustomer/decorators/local

## quick/countcustomer/decorators/global

Adds a list of globally available decorators only to the dashboard JQAdm client

```
admin/jqadm/dashboard/order/quick/countcustomer/decorators/global = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2021.04

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/dashboard/order/quick/countcustomer/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/order/quick/countcustomer/decorators/excludes
* admin/jqadm/dashboard/order/quick/countcustomer/decorators/local

## quick/countcustomer/decorators/local

Adds a list of local decorators only to the dashboard JQAdm client

```
admin/jqadm/dashboard/order/quick/countcustomer/decorators/local = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2021.04

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Dashboard\Decorator\*") around the JQAdm client.

```
 admin/jqadm/dashboard/order/quick/countcustomer/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Dashboard\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/order/quick/countcustomer/decorators/excludes
* admin/jqadm/dashboard/order/quick/countcustomer/decorators/global

## quick/countcustomer/name

Name of the order quick/countcustomer subpart used by the JQAdm dashboard implementation

```
admin/jqadm/dashboard/order/quick/countcustomer/name = Standard
```

* Default: Standard
* Type: string - Last part of the JQAdm class name
* Since: 2021.04

Use "Myname" if your class is named "\Aimeos\Admin\Jqadm\Dashboard\Order\Quick\Countorder\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## quick/countcustomer/subparts

List of JQAdm sub-clients rendered within the dashboard quick/countcustomer section

```
admin/jqadm/dashboard/order/quick/countcustomer/subparts = Array
(
)
```

* Default: Array
(
)

* Type: array - List of sub-client names
* Since: 2021.04

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


## quick/countcustomer/template-item

Relative path to the HTML body template of the order per quick/countcustomer subpart for the dashboard.

```
admin/jqadm/dashboard/order/quick/countcustomer/template-item = dashboard/item-order-quick-countcustomer
```

* Default: dashboard/item-order-quick-countcustomer
* Type: string - Relative path to the template creating the HTML code
* Since: 2021.04

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in templates/admin/jqadm).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "default" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "default"
should be replaced by the name of the new class.


## quick/counttotal/decorators/excludes

Excludes decorators added by the "common" option from the dashboard JQAdm client

```
admin/jqadm/dashboard/order/quick/counttotal/decorators/excludes = 
```

* Type: array - List of decorator names
* Since: 2021.04

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"admin/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/dashboard/order/quick/counttotal/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"admin/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/order/quick/counttotal/decorators/global
* admin/jqadm/dashboard/order/quick/counttotal/decorators/local

## quick/counttotal/decorators/global

Adds a list of globally available decorators only to the dashboard JQAdm client

```
admin/jqadm/dashboard/order/quick/counttotal/decorators/global = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2021.04

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/dashboard/order/quick/counttotal/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/order/quick/counttotal/decorators/excludes
* admin/jqadm/dashboard/order/quick/counttotal/decorators/local

## quick/counttotal/decorators/local

Adds a list of local decorators only to the dashboard JQAdm client

```
admin/jqadm/dashboard/order/quick/counttotal/decorators/local = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2021.04

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Dashboard\Decorator\*") around the JQAdm client.

```
 admin/jqadm/dashboard/order/quick/counttotal/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Dashboard\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/order/quick/counttotal/decorators/excludes
* admin/jqadm/dashboard/order/quick/counttotal/decorators/global

## quick/counttotal/name

Name of the order quick/counttotal subpart used by the JQAdm dashboard implementation

```
admin/jqadm/dashboard/order/quick/counttotal/name = Standard
```

* Default: Standard
* Type: string - Last part of the JQAdm class name
* Since: 2021.04

Use "Myname" if your class is named "\Aimeos\Admin\Jqadm\Dashboard\Order\Quick\Counttotal\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## quick/counttotal/subparts

List of JQAdm sub-clients rendered within the dashboard quick/counttotal section

```
admin/jqadm/dashboard/order/quick/counttotal/subparts = Array
(
)
```

* Default: Array
(
)

* Type: array - List of sub-client names
* Since: 2021.04

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


## quick/counttotal/template-item

Relative path to the HTML body template of the order per quick/counttotal subpart for the dashboard.

```
admin/jqadm/dashboard/order/quick/counttotal/template-item = dashboard/item-order-quick-counttotal
```

* Default: dashboard/item-order-quick-counttotal
* Type: string - Relative path to the template creating the HTML code
* Since: 2021.04

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in templates/admin/jqadm).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "default" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "default"
should be replaced by the name of the new class.


## quick/countunfinished/decorators/excludes

Excludes decorators added by the "common" option from the dashboard JQAdm client

```
admin/jqadm/dashboard/order/quick/countunfinished/decorators/excludes = 
```

* Type: array - List of decorator names
* Since: 2021.04

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"admin/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/dashboard/order/quick/countunfinished/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"admin/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/order/quick/countunfinished/decorators/global
* admin/jqadm/dashboard/order/quick/countunfinished/decorators/local

## quick/countunfinished/decorators/global

Adds a list of globally available decorators only to the dashboard JQAdm client

```
admin/jqadm/dashboard/order/quick/countunfinished/decorators/global = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2021.04

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/dashboard/order/quick/countunfinished/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/order/quick/countunfinished/decorators/excludes
* admin/jqadm/dashboard/order/quick/countunfinished/decorators/local

## quick/countunfinished/decorators/local

Adds a list of local decorators only to the dashboard JQAdm client

```
admin/jqadm/dashboard/order/quick/countunfinished/decorators/local = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2021.04

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Dashboard\Decorator\*") around the JQAdm client.

```
 admin/jqadm/dashboard/order/quick/countunfinished/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Dashboard\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/order/quick/countunfinished/decorators/excludes
* admin/jqadm/dashboard/order/quick/countunfinished/decorators/global

## quick/countunfinished/name

Name of the order quick/countunfinished subpart used by the JQAdm dashboard implementation

```
admin/jqadm/dashboard/order/quick/countunfinished/name = Standard
```

* Default: Standard
* Type: string - Last part of the JQAdm class name
* Since: 2021.04

Use "Myname" if your class is named "\Aimeos\Admin\Jqadm\Dashboard\Order\Quick\Countorder\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## quick/countunfinished/subparts

List of JQAdm sub-clients rendered within the dashboard quick/countunfinished section

```
admin/jqadm/dashboard/order/quick/countunfinished/subparts = Array
(
)
```

* Default: Array
(
)

* Type: array - List of sub-client names
* Since: 2021.04

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


## quick/countunfinished/template-item

Relative path to the HTML body template of the order per quick/countunfinished subpart for the dashboard.

```
admin/jqadm/dashboard/order/quick/countunfinished/template-item = dashboard/item-order-quick-countunfinished
```

* Default: dashboard/item-order-quick-countunfinished
* Type: string - Relative path to the template creating the HTML code
* Since: 2021.04

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in templates/admin/jqadm).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "default" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "default"
should be replaced by the name of the new class.


## quick/decorators/excludes

Excludes decorators added by the "common" option from the dashboard JQAdm client

```
admin/jqadm/dashboard/order/quick/decorators/excludes = 
```

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
 admin/jqadm/dashboard/order/quick/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"admin/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/order/quick/decorators/global
* admin/jqadm/dashboard/order/quick/decorators/local

## quick/decorators/global

Adds a list of globally available decorators only to the dashboard JQAdm client

```
admin/jqadm/dashboard/order/quick/decorators/global = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2018.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/dashboard/order/quick/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/order/quick/decorators/excludes
* admin/jqadm/dashboard/order/quick/decorators/local

## quick/decorators/local

Adds a list of local decorators only to the dashboard JQAdm client

```
admin/jqadm/dashboard/order/quick/decorators/local = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2018.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Dashboard\Decorator\*") around the JQAdm client.

```
 admin/jqadm/dashboard/order/quick/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Dashboard\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/dashboard/order/quick/decorators/excludes
* admin/jqadm/dashboard/order/quick/decorators/global

## quick/name

Name of the quick order subpart used by the JQAdm dashboard implementation

```
admin/jqadm/dashboard/order/quick/name = Standard
```

* Default: Standard
* Type: string - Last part of the JQAdm class name
* Since: 2016.07

Use "Myname" if your class is named "\Aimeos\Admin\Jqadm\Dashboard\Order\Quick\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## quick/subparts

List of JQAdm sub-clients rendered within the dashboard order section

```
admin/jqadm/dashboard/order/quick/subparts = Array
(
    [counttotal] => counttotal
    [countcompleted] => countcompleted
    [countunfinished] => countunfinished
    [countcustomer] => countcustomer
)
```

* Default: Array
(
)

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


## quick/template-list

Relative path to the HTML body template of the order quick subpart for the dashboard.

```
admin/jqadm/dashboard/order/quick/template-list = dashboard/item-order-quick
```

* Default: dashboard/item-order-quick
* Type: string - Relative path to the template creating the HTML code
* Since: 2018.01

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in templates/admin/jqadm).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "default" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "default"
should be replaced by the name of the new class.


## salesday/decorators/excludes

Excludes decorators added by the "common" option from the dashboard JQAdm client

```
admin/jqadm/dashboard/order/salesday/decorators/excludes = 
```

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
(
)

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
(
)

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


## salesday/subparts

List of JQAdm sub-clients rendered within the dashboard salesday section

```
admin/jqadm/dashboard/order/salesday/subparts = Array
(
)
```

* Default: Array
(
)

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
admin/jqadm/dashboard/order/salesday/template-item = dashboard/item-order-salesday
```

* Default: dashboard/item-order-salesday
* Type: string - Relative path to the template creating the HTML code
* Since: 2018.01

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in templates/admin/jqadm).

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
(
)

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
(
)

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


## salesmonth/subparts

List of JQAdm sub-clients rendered within the dashboard salesmonth section

```
admin/jqadm/dashboard/order/salesmonth/subparts = Array
(
)
```

* Default: Array
(
)

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
admin/jqadm/dashboard/order/salesmonth/template-item = dashboard/item-order-salesmonth
```

* Default: dashboard/item-order-salesmonth
* Type: string - Relative path to the template creating the HTML code
* Since: 2018.01

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in templates/admin/jqadm).

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
(
)

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
(
)

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


## salesweekday/subparts

List of JQAdm sub-clients rendered within the dashboard salesweekday section

```
admin/jqadm/dashboard/order/salesweekday/subparts = Array
(
)
```

* Default: Array
(
)

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
admin/jqadm/dashboard/order/salesweekday/template-item = dashboard/item-order-salesweekday
```

* Default: dashboard/item-order-salesweekday
* Type: string - Relative path to the template creating the HTML code
* Since: 2016.04

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in templates/admin/jqadm).

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
(
)

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
(
)

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


## servicedelivery/subparts

List of JQAdm sub-clients rendered within the dashboard servicedelivery section

```
admin/jqadm/dashboard/order/servicedelivery/subparts = Array
(
)
```

* Default: Array
(
)

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
admin/jqadm/dashboard/order/servicedelivery/template-item = dashboard/item-order-servicedelivery
```

* Default: dashboard/item-order-servicedelivery
* Type: string - Relative path to the template creating the HTML code
* Since: 2016.04

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in templates/admin/jqadm).

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
(
)

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
(
)

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


## servicepayment/subparts

List of JQAdm sub-clients rendered within the dashboard servicepayment section

```
admin/jqadm/dashboard/order/servicepayment/subparts = Array
(
)
```

* Default: Array
(
)

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
admin/jqadm/dashboard/order/servicepayment/template-item = dashboard/item-order-servicepayment
```

* Default: dashboard/item-order-servicepayment
* Type: string - Relative path to the template creating the HTML code
* Since: 2016.04

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in templates/admin/jqadm).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "default" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "default"
should be replaced by the name of the new class.


## subparts

List of JQAdm sub-clients rendered within the dashboard order section

```
admin/jqadm/dashboard/order/subparts = Array
(
    [quick] => quick
    [latest] => latest
    [salesday] => salesday
    [salesmonth] => salesmonth
    [salesweekday] => salesweekday
    [countday] => countday
    [countpaystatus] => countpaystatus
    [counthour] => counthour
    [countcountry] => countcountry
    [servicepayment] => servicepayment
    [servicedelivery] => servicedelivery
)
```

* Default: Array
(
)

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
admin/jqadm/dashboard/order/template-list = dashboard/list-order
```

* Default: dashboard/list-order
* Type: string - Relative path to the template creating the HTML code
* Since: 2018.01

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in templates/admin/jqadm).

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
(
)

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
(
)

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


## subparts

List of JQAdm sub-clients rendered within the dashboard setting section

```
admin/jqadm/dashboard/setting/subparts = Array
(
)
```

* Default: Array
(
)

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
admin/jqadm/dashboard/setting/template-list = dashboard/list-setting
```

* Default: dashboard/list-setting
* Type: string - Relative path to the template creating the HTML code
* Since: 2020.01

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in templates/admin/jqadm).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "default" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "default"
should be replaced by the name of the new class.


# subparts

List of JQAdm sub-clients rendered within the dashboard section

```
admin/jqadm/dashboard/subparts = Array
(
    [notify] => notify
    [setting] => setting
    [job] => job
    [order] => order
)
```

* Default: Array
(
)

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
admin/jqadm/dashboard/template-list = dashboard/list
```

* Default: dashboard/list
* Type: string - Relative path to the template creating the HTML code
* Since: 2016.04

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in templates/admin/jqadm).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "default" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "default"
should be replaced by the name of the new class.

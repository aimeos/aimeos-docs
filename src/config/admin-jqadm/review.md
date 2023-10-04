
# decorators
## excludes

Excludes decorators added by the "common" option from the review JQAdm client

```
admin/jqadm/review/decorators/excludes = 
```

* Type: array - List of decorator names
* Since: 2020.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"client/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/review/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"client/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/review/decorators/global
* admin/jqadm/review/decorators/local

## global

Adds a list of globally available decorators only to the review JQAdm client

```
admin/jqadm/review/decorators/global = 
```

* Type: array - List of decorator names
* Since: 2020.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/review/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/review/decorators/excludes
* admin/jqadm/review/decorators/local

## local

Adds a list of local decorators only to the review JQAdm client

```
admin/jqadm/review/decorators/local = 
```

* Type: array - List of decorator names
* Since: 2020.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Review\Decorator\*") around the JQAdm client.

```
 admin/jqadm/review/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Review\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/review/decorators/excludes
* admin/jqadm/review/decorators/global

# domains

List of domain names reviews can be assigend to

```
admin/jqadm/review/domains = Array
(
    [0] => product
)
```

* Default: Array
(
    [0] => product
)

* Type: array - List of domains names
* Since: 2020.10

Changes the list of domain names shown in the review list view which can be
filtered for.


# fields

List of review columns that should be displayed in the list view

```
admin/jqadm/review/fields = Array
(
    [0] => review.status
    [1] => review.rating
    [2] => review.comment
    [3] => review.response
    [4] => review.ctime
)
```

* Default: Array
(
    [0] => review.status
    [1] => review.rating
    [2] => review.comment
    [3] => review.response
    [4] => review.ctime
)

* Type: array - List of field names, i.e. search keys
* Since: 2020.10

Changes the list of review columns shown by default in the review list view.
The columns can be changed by the editor as required within the administraiton
interface.

The names of the colums are in fact the search keys defined by the managers,
e.g. "review.id" for the customer ID.


# name

Class name of the used account favorite client implementation

```
admin/jqadm/review/name = 
```

* Type: string - Last part of the class name
* Since: 2017.07

Each default admin client can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the client factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Admin\JQAdm\Review\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Admin\JQAdm\Review\Myfavorite
```

then you have to set the this configuration option:

```
 admin/jqadm/review/name = Myfavorite
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyFavorite"!


# subparts

List of JQAdm sub-clients rendered within the review section

```
admin/jqadm/review/subparts = Array
(
)
```

* Default: Array
(
)

* Type: array - List of sub-client names
* Since: 2020.10

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


# template-item

Relative path to the HTML body template for the review item.

```
admin/jqadm/review/template-item = review/item
```

* Default: review/item
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


# template-list

Relative path to the HTML body template for the review list.

```
admin/jqadm/review/template-list = review/list
```

* Default: review/list
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

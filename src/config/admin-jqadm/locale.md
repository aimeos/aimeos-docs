
# currency
## decorators/excludes

Excludes decorators added by the "common" option from the locale JQAdm client

```
admin/jqadm/locale/currency/decorators/excludes = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"client/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/locale/currency/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"client/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/locale/currency/decorators/global
* admin/jqadm/locale/currency/decorators/local

## decorators/global

Adds a list of globally available decorators only to the locale JQAdm client

```
admin/jqadm/locale/currency/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/locale/currency/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/locale/currency/decorators/excludes
* admin/jqadm/locale/currency/decorators/local

## decorators/local

Adds a list of local decorators only to the locale JQAdm client

```
admin/jqadm/locale/currency/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Locale\Currency\Decorator\*") around the JQAdm client.

```
 admin/jqadm/locale/currency/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Locale\Currency\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/locale/currency/decorators/excludes
* admin/jqadm/locale/currency/decorators/global

## fields

List of locale columns that should be displayed in the list view

```
admin/jqadm/locale/currency/fields = Array
(
    [0] => locale.currency.status
    [1] => locale.currency.code
    [2] => locale.currency.label
)
```

* Default: Array
* Type: array - List of field names, i.e. search keys
* Since: 2017.10

Changes the list of locale columns shown by default in the locale list view.
The columns can be changed by the editor as required within the administraiton
interface.

The names of the colums are in fact the search keys defined by the managers,
e.g. "locale.currency.id" for the locale ID.


## name

Class name of the used account favorite client implementation

```
admin/jqadm/locale/currency/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2017.10

Each default admin client can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the client factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Admin\JQAdm\Locale\Currency\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Admin\JQAdm\Locale\Currency\Myfavorite
```

then you have to set the this configuration option:

```
 admin/jqadm/locale/currency/name = Myfavorite
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyFavorite"!


## standard/subparts

List of JQAdm sub-clients rendered within the locale section

```
admin/jqadm/locale/currency/standard/subparts = Array
(
)
```

* Default: Array
* Type: array - List of sub-client names
* Since: 2017.10

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


## template-item

Relative path to the HTML body template for the locale item.

```
admin/jqadm/locale/currency/template-item = locale/currency/item-standard
```

* Default: locale/currency/item-standard
* Type: string - Relative path to the template creating the HTML code
* Since: 2017.10

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


## template-list

Relative path to the HTML body template for the locale list.

```
admin/jqadm/locale/currency/template-list = locale/currency/list-standard
```

* Default: locale/currency/list-standard
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


# decorators
## excludes

Excludes decorators added by the "common" option from the locale JQAdm client

```
admin/jqadm/locale/decorators/excludes = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"client/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/locale/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"client/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/locale/decorators/global
* admin/jqadm/locale/decorators/local

## global

Adds a list of globally available decorators only to the locale JQAdm client

```
admin/jqadm/locale/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/locale/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/locale/decorators/excludes
* admin/jqadm/locale/decorators/local

## local

Adds a list of local decorators only to the locale JQAdm client

```
admin/jqadm/locale/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Locale\Decorator\*") around the JQAdm client.

```
 admin/jqadm/locale/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Locale\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/locale/decorators/excludes
* admin/jqadm/locale/decorators/global

# fields

List of locale columns that should be displayed in the list view

```
admin/jqadm/locale/fields = Array
(
    [0] => locale.status
    [1] => locale.languageid
    [2] => locale.currencyid
    [3] => locale.position
)
```

* Default: Array
* Type: array - List of field names, i.e. search keys
* Since: 2017.10

Changes the list of locale columns shown by default in the locale list view.
The columns can be changed by the editor as required within the administraiton
interface.

The names of the colums are in fact the search keys defined by the managers,
e.g. "locale.id" for the locale ID.


# language
## decorators/excludes

Excludes decorators added by the "common" option from the locale JQAdm client

```
admin/jqadm/locale/language/decorators/excludes = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"client/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/locale/language/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"client/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/locale/language/decorators/global
* admin/jqadm/locale/language/decorators/local

## decorators/global

Adds a list of globally available decorators only to the locale JQAdm client

```
admin/jqadm/locale/language/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/locale/language/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/locale/language/decorators/excludes
* admin/jqadm/locale/language/decorators/local

## decorators/local

Adds a list of local decorators only to the locale JQAdm client

```
admin/jqadm/locale/language/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Locale\Language\Decorator\*") around the JQAdm client.

```
 admin/jqadm/locale/language/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Locale\Language\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/locale/language/decorators/excludes
* admin/jqadm/locale/language/decorators/global

## fields

List of locale columns that should be displayed in the list view

```
admin/jqadm/locale/language/fields = Array
(
    [0] => locale.language.status
    [1] => locale.language.code
    [2] => locale.language.label
)
```

* Default: Array
* Type: array - List of field names, i.e. search keys
* Since: 2017.10

Changes the list of locale columns shown by default in the locale list view.
The columns can be changed by the editor as required within the administraiton
interface.

The names of the colums are in fact the search keys defined by the managers,
e.g. "locale.language.id" for the locale ID.


## name

Class name of the used account favorite client implementation

```
admin/jqadm/locale/language/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2017.10

Each default admin client can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the client factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Admin\JQAdm\Locale\Language\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Admin\JQAdm\Locale\Language\Myfavorite
```

then you have to set the this configuration option:

```
 admin/jqadm/locale/language/name = Myfavorite
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyFavorite"!


## standard/subparts

List of JQAdm sub-clients rendered within the locale section

```
admin/jqadm/locale/language/standard/subparts = Array
(
)
```

* Default: Array
* Type: array - List of sub-client names
* Since: 2017.10

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


## template-item

Relative path to the HTML body template for the locale item.

```
admin/jqadm/locale/language/template-item = locale/language/item-standard
```

* Default: locale/language/item-standard
* Type: string - Relative path to the template creating the HTML code
* Since: 2017.10

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


## template-list

Relative path to the HTML body template for the locale list.

```
admin/jqadm/locale/language/template-list = locale/language/list-standard
```

* Default: locale/language/list-standard
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


# name

Class name of the used account favorite client implementation

```
admin/jqadm/locale/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2017.10

Each default admin client can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the client factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Admin\JQAdm\Locale\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Admin\JQAdm\Locale\Myfavorite
```

then you have to set the this configuration option:

```
 admin/jqadm/locale/name = Myfavorite
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyFavorite"!


# site
## decorators/excludes

Excludes decorators added by the "common" option from the locale JQAdm client

```
admin/jqadm/locale/site/decorators/excludes = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"client/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/locale/site/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"client/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/locale/site/decorators/global
* admin/jqadm/locale/site/decorators/local

## decorators/global

Adds a list of globally available decorators only to the locale JQAdm client

```
admin/jqadm/locale/site/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/locale/site/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/locale/site/decorators/excludes
* admin/jqadm/locale/site/decorators/local

## decorators/local

Adds a list of local decorators only to the locale JQAdm client

```
admin/jqadm/locale/site/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Locale\Site\Decorator\*") around the JQAdm client.

```
 admin/jqadm/locale/site/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Locale\Site\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/locale/site/decorators/excludes
* admin/jqadm/locale/site/decorators/global

## fields

List of locale columns that should be displayed in the list view

```
admin/jqadm/locale/site/fields = Array
(
    [0] => locale.site.status
    [1] => locale.site.code
    [2] => locale.site.label
    [3] => locale.site.config
)
```

* Default: Array
* Type: array - List of field names, i.e. search keys
* Since: 2017.10

Changes the list of locale columns shown by default in the locale list view.
The columns can be changed by the editor as required within the administraiton
interface.

The names of the colums are in fact the search keys defined by the managers,
e.g. "locale.site.id" for the locale ID.


## item/config/suggest

List of suggested configuration keys in locale site item panel

```
admin/jqadm/locale/site/item/config/suggest = Array
(
)
```

* Default: Array
* Type: string - List of suggested config keys
* Since: 2017.10

Locale site items can store arbitrary key value pairs. This setting gives editors
a hint which config keys are available and are used in the templates.


## name

Class name of the used account favorite client implementation

```
admin/jqadm/locale/site/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2017.10

Each default admin client can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the client factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Admin\JQAdm\Locale\Site\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Admin\JQAdm\Locale\Site\Myfavorite
```

then you have to set the this configuration option:

```
 admin/jqadm/locale/site/name = Myfavorite
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyFavorite"!


## standard/subparts

List of JQAdm sub-clients rendered within the locale section

```
admin/jqadm/locale/site/standard/subparts = Array
(
)
```

* Default: Array
* Type: array - List of sub-client names
* Since: 2017.10

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


## template-item

Relative path to the HTML body template for the locale item.

```
admin/jqadm/locale/site/template-item = locale/site/item-standard
```

* Default: locale/site/item-standard
* Type: string - Relative path to the template creating the HTML code
* Since: 2017.10

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


## template-list

Relative path to the HTML body template for the locale list.

```
admin/jqadm/locale/site/template-list = locale/site/list-standard
```

* Default: locale/site/list-standard
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


# standard
## subparts

List of JQAdm sub-clients rendered within the locale section

```
admin/jqadm/locale/standard/subparts = Array
(
)
```

* Default: Array
* Type: array - List of sub-client names
* Since: 2017.10

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

Relative path to the HTML body template for the locale item.

```
admin/jqadm/locale/template-item = locale/item-standard
```

* Default: locale/item-standard
* Type: string - Relative path to the template creating the HTML code
* Since: 2017.10

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


# template-list

Relative path to the HTML body template for the locale list.

```
admin/jqadm/locale/template-list = locale/list-standard
```

* Default: locale/list-standard
* Type: string - Relative path to the template creating the HTML code
* Since: 2017.10

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

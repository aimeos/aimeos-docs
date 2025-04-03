
# api
## decorators/excludes

Excludes decorators added by the "common" option from the settings JQAdm client

```
admin/jqadm/settings/api/decorators/excludes = 
```

* Type: array - List of decorator names
* Since: 2024.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"admin/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/settings/api/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"admin/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/settings/api/decorators/global
* admin/jqadm/settings/api/decorators/local

## decorators/global

Adds a list of globally available decorators only to the settings JQAdm client

```
admin/jqadm/settings/api/decorators/global = Array
(
)
```

* Default: 
```
Array
(
)
```
* Type: array - List of decorator names
* Since: 2024.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/settings/api/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/settings/api/decorators/excludes
* admin/jqadm/settings/api/decorators/local

## decorators/local

Adds a list of local decorators only to the settings JQAdm client

```
admin/jqadm/settings/api/decorators/local = Array
(
)
```

* Default: 
```
Array
(
)
```
* Type: array - List of decorator names
* Since: 2024.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Settings\Decorator\*") around the JQAdm client.

```
 admin/jqadm/settings/api/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Settings\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/settings/api/decorators/excludes
* admin/jqadm/settings/api/decorators/global

## deepl/decorators/excludes

Excludes decorators added by the "common" option from the settings JQAdm client

```
admin/jqadm/settings/api/deepl/decorators/excludes = 
```

* Type: array - List of decorator names
* Since: 2024.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"admin/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/settings/api/deepl/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"admin/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/settings/api/deepl/decorators/global
* admin/jqadm/settings/api/deepl/decorators/local

## deepl/decorators/global

Adds a list of globally available decorators only to the settings JQAdm client

```
admin/jqadm/settings/api/deepl/decorators/global = Array
(
)
```

* Default: 
```
Array
(
)
```
* Type: array - List of decorator names
* Since: 2024.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/settings/api/deepl/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/settings/api/deepl/decorators/excludes
* admin/jqadm/settings/api/deepl/decorators/local

## deepl/decorators/local

Adds a list of local decorators only to the settings JQAdm client

```
admin/jqadm/settings/api/deepl/decorators/local = Array
(
)
```

* Default: 
```
Array
(
)
```
* Type: array - List of decorator names
* Since: 2024.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Settings\Decorator\*") around the JQAdm client.

```
 admin/jqadm/settings/api/deepl/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Settings\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/settings/api/deepl/decorators/excludes
* admin/jqadm/settings/api/deepl/decorators/global

## deepl/name

Name of the api DeepL subpart used by the JQAdm settings implementation

```
admin/jqadm/settings/api/deepl/name = Standard
```

* Default: `Standard`
* Type: string - Last part of the JQAdm class name
* Since: 2024.10

Use "Myname" if your class is named "\Aimeos\Admin\Jqadm\Settings\Api\Deepl\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## deepl/template-item

Relative path to the HTML body template of the api DeepL subpart for settings.

```
admin/jqadm/settings/api/deepl/template-item = settings/item-api-deepl
```

* Default: `settings/item-api-deepl`
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

Name of the api subpart used by the JQAdm settings implementation

```
admin/jqadm/settings/api/name = Standard
```

* Default: `Standard`
* Type: string - Last part of the JQAdm class name
* Since: 2024.10

Use "Myname" if your class is named "\Aimeos\Admin\Jqadm\Settings\Api\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## openai/decorators/excludes

Excludes decorators added by the "common" option from the settings JQAdm client

```
admin/jqadm/settings/api/openai/decorators/excludes = 
```

* Type: array - List of decorator names
* Since: 2024.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"admin/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/settings/api/openai/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"admin/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/settings/api/openai/decorators/global
* admin/jqadm/settings/api/openai/decorators/local

## openai/decorators/global

Adds a list of globally available decorators only to the settings JQAdm client

```
admin/jqadm/settings/api/openai/decorators/global = Array
(
)
```

* Default: 
```
Array
(
)
```
* Type: array - List of decorator names
* Since: 2024.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/settings/api/openai/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/settings/api/openai/decorators/excludes
* admin/jqadm/settings/api/openai/decorators/local

## openai/decorators/local

Adds a list of local decorators only to the settings JQAdm client

```
admin/jqadm/settings/api/openai/decorators/local = Array
(
)
```

* Default: 
```
Array
(
)
```
* Type: array - List of decorator names
* Since: 2024.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Settings\Decorator\*") around the JQAdm client.

```
 admin/jqadm/settings/api/openai/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Settings\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/settings/api/openai/decorators/excludes
* admin/jqadm/settings/api/openai/decorators/global

## openai/name

Name of the api DeepL subpart used by the JQAdm settings implementation

```
admin/jqadm/settings/api/openai/name = Standard
```

* Default: `Standard`
* Type: string - Last part of the JQAdm class name
* Since: 2024.10

Use "Myname" if your class is named "\Aimeos\Admin\Jqadm\Settings\Api\Openai\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## openai/template-item

Relative path to the HTML body template of the api DeepL subpart for settings.

```
admin/jqadm/settings/api/openai/template-item = settings/item-api-openai
```

* Default: `settings/item-api-openai`
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


## removebg/decorators/excludes

Excludes decorators added by the "common" option from the settings JQAdm client

```
admin/jqadm/settings/api/removebg/decorators/excludes = 
```

* Type: array - List of decorator names
* Since: 2024.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"admin/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/settings/api/removebg/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"admin/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/settings/api/removebg/decorators/global
* admin/jqadm/settings/api/removebg/decorators/local

## removebg/decorators/global

Adds a list of globally available decorators only to the settings JQAdm client

```
admin/jqadm/settings/api/removebg/decorators/global = Array
(
)
```

* Default: 
```
Array
(
)
```
* Type: array - List of decorator names
* Since: 2024.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/settings/api/removebg/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/settings/api/removebg/decorators/excludes
* admin/jqadm/settings/api/removebg/decorators/local

## removebg/decorators/local

Adds a list of local decorators only to the settings JQAdm client

```
admin/jqadm/settings/api/removebg/decorators/local = Array
(
)
```

* Default: 
```
Array
(
)
```
* Type: array - List of decorator names
* Since: 2024.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Settings\Decorator\*") around the JQAdm client.

```
 admin/jqadm/settings/api/removebg/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Settings\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/settings/api/removebg/decorators/excludes
* admin/jqadm/settings/api/removebg/decorators/global

## removebg/name

Name of the api DeepL subpart used by the JQAdm settings implementation

```
admin/jqadm/settings/api/removebg/name = Standard
```

* Default: `Standard`
* Type: string - Last part of the JQAdm class name
* Since: 2024.10

Use "Myname" if your class is named "\Aimeos\Admin\Jqadm\Settings\Api\Removebg\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## removebg/template-item

Relative path to the HTML body template of the api DeepL subpart for settings.

```
admin/jqadm/settings/api/removebg/template-item = settings/item-api-removebg
```

* Default: `settings/item-api-removebg`
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

List of JQAdm sub-clients rendered within the settings API section

```
admin/jqadm/settings/api/subparts = Array
(
    [deepl] => deepl
    [openai] => openai
    [removebg] => removebg
)
```

* Default: 
```
Array
(
)
```
* Type: array - List of sub-client names
* Since: 2014.10

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

Relative path to the HTML body template of the api subpart for settings.

```
admin/jqadm/settings/api/template-item = settings/item-api
```

* Default: `settings/item-api`
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


# decorators
## excludes

Excludes decorators added by the "common" option from the settings JQAdm client

```
admin/jqadm/settings/decorators/excludes = 
```

* Type: array - List of decorator names
* Since: 2021.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"client/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/settings/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"client/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/settings/decorators/global
* admin/jqadm/settings/decorators/local

## global

Adds a list of globally available decorators only to the settings JQAdm client

```
admin/jqadm/settings/decorators/global = 
```

* Type: array - List of decorator names
* Since: 2021.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/settings/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/settings/decorators/excludes
* admin/jqadm/settings/decorators/local

## local

Adds a list of local decorators only to the settings JQAdm client

```
admin/jqadm/settings/decorators/local = 
```

* Type: array - List of decorator names
* Since: 2021.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Settings\Decorator\*") around the JQAdm client.

```
 admin/jqadm/settings/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Settings\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/settings/decorators/excludes
* admin/jqadm/settings/decorators/global

# logo-size

Maximum width and height of the logo images

```
admin/jqadm/settings/logo-size = Array
(
    [maxwidth] => 
    [maxheight] => 
)
```

* Default: 
```
Array
(
    [maxwidth] => 
    [maxheight] => 
)
```
* Type: array - Associative list with maxwidth/maxheight keys and the maximum width/height in pixels (or NULL)
* Since: 2024.04

This configuration setting allows to define the maximum width and height
of the logo images. The images will be scaled down to the given size if
they are larger than the configured values. If the width or height is
set to null, the image will be scaled proportionally to the other value.


# name

Class name of the used settings panel implementation

```
admin/jqadm/settings/name = 
```

* Type: string - Last part of the class name
* Since: 2021.07

Each default admin client can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the client factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Admin\JQAdm\Settings\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Admin\JQAdm\Settings\Myfavorite
```

then you have to set the this configuration option:

```
 admin/jqadm/settings/name = Myfavorite
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyFavorite"!


# subparts

List of JQAdm sub-clients rendered within the settings section

```
admin/jqadm/settings/subparts = Array
(
    [theme] => theme
    [api] => api
)
```

* Default: 
```
Array
(
)
```
* Type: array - List of sub-client names
* Since: 2021.07

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

Relative path to the HTML body template for the settings item.

```
admin/jqadm/settings/template-item = settings/item
```

* Default: `settings/item`
* Type: string - Relative path to the template creating the HTML code
* Since: 2021.07

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


# theme
## decorators/excludes

Excludes decorators added by the "common" option from the settings JQAdm client

```
admin/jqadm/settings/theme/decorators/excludes = 
```

* Type: array - List of decorator names
* Since: 2022.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"admin/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/settings/theme/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"admin/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/settings/theme/decorators/global
* admin/jqadm/settings/theme/decorators/local

## decorators/global

Adds a list of globally available decorators only to the settings JQAdm client

```
admin/jqadm/settings/theme/decorators/global = Array
(
)
```

* Default: 
```
Array
(
)
```
* Type: array - List of decorator names
* Since: 2022.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/settings/theme/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/settings/theme/decorators/excludes
* admin/jqadm/settings/theme/decorators/local

## decorators/local

Adds a list of local decorators only to the settings JQAdm client

```
admin/jqadm/settings/theme/decorators/local = Array
(
)
```

* Default: 
```
Array
(
)
```
* Type: array - List of decorator names
* Since: 2022.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Settings\Decorator\*") around the JQAdm client.

```
 admin/jqadm/settings/theme/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Settings\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/settings/theme/decorators/excludes
* admin/jqadm/settings/theme/decorators/global

## name

Name of the theme subpart used by the JQAdm settings implementation

```
admin/jqadm/settings/theme/name = Standard
```

* Default: `Standard`
* Type: string - Last part of the JQAdm class name
* Since: 2022.10

Use "Myname" if your class is named "\Aimeos\Admin\Jqadm\Settings\Theme\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## template-item

Relative path to the HTML body template of the theme subpart for settings.

```
admin/jqadm/settings/theme/template-item = settings/item-theme
```

* Default: `settings/item-theme`
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

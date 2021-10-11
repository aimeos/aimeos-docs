
# decorators
## excludes

Excludes decorators added by the "common" option from the catalog frontend controllers

```
controller/frontend/catalog/decorators/excludes = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"controller/frontend/common/decorators/default" before they are wrapped
around the frontend controller.

```
 controller/frontend/catalog/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Controller\Frontend\Common\Decorator\*") added via
"controller/frontend/common/decorators/default" for the catalog frontend controller.

See also:

* controller/frontend/common/decorators/default
* controller/frontend/catalog/decorators/global
* controller/frontend/catalog/decorators/local

## global

Adds a list of globally available decorators only to the catalog frontend controllers

```
controller/frontend/catalog/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Controller\Frontend\Common\Decorator\*") around the frontend controller.

```
 controller/frontend/catalog/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Controller\Frontend\Common\Decorator\Decorator1" only to the frontend controller.

See also:

* controller/frontend/common/decorators/default
* controller/frontend/catalog/decorators/excludes
* controller/frontend/catalog/decorators/local

## local

Adds a list of local decorators only to the catalog frontend controllers

```
controller/frontend/catalog/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Controller\Frontend\Catalog\Decorator\*") around the frontend controller.

```
 controller/frontend/catalog/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Controller\Frontend\Catalog\Decorator\Decorator2" only to the frontend
controller.

See also:

* controller/frontend/common/decorators/default
* controller/frontend/catalog/decorators/excludes
* controller/frontend/catalog/decorators/global

# levels-always

The number of levels in the category tree that should be always displayed

```
controller/frontend/catalog/levels-always = 
```

* Default: 
* Type: integer - Number of tree levels
* Since: 2019.04

Usually, only the root node and the first level of the category
tree is shown in the frontend. Only if the user clicks on a
node in the first level, the page reloads and the sub-nodes of
the chosen category are rendered as well.

Using this configuration option you can enforce the given number
of levels to be always displayed. The root node uses level 0, the
categories below level 1 and so on.

In most cases you can set this value via the administration interface
of the shop application. In that case you often can configure the
levels individually for each catalog filter.

Note: This setting was available between 2014.03 and 2019.04 as
client/html/catalog/filter/tree/levels-always

See also:

* controller/frontend/catalog/levels-only

# levels-only

No more than this number of levels in the category tree should be displayed

```
controller/frontend/catalog/levels-only = 4
```

* Default: 
* Type: integer - Number of tree levels
* Since: 2014.03

If the user clicks on a category node, the page reloads and the
sub-nodes of the chosen category are rendered as well.
Using this configuration option you can enforce that no more than
the given number of levels will be displayed at all. The root
node uses level 0, the categories below level 1 and so on.

In most cases you can set this value via the administration interface
of the shop application. In that case you often can configure the
levels individually for each catalog filter.

Note: This setting was available between 2014.03 and 2019.04 as
client/html/catalog/filter/tree/levels-only

See also:

* controller/frontend/catalog/levels-always

# name

Class name of the used catalog frontend controller implementation

```
controller/frontend/catalog/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2014.03

Each default frontend controller can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the controller factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Controller\Frontend\Catalog\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Controller\Frontend\Catalog\Mycatalog
```

then you have to set the this configuration option:

```
 controller/jobs/frontend/catalog/name = Mycatalog
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyCatalog"!

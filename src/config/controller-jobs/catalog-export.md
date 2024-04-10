
# sitemap
## decorators/excludes

Excludes decorators added by the "common" option from the catalog export sitemap job controller

```
controller/jobs/catalog/export/sitemap/decorators/excludes = Array
(
)
```

* Default: `Array
(
)
`
* Type: array - List of decorator names
* Since: 2019.02

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"controller/jobs/common/decorators/default" before they are wrapped
around the job controller.

```
 controller/jobs/catalog/export/sitemap/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Controller\Jobs\Common\Decorator\*") added via
"controller/jobs/common/decorators/default" to the job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/catalog/export/sitemap/decorators/global
* controller/jobs/catalog/export/sitemap/decorators/local

## decorators/global

Adds a list of globally available decorators only to the catalog export sitemap job controller

```
controller/jobs/catalog/export/sitemap/decorators/global = Array
(
)
```

* Default: `Array
(
)
`
* Type: array - List of decorator names
* Since: 2019.02

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Controller\Jobs\Common\Decorator\*") around the job controller.

```
 controller/jobs/catalog/export/sitemap/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Controller\Jobs\Common\Decorator\Decorator1" only to the job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/catalog/export/sitemap/decorators/excludes
* controller/jobs/catalog/export/sitemap/decorators/local

## decorators/local

Adds a list of local decorators only to the catalog export sitemap job controller

```
controller/jobs/catalog/export/sitemap/decorators/local = Array
(
)
```

* Default: `Array
(
)
`
* Type: array - List of decorator names
* Since: 2019.02

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Controller\Jobs\Catalog\Export\Sitemap\Decorator\*") around the job
controller.

```
 controller/jobs/catalog/export/sitemap/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Controller\Jobs\Catalog\Export\Sitemap\Decorator\Decorator2"
only to the job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/catalog/export/sitemap/export/sitemap/decorators/excludes
* controller/jobs/catalog/export/sitemap/export/sitemap/decorators/global

## domains

List of associated items from other domains that should be fetched for the sitemap

```
controller/jobs/catalog/export/sitemap/domains = Array
(
    [0] => text
)
```

* Default: `Array
(
    [0] => text
)
`
* Type: array - List of domain names
* Since: 2019.02

Catalogs consist not only of the base data but also of texts, media and
other details. Those information is associated to the catalog via their lists.
Using the "domains" option you can make more or less associated items available
in the template.

See also:

* controller/jobs/catalog/export/sitemap/max-items

## hidden

Export hidden categories in site map

```
controller/jobs/catalog/export/sitemap/hidden = 
```

* Default: ``
* Type: bool - TRUE to export hidden categories, FALSE if not
* Since: 2022.01

The catalog site map contains no hidden categories by default. If they
should be part of the export, set this configuration option to TRUE.

See also:

* controller/jobs/catalog/export/sitemap/container/options
* controller/jobs/catalog/export/sitemap/location
* controller/jobs/catalog/export/sitemap/max-items
* controller/jobs/catalog/export/sitemap/max-query
* controller/jobs/catalog/export/sitemap/changefreq

## max-items

Maximum number of categories per site map

```
controller/jobs/catalog/export/sitemap/max-items = 10
```

* Default: `10000`
* Type: integer - Number of categories per file
* Since: 2019.02

Each site map file must not contain more than 50,000 links and it's
size must be less than 10MB. If your catalog URLs are rather long
and one of your site map files is bigger than 10MB, you should set
the number of categories per file to a smaller value until each file
is less than 10MB.

More details about site maps can be found at
[sitemaps.org](http://www.sitemaps.org/protocol.html)

See also:

* controller/jobs/catalog/export/sitemap/domains

## name

Class name of the used catalog sitemap export scheduler controller implementation

```
controller/jobs/catalog/export/sitemap/name = Standard
```

* Default: `Standard`
* Type: string - Last part of the class name
* Since: 2019.02

Each default job controller can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the controller factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Controller\Jobs\Catalog\Export\Sitemap\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Controller\Jobs\Catalog\Export\Sitemap\Mysitemap
```

then you have to set the this configuration option:

```
 controller/jobs/catalog/export/sitemap/name = Mysitemap
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MySitemap"!


## template

Relative path to the XML template of the catalog site map job controller.

```
controller/jobs/catalog/export/sitemap/template = catalog/export/sitemap-items
```

* Default: `catalog/export/sitemap-items`
* Type: string - Relative path to the template creating XML code for the site map
* Since: 2022.10

The template file contains the XML code and processing instructions
to generate the site map files. The configuration string is the path
to the template file relative to the templates directory (usually in
templates/controller/jobs).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "standard" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "standard"
should be replaced by the name of the new class.


## template-index

Relative path to the XML site map index template of the catalog site map job controller.

```
controller/jobs/catalog/export/sitemap/template-index = catalog/export/sitemap-index
```

* Default: `catalog/export/sitemap-index`
* Type: string - Relative path to the template creating XML code for the site map index
* Since: 2015.01

The template file contains the XML code and processing instructions
to generate the site map index files. The configuration string is the path
to the template file relative to the templates directory (usually in
templates/controller/jobs).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "standard" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "standard"
should be replaced by the name of the new class.

See also:

* controller/jobs/catalog/export/sitemap/template-items

# decorators
## excludes

Excludes decorators added by the "common" option from the product export job controller

```
controller/jobs/product/export/decorators/excludes = Array
(
)
```

* Default: `Array
(
)
`
* Type: array - List of decorator names
* Since: 2015.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"controller/jobs/common/decorators/default" before they are wrapped
around the job controller.

```
 controller/jobs/product/export/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Controller\Jobs\Common\Decorator\*") added via
"controller/jobs/common/decorators/default" to the job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/product/export/decorators/global
* controller/jobs/product/export/decorators/local

## global

Adds a list of globally available decorators only to the product export job controller

```
controller/jobs/product/export/decorators/global = Array
(
)
```

* Default: `Array
(
)
`
* Type: array - List of decorator names
* Since: 2015.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Controller\Jobs\Common\Decorator\*") around the job controller.

```
 controller/jobs/product/export/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Controller\Jobs\Common\Decorator\Decorator1" only to the job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/product/export/decorators/excludes
* controller/jobs/product/export/decorators/local

## local

Adds a list of local decorators only to the product export job controller

```
controller/jobs/product/export/decorators/local = Array
(
)
```

* Default: `Array
(
)
`
* Type: array - List of decorator names
* Since: 2015.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Controller\Jobs\Product\Export\Decorator\*") around the job
controller.

```
 controller/jobs/product/export/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Controller\Jobs\Product\Export\Decorator\Decorator2"
only to the job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/product/export/decorators/excludes
* controller/jobs/product/export/decorators/global

# domains

List of associated items from other domains that should be exported too

```
controller/jobs/product/export/domains = Array
(
    [0] => attribute
    [1] => media
    [2] => price
    [3] => product
    [4] => text
)
```

* Default: `Array
(
    [0] => attribute
    [1] => media
    [2] => price
    [3] => product
    [4] => text
)
`
* Type: array - List of domain names
* Since: 2015.01

Products consist not only of the base data but also of texts, media
files, prices, attrbutes and other details. Those information is
associated to the products via their lists. Using the "domains" option
you can make more or less associated items available in the template.

See also:

* controller/jobs/product/export/filename
* controller/jobs/product/export/max-items

# filename

Template for the generated file names

```
controller/jobs/product/export/filename = aimeos-products-%1$d.xml
```

* Default: `aimeos-products-%1$d_%2$s.xml`
* Type: string - File name template
* Since: 2018.04

The generated export files will be named according to the given
string which can contain two place holders: The number of the
exported product and the ISO date/time when the file was created.

See also:

* controller/jobs/product/export/max-items
* controller/jobs/product/export/domains

# max-items

Maximum number of exported products per file

```
controller/jobs/product/export/max-items = 15
```

* Default: `10000`
* Type: integer - Number of products entries per file
* Since: 2015.01

Limits the number of exported products per file as the memory
consumption of processing big files is rather high. Splitting
the data into several files that can also be processed in
parallel is able to speed up importing the files again.

See also:

* controller/jobs/product/export/filename
* controller/jobs/product/export/domains

# name

Class name of the used product suggestions scheduler controller implementation

```
controller/jobs/product/export/name = Standard
```

* Default: `Standard`
* Type: string - Last part of the class name
* Since: 2015.01

Each default job controller can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the controller factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Controller\Jobs\Product\Export\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Controller\Jobs\Product\Export\Myalgorithm
```

then you have to set the this configuration option:

```
 controller/jobs/product/export/name = Myalgorithm
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyOptimizer"!


# partials
## attribute

Name of the partial used for exporting the attribute items into the product XML

```
controller/jobs/product/export/partials/attribute = 
```

* Type: string - Name of the product attribute partial
* Since: 2019.04

When exporting products into XML files, the assoicated attribute items are
added to the product XML node. This partial receives the list and attribute
items that associate the attributes to the product. Then, the partial creates
the XML tags for these items that will be inserted into the product XML.


## media

Name of the partial used for exporting the media items into the product XML

```
controller/jobs/product/export/partials/media = 
```

* Type: string - Name of the product media partial
* Since: 2019.04

When exporting products into XML files, the assoicated media items are
added to the product XML node. This partial receives the list and media
items that associate the media to the product. Then, the partial creates
the XML tags for these items that will be inserted into the product XML.


## price

Name of the partial used for exporting the price items into the product XML

```
controller/jobs/product/export/partials/price = 
```

* Type: string - Name of the product price partial
* Since: 2019.04

When exporting products into XML files, the assoicated price items are
added to the product XML node. This partial receives the list and price
items that associate the prices to the product. Then, the partial creates
the XML tags for these items that will be inserted into the product XML.


## product

Name of the partial used for exporting the product items into the product XML

```
controller/jobs/product/export/partials/product = 
```

* Type: string - Name of the product product partial
* Since: 2019.04

When exporting products into XML files, the assoicated product items are
added to the product XML node. This partial receives the list and product
items that associate the products to the product. Then, the partial creates
the XML tags for these items that will be inserted into the product XML.


## text

Name of the partial used for exporting the text items into the product XML

```
controller/jobs/product/export/partials/text = 
```

* Type: string - Name of the product text partial
* Since: 2019.04

When exporting products into XML files, the assoicated text items are
added to the product XML node. This partial receives the list and text
items that associate the texts to the product. Then, the partial creates
the XML tags for these items that will be inserted into the product XML.


# sitemap
## decorators/excludes

Excludes decorators added by the "common" option from the product export sitemap job controller

```
controller/jobs/product/export/sitemap/decorators/excludes = Array
(
)
```

* Default: `Array
(
)
`
* Type: array - List of decorator names
* Since: 2015.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"controller/jobs/common/decorators/default" before they are wrapped
around the job controller.

```
 controller/jobs/product/export/sitemap/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Controller\Jobs\Common\Decorator\*") added via
"controller/jobs/common/decorators/default" to the job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/product/export/sitemap/decorators/global
* controller/jobs/product/export/sitemap/decorators/local

## decorators/global

Adds a list of globally available decorators only to the product export sitemap job controller

```
controller/jobs/product/export/sitemap/decorators/global = Array
(
)
```

* Default: `Array
(
)
`
* Type: array - List of decorator names
* Since: 2015.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Controller\Jobs\Common\Decorator\*") around the job controller.

```
 controller/jobs/product/export/sitemap/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Controller\Jobs\Common\Decorator\Decorator1" only to the job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/product/export/sitemap/decorators/excludes
* controller/jobs/product/export/sitemap/decorators/local

## decorators/local

Adds a list of local decorators only to the product export sitemap job controller

```
controller/jobs/product/export/sitemap/decorators/local = Array
(
)
```

* Default: `Array
(
)
`
* Type: array - List of decorator names
* Since: 2015.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Controller\Jobs\Product\Export\Sitemap\Decorator\*") around the job
controller.

```
 controller/jobs/product/export/sitemap/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Controller\Jobs\Product\Export\Sitemap\Decorator\Decorator2"
only to the job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/product/export/sitemap/export/sitemap/decorators/excludes
* controller/jobs/product/export/sitemap/export/sitemap/decorators/global

## domains

List of associated items from other domains that should be fetched for the sitemap

```
controller/jobs/product/export/sitemap/domains = Array
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
other details. Those information is associated to the product via their lists.
Using the "domains" option you can make more or less associated items available
in the template.

See also:

* controller/jobs/product/export/sitemap/max-items

## hidden

Export hidden products in site map

```
controller/jobs/product/export/sitemap/hidden = 
```

* Default: ``
* Type: bool - TRUE to export hidden products, FALSE if not
* Since: 2022.01

The product site map contains no hidden products by default. If they
should be part of the export, set this configuration option to TRUE.

See also:

* controller/jobs/product/export/sitemap/container/options
* controller/jobs/product/export/sitemap/location
* controller/jobs/product/export/sitemap/max-items
* controller/jobs/product/export/sitemap/max-query
* controller/jobs/product/export/sitemap/changefreq

## max-items

Maximum number of categories per site map

```
controller/jobs/product/export/sitemap/max-items = 15
```

* Default: `10000`
* Type: integer - Number of categories per file
* Since: 2019.02

Each site map file must not contain more than 50,000 links and it's
size must be less than 10MB. If your product URLs are rather long
and one of your site map files is bigger than 10MB, you should set
the number of categories per file to a smaller value until each file
is less than 10MB.

More details about site maps can be found at
[sitemaps.org](http://www.sitemaps.org/protocol.html)

See also:

* controller/jobs/product/export/sitemap/domains

## name

Class name of the used product suggestions scheduler controller implementation

```
controller/jobs/product/export/sitemap/name = Standard
```

* Default: `Standard`
* Type: string - Last part of the class name
* Since: 2015.01

Each default job controller can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the controller factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Controller\Jobs\Product\Export\Sitemap\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Controller\Jobs\Product\Export\Sitemap\Mysitemap
```

then you have to set the this configuration option:

```
 controller/jobs/product/export/sitemap/name = Mysitemap
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MySitemap"!


## template

Relative path to the XML template of the product site map job controller.

```
controller/jobs/product/export/sitemap/template = product/export/sitemap-items
```

* Default: `product/export/sitemap-items`
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

Relative path to the XML site map index template of the product site map job controller.

```
controller/jobs/product/export/sitemap/template-index = product/export/sitemap-index
```

* Default: `product/export/sitemap-index`
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

* controller/jobs/product/export/sitemap/template-items

# template-items

Relative path to the XML items template of the product site map job controller.

```
controller/jobs/product/export/template-items = product/export/items-body-standard
```

* Default: `product/export/items-body-standard`
* Type: string - Relative path to the template creating XML code for the site map items
* Since: 2015.01

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

See also:

* controller/jobs/product/export/domains
* controller/jobs/product/export/filename
* controller/jobs/product/export/max-items
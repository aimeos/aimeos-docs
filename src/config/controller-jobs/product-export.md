
# decorators
## excludes

Excludes decorators added by the "common" option from the product export job controller

```
controller/jobs/product/export/decorators/excludes = Array
(
)
```

* Default: Array
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

* Default: Array
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

* Default: Array
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
controller/jobs/product/export/domains = 
```

* Default: 
* Type: array - List of domain names
* Since: 2015.01

Products consist not only of the base data but also of texts, media
files, prices, attrbutes and other details. Those information is
associated to the products via their lists. Using the "domains" option
you can make more or less associated items available in the template.

See also:

* controller/jobs/product/export/standard/container/type
* controller/jobs/product/export/standard/container/content
* controller/jobs/product/export/standard/container/options
* controller/jobs/product/export/filename
* controller/jobs/product/export/location
* controller/jobs/product/export/max-items
* controller/jobs/product/export/max-query

# filename

Template for the generated file names

```
controller/jobs/product/export/filename = aimeos-products-%1$d.xml
```

* Default: aimeos-products-%1$d_%2$s.xml
* Type: string - File name template
* Since: 2018.04

The generated export files will be named according to the given
string which can contain two place holders: The number of the
exported product and the ISO date/time when the file was created.

See also:

* controller/jobs/product/export/standard/container/type
* controller/jobs/product/export/standard/container/content
* controller/jobs/product/export/standard/container/options
* controller/jobs/product/export/location
* controller/jobs/product/export/max-items
* controller/jobs/product/export/max-query
* controller/jobs/product/export/domains

# location

Directory where the generated site maps should be placed into

```
controller/jobs/product/export/location = /var/www/aimeos/aimeos-core/ext/ai-controller-jobs/controller/jobs/tests/tmp
```

* Default: 
* Type: string - Absolute directory to store the exported files into
* Since: 2015.01

You have to configure a directory for the generated files on your
server that is writeable by the process generating the files, e.g.

See also:

* controller/jobs/product/export/standard/container/options
* controller/jobs/product/export/max-items
* controller/jobs/product/export/max-query

# max-items

Maximum number of exported products per file

```
controller/jobs/product/export/max-items = 15
```

* Default: 10000
* Type: integer - Number of products entries per file
* Since: 2015.01

Limits the number of exported products per file as the memory
consumption of processing big files is rather high. Splitting
the data into several files that can also be processed in
parallel is able to speed up importing the files again.

See also:

* controller/jobs/product/export/standard/container/type
* controller/jobs/product/export/standard/container/content
* controller/jobs/product/export/standard/container/options
* controller/jobs/product/export/filename
* controller/jobs/product/export/location
* controller/jobs/product/export/max-query
* controller/jobs/product/export/domains

# max-query

Maximum number of products per query

```
controller/jobs/product/export/max-query = 5
```

* Default: 1000
* Type: integer - Number of products per query
* Since: 2015.01

The products are fetched from the database in bunches for efficient
retrieval. The higher the value, the lower the total time the database
is busy finding the records. Higher values also means that record
updates in the tables need to wait longer and the memory consumption
of the PHP process is higher.

See also:

* controller/jobs/product/export/standard/container/type
* controller/jobs/product/export/standard/container/content
* controller/jobs/product/export/standard/container/options
* controller/jobs/product/export/filename
* controller/jobs/product/export/location
* controller/jobs/product/export/max-items
* controller/jobs/product/export/domains

# name

Class name of the used product suggestions scheduler controller implementation

```
controller/jobs/product/export/name = Standard
```

* Default: Standard
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

* Default: 
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

* Default: 
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

* Default: 
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

* Default: 
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

* Default: 
* Type: string - Name of the product text partial
* Since: 2019.04

When exporting products into XML files, the assoicated text items are
added to the product XML node. This partial receives the list and text
items that associate the texts to the product. Then, the partial creates
the XML tags for these items that will be inserted into the product XML.


# sitemap
## baseurl

URL to the folder where the site maps can be accessed, without the filenames.

```
controller/jobs/product/export/sitemap/baseurl = https://www.yourshop.com/sitemaps/
```

* Default: 
* Type: string - Absolute URL
* Since: 2019.06

The site maps must be publically available for download by the search
engines. Individual site map files need a fully qualified URL in the index file.

https://www.yourshop.com/your/sitemap/path/

The location of the site map index file should then be
added to the robots.txt in the document root of your domain:

Sitemap: https://www.yourshop.com/your/sitemap/path/aimeos-sitemap-index.xml

More details about site maps can be found at
[sitemaps.org](http://www.sitemaps.org/protocol.html)

See also:

* controller/jobs/product/export/sitemap/container/options
* controller/jobs/product/export/sitemap/max-items
* controller/jobs/product/export/sitemap/max-query
* controller/jobs/product/export/sitemap/changefreq
* controller/jobs/product/export/sitemap/location

## changefreq

Change frequency of the products

```
controller/jobs/product/export/sitemap/changefreq = daily
```

* Default: daily
* Type: string - One of the pre-defined strings (see description)
* Since: 2015.01

Depending on how often the product content changes (e.g. price updates)
and the site map files are generated you can give search engines a
hint how often they should reindex your site. The site map schema
allows a few pre-defined strings for the change frequency:

* always
* hourly
* daily
* weekly
* monthly
* yearly
* never

More information can be found at
[sitemap.org](http://www.sitemaps.org/protocol.html#xmlTagDefinitions)

See also:

* controller/jobs/product/export/sitemap/container/options
* controller/jobs/product/export/sitemap/location
* controller/jobs/product/export/sitemap/max-items
* controller/jobs/product/export/sitemap/max-query

## container/options

List of file container options for the site map files

```
controller/jobs/product/export/sitemap/container/options = Array
(
    [gzip-mode] => wb
)
```

* Default: Array
* Type: array - Associative list of option name/value pairs
* Since: 2015.01

The directory and the generated site map files are stored using
container/content objects from the core, namely the "Directory"
container and the "Binary" content classes. Both implementations
support some options:

* dir-perm (default: 0755): Permissions if the directory must be created
* gzip-level (default: 5): GZip compression level from 0 to 9 (0 = fast, 9 = best)
* gzip-mode (default: "wb"): Overwrite existing files in binary mode

See also:

* controller/jobs/product/export/sitemap/location
* controller/jobs/product/export/sitemap/max-items
* controller/jobs/product/export/sitemap/max-query
* controller/jobs/product/export/sitemap/changefreq

## decorators/excludes

Excludes decorators added by the "common" option from the product export sitemap job controller

```
controller/jobs/product/export/sitemap/decorators/excludes = Array
(
)
```

* Default: Array
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

* Default: Array
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

* Default: Array
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

* Default: Array
* Type: array - List of domain names
* Since: 2018.07

Products consist not only of the base data but also of texts, media
files, prices, attrbutes and other details. Those information is
associated to the products via their lists. Using the "domains" option
you can make more or less associated items available in the template.

See also:

* controller/jobs/product/export/sitemap/container/options
* controller/jobs/product/export/sitemap/location
* controller/jobs/product/export/sitemap/max-items
* controller/jobs/product/export/sitemap/max-query
* controller/jobs/product/export/sitemap/changefreq

## location

Directory where the generated site maps should be placed into

```
controller/jobs/product/export/sitemap/location = /var/www/aimeos/aimeos-core/ext/ai-controller-jobs/controller/jobs/tests/tmp
```

* Default: 
* Type: string - Absolute directory to store the site maps into
* Since: 2015.01

The site maps must be publically available for download by the search
engines. Therefore, you have to configure a directory for the site
maps in your web space that is writeable by the process generating
the files, e.g.

The location of the site map index file should then be
added to the robots.txt in the document root of your domain:

Sitemap: https://www.yourshop.com/your/sitemap/path/aimeos-sitemap-index.xml

The "sitemapindex-aimeos.xml" file is the site map index file that
references the real site map files which contains the links to the
products. Please make sure that the protocol and domain
(https://www.yourshop.com/) is the same as the ones used in the
product links!

More details about site maps can be found at
[sitemaps.org](http://www.sitemaps.org/protocol.html)

See also:

* controller/jobs/product/export/sitemap/container/options
* controller/jobs/product/export/sitemap/max-items
* controller/jobs/product/export/sitemap/max-query
* controller/jobs/product/export/sitemap/changefreq

## max-items

Maximum number of products per site map

```
controller/jobs/product/export/sitemap/max-items = 5
```

* Default: 50000
* Type: integer - Number of products per file
* Since: 2015.01

Each site map file must not contain more than 50,000 links and it's
size must be less than 10MB. If your product URLs are rather long
and one of your site map files is bigger than 10MB, you should set
the number of products per file to a smaller value until each file
is less than 10MB.

More details about site maps can be found at
[sitemaps.org](http://www.sitemaps.org/protocol.html)

See also:

* controller/jobs/product/export/sitemap/container/options
* controller/jobs/product/export/sitemap/location
* controller/jobs/product/export/sitemap/max-query
* controller/jobs/product/export/sitemap/changefreq
* controller/jobs/product/export/sitemap/domains

## max-query

Maximum number of products per query

```
controller/jobs/product/export/sitemap/max-query = 5
```

* Default: 1000
* Type: integer - Number of products per query
* Since: 2015.01

The products are fetched from the database in bunches for efficient
retrieval. The higher the value, the lower the total time the database
is busy finding the records. Higher values also means that record
updates in the tables need to wait longer and the memory consumption
of the PHP process is higher.

Note: The value of max-query must be smaller than or equal to
{@see controller/jobs/product/export/sitemap/max-items max-items}

See also:

* controller/jobs/product/export/sitemap/container/options
* controller/jobs/product/export/sitemap/location
* controller/jobs/product/export/sitemap/max-items
* controller/jobs/product/export/sitemap/changefreq
* controller/jobs/product/export/sitemap/domains

## name

Class name of the used product suggestions scheduler controller implementation

```
controller/jobs/product/export/sitemap/name = Standard
```

* Default: Standard
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


## standard/template-footer

Relative path to the XML site map footer template of the product site map job controller.

```
controller/jobs/product/export/sitemap/standard/template-footer = product/export/sitemap-items-footer-standard
```

* Default: product/export/sitemap-items-footer-standard
* Type: string - Relative path to the template creating XML code for the site map footer
* Since: 2015.01

The template file contains the XML code and processing instructions
to generate the site map footer. The configuration string is the path
to the template file relative to the templates directory (usually in
controller/jobs/templates).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "standard" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "standard"
should be replaced by the name of the new class.

See also:

* controller/jobs/product/export/sitemap/standard/template-header
* controller/jobs/product/export/sitemap/standard/template-items
* controller/jobs/product/export/sitemap/standard/template-index

## standard/template-header

Relative path to the XML site map header template of the product site map job controller.

```
controller/jobs/product/export/sitemap/standard/template-header = product/export/sitemap-items-header-standard
```

* Default: product/export/sitemap-items-header-standard
* Type: string - Relative path to the template creating XML code for the site map header
* Since: 2015.01

The template file contains the XML code and processing instructions
to generate the site map header. The configuration string is the path
to the template file relative to the templates directory (usually in
controller/jobs/templates).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "standard" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "standard"
should be replaced by the name of the new class.

See also:

* controller/jobs/product/export/sitemap/standard/template-items
* controller/jobs/product/export/sitemap/standard/template-footer
* controller/jobs/product/export/sitemap/standard/template-index

## standard/template-index

Relative path to the XML site map index template of the product site map job controller.

```
controller/jobs/product/export/sitemap/standard/template-index = product/export/sitemap-index-standard
```

* Default: product/export/sitemap-index-standard
* Type: string - Relative path to the template creating XML code for the site map index
* Since: 2015.01

The template file contains the XML code and processing instructions
to generate the site map index files. The configuration string is the path
to the template file relative to the templates directory (usually in
controller/jobs/templates).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "standard" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "standard"
should be replaced by the name of the new class.

See also:

* controller/jobs/product/export/sitemap/standard/template-header
* controller/jobs/product/export/sitemap/standard/template-items
* controller/jobs/product/export/sitemap/standard/template-footer

## standard/template-items

Relative path to the XML items template of the product site map job controller.

```
controller/jobs/product/export/sitemap/standard/template-items = product/export/sitemap-items-body-standard
```

* Default: product/export/sitemap-items-body-standard
* Type: string - Relative path to the template creating XML code for the site map items
* Since: 2015.01

The template file contains the XML code and processing instructions
to generate the site map files. The configuration string is the path
to the template file relative to the templates directory (usually in
controller/jobs/templates).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "standard" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "standard"
should be replaced by the name of the new class.

See also:

* controller/jobs/product/export/sitemap/standard/template-header
* controller/jobs/product/export/sitemap/standard/template-footer
* controller/jobs/product/export/sitemap/standard/template-index

# standard
## container/content

List of file container options for the export files

```
controller/jobs/product/export/standard/container/content = Binary
```

* Default: Binary
* Type: array - Associative list of option name/value pairs
* Since: 2015.01

The generated files are stored using container/content objects from
the core.

See also:

* controller/jobs/product/export/standard/container/type
* controller/jobs/product/export/standard/container/options
* controller/jobs/product/export/location
* controller/jobs/product/export/max-items
* controller/jobs/product/export/max-query

## container/options

List of file container options for the export files

```
controller/jobs/product/export/standard/container/options = Array
(
)
```

* Default: Array
* Type: array - Associative list of option name/value pairs
* Since: 2015.01

The generated files are stored using container/content objects from
the core.

See also:

* controller/jobs/product/export/standard/container/type
* controller/jobs/product/export/standard/container/content
* controller/jobs/product/export/location
* controller/jobs/product/export/max-items
* controller/jobs/product/export/max-query

## container/type

List of file container options for the export files

```
controller/jobs/product/export/standard/container/type = Directory
```

* Default: Directory
* Type: string - Container name
* Since: 2015.01

The generated files are stored using container/content objects from
the core.

See also:

* controller/jobs/product/export/standard/container/content
* controller/jobs/product/export/standard/container/options
* controller/jobs/product/export/location
* controller/jobs/product/export/max-items
* controller/jobs/product/export/max-query

## template-footer

Relative path to the XML site map footer template of the product site map job controller.

```
controller/jobs/product/export/standard/template-footer = product/export/items-footer-standard
```

* Default: product/export/items-footer-standard
* Type: string - Relative path to the template creating XML code for the site map footer
* Since: 2015.01

The template file contains the XML code and processing instructions
to generate the site map footer. The configuration string is the path
to the template file relative to the templates directory (usually in
controller/jobs/templates).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "standard" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "standard"
should be replaced by the name of the new class.

See also:

* controller/jobs/product/export/standard/template-header
* controller/jobs/product/export/standard/template-items
* controller/jobs/product/export/standard/template-index

## template-header

Relative path to the XML site map header template of the product site map job controller.

```
controller/jobs/product/export/standard/template-header = product/export/items-header-standard
```

* Default: product/export/items-header-standard
* Type: string - Relative path to the template creating XML code for the site map header
* Since: 2015.01

The template file contains the XML code and processing instructions
to generate the site map header. The configuration string is the path
to the template file relative to the templates directory (usually in
controller/jobs/templates).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "standard" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "standard"
should be replaced by the name of the new class.

See also:

* controller/jobs/product/export/standard/template-items
* controller/jobs/product/export/standard/template-footer
* controller/jobs/product/export/standard/template-index

## template-items

Relative path to the XML items template of the product site map job controller.

```
controller/jobs/product/export/standard/template-items = product/export/items-body-standard
```

* Default: product/export/items-body-standard
* Type: string - Relative path to the template creating XML code for the site map items
* Since: 2015.01

The template file contains the XML code and processing instructions
to generate the site map files. The configuration string is the path
to the template file relative to the templates directory (usually in
controller/jobs/templates).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "standard" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "standard"
should be replaced by the name of the new class.

See also:

* client/html/account/favorite/standard/template-header
* controller/jobs/product/export/standard/template-footer
* controller/jobs/product/export/standard/template-index

# sitemap
## baseurl

URL to the folder where the site maps can be accessed, without the filenames.

```
controller/jobs/catalog/export/sitemap/baseurl = https://www.yourshop.com/sitemaps/
```

* Default: 
* Type: string - Absolute URL
* Since: 2019.06

The site maps must be publically available for download by the search
engines. Individual site map files need a fully qualified URL in the index file.

https://www.yourshop.com/your/sitemap/path/

The location of the site map index file should then be
added to the robots.txt in the document root of your domain:

Sitemap: https://www.yourshop.com/your/sitemap/path/aimeos-catalog-sitemap-index.xml

More details about site maps can be found at
[sitemaps.org](http://www.sitemaps.org/protocol.html)

See also:

* controller/jobs/catalog/export/sitemap/container/options
* controller/jobs/catalog/export/sitemap/max-items
* controller/jobs/catalog/export/sitemap/max-query
* controller/jobs/catalog/export/sitemap/changefreq
* controller/jobs/catalog/export/sitemap/location

## changefreq

Change frequency of the catalog

```
controller/jobs/catalog/export/sitemap/changefreq = daily
```

* Default: daily
* Type: string - One of the pre-defined strings (see description)
* Since: 2019.02

Depending on how often the catalog content changes
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

* controller/jobs/catalog/export/sitemap/container/options
* controller/jobs/catalog/export/sitemap/location
* controller/jobs/catalog/export/sitemap/max-items
* controller/jobs/catalog/export/sitemap/max-query

## container/options

List of file container options for the site map files

```
controller/jobs/catalog/export/sitemap/container/options = Array
(
    [gzip-mode] => wb
)
```

* Default: Array
* Type: array - Associative list of option name/value pairs
* Since: 2019.02

The directory and the generated site map files are stored using
container/content objects from the core, namely the "Directory"
container and the "Binary" content classes. Both implementations
support some options:

* dir-perm (default: 0755): Permissions if the directory must be created
* gzip-level (default: 5): GZip compression level from 0 to 9 (0 = fast, 9 = best)
* gzip-mode (default: "wb"): Overwrite existing files in binary mode

See also:

* controller/jobs/catalog/export/sitemap/location
* controller/jobs/catalog/export/sitemap/max-items
* controller/jobs/catalog/export/sitemap/max-query
* controller/jobs/catalog/export/sitemap/changefreq

## decorators/excludes

Excludes decorators added by the "common" option from the catalog export sitemap job controller

```
controller/jobs/catalog/export/sitemap/decorators/excludes = Array
(
)
```

* Default: Array
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

* Default: Array
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

* Default: Array
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

* Default: Array
* Type: array - List of domain names
* Since: 2019.02

Catalogs consist not only of the base data but also of texts, media and
other details. Those information is associated to the catalog via their lists.
Using the "domains" option you can make more or less associated items available
in the template.

See also:

* controller/jobs/catalog/export/sitemap/container/options
* controller/jobs/catalog/export/sitemap/location
* controller/jobs/catalog/export/sitemap/max-items
* controller/jobs/catalog/export/sitemap/max-query
* controller/jobs/catalog/export/sitemap/changefreq

## location

Directory where the generated site maps should be placed into

```
controller/jobs/catalog/export/sitemap/location = 
```

* Default: 
* Type: string - Absolute directory to store the site maps into
* Since: 2019.02

The site maps must be publically available for download by the search
engines. Therefore, you have to configure a directory for the site
maps in your web space that is writeable by the process generating
the files, e.g.

The location of the site map index file should then be
added to the robots.txt in the document root of your domain:

Sitemap: https://www.yourshop.com/your/sitemap/path/aimeos-sitemap-index.xml

The "sitemapindex-aimeos.xml" file is the site map index file that
references the real site map files which contains the links to the
catalogs. Please make sure that the protocol and domain
(https://www.yourshop.com/) is the same as the ones used in the
catalog links!

More details about site maps can be found at
[sitemaps.org](http://www.sitemaps.org/protocol.html)

See also:

* controller/jobs/catalog/export/sitemap/container/options
* controller/jobs/catalog/export/sitemap/max-items
* controller/jobs/catalog/export/sitemap/max-query
* controller/jobs/catalog/export/sitemap/changefreq

## max-items

Maximum number of categories per site map

```
controller/jobs/catalog/export/sitemap/max-items = 5
```

* Default: 50000
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

* controller/jobs/catalog/export/sitemap/container/options
* controller/jobs/catalog/export/sitemap/location
* controller/jobs/catalog/export/sitemap/max-query
* controller/jobs/catalog/export/sitemap/changefreq
* controller/jobs/catalog/export/sitemap/domains

## max-query

Maximum number of categories per query

```
controller/jobs/catalog/export/sitemap/max-query = 5
```

* Default: 1000
* Type: integer - Number of categories per query
* Since: 2019.02

The catalogs are fetched from the database in bunches for efficient
retrieval. The higher the value, the lower the total time the database
is busy finding the records. Higher values also means that record
updates in the tables need to wait longer and the memory consumption
of the PHP process is higher.

Note: The value of max-query must be smaller than or equal to
{@see controller/jobs/catalog/export/sitemap/max-items max-items}

See also:

* controller/jobs/catalog/export/sitemap/container/options
* controller/jobs/catalog/export/sitemap/location
* controller/jobs/catalog/export/sitemap/max-items
* controller/jobs/catalog/export/sitemap/changefreq
* controller/jobs/catalog/export/sitemap/domains

## name

Class name of the used catalog sitemap export scheduler controller implementation

```
controller/jobs/catalog/export/sitemap/name = Standard
```

* Default: Standard
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


## standard/template-footer

Relative path to the XML site map footer template of the catalog site map job controller.

```
controller/jobs/catalog/export/sitemap/standard/template-footer = catalog/export/sitemap-items-footer-standard
```

* Default: catalog/export/sitemap-items-footer-standard
* Type: string - Relative path to the template creating XML code for the site map footer
* Since: 2019.02

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

* controller/jobs/catalog/export/sitemap/standard/template-header
* controller/jobs/catalog/export/sitemap/standard/template-items
* controller/jobs/catalog/export/sitemap/standard/template-index

## standard/template-header

Relative path to the XML site map header template of the catalog site map job controller.

```
controller/jobs/catalog/export/sitemap/standard/template-header = catalog/export/sitemap-items-header-standard
```

* Default: catalog/export/sitemap-items-header-standard
* Type: string - Relative path to the template creating XML code for the site map header
* Since: 2019.02

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

* controller/jobs/catalog/export/sitemap/standard/template-items
* controller/jobs/catalog/export/sitemap/standard/template-footer
* controller/jobs/catalog/export/sitemap/standard/template-index

## standard/template-index

Relative path to the XML site map index template of the catalog site map job controller.

```
controller/jobs/catalog/export/sitemap/standard/template-index = catalog/export/sitemap-index-standard
```

* Default: catalog/export/sitemap-index-standard
* Type: string - Relative path to the template creating XML code for the site map index
* Since: 2019.02

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

* controller/jobs/catalog/export/sitemap/standard/template-header
* controller/jobs/catalog/export/sitemap/standard/template-items
* controller/jobs/catalog/export/sitemap/standard/template-footer

## standard/template-items

Relative path to the XML items template of the catalog site map job controller.

```
controller/jobs/catalog/export/sitemap/standard/template-items = catalog/export/sitemap-items-body-standard
```

* Default: catalog/export/sitemap-items-body-standard
* Type: string - Relative path to the template creating XML code for the site map items
* Since: 2019.02

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

* controller/jobs/catalog/export/sitemap/standard/template-header
* controller/jobs/catalog/export/sitemap/standard/template-footer
* controller/jobs/catalog/export/sitemap/standard/template-index
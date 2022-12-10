Most of the time, you already have an ERP system which manages all your products and most of the information required to fill your shop are stored there. In this case, most often you want to bulk import the product information from the ERP system into your shop and update it regularly. You can use the product import job controller for CSV files to import/update the products.

!!! note
    The product import is triggered via a cronjob/scheduler that executes the "product/import/csv" job controller.

# Data location and format

When you export your product data from your ERP system, you need to store the files in a location where they are accessible by the importer. This location has to be configured by the [controller/jobs/product/import/csv/location](../config/controller-jobs/product-import.md#location) setting and it must point to the import file or directory (depending on the container type you would like to use).

Several container types are supported as long as their content consists of CSV-like data:

* Directory container / CSV files
* Zip container / compressed CSV files

You can configure the container type and content format via the [controller/jobs/product/import/csv/container/type](../config/controller-jobs/product-import.md#type) and [controller/jobs/product/import/csv/container/content](../config/controller-jobs/product-import.md#content) settings. Depending on the container/content, you are able to use additional options which are described in the article about creating and reading [container/content files](../infrastructure/read-write-files.md).

For CSV files, there exists a wide range of possibilities about their format because it's not standardized besides the fact that fields are separated by comma (,) but even that isn't set in stone. As a guideline, you should use the following format, which is able to handle all edge cases:

```
 "a string","an ""escaped quote""","a new
 line","a second string"\n
```

The basic rules are:

* All field data must be surrounded by double quotation marks (")
* Fields should be separated by comma
* Double quotation marks need to be escaped by a double quotation mark (duplicating the character)
* A new line character within the field data doesn't need to be treated specially
* The line ending must be a new line character (or a "\r\n" produced by Windows)

Your CSV files can **start with a header** describing the columns, so they are more readable by humans. In this case, you need to configure the import to **skip these lines** using the [controller/jobs/product/import/csv/skip-lines](../config/controller-jobs/product-import.md#skip-lines) configuration.

For additional tuning of the CSV import, the [controller/common/product/import/csv/max-size](../config/controller-jobs/product-import.md#max-size) setting can help you to speed up the import or to reduce the memory consumption of the importer. If you set the number of CSV lines processed in one chunk higher, it will save some database queries at the cost of more memory required to cache the result sets. Similarly, lower values will result in more database queries but also to less allocated memory, which is useful if you have a hard memory limit.

!!! note
    If you are using TYPO3, you have to put all configuration into the TSConfig field of the appropriate scheduler task. For all other frameworks, the settings must be added to the configuration file.

!!! tip
    If something goes wrong or for the progress status when importing big files, messages will be written to the "madmin_log" table in your database. You can see them in the "Log" panel located in the extended left navigation bar of the administration interface.

# Default mapping

You can freely configure how your data is organized in the CSV file but for a quick start, there's a default mapping available that can also be used as example:

```php
[
    'item' => [
        0 => 'product.code', // e.g. unique EAN code
        1 => 'product.label', // UTF-8 encoded text, also used as product name
        2 => 'product.type', // type of the product, e.g. "default" or "selection"
        3 => 'product.status', // enabled (1) or disabled (0)
    ],
    'text' => [
        4 => 'text.type', // e.g. "short" for short description
        5 => 'text.content', // UTF-8 encoded text
        6 => 'text.type', // e.g. "long" for long description
        7 => 'text.content', // UTF-8 encoded text
    ],
    'media' => [
        8 => 'media.url', // relative URL of the product image on the server
    ],
    'price' => [
        9 => 'price.currencyid', // three letter ISO currency code
        10 => 'price.quantity', // the quantity the price (for block pricing)
        11 => 'price.value', // price with decimals separated by a dot
        12 => 'price.taxrate', // tax rate with decimals separated by a dot
    ],
    'attribute' => [
        13 => 'attribute.code', // code of an attribute, will be created if not exists
        14 => 'attribute.type', // e.g. "size", "length", "width", "color", etc.
    ],
    'product' => [
        15 => 'product.code', // e.g. EAN code of another product
        16 => 'product.lists.type', // e.g. "suggestion" for suggested product
    ],
    'property' => [
        17 => 'product.property.value', // arbitrary value for the corresponding type
        18 => 'product.property.type', // e.g. "package-weight"
    ],
    'catalog' => [
        19 => 'catalog.code', // e.g. Unique category code
        20 => 'catalog.lists.type', // e.g. "promotion" for top seller products
    ],
]
```

As you can see, the data from the CSV file is mapped according to its field position in the line to the key of a MShop domain item (e.g. "product.code"). Additionally, fields that belong together are grouped together. The keys of these groups are the names of the data processors that cares about importing the data.

# Test import

You can test the CSV import using the example file and default mapping: [product-import-example.csv](https://aimeos.org/fileadmin/download/products-import-example.csv)

Before you start, add these settings to your configuration:

* [controller/jobs/product/import/csv/location](../config/controller-jobs/product-import.md#location) = <absolute path to the directory with the file>
* [controller/jobs/product/import/csv/skip-lines](../config/controller-jobs/product-import.md#skip-lines) = 1

!!! warning
    The CSV file must be the only file in your configured directory. If you are using TYPO3, the configuration must be added to the TS-Config field of the scheduler task.

# Adapt the mapping

In order to change the default mapping, you can either use the [controller/jobs/product/import/csv/mapping](../config/controller-jobs/product-import.md#mapping) setting.

You can freely rearrange the group names and e.g. put "media" before "text" or after "attribute". This changes the order at which the data is imported and in this example, first the product item, than the text and media data is imported and so on.

Similarly, the mapping inside the groups can be changed to your needs and can be reordered as well. The indexes of the mapping in the groups don't have to be consecutive either, e.g. the "product.code" is at index "0", the next field contains some irrelevant data and afterwards the "media.url" is stored at position "2" before the rest of the product item data follows at index "3" and above. This would lead to a mapping like this:

```php
[
    'item' => [
        0 => 'product.code', // e.g. unique EAN code
        5 => 'product.status', // enabled (1) or disabled (0)
        3 => 'product.label', // UTF-8 encoded text, also used as product name
        4 => 'product.type', // type of the product, e.g. "default" or "selection"
    ],
    // ...
    'media' => [
        2 => 'media.url', // relative URL of the product image on the server
    ],
    // ...
]
```

In fact, you can leave out indexes that shouldn't be imported and use an arbitrary index order. For the reason to understand the mapping immediately, you should at least use a more or less consecutive indexing within the processor group.

# Processor groups

Each group in the mapping (e.g. "item", "text" or "media") defines the CSV fields that will be evaluated by the corresponding processor implementation. A processor is a class that cares about importing "its" data for the product, e.g. the "text" processor imports the data that will be stored in the *mshop_text* table and to associate this data via the *mshop_product_list* table to the corresponding product.

To speed up importing the data, all existing product related data is fetched at once for each product item. You can change the retrieved relations via the [controller/jobs/product/import/csv/domains](../config/controller-jobs/product-import.md#domains) setting. This is especially useful if you don't want to import certain relations like associated products as it reduces the amount of data retrieved from the storage and speeds up the import.

!!! warning
    If you remove a name from the "domains" configuration but still have a mapping defined and your CSV file contains data for this domain, the import is likely to fail because the importer than tries to import duplicate entries. On the other hand, retrieving more domain items than necessary only slows down the importer.

All processors besides the "item" processor are able to import multiple sets at once, e.g. the "text" processor can store several texts available in the CSV line for one product. This means that you can configure the mapping to reference an arbitrary number of text, media, etc. data in one processor group:

```php
[
    // ...
    'text' => [
        5 => 'text.content',
        8 => 'text.type',
        6 => 'text.content',
        9 => 'text.type',
        7 => 'text.content',
        10 => 'text.type',
    ],
    // ...
]
```

This mapping tells the processor to expect three texts ("text.content") and their types ("text.type") in the CSV fields.

!!! warning
The data that belongs together needs to be listed together in the mapping! If the processor finds the same domain item key (e.g. "text.content") in the mapping, it assumes that a new data set begins.

The position of the data in the CSV fields is arbitrary again like shown in the example. It would expect a CSV structure like this:

```
...,"text 1","text 2","text 3","name","short","long",...
```

Contrary, this mapping **won't work**:

```php
[
    // ...
    'text' => [
        5 => 'text.content',
        6 => 'text.content',
        7 => 'text.type',
        8 => 'text.type',
    ],
    // ...
]
```

In this case the processor would assume that the first field (position 5) doesn't have a text type associated and the last field (position 8) doesn't contain a text content. Both will fail during the import.

## Item

The "item" group is the most important data group because it contains the mapping for the product item that must be stored in the database before the rest of the processors can start to insert or update the data they are managing. It accepts data for these domain item keys:

```php
[
    'item' => [
        0 => 'product.code',
        1 => 'product.type',
        2 => 'product.label',
        3 => 'product.status',
        4 => 'product.datestart',
        6 => 'product.dateend',
    ],
]
```

Values for code and type are the absolute minimum that is required to create or update a product item. If no status value is available, the value for "enabled" ("1") will be automatically added. The product label is also used for the product name if no text of type "name" is imported.

## Text

Several product related texts can be part of each CSV line. Supported domain item keys are:

```php
[
    'text' => [
        0 => 'text.languageid',
        1 => 'text.type',
        2 => 'text.label',
        3 => 'text.content',
        4 => 'text.status',
    ],
]
```

The content and the type is required as the minimum amount of data. If you don't have a CSV field for the language ID, the text is imported with the language of the first locale item of the site the importer is running for. Similarly, the label will be the content shorten to max. 100 bytes and the status is set to enabled ("1") if not available.

Additionally, you can import values for the product list relation as well:

```php
[
    'text' => [
        // ...
        7 => 'product.lists.type',
        8 => 'product.lists.datestart',
        9 => 'product.lists.dateend',
        10 => 'product.lists.config',
        11 => 'product.lists.position',
        12 => 'product.lists.status',
    ],
]
```

Here, the type is absolutely necessary. If no value for the position is available, the automatically calculated position is used. The status is set to "enabled" ("1") if not set explicitly.

If one or more relations should stay untouched, you can explicitly configure the list of product list types that will be inserted, updated or deleted via the [controller/jobs/product/import/csv/processor/text/listtypes](../config/controller-jobs/product-import.md#listtypes) setting.

## Media

Several product related images and other media types can be part of each CSV line. Supported domain item keys are:

```php
[
    'media' => [
         0 => 'media.languageid',
        1 => 'media.type',
        2 => 'media.label',
        3 => 'media.mimetype',
        4 => 'media.preview',
        // 4 => 'media.previews', // for several preview images
        5 => 'media.url',
        6 => 'media.status',
    ],
]
```

The URL and the type is required as the minimum amount of data. If you don't have a CSV field for the language ID, the media item is imported with no language and is then considered language independent. The label and preview fields will be filled with the URL and the status is set to enabled ("1") if not available.

The "media.previews" column must contain a JSON encoded object of image width as keys and path to the file as values, e.g. `{"240":"path/to/file","720":"path/to/file2"}`. The "media.url", "media.preview" and "media.previews" fields can contain multiple values separated by a new line:

```
media.url: path/to/file\npath/to/file2
media.preview: path/to/preview\npath/topreview2
media.previews: {"240":"path/to/preview","720":"path/to/preview_720"}\n{"240":"path/to/preview2","720":"path/to/preview2_720"}
```

Additionally, you can import values for the product list relation as well:

```php
[
     'media' => [
        // ...
        9 => 'product.lists.type',
        10 => 'product.lists.datestart',
        11 => 'product.lists.dateend',
        12 => 'product.lists.config',
        13 => 'product.lists.position',
        14 => 'product.lists.status',
    ],
]
```

Here, the type is absolutely necessary. If no value for the position is available, the automatically calculated position is used. The status is set to "enabled" ("1") if not set explicitly.

If one or more relations should stay untouched, you can explicitly configure the list of product list types that will be inserted, updated or deleted via the [controller/jobs/product/import/csv/processor/media/listtypes](../config/controller-jobs/product-import.md#listtypes) setting.

## Price

Several product related prices can be part of each CSV line. Supported domain item keys are:

```php
[
    'price' => [
        0 => 'price.type',
        1 => 'price.label',
        2 => 'price.currencyid',
        3 => 'price.value',
        4 => 'price.costs',
        5 => 'price.rebate',
        6 => 'price.taxrate',
        7 => 'price.status',
    ],
]
```

The value, currency ID and type are required as the minimum amount of data. If you don't have a CSV field for the status, it's set to enabled ("1").

Additionally, you can import values for the product list relation as well:

```php
[
    'price' => [
        // ...
        10 => 'product.lists.type',
        11 => 'product.lists.datestart',
        12 => 'product.lists.dateend',
        13 => 'product.lists.config',
        14 => 'product.lists.position',
        15 => 'product.lists.status',
    ],
]
```

Here, the type is absolutely necessary. If no value for the position is available, the automatically calculated position is used. The status is set to "enabled" ("1") if not set explicitly.

If one or more relations should stay untouched, you can explicitly configure the list of product list types that will be inserted, updated or deleted via the [controller/jobs/product/import/csv/processor/price/listtypes](../config/controller-jobs/product-import.md#listtypes) setting.

## Attribute

Several product related attributes can be part of each CSV line. Supported domain item keys are:

```php
[
    'attribute' => [
        0 => 'attribute.type',
        1 => 'attribute.code',
        2 => 'attribute.label',
        3 => 'attribute.position',
        4 => 'attribute.status',
    ],
]
```

The value and the type are required as the minimum amount of data.

Attributes are usually shared among several products and therefore, the attribute processor associates them to the imported product. Nevertheless, if an attribute doesn't exist, it will be created automatically. You will then be able to enrich these attributes manually by adding texts for different languages or prices if it's an optional attribute. Furthermore, if you don't have a CSV field for the status, it's set to enabled ("1").

Additionally, you can import values for the product list relation as well:

```php
[
    'attribute' => [
        // ...
        7 => 'product.lists.type',
        8 => 'product.lists.datestart',
        9 => 'product.lists.dateend',
        10 => 'product.lists.config',
        11 => 'product.lists.position',
        12 => 'product.lists.status',
    ],
]
```

Here, the type is absolutely necessary. If no value for the position is available, the automatically calculated position is used. The status is set to "enabled" ("1") if not set explicitly.

If one or more relations should stay untouched, you can explicitly configure the list of product list types that will be inserted, updated or deleted via the [controller/jobs/product/import/csv/processor/attribute/listtypes](../config/controller-jobs/product-import.md#listtypes) setting.

## Product

Several product relations can be part of each CSV line. Supported domain item key is only:

```php
[
    'product' => [
        0 => 'product.code',
    ],
]
```

and it's also the minimum amount of data. The real power of the product relations is in the values for the product list relation:

```php
[
    'product' => [
        // ...
        1 => 'product.lists.type',
        2 => 'product.lists.datestart',
        3 => 'product.lists.dateend',
        4 => 'product.lists.config',
        5 => 'product.lists.position',
        6 => 'product.lists.status',
    ],
]
```

Here, the type is absolutely necessary. If no value for the position is available, the automatically calculated position is used. The status is set to "enabled" ("1") if not set explicitly.

If one or more relations should stay untouched, you can explicitly configure the list of product list types that will be inserted, updated or deleted via the [controller/jobs/product/import/csv/processor/product/listtypes](../config/controller-jobs/product-import.md#listtypes) setting.

## Property

Several product related properties (non-shared product data) can be part of each CSV line. Supported domain item keys are:

```php
[
    'property' => [
        0 => 'product.property.type',
        1 => 'product.property.languageid',
        2 => 'product.property.value',
    ],
]
```

The value and the type are required as the minimum amount of data. If you don't have a CSV field for the language ID, the property is imported with no language and is then considered language independent.

## Catalog

Several category relations can be part of each CSV line. Supported domain item key is only:

```php
[
    'catalog' => [
        0 => 'catalog.code',
    ],
]
```

and it's also the minimum amount of data. The real power of the catalog relations is in the values for the catalog list relation:

```php
[
    'catalog' => [
        1 => 'catalog.lists.type',
        2 => 'catalog.lists.datestart',
        3 => 'catalog.lists.dateend',
        4 => 'catalog.lists.config',
        5 => 'catalog.lists.position',
        6 => 'catalog.lists.status',
    ],
]
```

Here, the type is absolutely necessary. If no value for the position is available, the automatically calculated position is used. The status is set to "enabled" ("1") if not set explicitly.

If one or more relations should stay untouched, you can explicitly configure the list of product list types that will be inserted, updated or deleted via the [controller/jobs/product/import/csv/processor/catalog/listtypes](../config/controller-jobs/product-import.md#processorcataloglisttypes) setting.

## Supplier

Several supplier relations can be part of each CSV line. Supported domain item key is only:

```php
[
    'supplier' => [
        0 => 'supplier.code',
    ],
]
```

and it's also the minimum amount of data. The real power of the supplier relations is in the values for the supplier list relation:

```php
[
    'supplier' => [
        1 => 'supplier.lists.type',
        2 => 'supplier.lists.datestart',
        3 => 'supplier.lists.dateend',
        4 => 'supplier.lists.config',
        5 => 'supplier.lists.position',
        6 => 'supplier.lists.status',
    ],
]
```

Here, the type is absolutely necessary. If no value for the position is available, the automatically calculated position is used. The status is set to "enabled" ("1") if not set explicitly.

If one or more relations should stay untouched, you can explicitly configure the list of product list types that will be inserted, updated or deleted via the [controller/jobs/product/import/csv/processor/supplier/listtypes](../config/controller-jobs/product-import.md#processorsupplierlisttypes) setting.

## Stock

If you want to set or update the stock levels during the product import as well, you can configure the mapping for your CSV file to support these domain item keys:

```php
[
    'stock' => [
        0 => 'stock.stocklevel',
        1 => 'stock.type',
        2 => 'stock.dateback',
    ],
]
```

The stock level is required as the minimum amount of data. If you don't have a CSV field for the type or type ID, the "default" type is assumed. Both, the "stock.stocklevel" and the "stock.dateback" values can be empty. For the stock level this means an unlimited value while for the "dateback" value it's an unknown date.

# Data converters

Not all data in the CSV file is already in the required format. Maybe the text encoding isn't UTF-8, the date is not in ISO format or something similar. In order to convert the data before it's imported, you can specify a list of converter objects that should be applied to the data from the CSV file.

To each field in the CSV file, you can apply one or more converters, e.g. to encode a Latin text to UTF8 for the second CSV field via the [controller/jobs/product/import/csv/converter](../config/controller-jobs/product-import.md#converter) or - specific for the job controller - [controller/jobs/product/import/csv/converter](../config/controller-jobs/product-import.md#converter) settings:

```php
[
    1 => 'Text/LatinUTF8'
]
```

Similarly, you can also apply several converters at once to the same field:

```php
[
    1 => [
        'Text/LatinUTF8',
        'DateTime/EnglishISO'
    ]
]
```

It would convert the data of the second CSV field first to UTF-8 and afterwards try to translate it to an ISO date format.

!!! note
    Keep in mind that the position of the CSV fields start at zero (0). If you only need to convert a few fields, you don't have to configure all fields. Only specify the positions in the array you really need!

The available converter objects are named `Aimeos\MW\Convert\<type>\<conversion>` where <type> is the data type and <conversion> the way of the conversion. In the configuration, the type and conversion must be separated by a slash (`<type>/<conversion>`).

To create your own custom converter, you can use the UTF-8 converter class as skeleton:

```php
namespace Aimeos\MW\Convert\Text;

class LatinUTF8 implements \Aimeos\MW\Convert\Interface
{
    public function translate( $value )
    {
        return utf8_encode( $value );
    }

    public function reverse( $value )
    {
        return utf8_decode( $value );
    }
}
```

The `reverse()` method isn't necessary for the product importer, but the converter classes are used for the search plugins as well which translates data to keep the defined semantics.

# Backups

After a CSV file was imported successfully, you can move it to another location, so it won't be imported again and isn't overwritten by the next file that is stored at the same location in the file system. You should use an absolute path for the [controller/jobs/product/import/csv/backup](../config/controller-jobs/product-import.md#backup) setting to be sure but can be relative path if you absolutely know from where the job will be executed from.

The name of the new backup location can contain placeholders understood by the PHP `date_format()` function to create dynamic paths, e.g. `backup/%Y-%m-%d` which would create "backup/2000-01-01". For more information about the date_format() placeholders, please have a look into the PHP documentation of [date_format() function](https://www.php.net/manual/en/datetime.format.php).

!!! note
    If no backup name is configured, the file or directory won't be moved away. Please make also sure that the parent directory and the new directory are writable so the file or directory could be moved.

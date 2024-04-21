If you already manage your categories in an ERP system you want to bulk import the category tree and related information from that system into your shop and update it regularly. Therefore, you can use the catalog import job controller which processes CSV files and imports/updates the categories accordingly.

!!! note
    The catalog import is triggered via a cronjob/scheduler that executes the "catalog/import/csv" job controller.
    If you are using TYPO3, you have to put all configuration into the TSConfig field of the appropriate scheduler task. For all other frameworks, the settings must be added to the configuration file.

!!! tip
    If something goes wrong or for the progress status when importing big files, messages will be written to the "madmin_log" table in your database. You can see them in the "Log" panel of the administration interface if you have access to.

# File location

When you export your categories from your ERP system, you need to store the files in a location where they are accessible by the importer. The default location where the importer expects them is:

* Laravel: ./storage/import/catalog/<sitecode>/
* TYPO3: /uploads/tx_aimeos/.secure/import/catalog/<sitecode>/

If you only have one site, the site code is "default" after installation. The relative directory inside the "fs-import" file system ("catalog") can be configured by the [controller/jobs/catalog/import/csv/location](../config/controller-jobs/catalog-import.md#location) setting.

# File format

For CSV files, there exists a wide range of possibilities about their format because it's not standardized besides the fact that fields are separated by comma (,) but even that isn't set in stone. As a guideline, you should use the following format, which is able to handle all edge cases and which can be also created by Excel/OpenOffice as well:

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

Your CSV files can **start with a header** describing the columns, so they are more readable by humans. In this case, you need to configure the import to **skip these lines** using the [controller/jobs/catalog/import/csv/skip-lines](../config/controller-jobs/catalog-import.md#skip-lines) configuration.

# Column mapping

You can freely configure how your data is organized in the CSV file but for a quick start, there's a default mapping available that can also be used as example:

```php
[
    'item' => [
        0 => 'catalog.code', // e.g. unique category code
        1 => 'catalog.parent', // Code of parent catalog node
        2 => 'catalog.label', // UTF-8 encoded text, also used as catalog name
        3 => 'catalog.status', // If category should be shown in the frontend
    ],
    'text' => [
        4 => 'text.type', // e.g. "short" for short description
        5 => 'text.content', // UTF-8 encoded text
    ],
    'media' => [
        6 => 'media.url', // relative URL of the catalog image on the server
    ],
]
```

As you can see, the data from the CSV file is mapped according to its field position in the line to the key of a MShop domain item (e.g. "catalog.code"). Additionally, fields that belong together are grouped together. The keys of these groups are the names of the data processors that cares about importing the data.

# Adapt the mapping

In order to change the default mapping, you must use the [controller/jobs/catalog/import/csv/mapping](../config/controller-jobs/catalog-import.md#mapping) setting.

You can freely rearrange the group names and e.g. put "media" before "text". This changes the order at which the data is imported and in this example, first the catalog item, than the text and media data is imported and so on.

Similarly, the mapping inside the groups can be changed to your needs and can be reordered as well. The indexes of the mapping in the groups don't have to be consecutive either, e.g. the "catalog.code" is at index "0", the next field contains some irrelevant data and afterwards the "media.url" is stored at position "2" before the rest of the catalog item data follows at index "3" and above. This would lead to a mapping like this:

```php
[
    'item' => [
        0 => 'catalog.code', // e.g. unique EAN code
        5 => 'catalog.status', // enabled (1) or disabled (0)
        3 => 'catalog.label', // UTF-8 encoded text, also used as category name
        4 => 'catalog.parent', // Code of parent catalog node
    ],
    // ...
    'media' => [
        2 => 'media.url', // relative URL of the catalog image on the server
    ],
    // ...
]
```

In fact, you can leave out indexes that shouldn't be imported and use an arbitrary index order. For the reason to understand the mapping immediately, you should at least use a more or less consecutive indexing within the processor group.

# Processor groups

Each group in the mapping (e.g. "item", "text" or "media") defines the CSV fields that will be evaluated by the corresponding processor implementation. A processor is a class that cares about importing "its" data for the category, e.g. the "text" processor imports the data that will be stored in the *mshop_text* table and to associate this data via the *mshop_catalog_list* table to the corresponding catalog.

To speed up importing the data, all existing catalog related data is fetched at once for each catalog item. You can change the retrieved relations via the [controller/jobs/catalog/import/csv/domains](../config/controller-jobs/catalog-import.md#domains) setting. This is especially useful if you don't want to import certain relations like associated media as it reduces the amount of data retrieved from the storage and speeds up the import.

!!! warning
    If you remove a name from the "domains" configuration but still have a mapping defined and your CSV file contains data for this domain, the import is likely to fail because the importer than tries to import duplicate entries. On the other hand, retrieving more domain items than necessary only slows down the importer.

All processors besides the "item" processor are able to import multiple sets at once, e.g. the "text" processor can store several texts available in the CSV line for one category. This means that you can configure the mapping to reference an arbitrary number of text, media, etc. data in one processor group:

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

The "item" group is the most important data group because it contains the mapping for the catalog item that must be stored in the database before the rest of the processors can start to insert or update the data they are managing. It accepts data for these domain item keys:

```php
[
    'item' => [
        0 => 'catalog.code',
        1 => 'catalog.parent',
        2 => 'catalog.label',
        3 => 'catalog.status',
    ],
]
```

Values for "catalog.code" and "catalog.parent" are the absolute minimum that is required to create or update a catalog item. If no status value is available, the value for "enabled" ("1") will be automatically added. The catalog label is also used for the category name if no text of type "name" is imported.

!!! warning
    The order of the categories in your CSV file must be "in-order" which means that the category used in "catalog.parent" must be previously listed in the CSV file. Furthermore, the order of the lines in the CSV files defines the order of the categories within the parent category.

## Text

Several catalog related texts can be part of each CSV line. Supported domain item keys are:

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

The content and the type is required as the minimum amount of data. If you don't have a CSV field for the language ID, the text is imported with the language of the first locale item of the site the importer is running for. Similarly, the label will be the content shorten to max. 255 bytes and the status is set to enabled ("1") if not available.

Additionally, you can import values for the catalog list relation as well:

```php
[
    'text' => [
        // ...
        7 => 'catalog.lists.type',
        8 => 'catalog.lists.datestart',
        9 => 'catalog.lists.dateend',
        10 => 'catalog.lists.config',
        11 => 'catalog.lists.position',
        12 => 'catalog.lists.status',
    ],
]
```

Here, the type is absolutely necessary. If no value for the position is available, the automatically calculated position is used. The status is set to "enabled" ("1") if not set explicitly.

If one or more relations should stay untouched, you can explicitly configure the list of catalog list types that will be inserted, updated or deleted via the [controller/jobs/catalog/import/csv/processor/text/listtypes](../config/controller-jobs/catalog-import.md#listtypes) setting.

## Media

Several catalog related images and other media types can be part of each CSV line. Supported domain item keys are:

```php
[
    'media' => [
        0 => 'media.languageid',
        1 => 'media.type',
        2 => 'media.label',
        3 => 'media.mimetype',
        4 => 'media.preview',
        5 => 'media.url',
        6 => 'media.status',
    ],
]
```

The URL and the type is required as the minimum amount of data. If you don't have a CSV field for the language ID, the media item is imported with no language and is then considered language independent. The label and preview fields will be filled with the URL and the status is set to enabled ("1") if not available.

Additionally, you can import values for the catalog list relation as well:

```php
[
     'media' => [
        // ...
        9 => 'catalog.lists.type',
        10 => 'catalog.lists.datestart',
        11 => 'catalog.lists.dateend',
        12 => 'catalog.lists.config',
        13 => 'catalog.lists.position',
        14 => 'catalog.lists.status',
    ],
]
```

Here, the type is absolutely necessary. If no value for the position is available, the automatically calculated position is used. The status is set to "enabled" ("1") if not set explicitly.

If one or more relations should stay untouched, you can explicitly configure the list of catalog list types that will be inserted, updated or deleted via the [controller/jobs/catalog/import/csv/processor/media/listtypes](../config/controller-jobs/catalog-import.md#listtypes) setting.

# Backups

After a CSV file was imported successfully, you can move it to another location, so it won't be imported again and isn't overwritten by the next file that is stored at the same location in the file system. You must use a path for the [controller/jobs/catalog/import/csv/backup](../config/controller-jobs/catalog-import.md#backup) setting relative to the `fs-import` virtual file system.

The name of the new backup location can contain placeholders understood by the PHP `date_format()` function to create dynamic paths, e.g. "backup/%Y-%m-%d" which would create "backup/2000-01-01". For more information about the date_format() placeholders, please have a look into the PHP documentation of [date_format() function](https://www.php.net/manual/en/datetime.format.php).

!!! warning
    If no backup name is configured, the file will be deleted.

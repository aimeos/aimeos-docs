If you already manage your products in an ERP system you want to update their prices in the shop regularly. Therefore, you can use the stock import job controller which processes CSV files and imports/updates the stock levels of products accordingly.

!!! note
    The stock import is triggered via a cronjob/scheduler that executes the "stock/import/csv" job controller.
    If you are using TYPO3, you have to put all configuration into the TSConfig field of the appropriate scheduler task. For all other frameworks, the settings must be added to the configuration file.

!!! tip
    If something goes wrong or for the progress status when importing big files, messages will be written to the "madmin_log" table in your database. You can see them in the "Log" panel of the administration interface if you have access to.

# File location

When you export your stock levels from your ERP system, you need to store the files in a location where they are accessible by the importer. The default location where the importer expects them is:

* Laravel: ./storage/import/stock/<sitecode>/
* TYPO3: /uploads/tx_aimeos/.secure/import/stock/<sitecode>/

If you only have one site, the site code is "default" after installation. The relative directory inside the "fs-import" file system ("stock") can be configured by the [controller/jobs/stock/import/csv/location](../config/controller-jobs/stock-import.md#location) setting.

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

Your CSV files can **start with a header** describing the columns, so they are more readable by humans. In this case, you need to configure the import to **skip these lines** using the [controller/jobs/stock/import/csv/skip-lines](../config/controller-jobs/stock-import.md#skip-lines) configuration.

# Column mapping

The columns in the CSV file are mapped to these stock item properties:

1. Product code
2. Stock level
3. Stock type (warehouse, optional)
4. Back in stock date (ISO format, optional)
5. Delivery timeframe (string, optional)

An example file (name is arbitrary) stored in the ./stock/ directory of the `fs-import` file system may look like:

```
"product code","stocklevel","stock type","back date","delivery timeframe"
"demo-article",100,"","","2-3 days"
"demo-article",0,"berlin","2100-01-01 00:00:00","4-5 days"
```

!!! note
    The stock type "berlin" needs to be created in the Types > Stock panel of the admin backend before importing this example.

# Backups

After a CSV file was imported successfully, you can move it to another location, so it won't be imported again and isn't overwritten by the next file that is stored at the same location in the file system. You must use a path for the [controller/jobs/stock/import/csv/backup](../config/controller-jobs/stock-import.md#backup) setting relative to the `fs-import` virtual file system.

The name of the new backup location can contain placeholders understood by the PHP `date_format()` function to create dynamic paths, e.g. "backup/%Y-%m-%d" which would create "backup/2000-01-01". For more information about the date_format() placeholders, please have a look into the PHP documentation of [date_format() function](https://www.php.net/manual/en/datetime.format.php).

!!! warning
    If no backup name is configured, the file will be deleted.

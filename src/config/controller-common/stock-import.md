
# csv
## max-size

Maximum number of CSV rows to import at once

```
controller/common/stock/import/csv/max-size = 1000
```

* Default: 1000
* Type: integer - Number of rows
* Since: 2019.04

It's more efficient to read and import more than one row at a time
to speed up the import. Usually, the bigger the chunk that is imported
at once, the less time the importer will need. The downside is that
the amount of memory required by the import process will increase as
well. Therefore, it's a trade-off between memory consumption and
import speed.

**Note:** The maximum size is 10000 records

See also:

* controller/jobs/stock/import/csv/backup
* controller/jobs/stock/import/csv/skip-lines
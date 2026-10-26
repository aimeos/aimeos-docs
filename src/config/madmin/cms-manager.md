
# resource

Name of the database connection resource to use

```
madmin/cms/manager/resource = 
```

* Type: string - Database connection name
* Since: 2023.04
* Since: 2023.04

You can configure a different database connection for each data domain
and if no such connection name exists, the "db" connection will be used.
It's also possible to use the same database connection for different
data domains by configuring the same connection name using this setting.

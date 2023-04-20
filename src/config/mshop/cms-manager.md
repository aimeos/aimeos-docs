
# decorators
## excludes

```
mshop/cms/manager/decorators/excludes = Array
(
)
```

* Default: Array
(
)



## global

```
mshop/cms/manager/decorators/global = Array
(
)
```

* Default: Array
(
)



## local

```
mshop/cms/manager/decorators/local = Array
(
)
```

* Default: Array
(
)



# delete
## ansi

```
mshop/cms/manager/delete/ansi = 
 DELETE FROM "mshop_cms"
 WHERE :cond AND siteid LIKE ?
```

* Default: mshop/cms/manager/delete


## mysql

```
mshop/cms/manager/delete/mysql = 
 DELETE FROM "mshop_cms"
 WHERE :cond AND siteid LIKE ?
```

* Default: 
 DELETE FROM "mshop_cms"
 WHERE :cond AND siteid LIKE ?



# lists
## decorators/excludes

```
mshop/cms/manager/lists/decorators/excludes = Array
(
)
```

* Default: Array
(
)



## decorators/global

```
mshop/cms/manager/lists/decorators/global = Array
(
)
```

* Default: Array
(
)



## decorators/local

```
mshop/cms/manager/lists/decorators/local = Array
(
)
```

* Default: Array
(
)



## delete/ansi

```
mshop/cms/manager/lists/delete/ansi = 
 DELETE FROM "mshop_cms_list"
 WHERE :cond AND siteid LIKE ?
```

* Default: mshop/cms/manager/lists/delete


## delete/mysql

```
mshop/cms/manager/lists/delete/mysql = 
 DELETE FROM "mshop_cms_list"
 WHERE :cond AND siteid LIKE ?
```

* Default: 
 DELETE FROM "mshop_cms_list"
 WHERE :cond AND siteid LIKE ?



## name

```
mshop/cms/manager/lists/name = Standard
```

* Default: Standard


## submanagers

```
mshop/cms/manager/lists/submanagers = Array
(
    [0] => type
)
```

* Default: Array
(
    [0] => type
)



## type/decorators/excludes

```
mshop/cms/manager/lists/type/decorators/excludes = Array
(
)
```

* Default: Array
(
)



## type/decorators/global

```
mshop/cms/manager/lists/type/decorators/global = Array
(
)
```

* Default: Array
(
)



## type/decorators/local

```
mshop/cms/manager/lists/type/decorators/local = Array
(
)
```

* Default: Array
(
)



## type/delete/ansi

```
mshop/cms/manager/lists/type/delete/ansi = 
 DELETE FROM "mshop_cms_list_type"
 WHERE :cond AND siteid LIKE ?
```

* Default: mshop/cms/manager/lists/type/delete


## type/delete/mysql

```
mshop/cms/manager/lists/type/delete/mysql = 
 DELETE FROM "mshop_cms_list_type"
 WHERE :cond AND siteid LIKE ?
```

* Default: 
 DELETE FROM "mshop_cms_list_type"
 WHERE :cond AND siteid LIKE ?



## type/name

```
mshop/cms/manager/lists/type/name = Standard
```

* Default: Standard


## type/submanagers

```
mshop/cms/manager/lists/type/submanagers = Array
(
)
```

* Default: Array
(
)



# name

```
mshop/cms/manager/name = Standard
```

* Default: Standard


# resource

```
mshop/cms/manager/resource = db-cms
```

* Default: db-cms


# sitemode

```
mshop/cms/manager/sitemode = 0
```

* Default: 0


# submanagers

```
mshop/cms/manager/submanagers = Array
(
    [0] => lists
)
```

* Default: Array
(
    [0] => lists
)


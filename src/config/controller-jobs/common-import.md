
# xml
## processor/address/name

Name of the address processor implementation

```
controller/jobs/common/import/xml/processor/address/name = Standard
```

* Default: `Standard`
* Type: string - Last part of the processor class name
* Since: 2019.04

Use "Myname" if your class is named "\Aimeos\Controller\Jobs\Common\Import\Xml\Processor\Address\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## processor/group/allowed

List of group codes that are allowed to be assigned to customers by imports

```
controller/jobs/common/import/xml/processor/group/allowed = 
```

* Type: array - List of group codes
* Since: 2025.10

Assigning privileged groups like "admin" or "editor" via imports would allow
escalating privileges. If set, only the listed group codes can be assigned.

See also:

* controller/jobs/common/import/xml/processor/group/denied

## processor/group/denied

List of group codes that must not be assigned to customers by imports

```
controller/jobs/common/import/xml/processor/group/denied = Array
(
    [0] => admin
    [1] => editor
)
```

* Default: 
```
Array
(
    [0] => admin
    [1] => editor
)
```
* Type: array - List of group codes
* Since: 2025.10

Prevents privilege escalation by disallowing privileged groups like "admin"
and "editor" from being assigned to customers through XML imports.

See also:

* controller/jobs/common/import/xml/processor/group/allowed

## processor/group/name

Name of the group processor implementation

```
controller/jobs/common/import/xml/processor/group/name = Standard
```

* Default: `Standard`
* Type: string - Last part of the processor class name
* Since: 2019.04

Use "Myname" if your class is named "\Aimeos\Controller\Jobs\Common\Import\Xml\Processor\Group\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## processor/lists/attribute/name

Name of the lists processor implementation

```
controller/jobs/common/import/xml/processor/lists/attribute/name = Standard
```

* Default: `Standard`
* Type: string - Last part of the processor class name
* Since: 2019.04

Use "Myname" if your class is named "\Aimeos\Controller\Jobs\Common\Import\Xml\Processor\Lists\Attribute\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## processor/lists/catalog/name

Name of the lists processor implementation

```
controller/jobs/common/import/xml/processor/lists/catalog/name = Standard
```

* Default: `Standard`
* Type: string - Last part of the processor class name
* Since: 2019.04

Use "Myname" if your class is named "\Aimeos\Controller\Jobs\Common\Import\Xml\Processor\Lists\Catalog\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## processor/lists/media/name

Name of the lists processor implementation

```
controller/jobs/common/import/xml/processor/lists/media/name = Standard
```

* Default: `Standard`
* Type: string - Last part of the processor class name
* Since: 2019.04

Use "Myname" if your class is named "\Aimeos\Controller\Jobs\Common\Import\Xml\Processor\Lists\Media\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## processor/lists/name

Name of the lists processor implementation

```
controller/jobs/common/import/xml/processor/lists/name = Standard
```

* Default: `Standard`
* Type: string - Last part of the processor class name
* Since: 2019.04

Use "Myname" if your class is named "\Aimeos\Controller\Jobs\Common\Import\Xml\Processor\Lists\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## processor/lists/price/name

Name of the lists processor implementation

```
controller/jobs/common/import/xml/processor/lists/price/name = Standard
```

* Default: `Standard`
* Type: string - Last part of the processor class name
* Since: 2019.04

Use "Myname" if your class is named "\Aimeos\Controller\Jobs\Common\Import\Xml\Processor\Lists\Price\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## processor/lists/product/name

Name of the lists processor implementation

```
controller/jobs/common/import/xml/processor/lists/product/name = Standard
```

* Default: `Standard`
* Type: string - Last part of the processor class name
* Since: 2019.04

Use "Myname" if your class is named "\Aimeos\Controller\Jobs\Common\Import\Xml\Processor\Lists\Product\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## processor/lists/supplier/name

Name of the lists processor implementation

```
controller/jobs/common/import/xml/processor/lists/supplier/name = 
```

* Type: string - Last part of the processor class name
* Since: 2019.04

Use "Myname" if your class is named "\Aimeos\Controller\Jobs\Common\Import\Xml\Processor\Lists\Supplier\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## processor/lists/text/name

Name of the lists processor implementation

```
controller/jobs/common/import/xml/processor/lists/text/name = Standard
```

* Default: `Standard`
* Type: string - Last part of the processor class name
* Since: 2019.04

Use "Myname" if your class is named "\Aimeos\Controller\Jobs\Common\Import\Xml\Processor\Lists\Text\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## processor/property/name

Name of the property processor implementation

```
controller/jobs/common/import/xml/processor/property/name = Standard
```

* Default: `Standard`
* Type: string - Last part of the processor class name
* Since: 2019.04

Use "Myname" if your class is named "\Aimeos\Controller\Jobs\Common\Import\Xml\Processor\Property\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".

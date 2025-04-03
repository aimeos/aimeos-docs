
# delivery
## hidden

List of delivery address input fields that are optional

```
client/html/common/address/delivery/hidden = Array
(
)
```

* Default: 
```
Array
(
)
```
* Type: array - List of field keys
* Since: 2015.02

You can configure the list of delivery address fields that
are hidden when a customer enters his delivery address.
Available field keys are:

* company
* vatid
* salutation
* firstname
* lastname
* address1
* address2
* address3
* postal
* city
* state
* languageid
* countryid
* telephone
* telefax
* email
* website

Caution: Only hide fields that don't require any input

See also:

* client/html/checkout/standard/address/delivery/disable-new
* client/html/common/address/delivery/mandatory
* client/html/common/address/delivery/optional
* client/html/common/address/salutations
* common/countries
* common/states

## mandatory

List of delivery address input fields that are required

```
client/html/common/address/delivery/mandatory = Array
(
    [0] => firstname
    [1] => lastname
    [2] => address1
    [3] => postal
    [4] => city
    [5] => languageid
)
```

* Default: 
```
Array
(
)
```
* Type: array - List of field keys
* Since: 2015.02

You can configure the list of delivery address fields that are
necessary and must be filled by the customer before he can
continue the checkout process. Available field keys are:

* company
* vatid
* salutation
* firstname
* lastname
* address1
* address2
* address3
* postal
* city
* state
* languageid
* countryid
* telephone
* telefax
* email
* website

See also:

* client/html/checkout/standard/address/delivery/disable-new
* client/html/common/address/delivery/optional
* client/html/common/address/delivery/hidden
* client/html/common/address/salutations
* client/html/common/address/validate
* common/countries
* common/states

## optional

List of delivery address input fields that are optional

```
client/html/common/address/delivery/optional = Array
(
    [0] => salutation
    [1] => company
    [2] => vatid
    [3] => address2
    [4] => countryid
    [5] => state
)
```

* Default: 
```
Array
(
)
```
* Type: array - List of field keys
* Since: 2015.02

You can configure the list of delivery address fields that
customers can fill but don't have to before they can
continue the checkout process. Available field keys are:

* company
* vatid
* salutation
* firstname
* lastname
* address1
* address2
* address3
* postal
* city
* state
* languageid
* countryid
* telephone
* telefax
* email
* website
* nostore

Using the "nostore" field displays the option to avoid storing the
delivery address permanently in the customer account.

See also:

* client/html/checkout/standard/address/delivery/disable-new
* client/html/common/address/delivery/mandatory
* client/html/common/address/delivery/hidden
* client/html/common/address/salutations
* client/html/common/address/validate
* common/countries
* common/states

# payment
## hidden

List of payment address input fields that are optional and should be hidden

```
client/html/common/address/payment/hidden = Array
(
)
```

* Default: 
```
Array
(
)
```
* Type: array - List of field keys
* Since: 2015.02

You can configure the list of payment address fields that
are hidden when a customer enters his new payment address.
Available field keys are:

* company
* vatid
* salutation
* firstname
* lastname
* address1
* address2
* address3
* postal
* city
* state
* languageid
* countryid
* telephone
* telefax
* mobile
* email
* website

Caution: Only hide fields that don't require any input

See also:

* client/html/checkout/standard/address/payment/disable-new
* client/html/common/address/payment/mandatory
* client/html/common/address/payment/optional
* client/html/common/address/salutations
* common/countries
* common/states

## mandatory

List of payment address input fields that are required

```
client/html/common/address/payment/mandatory = Array
(
    [0] => firstname
    [1] => lastname
    [2] => address1
    [3] => postal
    [4] => city
    [5] => languageid
    [6] => email
)
```

* Default: 
```
Array
(
)
```
* Type: array - List of field keys
* Since: 2015.02

You can configure the list of payment address fields that are
necessary and must be filled by the customer before he can
continue the checkout process. Available field keys are:

* company
* vatid
* salutation
* firstname
* lastname
* address1
* address2
* address3
* postal
* city
* state
* languageid
* countryid
* telephone
* telefax
* mobile
* email
* website

Until 2015-02, the configuration option was available as
"client/html/common/address/payment/mandatory" starting from 2014-03.

See also:

* client/html/checkout/standard/address/payment/disable-new
* client/html/common/address/validate
* client/html/common/address/payment/optional
* client/html/common/address/payment/hidden
* client/html/common/address/salutations
* common/countries
* common/states

## optional

List of payment address input fields that are optional

```
client/html/common/address/payment/optional = Array
(
    [0] => salutation
    [1] => company
    [2] => vatid
    [3] => address2
    [4] => countryid
    [5] => state
)
```

* Default: 
```
Array
(
)
```
* Type: array - List of field keys
* Since: 2015.02

You can configure the list of payment address fields that
customers can fill but don't have to before they can
continue the checkout process. Available field keys are:

* company
* vatid
* salutation
* firstname
* lastname
* address1
* address2
* address3
* postal
* city
* state
* languageid
* countryid
* telephone
* telefax
* mobile
* email
* website

Until 2015-02, the configuration option was available as
"client/html/common/address/payment/optional" starting from 2014-03.

See also:

* client/html/checkout/standard/address/payment/disable-new
* client/html/common/address/validate
* client/html/common/address/payment/mandatory
* client/html/common/address/payment/hidden
* client/html/common/address/salutations
* common/countries
* common/states

# salutations

List of salutions the customer can select from

```
client/html/common/address/salutations = Array
(
    [0] => 
    [1] => mr
    [2] => ms
)
```

* Default: 
```
Array
(
)
```
* Type: array - List of available salutation codes
* Since: 2021.04
* Since: 2024.04

The following salutations are available:

* empty string for "unknown"
* company
* mr
* ms

You can modify the list of salutation codes and remove the ones
which shouldn't be used or add new ones.

See also:

* client/html/account/profile/address/salutations
* common/countries
* common/states

# validate

List of regular expressions to validate the data of the address fields

```
client/html/common/address/validate = 
```

* Type: array - Associative list of field names and regular expressions
* Since: 2014.09

To validate the address input data of the customer, an individual
[Perl compatible regular expression](http://php.net/manual/en/pcre.pattern.php)
can be applied to each field. Available fields are:

* company
* vatid
* salutation
* firstname
* lastname
* address1
* address2
* address3
* postal
* city
* state
* languageid
* countryid
* telephone
* telefax
* mobile
* email
* website

Some fields are validated automatically because they are not
dependent on a country specific rule. These fields are:

* salutation
* email
* website

To validate e.g the postal/zip code, you can define a regular
expression like this if you want to allow only digits:

```
 client/html/common/address/validate/postal = '^[0-9]+$'
```

Several regular expressions can be defined line this:

```
 client/html/common/address/validate = array(
     'postal' = '^[0-9]+$',
     'vatid' = '^[A-Z]{2}[0-9]{8}$',
 )
```

Don't add any delimiting characters like slashes (/) to the beginning
or the end of the regular expression. They will be added automatically.
Any slashes inside the expression must be escaped by backlashes,
i.e. "/".

Until 2015-02, the configuration option was available as
"client/html/common/address/payment/validate" starting from 2014-09.

See also:

* client/html/common/address/delivery/mandatory
* client/html/common/address/delivery/optional
* client/html/common/address/payment/mandatory
* client/html/common/address/payment/optional

## address1

Regular expression to check the "address1" address value

```
client/html/common/address/validate/address1 = 
```


See also:

* client/html/common/address/validate
* client/html/common/address/validate

## address2

Regular expression to check the "address2" address value

```
client/html/common/address/validate/address2 = 
```


See also:

* client/html/common/address/validate
* client/html/common/address/validate

## address3

Regular expression to check the "address3" address value

```
client/html/common/address/validate/address3 = 
```


See also:

* client/html/common/address/validate
* client/html/common/address/validate

## city

Regular expression to check the "city" address value

```
client/html/common/address/validate/city = 
```


See also:

* client/html/common/address/validate
* client/html/common/address/validate

## company

Regular expression to check the "company" address value

```
client/html/common/address/validate/company = 
```


See also:

* client/html/common/address/validate
* client/html/common/address/validate

## countryid

Regular expression to check the "countryid" address value

```
client/html/common/address/validate/countryid = 
```


See also:

* client/html/common/address/validate
* client/html/common/address/validate

## email

Regular expression to check the "email" address value

```
client/html/common/address/validate/email = ^.+@[a-zA-Z0-9\-]+(\.[a-zA-Z0-9\-]+)*$
```

* Default: `^.+@[a-zA-Z0-9\-]+(\.[a-zA-Z0-9\-]+)*$`

See also:

* client/html/common/address/validate
* client/html/common/address/validate

## firstname

Regular expression to check the "firstname" address value

```
client/html/common/address/validate/firstname = 
```


See also:

* client/html/common/address/validate
* client/html/common/address/validate

## languageid

Regular expression to check the "languageid" address value

```
client/html/common/address/validate/languageid = 
```


See also:

* client/html/common/address/validate
* client/html/common/address/validate

## lastname

Regular expression to check the "lastname" address value

```
client/html/common/address/validate/lastname = 
```


See also:

* client/html/common/address/validate
* client/html/common/address/validate

## mobile

Regular expression to check the "mobile" address value

```
client/html/common/address/validate/mobile = 
```


See also:

* client/html/common/address/validate

## postal

Regular expression to check the "postal" address value

```
client/html/common/address/validate/postal = 
```


See also:

* client/html/common/address/validate
* client/html/common/address/validate

## salutation

Regular expression to check the "salutation" address value

```
client/html/common/address/validate/salutation = 
```


See also:

* client/html/common/address/validate
* client/html/common/address/validate

## state

Regular expression to check the "state" address value

```
client/html/common/address/validate/state = 
```


See also:

* client/html/common/address/validate
* client/html/common/address/validate

## telefax

Regular expression to check the "telefax" address value

```
client/html/common/address/validate/telefax = 
```


See also:

* client/html/common/address/validate
* client/html/common/address/validate

## telephone

Regular expression to check the "telephone" address value

```
client/html/common/address/validate/telephone = 
```


See also:

* client/html/common/address/validate
* client/html/common/address/validate

## title

Regular expression to check the "title" address value

```
client/html/common/address/validate/title = 
```


See also:

* client/html/common/address/validate

## vatid

Regular expression to check the "vatid" address value

```
client/html/common/address/validate/vatid = 
```


See also:

* client/html/common/address/validate
* client/html/common/address/validate

## website

Regular expression to check the "website" address value

```
client/html/common/address/validate/website = ^([a-z]+://)?[a-zA-Z0-9\-]+(\.[a-zA-Z0-9\-]+)+(:[0-9]+)?(/.*)?$
```

* Default: `^([a-z]+://)?[a-zA-Z0-9\-]+(\.[a-zA-Z0-9\-]+)+(:[0-9]+)?(/.*)?$`

See also:

* client/html/common/address/validate
* client/html/common/address/validate
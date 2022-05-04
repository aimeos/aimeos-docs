
# address
## billing/decorators/global

```
client/html/checkout/standard/address/billing/decorators/global = Array
(
)
```

* Default: Array
(
)



## billing/decorators/local

```
client/html/checkout/standard/address/billing/decorators/local = Array
(
)
```

* Default: Array
(
)



## billing/disable-new

Disables the option to enter a new billing address for an order

```
client/html/checkout/standard/address/billing/disable-new = 
```

* Default: 
* Type: boolean - A value of "1" to disable, "0" enables the billing address form
* Since: 2015.02

Besides the main billing address, customers can usually enter a new
billing address as well. To suppress displaying the form fields for
a billing address, you can set this configuration option to "1".

Until 2015-02, the configuration option was available as
"client/html/common/address/billing/disable-new" starting from 2014-03.

See also:

* client/html/checkout/standard/address/billing/salutations
* client/html/checkout/standard/address/billing/mandatory
* client/html/checkout/standard/address/billing/optional
* client/html/checkout/standard/address/billing/hidden

## billing/hidden

List of billing address input fields that are optional and should be hidden

```
client/html/checkout/standard/address/billing/hidden = Array
(
)
```

* Default: Array
(
)

* Type: array - List of field keys
* Since: 2015.02

You can configure the list of billing address fields that
are hidden when a customer enters his new billing address.
Available field keys are:

* order.base.address.company
* order.base.address.vatid
* order.base.address.salutation
* order.base.address.firstname
* order.base.address.lastname
* order.base.address.address1
* order.base.address.address2
* order.base.address.address3
* order.base.address.postal
* order.base.address.city
* order.base.address.state
* order.base.address.languageid
* order.base.address.countryid
* order.base.address.telephone
* order.base.address.telefax
* order.base.address.email
* order.base.address.website

Caution: Only hide fields that don't require any input

Until 2015-02, the configuration option was available as
"client/html/common/address/billing/hidden" starting from 2014-03.

See also:

* client/html/checkout/standard/address/billing/disable-new
* client/html/checkout/standard/address/billing/salutations
* client/html/checkout/standard/address/billing/mandatory
* client/html/checkout/standard/address/billing/optional
* common/countries
* common/states

## billing/mandatory

List of billing address input fields that are required

```
client/html/checkout/standard/address/billing/mandatory = Array
(
    [0] => order.base.address.firstname
    [1] => order.base.address.lastname
    [2] => order.base.address.address1
    [3] => order.base.address.postal
    [4] => order.base.address.city
    [5] => order.base.address.languageid
    [6] => order.base.address.email
)
```

* Default: Array
(
    [0] => order.base.address.firstname
    [1] => order.base.address.lastname
    [2] => order.base.address.address1
    [3] => order.base.address.postal
    [4] => order.base.address.city
    [5] => order.base.address.languageid
    [6] => order.base.address.email
)

* Type: array - List of field keys
* Since: 2015.02

You can configure the list of billing address fields that are
necessary and must be filled by the customer before he can
continue the checkout process. Available field keys are:

* order.base.address.company
* order.base.address.vatid
* order.base.address.salutation
* order.base.address.firstname
* order.base.address.lastname
* order.base.address.address1
* order.base.address.address2
* order.base.address.address3
* order.base.address.postal
* order.base.address.city
* order.base.address.state
* order.base.address.languageid
* order.base.address.countryid
* order.base.address.telephone
* order.base.address.telefax
* order.base.address.email
* order.base.address.website

Until 2015-02, the configuration option was available as
"client/html/common/address/billing/mandatory" starting from 2014-03.

See also:

* client/html/checkout/standard/address/billing/disable-new
* client/html/checkout/standard/address/billing/salutations
* client/html/checkout/standard/address/billing/optional
* client/html/checkout/standard/address/billing/hidden
* client/html/checkout/standard/address/validate
* common/countries
* common/states

## billing/name

Name of the billing part used by the checkout standard address client implementation

```
client/html/checkout/standard/address/billing/name = Standard
```

* Default: Standard
* Type: string - Last part of the client class name
* Since: 2014.03

Use "Myname" if your class is named "\Aimeos\Client\Checkout\Standard\Address\Billing\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## billing/optional

List of billing address input fields that are optional

```
client/html/checkout/standard/address/billing/optional = Array
(
    [0] => order.base.address.salutation
    [1] => order.base.address.company
    [2] => order.base.address.vatid
    [3] => order.base.address.address2
    [4] => order.base.address.countryid
    [5] => order.base.address.state
)
```

* Default: Array
(
    [0] => order.base.address.salutation
    [1] => order.base.address.company
    [2] => order.base.address.vatid
    [3] => order.base.address.address2
    [4] => order.base.address.countryid
    [5] => order.base.address.state
)

* Type: array - List of field keys
* Since: 2015.02

You can configure the list of billing address fields that
customers can fill but don't have to before they can
continue the checkout process. Available field keys are:

* order.base.address.company
* order.base.address.vatid
* order.base.address.salutation
* order.base.address.firstname
* order.base.address.lastname
* order.base.address.address1
* order.base.address.address2
* order.base.address.address3
* order.base.address.postal
* order.base.address.city
* order.base.address.state
* order.base.address.languageid
* order.base.address.countryid
* order.base.address.telephone
* order.base.address.telefax
* order.base.address.email
* order.base.address.website

Until 2015-02, the configuration option was available as
"client/html/common/address/billing/optional" starting from 2014-03.

See also:

* client/html/checkout/standard/address/billing/disable-new
* client/html/checkout/standard/address/billing/salutations
* client/html/checkout/standard/address/billing/mandatory
* client/html/checkout/standard/address/billing/hidden
* client/html/checkout/standard/address/validate
* common/countries
* common/states

## billing/salutations

List of salutions the customer can select from for the billing address

```
client/html/checkout/standard/address/billing/salutations = Array
(
    [0] => 
    [1] => mr
    [2] => ms
)
```

* Default: Array
(
    [0] => 
    [1] => mr
    [2] => ms
)

* Type: array - List of available salutation codes
* Since: 2015.02

The following salutations are available:

* empty string for "unknown"
* company
* mr
* ms

You can modify the list of salutation codes and remove the ones
which shouldn't be used or add new ones.

See also:

* client/html/checkout/standard/address/billing/disable-new
* client/html/checkout/standard/address/billing/mandatory
* client/html/checkout/standard/address/billing/optional
* client/html/checkout/standard/address/billing/hidden
* client/html/common/address/salutations
* common/countries
* common/states

## billing/template-body

Relative path to the HTML body template of the checkout standard address billing client.

```
client/html/checkout/standard/address/billing/template-body = 
```

* Default: 
* Type: string - Relative path to the template creating code for the HTML page body
* Since: 2014.03

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in client/html/templates).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but suffixed by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, it
should be suffixed by the name of the new class.

See also:

* client/html/checkout/standard/address/billing/template-header

## countries

```
client/html/checkout/standard/address/countries = Array
(
    [0] => AD
    [1] => AE
    [2] => AF
    [3] => AG
    [4] => AI
    [5] => AL
    [6] => AM
    [7] => AO
    [8] => AQ
    [9] => AR
    [10] => AS
    [11] => AT
    [12] => AU
    [13] => AW
    [14] => AX
    [15] => AZ
    [16] => BA
    [17] => BB
    [18] => BD
    [19] => BE
    [20] => BF
    [21] => BG
    [22] => BH
    [23] => BI
    [24] => BJ
    [25] => BL
    [26] => BM
    [27] => BN
    [28] => BO
    [29] => BQ
    [30] => BR
    [31] => BS
    [32] => BT
    [33] => BV
    [34] => BW
    [35] => BY
    [36] => BZ
    [37] => CA
    [38] => CC
    [39] => CD
    [40] => CF
    [41] => CG
    [42] => CH
    [43] => CI
    [44] => CK
    [45] => CL
    [46] => CM
    [47] => CN
    [48] => CO
    [49] => CR
    [50] => CU
    [51] => CV
    [52] => CW
    [53] => CX
    [54] => CY
    [55] => CZ
    [56] => DE
    [57] => DJ
    [58] => DK
    [59] => DM
    [60] => DO
    [61] => DZ
    [62] => EC
    [63] => EE
    [64] => EG
    [65] => EH
    [66] => ER
    [67] => ES
    [68] => ET
    [69] => FI
    [70] => FJ
    [71] => FK
    [72] => FM
    [73] => FO
    [74] => FR
    [75] => GA
    [76] => GB
    [77] => GD
    [78] => GE
    [79] => GF
    [80] => GG
    [81] => GH
    [82] => GI
    [83] => GL
    [84] => GM
    [85] => GN
    [86] => GP
    [87] => GQ
    [88] => GR
    [89] => GS
    [90] => GT
    [91] => GU
    [92] => GW
    [93] => GY
    [94] => HK
    [95] => HM
    [96] => HN
    [97] => HR
    [98] => HT
    [99] => HU
    [100] => ID
    [101] => IE
    [102] => IL
    [103] => IM
    [104] => IN
    [105] => IO
    [106] => IQ
    [107] => IR
    [108] => IS
    [109] => IT
    [110] => JE
    [111] => JM
    [112] => JO
    [113] => JP
    [114] => KE
    [115] => KG
    [116] => KH
    [117] => KI
    [118] => KM
    [119] => KN
    [120] => KP
    [121] => KR
    [122] => KW
    [123] => KY
    [124] => KZ
    [125] => LA
    [126] => LB
    [127] => LC
    [128] => LI
    [129] => LK
    [130] => LR
    [131] => LS
    [132] => LT
    [133] => LU
    [134] => LV
    [135] => LY
    [136] => MA
    [137] => MC
    [138] => MD
    [139] => ME
    [140] => MF
    [141] => MG
    [142] => MH
    [143] => MK
    [144] => ML
    [145] => MM
    [146] => MN
    [147] => MO
    [148] => MP
    [149] => MQ
    [150] => MR
    [151] => MS
    [152] => MT
    [153] => MU
    [154] => MV
    [155] => MW
    [156] => MX
    [157] => MY
    [158] => MZ
    [159] => NA
    [160] => NC
    [161] => NE
    [162] => NF
    [163] => NG
    [164] => NI
    [165] => NL
    [166] => NO
    [167] => NP
    [168] => NR
    [169] => NU
    [170] => NZ
    [171] => OM
    [172] => PA
    [173] => PE
    [174] => PF
    [175] => PG
    [176] => PH
    [177] => PK
    [178] => PL
    [179] => PM
    [180] => PN
    [181] => PR
    [182] => PS
    [183] => PT
    [184] => PW
    [185] => PY
    [186] => QA
    [187] => RE
    [188] => RO
    [189] => RS
    [190] => RU
    [191] => RW
    [192] => SA
    [193] => SB
    [194] => SC
    [195] => SD
    [196] => SE
    [197] => SG
    [198] => SH
    [199] => SI
    [200] => SJ
    [201] => SK
    [202] => SL
    [203] => SM
    [204] => SN
    [205] => SO
    [206] => SR
    [207] => SS
    [208] => ST
    [209] => SV
    [210] => SX
    [211] => SY
    [212] => SZ
    [213] => TC
    [214] => TD
    [215] => TF
    [216] => TG
    [217] => TH
    [218] => TJ
    [219] => TK
    [220] => TL
    [221] => TM
    [222] => TN
    [223] => TO
    [224] => TR
    [225] => TT
    [226] => TV
    [227] => TW
    [228] => TZ
    [229] => UA
    [230] => UG
    [231] => UM
    [232] => US
    [233] => UY
    [234] => UZ
    [235] => VA
    [236] => VC
    [237] => VE
    [238] => VG
    [239] => VI
    [240] => VN
    [241] => VU
    [242] => WF
    [243] => WS
    [244] => YE
    [245] => YT
    [246] => ZA
    [247] => ZM
    [248] => ZW
)
```

* Default: Array
(
)



## decorators/excludes

Excludes decorators added by the "common" option from the checkout standard address html client

```
client/html/checkout/standard/address/decorators/excludes = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2015.08

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"client/html/common/decorators/default" before they are wrapped
around the html client.

```
 client/html/checkout/standard/address/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Client\Html\Common\Decorator\*") added via
"client/html/common/decorators/default" to the html client.

See also:

* client/html/common/decorators/default
* client/html/checkout/standard/address/decorators/global
* client/html/checkout/standard/address/decorators/local

## decorators/global

Adds a list of globally available decorators only to the checkout standard address html client

```
client/html/checkout/standard/address/decorators/global = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2015.08

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Client\Html\Common\Decorator\*") around the html client.

```
 client/html/checkout/standard/address/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Client\Html\Common\Decorator\Decorator1" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/checkout/standard/address/decorators/excludes
* client/html/checkout/standard/address/decorators/local

## decorators/local

Adds a list of local decorators only to the checkout standard address html client

```
client/html/checkout/standard/address/decorators/local = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2015.08

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Client\Html\Checkout\Decorator\*") around the html client.

```
 client/html/checkout/standard/address/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Client\Html\Checkout\Decorator\Decorator2" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/checkout/standard/address/decorators/excludes
* client/html/checkout/standard/address/decorators/global

## delivery/decorators/global

```
client/html/checkout/standard/address/delivery/decorators/global = Array
(
)
```

* Default: Array
(
)



## delivery/decorators/local

```
client/html/checkout/standard/address/delivery/decorators/local = Array
(
)
```

* Default: Array
(
)



## delivery/disable-new

Disables the option to enter a different delivery address for an order

```
client/html/checkout/standard/address/delivery/disable-new = 
```

* Default: 
* Type: boolean - A value of "1" to disable, "0" enables the delivery address form
* Since: 2015.02

Besides the billing address, customers can usually enter a different
delivery address as well. To suppress displaying the form fields for
a delivery address, you can set this configuration option to "1".

See also:

* client/html/checkout/standard/address/delivery/salutations
* client/html/checkout/standard/address/delivery/mandatory
* client/html/checkout/standard/address/delivery/optional
* client/html/checkout/standard/address/delivery/hidden

## delivery/hidden

List of delivery address input fields that are optional

```
client/html/checkout/standard/address/delivery/hidden = Array
(
)
```

* Default: Array
(
)

* Type: array - List of field keys
* Since: 2015.02

You can configure the list of delivery address fields that
are hidden when a customer enters his delivery address.
Available field keys are:

* order.base.address.company
* order.base.address.vatid
* order.base.address.salutation
* order.base.address.firstname
* order.base.address.lastname
* order.base.address.address1
* order.base.address.address2
* order.base.address.address3
* order.base.address.postal
* order.base.address.city
* order.base.address.state
* order.base.address.languageid
* order.base.address.countryid
* order.base.address.telephone
* order.base.address.telefax
* order.base.address.email
* order.base.address.website

Caution: Only hide fields that don't require any input

See also:

* client/html/checkout/standard/address/delivery/disable-new
* client/html/checkout/standard/address/delivery/salutations
* client/html/checkout/standard/address/delivery/mandatory
* client/html/checkout/standard/address/delivery/optional
* common/countries
* common/states

## delivery/mandatory

List of delivery address input fields that are required

```
client/html/checkout/standard/address/delivery/mandatory = Array
(
    [0] => order.base.address.firstname
    [1] => order.base.address.lastname
    [2] => order.base.address.address1
    [3] => order.base.address.postal
    [4] => order.base.address.city
    [5] => order.base.address.languageid
)
```

* Default: Array
(
    [0] => order.base.address.firstname
    [1] => order.base.address.lastname
    [2] => order.base.address.address1
    [3] => order.base.address.postal
    [4] => order.base.address.city
    [5] => order.base.address.languageid
)

* Type: array - List of field keys
* Since: 2015.02

You can configure the list of delivery address fields that are
necessary and must be filled by the customer before he can
continue the checkout process. Available field keys are:

* order.base.address.company
* order.base.address.vatid
* order.base.address.salutation
* order.base.address.firstname
* order.base.address.lastname
* order.base.address.address1
* order.base.address.address2
* order.base.address.address3
* order.base.address.postal
* order.base.address.city
* order.base.address.state
* order.base.address.languageid
* order.base.address.countryid
* order.base.address.telephone
* order.base.address.telefax
* order.base.address.email
* order.base.address.website

See also:

* client/html/checkout/standard/address/delivery/disable-new
* client/html/checkout/standard/address/delivery/salutations
* client/html/checkout/standard/address/delivery/optional
* client/html/checkout/standard/address/delivery/hidden
* client/html/checkout/standard/address/validate
* common/countries
* common/states

## delivery/name

Name of the delivery part used by the checkout standard address client implementation

```
client/html/checkout/standard/address/delivery/name = Standard
```

* Default: Standard
* Type: string - Last part of the client class name
* Since: 2014.03

Use "Myname" if your class is named "\Aimeos\Client\Checkout\Standard\Address\Delivery\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## delivery/optional

List of delivery address input fields that are optional

```
client/html/checkout/standard/address/delivery/optional = Array
(
    [0] => order.base.address.salutation
    [1] => order.base.address.company
    [2] => order.base.address.vatid
    [3] => order.base.address.address2
    [4] => order.base.address.countryid
    [5] => order.base.address.state
)
```

* Default: Array
(
    [0] => order.base.address.salutation
    [1] => order.base.address.company
    [2] => order.base.address.vatid
    [3] => order.base.address.address2
    [4] => order.base.address.countryid
    [5] => order.base.address.state
)

* Type: array - List of field keys
* Since: 2015.02

You can configure the list of delivery address fields that
customers can fill but don't have to before they can
continue the checkout process. Available field keys are:

* order.base.address.company
* order.base.address.vatid
* order.base.address.salutation
* order.base.address.firstname
* order.base.address.lastname
* order.base.address.address1
* order.base.address.address2
* order.base.address.address3
* order.base.address.postal
* order.base.address.city
* order.base.address.state
* order.base.address.languageid
* order.base.address.countryid
* order.base.address.telephone
* order.base.address.telefax
* order.base.address.email
* order.base.address.website
* nostore

Using the "nostore" field displays the option to avoid storing the
delivery address permanently in the customer account.

See also:

* client/html/checkout/standard/address/delivery/disable-new
* client/html/checkout/standard/address/delivery/salutations
* client/html/checkout/standard/address/delivery/mandatory
* client/html/checkout/standard/address/delivery/hidden
* client/html/checkout/standard/address/validate
* common/countries
* common/states

## delivery/salutations

List of salutions the customer can select from for the delivery address

```
client/html/checkout/standard/address/delivery/salutations = Array
(
    [0] => 
    [1] => mr
    [2] => ms
)
```

* Default: Array
(
    [0] => 
    [1] => mr
    [2] => ms
)

* Type: array - List of available salutation codes
* Since: 2015.02

The following salutations are available:

* empty string for "unknown"
* company
* mr
* ms

You can modify the list of salutation codes and remove the ones
which shouldn't be used or add new ones.

See also:

* client/html/checkout/standard/address/delivery/disable-new
* client/html/checkout/standard/address/delivery/mandatory
* client/html/checkout/standard/address/delivery/optional
* client/html/checkout/standard/address/delivery/hidden
* client/html/common/address/salutations
* common/countries
* common/states

## delivery/template-body

Relative path to the HTML body template of the checkout standard address delivery client.

```
client/html/checkout/standard/address/delivery/template-body = 
```

* Default: 
* Type: string - Relative path to the template creating code for the HTML page body
* Since: 2014.03

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in client/html/templates).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but suffixed by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, it
should be suffixed by the name of the new class.

See also:

* client/html/checkout/standard/address/delivery/template-header

## name

Name of the address part used by the checkout standard client implementation

```
client/html/checkout/standard/address/name = Standard
```

* Default: Standard
* Type: string - Last part of the client class name
* Since: 2014.03

Use "Myname" if your class is named "\Aimeos\Client\Html\Checkout\Standard\Address\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## states

```
client/html/checkout/standard/address/states = Array
(
)
```

* Default: Array
(
)



## subparts

List of HTML sub-clients rendered within the checkout standard address section

```
client/html/checkout/standard/address/subparts = Array
(
    [0] => billing
    [1] => delivery
)
```

* Default: Array
(
    [0] => billing
    [1] => delivery
)

* Type: array - List of sub-client names
* Since: 2014.03

The output of the frontend is composed of the code generated by the HTML
clients. Each HTML client can consist of serveral (or none) sub-clients
that are responsible for rendering certain sub-parts of the output. The
sub-clients can contain HTML clients themselves and therefore a
hierarchical tree of HTML clients is composed. Each HTML client creates
the output that is placed inside the container of its parent.

At first, always the HTML code generated by the parent is printed, then
the HTML code of its sub-clients. The order of the HTML sub-clients
determines the order of the output of these sub-clients inside the parent
container. If the configured list of clients is

```
 array( "subclient1", "subclient2" )
```

you can easily change the order of the output by reordering the subparts:

```
 client/html/<clients>/subparts = array( "subclient1", "subclient2" )
```

You can also remove one or more parts if they shouldn't be rendered:

```
 client/html/<clients>/subparts = array( "subclient1" )
```

As the clients only generates structural HTML, the layout defined via CSS
should support adding, removing or reordering content by a fluid like
design.


## template-body

Relative path to the HTML body template of the checkout standard address client.

```
client/html/checkout/standard/address/template-body = 
```

* Default: 
* Type: string - Relative path to the template creating code for the HTML page body
* Since: 2014.03

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in client/html/templates).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but suffixed by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, it
should be suffixed by the name of the new class.

See also:

* client/html/checkout/standard/address/template-header

## validate

List of regular expressions to validate the data of the address fields

```
client/html/checkout/standard/address/validate = 
```

* Default: 
* Type: array - Associative list of field names and regular expressions
* Since: 2014.09

To validate the address input data of the customer, an individual
[Perl compatible regular expression](http://php.net/manual/en/pcre.pattern.php)
can be applied to each field. Available fields are:

* order.base.address.company
* order.base.address.vatid
* order.base.address.salutation
* order.base.address.firstname
* order.base.address.lastname
* order.base.address.address1
* order.base.address.address2
* order.base.address.address3
* order.base.address.postal
* order.base.address.city
* order.base.address.state
* order.base.address.languageid
* order.base.address.countryid
* order.base.address.telephone
* order.base.address.telefax
* order.base.address.email
* order.base.address.website

Some fields are validated automatically because they are not
dependent on a country specific rule. These fields are:

* order.base.address.salutation
* order.base.address.email
* order.base.address.website

To validate e.g the postal/zip code, you can define a regular
expression like this if you want to allow only digits:

```
 client/html/checkout/standard/address/validate/order.base.address.postal = '^[0-9]+$'
```

Several regular expressions can be defined line this:

```
 client/html/checkout/standard/address/validate = array(
     'order.base.address.postal' = '^[0-9]+$',
     'order.base.address.vatid' = '^[A-Z]{2}[0-9]{8}$',
 )
```

Don't add any delimiting characters like slashes (/) to the beginning
or the end of the regular expression. They will be added automatically.
Any slashes inside the expression must be escaped by backlashes,
i.e. "/".

Until 2015-02, the configuration option was available as
"client/html/common/address/billing/validate" starting from 2014-09.

See also:

* client/html/checkout/standard/address/billing/mandatory
* client/html/checkout/standard/address/billing/optional
* client/html/checkout/standard/address/delivery/mandatory
* client/html/checkout/standard/address/delivery/optional

## validate/address1

Regular expression to check the "address1" address value

```
client/html/checkout/standard/address/validate/address1 = 
```

* Default: 

See also:

* client/html/checkout/standard/address/validate
* client/html/checkout/standard/address/validate

## validate/address2

Regular expression to check the "address2" address value

```
client/html/checkout/standard/address/validate/address2 = 
```

* Default: 

See also:

* client/html/checkout/standard/address/validate
* client/html/checkout/standard/address/validate

## validate/address3

Regular expression to check the "address3" address value

```
client/html/checkout/standard/address/validate/address3 = 
```

* Default: 

See also:

* client/html/checkout/standard/address/validate
* client/html/checkout/standard/address/validate

## validate/city

Regular expression to check the "city" address value

```
client/html/checkout/standard/address/validate/city = 
```

* Default: 

See also:

* client/html/checkout/standard/address/validate
* client/html/checkout/standard/address/validate

## validate/company

Regular expression to check the "company" address value

```
client/html/checkout/standard/address/validate/company = 
```

* Default: 

See also:

* client/html/checkout/standard/address/validate
* client/html/checkout/standard/address/validate

## validate/countryid

Regular expression to check the "countryid" address value

```
client/html/checkout/standard/address/validate/countryid = 
```

* Default: 

See also:

* client/html/checkout/standard/address/validate
* client/html/checkout/standard/address/validate

## validate/email

Regular expression to check the "email" address value

```
client/html/checkout/standard/address/validate/email = ^.+@[a-zA-Z0-9\-]+(\.[a-zA-Z0-9\-]+)*$
```

* Default: ^.+@[a-zA-Z0-9\-]+(\.[a-zA-Z0-9\-]+)*$

See also:

* client/html/checkout/standard/address/validate
* client/html/checkout/standard/address/validate

## validate/firstname

Regular expression to check the "firstname" address value

```
client/html/checkout/standard/address/validate/firstname = 
```

* Default: 

See also:

* client/html/checkout/standard/address/validate
* client/html/checkout/standard/address/validate

## validate/languageid

Regular expression to check the "languageid" address value

```
client/html/checkout/standard/address/validate/languageid = 
```

* Default: 

See also:

* client/html/checkout/standard/address/validate
* client/html/checkout/standard/address/validate

## validate/lastname

Regular expression to check the "lastname" address value

```
client/html/checkout/standard/address/validate/lastname = 
```

* Default: 

See also:

* client/html/checkout/standard/address/validate
* client/html/checkout/standard/address/validate

## validate/postal

Regular expression to check the "postal" address value

```
client/html/checkout/standard/address/validate/postal = 
```

* Default: 

See also:

* client/html/checkout/standard/address/validate
* client/html/checkout/standard/address/validate

## validate/salutation

Regular expression to check the "salutation" address value

```
client/html/checkout/standard/address/validate/salutation = 
```

* Default: 

See also:

* client/html/checkout/standard/address/validate
* client/html/checkout/standard/address/validate

## validate/state

Regular expression to check the "state" address value

```
client/html/checkout/standard/address/validate/state = 
```

* Default: 

See also:

* client/html/checkout/standard/address/validate
* client/html/checkout/standard/address/validate

## validate/telefax

Regular expression to check the "telefax" address value

```
client/html/checkout/standard/address/validate/telefax = 
```

* Default: 

See also:

* client/html/checkout/standard/address/validate
* client/html/checkout/standard/address/validate

## validate/telephone

Regular expression to check the "telephone" address value

```
client/html/checkout/standard/address/validate/telephone = 
```

* Default: 

See also:

* client/html/checkout/standard/address/validate
* client/html/checkout/standard/address/validate

## validate/vatid

Regular expression to check the "vatid" address value

```
client/html/checkout/standard/address/validate/vatid = 
```

* Default: 

See also:

* client/html/checkout/standard/address/validate
* client/html/checkout/standard/address/validate

## validate/website

Regular expression to check the "website" address value

```
client/html/checkout/standard/address/validate/website = ^([a-z]+://)?[a-zA-Z0-9\-]+(\.[a-zA-Z0-9\-]+)+(:[0-9]+)?(/.*)?$
```

* Default: ^([a-z]+://)?[a-zA-Z0-9\-]+(\.[a-zA-Z0-9\-]+)+(:[0-9]+)?(/.*)?$

See also:

* client/html/checkout/standard/address/validate
* client/html/checkout/standard/address/validate

# decorators
## excludes

Excludes decorators added by the "common" option from the checkout standard html client

```
client/html/checkout/standard/decorators/excludes = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2014.05

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"client/html/common/decorators/default" before they are wrapped
around the html client.

```
 client/html/checkout/standard/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Client\Html\Common\Decorator\*") added via
"client/html/common/decorators/default" to the html client.

See also:

* client/html/common/decorators/default
* client/html/checkout/standard/decorators/global
* client/html/checkout/standard/decorators/local

## global

Adds a list of globally available decorators only to the checkout standard html client

```
client/html/checkout/standard/decorators/global = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2014.05

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Client\Html\Common\Decorator\*") around the html client.

```
 client/html/checkout/standard/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Client\Html\Common\Decorator\Decorator1" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/checkout/standard/decorators/excludes
* client/html/checkout/standard/decorators/local

## local

Adds a list of local decorators only to the checkout standard html client

```
client/html/checkout/standard/decorators/local = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2014.05

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Client\Html\Checkout\Decorator\*") around the html client.

```
 client/html/checkout/standard/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Client\Html\Checkout\Decorator\Decorator2" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/checkout/standard/decorators/excludes
* client/html/checkout/standard/decorators/global

# delivery
## decorators/global

```
client/html/checkout/standard/delivery/decorators/global = Array
(
)
```

* Default: Array
(
)



## decorators/local

```
client/html/checkout/standard/delivery/decorators/local = Array
(
)
```

* Default: Array
(
)



## domains

List of domain names whose items should be available in the checkout payment templates

```
client/html/checkout/standard/delivery/domains = Array
(
    [0] => media
    [1] => price
    [2] => text
)
```

* Default: Array
(
    [0] => media
    [1] => price
    [2] => text
)

* Type: array - List of domain names
* Since: 2019.04

The templates rendering checkout delivery related data usually add the
images, prices and texts associated to each item. If you want to display
additional content like the attributes, you can configure your own list
of domains (attribute, media, price, text, etc. are domains) whose items
are fetched from the storage.

See also:

* client/html/checkout/standard/payment/domains

## name

Name of the delivery part used by the checkout standard client implementation

```
client/html/checkout/standard/delivery/name = Standard
```

* Default: Standard
* Type: string - Last part of the client class name
* Since: 2014.03

Use "Myname" if your class is named "\Aimeos\Client\Html\Checkout\Standard\Delivery\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## template-body

Relative path to the HTML body template of the checkout standard delivery client.

```
client/html/checkout/standard/delivery/template-body = 
```

* Default: 
* Type: string - Relative path to the template creating code for the HTML page body
* Since: 2014.03

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in client/html/templates).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but suffixed by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, it
should be suffixed by the name of the new class.

See also:

* client/html/checkout/standard/delivery/template-header

# name

Class name of the used checkout standard client implementation

```
client/html/checkout/standard/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2014.03

Each default HTML client can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the client factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Client\Html\Checkout\Standard\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Client\Html\Checkout\Standard\Mycheckout
```

then you have to set the this configuration option:

```
 client/html/checkout/standard/name = Mycheckout
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyCheckout"!


# onepage

Shows all named checkout subparts at once for a one page checkout

```
client/html/checkout/standard/onepage = Array
(
)
```

* Default: Array
(
)

* Type: array - List of checkout subparts name
* Since: 2015.05

Normally, the checkout process is divided into several steps for entering
addresses, select delivery and payment options as well as showing the
summary page. This enables dependencies between two steps like showing
delivery options based on the address entered by the customer. Furthermore,
this is good way to limit the amount of information displayed which is
preferred by mobile users.

Contrary to that, a one page checkout displays all information on only
one page and customers get an immediate overview of which information
they have to enter and what options they can select from. This is an
advantage if only a very limited amount of information must be entered
or if there are almost no options to choose from and no dependencies
between exist.

Using this config options, shop developers are able to define which
checkout subparts are combined to a one page view. Simply add the names
of all checkout subparts to the list. Available checkout subparts for
a one page checkout are:

* address
* delivery
* payment
* summary


# partials
## address

Relative path to the address partial template file

```
client/html/checkout/standard/partials/address = checkout/standard/address-partial
```

* Default: checkout/standard/address-partial
* Type: string - Relative path to the template file
* Since: 2017.01

Partials are templates which are reused in other templates and generate
reoccuring blocks filled with data from the assigned values. The address
partial creates an HTML block with input fields for address forms.


## serviceattr

Relative path to the checkout service attribute partial template file

```
client/html/checkout/standard/partials/serviceattr = checkout/standard/serviceattr-partial
```

* Default: checkout/standard/serviceattr-partial
* Type: string - Relative path to the template file
* Since: 2017.07
* Since: 2017.07

Partials are templates which are reused in other templates and generate reoccuring
blocks filled with data from the assigned values. The service attribute partial creates
an HTML block for the checkout delivery/payment option input/select fields.

This is a very generic way to generate the list of service attribute pairs that will be
added as order service attributes in the basket. Depending on the type of the attribute,
it will create an input field, a select box or a list of selectable items. What attributes
are available to the customer depends on the definitions in the service providers and the
decorators wrapped around them.

If you want to adapt the output to your own project and you know you only have a specific
list of attributes, you can create the input and selections in a non-generic, straight
forward way. The $serviceAttributes[$id] array contains an associative list of codes as
keys (e.g. "time.hourminute") and items implementing \Aimeos\Base\Criteria\Attribute\Iface
as values, e.g.
```
  time.hourminute => \Aimeos\Base\Criteria\Attribute\Iface (
   code => 'time.hourminute',
   internalcode => 'hourminute',
   label => 'Delivery time',
   type => 'time',
   internaltype => 'time',
   default => '',
   required => true
  )
```


# payment
## decorators/global

```
client/html/checkout/standard/payment/decorators/global = Array
(
)
```

* Default: Array
(
)



## decorators/local

```
client/html/checkout/standard/payment/decorators/local = Array
(
)
```

* Default: Array
(
)



## domains

List of domain names whose items should be available in the checkout payment templates

```
client/html/checkout/standard/payment/domains = Array
(
    [0] => media
    [1] => price
    [2] => text
)
```

* Default: Array
(
    [0] => media
    [1] => price
    [2] => text
)

* Type: array - List of domain names
* Since: 2019.04

The templates rendering checkout payment related data usually add the
images, prices and texts associated to each item. If you want to display
additional content like the attributes, you can configure your own list
of domains (attribute, media, price, text, etc. are domains) whose items
are fetched from the storage.

See also:

* client/html/checkout/standard/delivery/domains

## name

Name of the payment part used by the checkout standard client implementation

```
client/html/checkout/standard/payment/name = Standard
```

* Default: Standard
* Type: string - Last part of the client class name
* Since: 2014.03

Use "Myname" if your class is named "\Aimeos\Client\Html\Checkout\Standard\Payment\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## template-body

Relative path to the HTML body template of the checkout standard payment client.

```
client/html/checkout/standard/payment/template-body = 
```

* Default: 
* Type: string - Relative path to the template creating code for the HTML page body
* Since: 2014.03

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in client/html/templates).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but suffixed by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, it
should be suffixed by the name of the new class.

See also:

* client/html/checkout/standard/payment/template-header

# process
## account/decorators/global

```
client/html/checkout/standard/process/account/decorators/global = Array
(
)
```

* Default: Array
(
)



## account/decorators/local

```
client/html/checkout/standard/process/account/decorators/local = Array
(
)
```

* Default: Array
(
)



## account/name

Name of the account part used by the checkout standard process client implementation

```
client/html/checkout/standard/process/account/name = Standard
```

* Default: Standard
* Type: string - Last part of the client class name
* Since: 2017.04

Use "Myname" if your class is named "\Aimeos\Client\Html\Checkout\Standard\Process\Account\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## address/decorators/global

```
client/html/checkout/standard/process/address/decorators/global = Array
(
)
```

* Default: Array
(
)



## address/decorators/local

```
client/html/checkout/standard/process/address/decorators/local = Array
(
)
```

* Default: Array
(
)



## address/name

Name of the address part used by the checkout standard process client implementation

```
client/html/checkout/standard/process/address/name = Standard
```

* Default: Standard
* Type: string - Last part of the client class name
* Since: 2017.04

Use "Myname" if your class is named "\Aimeos\Client\Html\Checkout\Standard\Process\Address\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## decorators/excludes

Excludes decorators added by the "common" option from the checkout standard process html client

```
client/html/checkout/standard/process/decorators/excludes = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2015.08

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"client/html/common/decorators/default" before they are wrapped
around the html client.

```
 client/html/checkout/standard/process/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Client\Html\Common\Decorator\*") added via
"client/html/common/decorators/default" to the html client.

See also:

* client/html/common/decorators/default
* client/html/checkout/standard/process/decorators/global
* client/html/checkout/standard/process/decorators/local

## decorators/global

Adds a list of globally available decorators only to the checkout standard process html client

```
client/html/checkout/standard/process/decorators/global = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2015.08

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Client\Html\Common\Decorator\*") around the html client.

```
 client/html/checkout/standard/process/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Client\Html\Common\Decorator\Decorator1" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/checkout/standard/process/decorators/excludes
* client/html/checkout/standard/process/decorators/local

## decorators/local

Adds a list of local decorators only to the checkout standard process html client

```
client/html/checkout/standard/process/decorators/local = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2015.08

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Client\Html\Checkout\Decorator\*") around the html client.

```
 client/html/checkout/standard/process/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Client\Html\Checkout\Decorator\Decorator2" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/checkout/standard/process/decorators/excludes
* client/html/checkout/standard/process/decorators/global

## name

Name of the process part used by the checkout standard client implementation

```
client/html/checkout/standard/process/name = Standard
```

* Default: Standard
* Type: string - Last part of the client class name
* Since: 2015.07

Use "Myname" if your class is named "\Aimeos\Client\Html\Checkout\Standard\Process\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## subparts

List of HTML sub-clients rendered within the checkout standard process section

```
client/html/checkout/standard/process/subparts = Array
(
    [0] => account
    [1] => address
)
```

* Default: Array
(
    [0] => account
    [1] => address
)

* Type: array - List of sub-client names
* Since: 2014.03

The output of the frontend is composed of the code generated by the HTML
clients. Each HTML client can consist of serveral (or none) sub-clients
that are responsible for rendering certain sub-parts of the output. The
sub-clients can contain HTML clients themselves and therefore a
hierarchical tree of HTML clients is composed. Each HTML client creates
the output that is placed inside the container of its parent.

At first, always the HTML code generated by the parent is printed, then
the HTML code of its sub-clients. The order of the HTML sub-clients
determines the order of the output of these sub-clients inside the parent
container. If the configured list of clients is

```
 array( "subclient1", "subclient2" )
```

you can easily change the order of the output by reordering the subparts:

```
 client/html/<clients>/subparts = array( "subclient1", "subclient2" )
```

You can also remove one or more parts if they shouldn't be rendered:

```
 client/html/<clients>/subparts = array( "subclient1" )
```

As the clients only generates structural HTML, the layout defined via CSS
should support adding, removing or reordering content by a fluid like
design.


## template-body

Relative path to the HTML body template of the checkout standard process client.

```
client/html/checkout/standard/process/template-body = 
```

* Default: 
* Type: string - Relative path to the template creating code for the HTML page body
* Since: 2014.03

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in client/html/templates).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but suffixed by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, it
should be suffixed by the name of the new class.

See also:

* client/html/checkout/standard/process/template-header

## validate

List of regular expressions for validating the payment details

```
client/html/checkout/standard/process/validate = Array
(
    [payment.cardno] => ^[0-9]{16,19}$
    [payment.cvv] => ^[0-9]{3}$
)
```

* Default: Array
(
    [payment.cardno] => ^[0-9]{16,19}$
    [payment.cvv] => ^[0-9]{3}$
)

* Type: array - Associative list of field names and regular expressions
* Since: 2015.07

To validate the payment input data of the customer, an individual Perl
compatible regular expression (http://php.net/manual/en/pcre.pattern.php)
can be applied to each field. Available fields are:

* payment.cardno
* payment.cvv
* payment.expirymonthyear

To validate e.g the CVV security code, you can define a regular expression
like this to allow only three digits:

```
 client/html/checkout/standard/process/validate/payment.cvv = '^[0-9]{3}$'
```

Several regular expressions can be defined line this:

```
 client/html/checkout/standard/process/validate = array(
  'payment.cardno' = '^[0-9]{16,19}$',
  'payment.cvv' = '^[0-9]{3}$',
 )
```

Don't add any delimiting characters like slashes (/) to the beginning or the
end of the regular expression. They will be added automatically. Any slashes
inside the expression must be escaped by backlashes, i.e. "/".

See also:

* client/html/checkout/standard/address/validate

# subparts

List of HTML sub-clients rendered within the checkout standard section

```
client/html/checkout/standard/subparts = Array
(
    [0] => address
    [1] => delivery
    [2] => payment
    [3] => summary
    [4] => process
)
```

* Default: Array
(
    [0] => address
    [1] => delivery
    [2] => payment
    [3] => summary
    [4] => process
)

* Type: array - List of sub-client names
* Since: 2014.03

The output of the frontend is composed of the code generated by the HTML
clients. Each HTML client can consist of serveral (or none) sub-clients
that are responsible for rendering certain sub-parts of the output. The
sub-clients can contain HTML clients themselves and therefore a
hierarchical tree of HTML clients is composed. Each HTML client creates
the output that is placed inside the container of its parent.

At first, always the HTML code generated by the parent is printed, then
the HTML code of its sub-clients. The order of the HTML sub-clients
determines the order of the output of these sub-clients inside the parent
container. If the configured list of clients is

```
 array( "subclient1", "subclient2" )
```

you can easily change the order of the output by reordering the subparts:

```
 client/html/<clients>/subparts = array( "subclient1", "subclient2" )
```

You can also remove one or more parts if they shouldn't be rendered:

```
 client/html/<clients>/subparts = array( "subclient1" )
```

As the clients only generates structural HTML, the layout defined via CSS
should support adding, removing or reordering content by a fluid like
design.


# summary
## address

Location of the address partial template for the checkout summary

```
client/html/checkout/standard/summary/address = common/summary/address
```

* Default: common/summary/address
* Type: string - Relative path to the address partial
* Since: 2017.01

To configure an alternative template for the address partial, you
have to configure its path relative to the template directory
(usually client/html/templates/). It's then used to display the
payment or delivery address block on the summary page during the
checkout process.

See also:

* client/html/checkout/standard/summary/detail
* client/html/checkout/standard/summary/options
* client/html/checkout/standard/summary/service

## decorators/global

```
client/html/checkout/standard/summary/decorators/global = Array
(
)
```

* Default: Array
(
)



## decorators/local

```
client/html/checkout/standard/summary/decorators/local = Array
(
)
```

* Default: Array
(
)



## detail

Location of the detail partial template for the checkout summary

```
client/html/checkout/standard/summary/detail = common/summary/detail
```

* Default: common/summary/detail
* Type: string - Relative path to the detail partial
* Since: 2017.01

To configure an alternative template for the detail partial, you
have to configure its path relative to the template directory
(usually client/html/templates/). It's then used to display the
product detail block on the summary page during the checkout process.

See also:

* client/html/checkout/standard/summary/address
* client/html/checkout/standard/summary/options
* client/html/checkout/standard/summary/service

## name

Name of the summary part used by the checkout standard client implementation

```
client/html/checkout/standard/summary/name = Standard
```

* Default: Standard
* Type: string - Last part of the client class name
* Since: 2014.03

Use "Myname" if your class is named "\Aimeos\Client\Html\Checkout\Standard\Summary\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## option/terms/cancel/url/action

Name of the action that should create the output

```
client/html/checkout/standard/summary/option/terms/cancel/url/action = standard
```

* Default: standard
* Type: string - Name of the action
* Since: 2014.03

In Model-View-Controller (MVC) applications, actions are the methods of a
controller that create parts of the output displayed in the generated HTML page.
Action names are usually alpha-numeric.

See also:

* client/html/checkout/standard/summary/option/terms/cancel/url/target
* client/html/checkout/standard/summary/option/terms/cancel/url/controller
* client/html/checkout/standard/summary/option/terms/cancel/url/config

## option/terms/cancel/url/config

Associative list of configuration options used for generating the URL

```
client/html/checkout/standard/summary/option/terms/cancel/url/config = Array
(
)
```

* Default: Array
(
)

* Type: string - Associative list of configuration options
* Since: 2014.03

You can specify additional options as key/value pairs used when generating
the URLs, like

```
 client/html/<clientname>/url/config = array( 'absoluteUri' => true )
```

The available key/value pairs depend on the application that embeds the e-commerce
framework. This is because the infrastructure of the application is used for
generating the URLs. The full list of available config options is referenced
in the "see also" section of this page.

See also:

* client/html/checkout/standard/summary/option/terms/cancel/url/target
* client/html/checkout/standard/summary/option/terms/cancel/url/controller
* client/html/checkout/standard/summary/option/terms/cancel/url/action
* client/html/url/config

## option/terms/cancel/url/controller

Name of the controller whose action should be called

```
client/html/checkout/standard/summary/option/terms/cancel/url/controller = Checkout
```

* Default: Checkout
* Type: string - Name of the controller
* Since: 2014.03

In Model-View-Controller (MVC) applications, the controller contains the methods
that create parts of the output displayed in the generated HTML page. Controller
names are usually alpha-numeric.

See also:

* client/html/checkout/standard/summary/option/terms/cancel/url/target
* client/html/checkout/standard/summary/option/terms/cancel/url/action
* client/html/checkout/standard/summary/option/terms/cancel/url/config

## option/terms/cancel/url/filter

```
client/html/checkout/standard/summary/option/terms/cancel/url/filter = Array
(
)
```

* Default: Array
(
)



## option/terms/cancel/url/target

Destination of the URL where the controller specified in the URL is known

```
client/html/checkout/standard/summary/option/terms/cancel/url/target = 
```

* Default: 
* Type: string - Destination of the URL
* Since: 2014.03

The destination can be a page ID like in a content management system or the
module of a software development framework. This "target" must contain or know
the controller that should be called by the generated URL.

See also:

* client/html/checkout/standard/summary/option/terms/cancel/url/controller
* client/html/checkout/standard/summary/option/terms/cancel/url/action
* client/html/checkout/standard/summary/option/terms/cancel/url/config

## option/terms/privacy/url/action

Name of the action that should create the output

```
client/html/checkout/standard/summary/option/terms/privacy/url/action = standard
```

* Default: standard
* Type: string - Name of the action
* Since: 2014.03

In Model-View-Controller (MVC) applications, actions are the methods of a
controller that create parts of the output displayed in the generated HTML page.
Action names are usually alpha-numeric.

See also:

* client/html/checkout/standard/summary/option/terms/privacy/url/target
* client/html/checkout/standard/summary/option/terms/privacy/url/controller
* client/html/checkout/standard/summary/option/terms/privacy/url/config

## option/terms/privacy/url/config

Associative list of configuration options used for generating the URL

```
client/html/checkout/standard/summary/option/terms/privacy/url/config = Array
(
)
```

* Default: Array
(
)

* Type: string - Associative list of configuration options
* Since: 2014.03

You can specify additional options as key/value pairs used when generating
the URLs, like

```
 client/html/<clientname>/url/config = array( 'absoluteUri' => true )
```

The available key/value pairs depend on the application that embeds the e-commerce
framework. This is because the infrastructure of the application is used for
generating the URLs. The full list of available config options is referenced
in the "see also" section of this page.

See also:

* client/html/checkout/standard/summary/option/terms/privacy/url/target
* client/html/checkout/standard/summary/option/terms/privacy/url/controller
* client/html/checkout/standard/summary/option/terms/privacy/url/action
* client/html/url/config

## option/terms/privacy/url/controller

Name of the controller whose action should be called

```
client/html/checkout/standard/summary/option/terms/privacy/url/controller = Checkout
```

* Default: Checkout
* Type: string - Name of the controller
* Since: 2014.03

In Model-View-Controller (MVC) applications, the controller contains the methods
that create parts of the output displayed in the generated HTML page. Controller
names are usually alpha-numeric.

See also:

* client/html/checkout/standard/summary/option/terms/privacy/url/target
* client/html/checkout/standard/summary/option/terms/privacy/url/action
* client/html/checkout/standard/summary/option/terms/privacy/url/config

## option/terms/privacy/url/filter

```
client/html/checkout/standard/summary/option/terms/privacy/url/filter = Array
(
)
```

* Default: Array
(
)



## option/terms/privacy/url/target

Destination of the URL where the controller specified in the URL is known

```
client/html/checkout/standard/summary/option/terms/privacy/url/target = 
```

* Default: 
* Type: string - Destination of the URL
* Since: 2014.03

The destination can be a page ID like in a content management system or the
module of a software development framework. This "target" must contain or know
the controller that should be called by the generated URL.

See also:

* client/html/checkout/standard/summary/option/terms/privacy/url/controller
* client/html/checkout/standard/summary/option/terms/privacy/url/action
* client/html/checkout/standard/summary/option/terms/privacy/url/config

## option/terms/url/action

Name of the action that should create the output

```
client/html/checkout/standard/summary/option/terms/url/action = standard
```

* Default: standard
* Type: string - Name of the action
* Since: 2014.03

In Model-View-Controller (MVC) applications, actions are the methods of a
controller that create parts of the output displayed in the generated HTML page.
Action names are usually alpha-numeric.

See also:

* client/html/checkout/standard/summary/option/terms/url/target
* client/html/checkout/standard/summary/option/terms/url/controller
* client/html/checkout/standard/summary/option/terms/url/config

## option/terms/url/config

Associative list of configuration options used for generating the URL

```
client/html/checkout/standard/summary/option/terms/url/config = Array
(
)
```

* Default: Array
(
)

* Type: string - Associative list of configuration options
* Since: 2014.03

You can specify additional options as key/value pairs used when generating
the URLs, like

```
 client/html/<clientname>/url/config = array( 'absoluteUri' => true )
```

The available key/value pairs depend on the application that embeds the e-commerce
framework. This is because the infrastructure of the application is used for
generating the URLs. The full list of available config options is referenced
in the "see also" section of this page.

See also:

* client/html/checkout/standard/summary/option/terms/url/target
* client/html/checkout/standard/summary/option/terms/url/controller
* client/html/checkout/standard/summary/option/terms/url/action
* client/html/url/config

## option/terms/url/controller

Name of the controller whose action should be called

```
client/html/checkout/standard/summary/option/terms/url/controller = Checkout
```

* Default: Checkout
* Type: string - Name of the controller
* Since: 2014.03

In Model-View-Controller (MVC) applications, the controller contains the methods
that create parts of the output displayed in the generated HTML page. Controller
names are usually alpha-numeric.

See also:

* client/html/checkout/standard/summary/option/terms/url/target
* client/html/checkout/standard/summary/option/terms/url/action
* client/html/checkout/standard/summary/option/terms/url/config

## option/terms/url/filter

```
client/html/checkout/standard/summary/option/terms/url/filter = Array
(
)
```

* Default: Array
(
)



## option/terms/url/target

Destination of the URL where the controller specified in the URL is known

```
client/html/checkout/standard/summary/option/terms/url/target = 
```

* Default: 
* Type: string - Destination of the URL
* Since: 2014.03

The destination can be a page ID like in a content management system or the
module of a software development framework. This "target" must contain or know
the controller that should be called by the generated URL.

See also:

* client/html/checkout/standard/summary/option/terms/url/controller
* client/html/checkout/standard/summary/option/terms/url/action
* client/html/checkout/standard/summary/option/terms/url/config

## options

Location of the options partial template for the checkout summary

```
client/html/checkout/standard/summary/options = checkout/standard/option-partial
```

* Default: checkout/standard/option-partial
* Type: string - Relative path to the options partial
* Since: 2017.01

To configure an alternative template for the options partial, you
have to configure its path relative to the template directory
(usually client/html/templates/). It's then used to display the
options block on the summary page during the checkout process.

See also:

* client/html/checkout/standard/summary/address
* client/html/checkout/standard/summary/detail
* client/html/checkout/standard/summary/service

## service

Location of the service partial template for the checkout summary

```
client/html/checkout/standard/summary/service = common/summary/service
```

* Default: common/summary/service
* Type: string - Relative path to the service partial
* Since: 2017.01

To configure an alternative template for the service partial, you
have to configure its path relative to the template directory
(usually client/html/templates/). It's then used to display the
payment or delivery service block on the summary page during the
checkout process.

See also:

* client/html/checkout/standard/summary/address
* client/html/checkout/standard/summary/detail
* client/html/checkout/standard/summary/options

## template-body

Relative path to the HTML body template of the checkout standard summary client.

```
client/html/checkout/standard/summary/template-body = 
```

* Default: 
* Type: string - Relative path to the template creating code for the HTML page body
* Since: 2014.03

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in client/html/templates).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but suffixed by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, it
should be suffixed by the name of the new class.

See also:

* client/html/checkout/standard/summary/template-header

# template-body

Relative path to the HTML body template of the checkout standard client.

```
client/html/checkout/standard/template-body = 
```

* Default: 
* Type: string - Relative path to the template creating code for the HTML page body
* Since: 2014.03

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in client/html/templates).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but suffixed by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, it
should be suffixed by the name of the new class.

See also:

* client/html/checkout/template-header

# template-header

Relative path to the HTML header template of the checkout standard client.

```
client/html/checkout/standard/template-header = 
```

* Default: 
* Type: string - Relative path to the template creating code for the HTML page head
* Since: 2014.03

The template file contains the HTML code and processing instructions
to generate the HTML code that is inserted into the HTML page header
of the rendered page in the frontend. The configuration string is the
path to the template file relative to the templates directory (usually
in client/html/templates).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but suffixed by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, it
should be suffixed by the name of the new class.

See also:

* client/html/checkout/template-body

# url
## action

Name of the action that should create the output

```
client/html/checkout/standard/url/action = standard
```

* Default: standard
* Type: string - Name of the action
* Since: 2014.03
* Since: 2014.03

In Model-View-Controller (MVC) applications, actions are the methods of a
controller that create parts of the output displayed in the generated HTML page.
Action names are usually alpha-numeric.

See also:

* client/html/checkout/standard/url/target
* client/html/checkout/standard/url/controller
* client/html/checkout/standard/url/config
* client/html/checkout/standard/url/target
* client/html/checkout/standard/url/controller
* client/html/checkout/standard/url/config

## config

Associative list of configuration options used for generating the URL

```
client/html/checkout/standard/url/config = Array
(
)
```

* Default: Array
(
)

* Type: string - Associative list of configuration options
* Since: 2014.03
* Since: 2014.03

You can specify additional options as key/value pairs used when generating
the URLs, like

```
 client/html/<clientname>/url/config = array( 'absoluteUri' => true )
```

The available key/value pairs depend on the application that embeds the e-commerce
framework. This is because the infrastructure of the application is used for
generating the URLs. The full list of available config options is referenced
in the "see also" section of this page.

See also:

* client/html/checkout/standard/url/target
* client/html/checkout/standard/url/controller
* client/html/checkout/standard/url/action
* client/html/url/config
* client/html/checkout/standard/url/target
* client/html/checkout/standard/url/controller
* client/html/checkout/standard/url/action
* client/html/url/config

## controller

Name of the controller whose action should be called

```
client/html/checkout/standard/url/controller = Checkout
```

* Default: Checkout
* Type: string - Name of the controller
* Since: 2014.03
* Since: 2014.03

In Model-View-Controller (MVC) applications, the controller contains the methods
that create parts of the output displayed in the generated HTML page. Controller
names are usually alpha-numeric.

See also:

* client/html/checkout/standard/url/target
* client/html/checkout/standard/url/action
* client/html/checkout/standard/url/config
* client/html/checkout/standard/url/target
* client/html/checkout/standard/url/action
* client/html/checkout/standard/url/config

## filter

```
client/html/checkout/standard/url/filter = Array
(
)
```

* Default: Array
(
)



## step-active

Name of the checkout process step to jump to if no previous step requires attention

```
client/html/checkout/standard/url/step-active = summary
```

* Default: summary
* Type: string - Name of the confirm standard HTML client
* Since: 2014.07

The checkout process consists of several steps which are usually
displayed one by another to the customer. If the data of a step
is already available, then that step is skipped. The active step
is the one that is displayed if all other steps are skipped.

If one of the previous steps misses some data the customer has
to enter, then this step is displayed first. After providing
the missing data, the whole series of steps are tested again
and if no other step requests attention, the configured active
step will be displayed.

The order of the steps is determined by the order of sub-parts
that are configured for the checkout client.

See also:

* client/html/checkout/subparts

## target

Destination of the URL where the controller specified in the URL is known

```
client/html/checkout/standard/url/target = 
```

* Default: 
* Type: string - Destination of the URL
* Since: 2014.03
* Since: 2014.03

The destination can be a page ID like in a content management system or the
module of a software development framework. This "target" must contain or know
the controller that should be called by the generated URL.

See also:

* client/html/checkout/standard/url/controller
* client/html/checkout/standard/url/action
* client/html/checkout/standard/url/config
* client/html/checkout/standard/url/controller
* client/html/checkout/standard/url/action
* client/html/checkout/standard/url/config
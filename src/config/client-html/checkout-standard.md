
# address
## decorators/excludes

Excludes decorators added by the "common" option from the checkout standard address html client

```
client/html/checkout/standard/address/decorators/excludes = 
```

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

* Default: `Array
(
)
`
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

* Default: `Array
(
)
`
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

* Default: `Array
(
)
`


## delivery/decorators/local

```
client/html/checkout/standard/address/delivery/decorators/local = Array
(
)
```

* Default: `Array
(
)
`


## delivery/disable-new

Disables the option to enter a different delivery address for an order

```
client/html/checkout/standard/address/delivery/disable-new = 
```

* Default: ``
* Type: boolean - A value of "1" to disable, "0" enables the delivery address form
* Since: 2015.02

Besides the billing address, customers can usually enter a different
delivery address as well. To suppress displaying the form fields for
a delivery address, you can set this configuration option to "1".

See also:

* client/html/common/address/salutations
* client/html/common/address/delivery/mandatory
* client/html/common/address/delivery/optional
* client/html/common/address/delivery/hidden

## delivery/name

Name of the delivery part used by the checkout standard address client implementation

```
client/html/checkout/standard/address/delivery/name = Standard
```

* Default: `Standard`
* Type: string - Last part of the client class name
* Since: 2014.03

Use "Myname" if your class is named "\Aimeos\Client\Checkout\Standard\Address\Delivery\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## delivery/template-body

Relative path to the HTML body template of the checkout standard address delivery client.

```
client/html/checkout/standard/address/delivery/template-body = checkout/standard/address-delivery-body
```

* Default: `checkout/standard/address-delivery-body`
* Type: string - Relative path to the template creating code for the HTML page body
* Since: 2014.03

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in templates/client/html).

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

* Default: `Standard`
* Type: string - Last part of the client class name

Use "Myname" if your class is named "\Aimeos\Client\Html\Checkout\Standard\Address\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## payment/decorators/global

```
client/html/checkout/standard/address/payment/decorators/global = Array
(
)
```

* Default: `Array
(
)
`


## payment/decorators/local

```
client/html/checkout/standard/address/payment/decorators/local = Array
(
)
```

* Default: `Array
(
)
`


## payment/disable-new

Disables the option to enter a new payment address for an order

```
client/html/checkout/standard/address/payment/disable-new = 
```

* Default: ``
* Type: boolean - A value of "1" to disable, "0" enables the payment address form
* Since: 2015.02

Besides the main payment address, customers can usually enter a new
payment address as well. To suppress displaying the form fields for
a payment address, you can set this configuration option to "1".

Until 2015-02, the configuration option was available as
"client/html/common/address/payment/disable-new" starting from 2014-03.

See also:

* client/html/common/address/payment/mandatory
* client/html/common/address/payment/optional
* client/html/common/address/payment/hidden
* client/html/common/address/salutations

## payment/name

Name of the payment part used by the checkout standard address client implementation

```
client/html/checkout/standard/address/payment/name = Standard
```

* Default: `Standard`
* Type: string - Last part of the client class name
* Since: 2014.03

Use "Myname" if your class is named "\Aimeos\Client\Checkout\Standard\Address\Billing\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## payment/template-body

Relative path to the HTML body template of the checkout standard address payment client.

```
client/html/checkout/standard/address/payment/template-body = checkout/standard/address-payment-body
```

* Default: `checkout/standard/address-payment-body`
* Type: string - Relative path to the template creating code for the HTML page body
* Since: 2014.03

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in templates/client/html).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but suffixed by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, it
should be suffixed by the name of the new class.

See also:

* client/html/checkout/standard/address/payment/template-header

## subparts

List of HTML sub-clients rendered within the checkout standard address section

```
client/html/checkout/standard/address/subparts = Array
(
    [0] => payment
    [1] => delivery
)
```

* Default: `Array
(
    [0] => payment
    [1] => delivery
)
`
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
client/html/checkout/standard/address/template-body = checkout/standard/address-body
```

* Default: `checkout/standard/address-body`
* Type: string - Relative path to the template creating code for the HTML page body
* Since: 2014.03

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in templates/client/html).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but suffixed by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, it
should be suffixed by the name of the new class.

See also:

* client/html/checkout/standard/address/template-header

# decorators
## excludes

Excludes decorators added by the "common" option from the checkout standard html client

```
client/html/checkout/standard/decorators/excludes = 
```

* Type: array - List of decorator names

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
client/html/checkout/standard/decorators/global = 
```

* Type: array - List of decorator names

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
client/html/checkout/standard/decorators/local = 
```

* Type: array - List of decorator names

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

* Default: `Array
(
)
`


## decorators/local

```
client/html/checkout/standard/delivery/decorators/local = Array
(
)
```

* Default: `Array
(
)
`


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

* Default: `Array
(
    [0] => media
    [1] => price
    [2] => text
)
`
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

* Default: `Standard`
* Type: string - Last part of the client class name

Use "Myname" if your class is named "\Aimeos\Client\Html\Checkout\Standard\Delivery\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## template-body

Relative path to the HTML body template of the checkout standard delivery client.

```
client/html/checkout/standard/delivery/template-body = checkout/standard/delivery-body
```

* Default: `checkout/standard/delivery-body`
* Type: string - Relative path to the template creating code for the HTML page body
* Since: 2014.03

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in templates/client/html).

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
client/html/checkout/standard/name = 
```

* Type: string - Last part of the class name

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

* Default: `Array
(
)
`
* Type: array - List of checkout subparts name

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
client/html/checkout/standard/partials/address = common/partials/address
```

* Default: `common/partials/address`
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

* Default: `checkout/standard/serviceattr-partial`
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

* Default: `Array
(
)
`


## decorators/local

```
client/html/checkout/standard/payment/decorators/local = Array
(
)
```

* Default: `Array
(
)
`


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

* Default: `Array
(
    [0] => media
    [1] => price
    [2] => text
)
`
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

* Default: `Standard`
* Type: string - Last part of the client class name

Use "Myname" if your class is named "\Aimeos\Client\Html\Checkout\Standard\Payment\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## template-body

Relative path to the HTML body template of the checkout standard payment client.

```
client/html/checkout/standard/payment/template-body = checkout/standard/payment-body
```

* Default: `checkout/standard/payment-body`
* Type: string - Relative path to the template creating code for the HTML page body
* Since: 2014.03

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in templates/client/html).

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

* Default: `Array
(
)
`


## account/decorators/local

```
client/html/checkout/standard/process/account/decorators/local = Array
(
)
```

* Default: `Array
(
)
`


## account/name

Name of the account part used by the checkout standard process client implementation

```
client/html/checkout/standard/process/account/name = Standard
```

* Default: `Standard`
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

* Default: `Array
(
)
`


## address/decorators/local

```
client/html/checkout/standard/process/address/decorators/local = Array
(
)
```

* Default: `Array
(
)
`


## address/name

Name of the address part used by the checkout standard process client implementation

```
client/html/checkout/standard/process/address/name = Standard
```

* Default: `Standard`
* Type: string - Last part of the client class name
* Since: 2017.04

Use "Myname" if your class is named "\Aimeos\Client\Html\Checkout\Standard\Process\Address\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## decorators/excludes

Excludes decorators added by the "common" option from the checkout standard process html client

```
client/html/checkout/standard/process/decorators/excludes = 
```

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

* Default: `Array
(
)
`
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

* Default: `Array
(
)
`
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

* Default: `Standard`
* Type: string - Last part of the client class name

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

* Default: `Array
(
    [0] => account
    [1] => address
)
`
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
client/html/checkout/standard/process/template-body = checkout/standard/process-body
```

* Default: `checkout/standard/process-body`
* Type: string - Relative path to the template creating code for the HTML page body
* Since: 2014.03

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in templates/client/html).

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

* Default: `Array
(
    [payment.cardno] => ^[0-9]{16,19}$
    [payment.cvv] => ^[0-9]{3}$
)
`
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

* client/html/common/address/validate

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

* Default: `Array
(
    [0] => address
    [1] => delivery
    [2] => payment
    [3] => summary
    [4] => process
)
`
* Type: array - List of sub-client names

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

* Default: `common/summary/address`
* Type: string - Relative path to the address partial
* Since: 2017.01

To configure an alternative template for the address partial, you
have to configure its path relative to the template directory
(usually templates/client/html/). It's then used to display the
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

* Default: `Array
(
)
`


## decorators/local

```
client/html/checkout/standard/summary/decorators/local = Array
(
)
```

* Default: `Array
(
)
`


## detail

Location of the detail partial template for the checkout summary

```
client/html/checkout/standard/summary/detail = common/summary/detail
```

* Default: `common/summary/detail`
* Type: string - Relative path to the detail partial
* Since: 2017.01

To configure an alternative template for the detail partial, you
have to configure its path relative to the template directory
(usually templates/client/html/). It's then used to display the
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

* Default: `Standard`
* Type: string - Last part of the client class name

Use "Myname" if your class is named "\Aimeos\Client\Html\Checkout\Standard\Summary\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## option/terms/cancel/url/action

Name of the action that should create the output

```
client/html/checkout/standard/summary/option/terms/cancel/url/action = standard
```

* Default: `standard`
* Type: string - Name of the action
* Since: 2014.03

In Model-View-Controller (MVC) applications, actions are the methods of a
controller that create parts of the output displayed in the generated HTML page.
Action names are usually alpha-numeric.

See also:

* client/html/checkout/standard/summary/option/terms/cancel/url/target
* client/html/checkout/standard/summary/option/terms/cancel/url/controller
* client/html/checkout/standard/summary/option/terms/cancel/url/config
* client/html/checkout/standard/summary/option/terms/cancel/url/filter

## option/terms/cancel/url/config

Associative list of configuration options used for generating the URL

```
client/html/checkout/standard/summary/option/terms/cancel/url/config = Array
(
)
```

* Default: `Array
(
)
`
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
* client/html/checkout/standard/summary/option/terms/cancel/url/filter

## option/terms/cancel/url/controller

Name of the controller whose action should be called

```
client/html/checkout/standard/summary/option/terms/cancel/url/controller = Checkout
```

* Default: `Checkout`
* Type: string - Name of the controller
* Since: 2014.03

In Model-View-Controller (MVC) applications, the controller contains the methods
that create parts of the output displayed in the generated HTML page. Controller
names are usually alpha-numeric.

See also:

* client/html/checkout/standard/summary/option/terms/cancel/url/target
* client/html/checkout/standard/summary/option/terms/cancel/url/action
* client/html/checkout/standard/summary/option/terms/cancel/url/config
* client/html/checkout/standard/summary/option/terms/cancel/url/filter

## option/terms/cancel/url/filter

Removes parameters for the detail page before generating the URL

```
client/html/checkout/standard/summary/option/terms/cancel/url/filter = Array
(
)
```

* Default: `Array
(
)
`
* Type: array - List of parameter names to remove
* Since: 2022.10

This setting removes the listed parameters from the URLs. Keep care to
remove no required parameters!

See also:

* client/html/checkout/standard/summary/option/terms/cancel/url/target
* client/html/checkout/standard/summary/option/terms/cancel/url/controller
* client/html/checkout/standard/summary/option/terms/cancel/url/action
* client/html/checkout/standard/summary/option/terms/cancel/url/config

## option/terms/cancel/url/target

Destination of the URL where the controller specified in the URL is known

```
client/html/checkout/standard/summary/option/terms/cancel/url/target = 
```

* Type: string - Destination of the URL
* Since: 2014.03

The destination can be a page ID like in a content management system or the
module of a software development framework. This "target" must contain or know
the controller that should be called by the generated URL.

See also:

* client/html/checkout/standard/summary/option/terms/cancel/url/controller
* client/html/checkout/standard/summary/option/terms/cancel/url/action
* client/html/checkout/standard/summary/option/terms/cancel/url/config
* client/html/checkout/standard/summary/option/terms/cancel/url/filter

## option/terms/privacy/url/action

Name of the action that should create the output

```
client/html/checkout/standard/summary/option/terms/privacy/url/action = standard
```

* Default: `standard`
* Type: string - Name of the action
* Since: 2014.03

In Model-View-Controller (MVC) applications, actions are the methods of a
controller that create parts of the output displayed in the generated HTML page.
Action names are usually alpha-numeric.

See also:

* client/html/checkout/standard/summary/option/terms/privacy/url/target
* client/html/checkout/standard/summary/option/terms/privacy/url/controller
* client/html/checkout/standard/summary/option/terms/privacy/url/config
* client/html/checkout/standard/summary/option/terms/privacy/url/filter

## option/terms/privacy/url/config

Associative list of configuration options used for generating the URL

```
client/html/checkout/standard/summary/option/terms/privacy/url/config = Array
(
)
```

* Default: `Array
(
)
`
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
* client/html/checkout/standard/summary/option/terms/privacy/url/filter

## option/terms/privacy/url/controller

Name of the controller whose action should be called

```
client/html/checkout/standard/summary/option/terms/privacy/url/controller = Checkout
```

* Default: `Checkout`
* Type: string - Name of the controller
* Since: 2014.03

In Model-View-Controller (MVC) applications, the controller contains the methods
that create parts of the output displayed in the generated HTML page. Controller
names are usually alpha-numeric.

See also:

* client/html/checkout/standard/summary/option/terms/privacy/url/target
* client/html/checkout/standard/summary/option/terms/privacy/url/action
* client/html/checkout/standard/summary/option/terms/privacy/url/config
* client/html/checkout/standard/summary/option/terms/privacy/url/filter

## option/terms/privacy/url/filter

Removes parameters for the detail page before generating the URL

```
client/html/checkout/standard/summary/option/terms/privacy/url/filter = Array
(
)
```

* Default: `Array
(
)
`
* Type: array - List of parameter names to remove
* Since: 2022.10

This setting removes the listed parameters from the URLs. Keep care to
remove no required parameters!

See also:

* client/html/checkout/standard/summary/option/terms/privacy/url/target
* client/html/checkout/standard/summary/option/terms/privacy/url/controller
* client/html/checkout/standard/summary/option/terms/privacy/url/action
* client/html/checkout/standard/summary/option/terms/privacy/url/config

## option/terms/privacy/url/target

Destination of the URL where the controller specified in the URL is known

```
client/html/checkout/standard/summary/option/terms/privacy/url/target = 
```

* Type: string - Destination of the URL
* Since: 2014.03

The destination can be a page ID like in a content management system or the
module of a software development framework. This "target" must contain or know
the controller that should be called by the generated URL.

See also:

* client/html/checkout/standard/summary/option/terms/privacy/url/controller
* client/html/checkout/standard/summary/option/terms/privacy/url/action
* client/html/checkout/standard/summary/option/terms/privacy/url/config
* client/html/checkout/standard/summary/option/terms/privacy/url/filter

## option/terms/url/action

Name of the action that should create the output

```
client/html/checkout/standard/summary/option/terms/url/action = standard
```

* Default: `standard`
* Type: string - Name of the action
* Since: 2014.03

In Model-View-Controller (MVC) applications, actions are the methods of a
controller that create parts of the output displayed in the generated HTML page.
Action names are usually alpha-numeric.

See also:

* client/html/checkout/standard/summary/option/terms/url/target
* client/html/checkout/standard/summary/option/terms/url/controller
* client/html/checkout/standard/summary/option/terms/url/config
* client/html/checkout/standard/summary/option/terms/url/filter

## option/terms/url/config

Associative list of configuration options used for generating the URL

```
client/html/checkout/standard/summary/option/terms/url/config = Array
(
)
```

* Default: `Array
(
)
`
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
* client/html/checkout/standard/summary/option/terms/url/filter

## option/terms/url/controller

Name of the controller whose action should be called

```
client/html/checkout/standard/summary/option/terms/url/controller = Checkout
```

* Default: `Checkout`
* Type: string - Name of the controller
* Since: 2014.03

In Model-View-Controller (MVC) applications, the controller contains the methods
that create parts of the output displayed in the generated HTML page. Controller
names are usually alpha-numeric.

See also:

* client/html/checkout/standard/summary/option/terms/url/target
* client/html/checkout/standard/summary/option/terms/url/action
* client/html/checkout/standard/summary/option/terms/url/config
* client/html/checkout/standard/summary/option/terms/url/filter

## option/terms/url/filter

Removes parameters for the detail page before generating the URL

```
client/html/checkout/standard/summary/option/terms/url/filter = Array
(
)
```

* Default: `Array
(
)
`
* Type: array - List of parameter names to remove
* Since: 2022.10

This setting removes the listed parameters from the URLs. Keep care to
remove no required parameters!

See also:

* client/html/checkout/standard/summary/option/terms/url/target
* client/html/checkout/standard/summary/option/terms/url/controller
* client/html/checkout/standard/summary/option/terms/url/action
* client/html/checkout/standard/summary/option/terms/url/config

## option/terms/url/target

Destination of the URL where the controller specified in the URL is known

```
client/html/checkout/standard/summary/option/terms/url/target = 
```

* Type: string - Destination of the URL
* Since: 2014.03

The destination can be a page ID like in a content management system or the
module of a software development framework. This "target" must contain or know
the controller that should be called by the generated URL.

See also:

* client/html/checkout/standard/summary/option/terms/url/controller
* client/html/checkout/standard/summary/option/terms/url/action
* client/html/checkout/standard/summary/option/terms/url/config
* client/html/checkout/standard/summary/option/terms/url/filter

## options

Location of the options partial template for the checkout summary

```
client/html/checkout/standard/summary/options = checkout/standard/option-partial
```

* Default: `checkout/standard/option-partial`
* Type: string - Relative path to the options partial
* Since: 2017.01

To configure an alternative template for the options partial, you
have to configure its path relative to the template directory
(usually templates/client/html/). It's then used to display the
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

* Default: `common/summary/service`
* Type: string - Relative path to the service partial
* Since: 2017.01

To configure an alternative template for the service partial, you
have to configure its path relative to the template directory
(usually templates/client/html/). It's then used to display the
payment or delivery service block on the summary page during the
checkout process.

See also:

* client/html/checkout/standard/summary/address
* client/html/checkout/standard/summary/detail
* client/html/checkout/standard/summary/options

## template-body

Relative path to the HTML body template of the checkout standard summary client.

```
client/html/checkout/standard/summary/template-body = checkout/standard/summary-body
```

* Default: `checkout/standard/summary-body`
* Type: string - Relative path to the template creating code for the HTML page body
* Since: 2014.03

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in templates/client/html).

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
client/html/checkout/standard/template-body = checkout/standard/body
```

* Default: `checkout/standard/body`
* Type: string - Relative path to the template creating code for the HTML page body

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in templates/client/html).

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
client/html/checkout/standard/template-header = checkout/standard/header
```

* Default: `checkout/standard/header`
* Type: string - Relative path to the template creating code for the HTML page head

The template file contains the HTML code and processing instructions
to generate the HTML code that is inserted into the HTML page header
of the rendered page in the frontend. The configuration string is the
path to the template file relative to the templates directory (usually
in templates/client/html).

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

* Default: `standard`
* Type: string - Name of the action
* Since: 2014.03

In Model-View-Controller (MVC) applications, actions are the methods of a
controller that create parts of the output displayed in the generated HTML page.
Action names are usually alpha-numeric.

See also:

* client/html/checkout/standard/url/target
* client/html/checkout/standard/url/controller
* client/html/checkout/standard/url/config
* client/html/checkout/standard/url/filter
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

* Default: `Array
(
)
`
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

* client/html/checkout/standard/url/target
* client/html/checkout/standard/url/controller
* client/html/checkout/standard/url/action
* client/html/checkout/standard/url/filter
* client/html/checkout/standard/url/target
* client/html/checkout/standard/url/controller
* client/html/checkout/standard/url/action
* client/html/url/config

## controller

Name of the controller whose action should be called

```
client/html/checkout/standard/url/controller = Checkout
```

* Default: `Checkout`
* Type: string - Name of the controller
* Since: 2014.03

In Model-View-Controller (MVC) applications, the controller contains the methods
that create parts of the output displayed in the generated HTML page. Controller
names are usually alpha-numeric.

See also:

* client/html/checkout/standard/url/target
* client/html/checkout/standard/url/action
* client/html/checkout/standard/url/config
* client/html/checkout/standard/url/filter
* client/html/checkout/standard/url/target
* client/html/checkout/standard/url/action
* client/html/checkout/standard/url/config

## filter

Removes parameters for the detail page before generating the URL

```
client/html/checkout/standard/url/filter = Array
(
)
```

* Default: `Array
(
)
`
* Type: array - List of parameter names to remove
* Since: 2022.10

This setting removes the listed parameters from the URLs. Keep care to
remove no required parameters!

See also:

* client/html/checkout/standard/url/target
* client/html/checkout/standard/url/controller
* client/html/checkout/standard/url/action
* client/html/checkout/standard/url/config

## step-active

Name of the checkout process step to jump to if no previous step requires attention

```
client/html/checkout/standard/url/step-active = summary
```

* Default: `summary`
* Type: string - Name of the confirm standard HTML client

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

* Type: string - Destination of the URL
* Since: 2014.03

The destination can be a page ID like in a content management system or the
module of a software development framework. This "target" must contain or know
the controller that should be called by the generated URL.

See also:

* client/html/checkout/standard/url/controller
* client/html/checkout/standard/url/action
* client/html/checkout/standard/url/config
* client/html/checkout/standard/url/filter
* client/html/checkout/standard/url/controller
* client/html/checkout/standard/url/action
* client/html/checkout/standard/url/config
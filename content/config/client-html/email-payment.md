
# attachments

List of file paths whose content should be attached to all payment e-mails

```
client/html/email/payment/attachments = Array
(
    [0] => invalid
)
```

* Default: Array
* Type: array - List of absolute file paths
* Since: 2016.10

This configuration option allows you to add files to the e-mails that are
sent to the customer when the payment status changes, e.g. for the order
confirmation e-mail. These files can't be customer specific.

See also:

* client/html/email/delivery/attachments

# bcc-email

E-Mail address all payment e-mails should be also sent to

```
client/html/email/payment/bcc-email = 
```

* Default: 
* Type: string|array - E-mail address or list of e-mail addresses
* Since: 2014.03

Using this option you can send a copy of all payment related e-mails
to a second e-mail account. This can be handy for testing and checking
the e-mails sent to customers.

It also allows shop owners with a very small volume of orders to be
notified about payment changes. Be aware that this isn't useful if the
order volumne is high or has peeks!

This configuration option overwrites the e-mail address set via
"client/html/email/bcc-email".

See also:

* client/html/email/bcc-email
* client/html/email/reply-email
* client/html/email/from-email

# decorators
## excludes

Excludes decorators added by the "common" option from the email payment html client

```
client/html/email/payment/decorators/excludes = Array
(
)
```

* Default: Array
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
 client/html/email/payment/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Client\Html\Common\Decorator\*") added via
"client/html/common/decorators/default" to the html client.

See also:

* client/html/common/decorators/default
* client/html/email/payment/decorators/global
* client/html/email/payment/decorators/local

## global

Adds a list of globally available decorators only to the email payment html client

```
client/html/email/payment/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2014.05

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Client\Html\Common\Decorator\*") around the html client.

```
 client/html/email/payment/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Client\Html\Common\Decorator\Decorator1" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/email/payment/decorators/excludes
* client/html/email/payment/decorators/local

## local

Adds a list of local decorators only to the email payment html client

```
client/html/email/payment/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2014.05

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Client\Html\Email\Decorator\*") around the html client.

```
 client/html/email/payment/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Client\Html\Email\Decorator\Decorator2" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/email/payment/decorators/excludes
* client/html/email/payment/decorators/global

# from-email

E-Mail address used when sending payment e-mails

```
client/html/email/payment/from-email = me@localhost
```

* Default: me@localhost
* Type: string - E-mail address
* Since: 2014.03

The e-mail address of the person or account that is used for sending
all shop related payment emails to customers. This configuration option
overwrites the e-mail address set via "client/html/email/from-email".

See also:

* client/html/email/payment/from-name
* client/html/email/from-email
* client/html/email/reply-email
* client/html/email/bcc-email

# from-name

Name used when sending payment e-mails

```
client/html/email/payment/from-name = My company
```

* Default: My company
* Type: string - Name shown in the e-mail
* Since: 2014.03

The name of the person or e-mail account that is used for sending all
shop related payment e-mails to customers. This configuration option
overwrite the name set in "client/html/email/from-name".

See also:

* client/html/email/from-name
* client/html/email/from-email
* client/html/email/reply-email
* client/html/email/bcc-email

# html
## decorators/excludes

Excludes decorators added by the "common" option from the "email payment html" html client

```
client/html/email/payment/html/decorators/excludes = 
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
 client/html/email/payment/html/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Client\Html\Common\Decorator\*") added via
"client/html/common/decorators/default" to the html client.

See also:

* client/html/common/decorators/default
* client/html/email/payment/html/decorators/global
* client/html/email/payment/html/decorators/local

## decorators/global

Adds a list of globally available decorators only to the "email payment html" html client

```
client/html/email/payment/html/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2015.08

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Client\Html\Common\Decorator\*") around the html client.

```
 client/html/email/payment/html/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Client\Html\Common\Decorator\Decorator1" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/email/payment/html/decorators/excludes
* client/html/email/payment/html/decorators/local

## decorators/local

Adds a list of local decorators only to the "email payment html" html client

```
client/html/email/payment/html/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2015.08

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Client\Html\Checkout\Decorator\*") around the html client.

```
 client/html/email/payment/html/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Client\Html\Checkout\Decorator\Decorator2" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/email/payment/html/decorators/excludes
* client/html/email/payment/html/decorators/global

## name

Name of the html part used by the email payment client implementation

```
client/html/email/payment/html/name = Standard
```

* Default: Standard
* Type: string - Last part of the client class name
* Since: 2014.03

Use "Myname" if your class is named "\Aimeos\Client\Html\Email\Payment\Html\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## standard/subparts

List of HTML sub-clients rendered within the email payment html section

```
client/html/email/payment/html/standard/subparts = Array
(
)
```

* Default: Array
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


## standard/template-body

Relative path to the HTML body template of the email payment html client.

```
client/html/email/payment/html/standard/template-body = email/payment/html-body-standard
```

* Default: email/payment/html-body-standard
* Type: string - Relative path to the template creating code for the HTML e-mail body
* Since: 2014.03

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the e-mail. The
configuration string is the path to the template file relative
to the templates directory (usually in client/html/templates).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "standard" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "standard"
should be replaced by the name of the new class.

The email payment html client allows to use a different template for
each payment status value. You can create a template for each payment
status and store it in the "email/payment/<status number>/" directory
below the "templates" directory (usually in client/html/templates). If no
specific layout template is found, the common template in the
"email/payment/" directory is used.

See also:

* client/html/email/payment/html/standard/template-header

# name

Class name of the used email payment client implementation

```
client/html/email/payment/name = Standard
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
 \Aimeos\Client\Html\Email\Payment\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Client\Html\Email\Payment\Mypayment
```

then you have to set the this configuration option:

```
 client/html/email/payment/name = Mypayment
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyPayment"!


# pdf
## decorators/excludes

Excludes decorators added by the "common" option from the "email payment pdf" html client

```
client/html/email/payment/pdf/decorators/excludes = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2020.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"client/html/common/decorators/default" before they are wrapped
around the html client.

```
 client/html/email/payment/pdf/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Client\Html\Common\Decorator\*") added via
"client/html/common/decorators/default" to the html client.

See also:

* client/html/common/decorators/default
* client/html/email/payment/pdf/decorators/global
* client/html/email/payment/pdf/decorators/local

## decorators/global

Adds a list of globally available decorators only to the "email payment html" html client

```
client/html/email/payment/pdf/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2020.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Client\Html\Common\Decorator\*") around the html client.

```
 client/html/email/payment/pdf/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Client\Html\Common\Decorator\Decorator1" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/email/payment/pdf/decorators/excludes
* client/html/email/payment/pdf/decorators/local

## decorators/local

Adds a list of local decorators only to the "email payment html" html client

```
client/html/email/payment/pdf/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2020.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Client\Html\Checkout\Decorator\*") around the html client.

```
 client/html/email/payment/pdf/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Client\Html\Checkout\Decorator\Decorator2" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/email/payment/pdf/decorators/excludes
* client/html/email/payment/pdf/decorators/global

## name

```
client/html/email/payment/pdf/name = Standard
```

* Default: Standard


## standard/subparts

List of HTML sub-clients rendered within the email payment PDF section

```
client/html/email/payment/pdf/standard/subparts = Array
(
)
```

* Default: Array
* Type: array - List of sub-client names
* Since: 2020.07

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


## standard/template-body

Relative path to the HTML body template of the email payment PDF client.

```
client/html/email/payment/pdf/standard/template-body = email/payment/pdf-body-standard
```

* Default: email/payment/pdf-body-standard
* Type: string - Relative path to the template creating code for the HTML e-mail body
* Since: 2020.07

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the e-mail. The
configuration string is the path to the template file relative
to the templates directory (usually in client/html/templates).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "standard" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "standard"
should be replaced by the name of the new class.

The email payment PDF client allows to use a different template for
each payment status value. You can create a template for each payment
status and store it in the "email/payment/<status number>/" directory
below the "templates" directory (usually in client/html/templates). If no
specific layout template is found, the common template in the
"email/payment/" directory is used.

See also:

* client/html/email/payment/pdf/standard/template-header

# reply-email

E-Mail address used by the customer when replying to payment e-mails

```
client/html/email/payment/reply-email = me@localhost
```

* Default: me@localhost
* Type: string - E-mail address
* Since: 2014.03

The e-mail address of the person or e-mail account the customer
should reply to in case of payment related questions or problems.
This configuration option overwrites the e-mail address set via
"client/html/email/reply-email".

See also:

* client/html/email/payment/reply-name
* client/html/email/reply-email
* client/html/email/from-email
* client/html/email/bcc-email

# reply-name

Recipient name displayed when the customer replies to payment e-mails

```
client/html/email/payment/reply-name = My company
```

* Default: My company
* Type: string - Name shown in the e-mail
* Since: 2014.03

The name of the person or e-mail account the customer should
reply to in case of payment related questions or problems. This
configuration option overwrites the name set via
"client/html/email/reply-name".

See also:

* client/html/email/payment/reply-email
* client/html/email/reply-name
* client/html/email/reply-email
* client/html/email/from-email
* client/html/email/bcc-email

# standard
## subparts

List of HTML sub-clients rendered within the email payment section

```
client/html/email/payment/standard/subparts = Array
(
    [0] => text
    [1] => html
    [2] => pdf
)
```

* Default: Array
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

Relative path to the HTML body template of the email payment client.

```
client/html/email/payment/standard/template-body = Array
(
    [0] => email/payment/6/body-standard
    [1] => email/payment/body-standard
)
```

* Default: Array
* Type: string - Relative path to the template creating code for the HTML page body
* Since: 2014.03

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in client/html/templates).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "standard" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "standard"
should be replaced by the name of the new class.

The email payment HTML client allows to use a different template for
each payment status value. You can create a template for each payment
status and store it in the "email/payment/<status number>/" directory
below the "templates" directory (usually in client/html/templates). If no
specific layout template is found, the common template in the
"email/payment/" directory is used.

See also:

* client/html/email/payment/standard/template-header

## template-header

Relative path to the HTML header template of the email payment client.

```
client/html/email/payment/standard/template-header = Array
(
    [0] => email/payment/6/header-standard
    [1] => email/payment/header-standard
)
```

* Default: Array
* Type: string - Relative path to the template creating code for the HTML page head
* Since: 2014.03

The template file contains the HTML code and processing instructions
to generate the HTML code that is inserted into the HTML page header
of the rendered page in the frontend. The configuration string is the
path to the template file relative to the templates directory (usually
in client/html/templates).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "standard" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "standard"
should be replaced by the name of the new class.

The email payment HTML client allows to use a different template for
each payment status value. You can create a template for each payment
status and store it in the "email/payment/<status number>/" directory
below the "templates" directory (usually in client/html/templates). If no
specific layout template is found, the common template in the
"email/payment/" directory is used.

See also:

* client/html/email/payment/standard/template-body

# text
## decorators/excludes

Excludes decorators added by the "common" option from the "email payment text" html client

```
client/html/email/payment/text/decorators/excludes = 
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
 client/html/email/payment/text/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Client\Html\Common\Decorator\*") added via
"client/html/common/decorators/default" to the html client.

See also:

* client/html/common/decorators/default
* client/html/email/payment/text/decorators/global
* client/html/email/payment/text/decorators/local

## decorators/global

Adds a list of globally available decorators only to the "email payment text" html client

```
client/html/email/payment/text/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2015.08

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Client\Html\Common\Decorator\*") around the html client.

```
 client/html/email/payment/text/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Client\Html\Common\Decorator\Decorator1" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/email/payment/text/decorators/excludes
* client/html/email/payment/text/decorators/local

## decorators/local

Adds a list of local decorators only to the "email payment text" html client

```
client/html/email/payment/text/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2015.08

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Client\Html\Checkout\Decorator\*") around the html client.

```
 client/html/email/payment/text/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Client\Html\Checkout\Decorator\Decorator2" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/email/payment/text/decorators/excludes
* client/html/email/payment/text/decorators/global

## name

Name of the text part used by the email payment client implementation

```
client/html/email/payment/text/name = Standard
```

* Default: Standard
* Type: string - Last part of the client class name
* Since: 2014.03

Use "Myname" if your class is named "\Aimeos\Client\Html\Email\Payment\Text\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## standard/subparts

List of HTML sub-clients rendered within the email payment text section

```
client/html/email/payment/text/standard/subparts = Array
(
)
```

* Default: Array
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


## standard/template-body

Relative path to the text body template of the email payment text client.

```
client/html/email/payment/text/standard/template-body = email/payment/text-body-standard
```

* Default: email/payment/text-body-standard
* Type: string - Relative path to the template creating code for the e-mail body
* Since: 2014.03

The template file contains the text and processing instructions
to generate the result shown in the body of the e-mail. The
configuration string is the path to the template file relative
to the templates directory (usually in client/html/templates).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "standard" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "standard"
should be replaced by the name of the new class.

The email payment text client allows to use a different template for
each payment status value. You can create a template for each payment
status and store it in the "email/payment/<status number>/" directory
below the "templates" directory (usually in client/html/templates). If no
specific layout template is found, the common template in the
"email/payment/" directory is used.

See also:

* client/html/email/payment/text/standard/template-header
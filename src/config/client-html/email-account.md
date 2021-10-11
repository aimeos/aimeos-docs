
# bcc-email

E-Mail address all account creation e-mails should be also sent to

```
client/html/email/account/bcc-email = 
```

* Default: 
* Type: string|array - E-mail address or list of e-mail addresses
* Since: 2015.09

Using this option you can send a copy of all account related e-mails
to a second e-mail account. This can be handy for testing and checking
the e-mails sent to customers.

It also allows shop owners with a very small volume of orders to be
notified about account changes. Be aware that this isn't useful if the
order volumne is high or has peeks!

This configuration option overwrites the e-mail address set via
"client/html/email/bcc-email".

See also:

* client/html/email/bcc-email
* client/html/email/reply-email
* client/html/email/from-email

# decorators
## excludes

Excludes decorators added by the "common" option from the email account html client

```
client/html/email/account/decorators/excludes = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2015.09

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"client/html/common/decorators/default" before they are wrapped
around the html client.

```
 client/html/email/account/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Client\Html\Common\Decorator\*") added via
"client/html/common/decorators/default" to the html client.

See also:

* client/html/common/decorators/default
* client/html/email/account/decorators/global
* client/html/email/account/decorators/local

## global

Adds a list of globally available decorators only to the email account html client

```
client/html/email/account/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2015.09

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Client\Html\Common\Decorator\*") around the html client.

```
 client/html/email/account/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Client\Html\Common\Decorator\Decorator1" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/email/account/decorators/excludes
* client/html/email/account/decorators/local

## local

Adds a list of local decorators only to the email account html client

```
client/html/email/account/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2015.09

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Client\Html\Email\Decorator\*") around the html client.

```
 client/html/email/account/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Client\Html\Email\Decorator\Decorator2" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/email/account/decorators/excludes
* client/html/email/account/decorators/global

# from-email

E-Mail address used when sending account creation e-mails

```
client/html/email/account/from-email = me@example.com
```

* Default: me@example.com
* Type: string - E-mail address
* Since: 2015.09

The e-mail address of the person or account that is used for sending
all shop related product notification e-mails to customers. This configuration option
overwrites the e-mail address set via "client/html/email/from-email".

See also:

* client/html/email/account/from-name
* client/html/email/from-email
* client/html/email/reply-email
* client/html/email/bcc-email

# from-name

Name used when sending account creation e-mails

```
client/html/email/account/from-name = My company
```

* Default: My company
* Type: string - Name shown in the e-mail
* Since: 2015.09

The name of the person or e-mail account that is used for sending all
shop related account e-mails to customers. This configuration option
overwrite the name set in "client/html/email/from-name".

See also:

* client/html/email/from-name
* client/html/email/from-email
* client/html/email/reply-email
* client/html/email/bcc-email

# html
## decorators/excludes

Excludes decorators added by the "common" option from the "email account html" html client

```
client/html/email/account/html/decorators/excludes = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2015.09

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"client/html/common/decorators/default" before they are wrapped
around the html client.

```
 client/html/email/account/html/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Client\Html\Common\Decorator\*") added via
"client/html/common/decorators/default" to the html client.

See also:

* client/html/common/decorators/default
* client/html/email/account/html/decorators/global
* client/html/email/account/html/decorators/local

## decorators/global

Adds a list of globally available decorators only to the "email account html" html client

```
client/html/email/account/html/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2015.09

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Client\Html\Common\Decorator\*") around the html client.

```
 client/html/email/account/html/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Client\Html\Common\Decorator\Decorator1" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/email/account/html/decorators/excludes
* client/html/email/account/html/decorators/local

## decorators/local

Adds a list of local decorators only to the "email account html" html client

```
client/html/email/account/html/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2015.09

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Client\Html\Checkout\Decorator\*") around the html client.

```
 client/html/email/account/html/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Client\Html\Checkout\Decorator\Decorator2" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/email/account/html/decorators/excludes
* client/html/email/account/html/decorators/global

## name

Name of the html part used by the account creation e-mail client implementation

```
client/html/email/account/html/name = Standard
```

* Default: Standard
* Type: string - Last part of the client class name
* Since: 2015.09

Use "Myname" if your class is named "\Aimeos\Client\Html\Email\Account\Html\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## subparts

List of HTML sub-clients rendered within the account creation e-mail html section

```
client/html/email/account/html/subparts = Array
(
)
```

* Default: Array
* Type: array - List of sub-client names
* Since: 2015.09

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

Relative path to the HTML body template of the account creation e-mail html client.

```
client/html/email/account/html/template-body = email/account/html-body-standard
```

* Default: email/account/html-body-standard
* Type: string - Relative path to the template creating code for the HTML e-mail body
* Since: 2015.09

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

The account creation e-mail html client allows to use a different template for
each account status value. You can create a template for each account
status and store it in the "email/account/<status number>/" directory
below the "templates" directory (usually in client/html/templates). If no
specific layout template is found, the common template in the
"email/account/" directory is used.

See also:

* client/html/email/account/html/template-header

# name

Class name of the used email account client implementation

```
client/html/email/account/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2015.09

Each default HTML client can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the client factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Client\Html\Email\Account\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Client\Html\Email\Account\Myaccount
```

then you have to set the this configuration option:

```
 client/html/email/account/name = Myaccount
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyAccount"!


# reply-email

E-Mail address used by the customer when replying to account creation e-mails

```
client/html/email/account/reply-email = me@example.com
```

* Default: me@example.com
* Type: string - E-mail address
* Since: 2015.09

The e-mail address of the person or e-mail account the customer
should reply to in case of account related questions or problems.
This configuration option overwrites the e-mail address set via
"client/html/email/reply-email".

See also:

* client/html/email/account/reply-name
* client/html/email/reply-email
* client/html/email/from-email
* client/html/email/bcc-email

# reply-name

Recipient name displayed when the customer replies to account creation e-mails

```
client/html/email/account/reply-name = My company
```

* Default: My company
* Type: string - Name shown in the e-mail
* Since: 2015.09

The name of the person or e-mail account the customer should
reply to in case of account related questions or problems. This
configuration option overwrites the name set via
"client/html/email/reply-name".

See also:

* client/html/email/account/reply-email
* client/html/email/reply-name
* client/html/email/reply-email
* client/html/email/from-email
* client/html/email/bcc-email

# subparts

List of HTML sub-clients rendered within the account creation e-mail

```
client/html/email/account/subparts = Array
(
    [0] => text
    [1] => html
)
```

* Default: Array
* Type: array - List of sub-client names
* Since: 2015.09

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


# template-body

Relative path to the HTML body template of the account creation e-mail client.

```
client/html/email/account/template-body = email/account/body-standard
```

* Default: email/account/body-standard
* Type: string - Relative path to the template creating code for the HTML page body
* Since: 2015.09

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

The product notification e-mail HTML client allows to use a different template for
each account status value. You can create a template for each account
status and store it in the "email/account/<status number>/" directory
below the "templates" directory (usually in client/html/templates). If no
specific layout template is found, the common template in the
"email/account/" directory is used.

See also:

* client/html/email/account/template-header

# template-header

Relative path to the HTML header template of the account creation e-mail client.

```
client/html/email/account/template-header = email/account/header-standard
```

* Default: email/account/header-standard
* Type: string - Relative path to the template creating code for the HTML page head
* Since: 2015.09

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

The product notification e-mail HTML client allows to use a different template for
each account status value. You can create a template for each account
status and store it in the "email/account/<status number>/" directory
below the "templates" directory (usually in client/html/templates). If no
specific layout template is found, the common template in the
"email/account/" directory is used.

See also:

* client/html/email/account/template-body

# text
## decorators/excludes

Excludes decorators added by the "common" option from the "email account text" html client

```
client/html/email/account/text/decorators/excludes = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2015.09

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"client/html/common/decorators/default" before they are wrapped
around the html client.

```
 client/html/email/account/text/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Client\Html\Common\Decorator\*") added via
"client/html/common/decorators/default" to the html client.

See also:

* client/html/common/decorators/default
* client/html/email/account/text/decorators/global
* client/html/email/account/text/decorators/local

## decorators/global

Adds a list of globally available decorators only to the "email account text" html client

```
client/html/email/account/text/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2015.09

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Client\Html\Common\Decorator\*") around the html client.

```
 client/html/email/account/text/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Client\Html\Common\Decorator\Decorator1" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/email/account/text/decorators/excludes
* client/html/email/account/text/decorators/local

## decorators/local

Adds a list of local decorators only to the "email account text" html client

```
client/html/email/account/text/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2015.09

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Client\Html\Checkout\Decorator\*") around the html client.

```
 client/html/email/account/text/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Client\Html\Checkout\Decorator\Decorator2" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/email/account/text/decorators/excludes
* client/html/email/account/text/decorators/global

## name

Name of the text part used by the account creation e-mail client implementation

```
client/html/email/account/text/name = Standard
```

* Default: Standard
* Type: string - Last part of the client class name
* Since: 2015.09

Use "Myname" if your class is named "\Aimeos\Client\Html\Email\Account\Text\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## subparts

List of HTML sub-clients rendered within the text section of a account creation email

```
client/html/email/account/text/subparts = Array
(
)
```

* Default: Array
* Type: array - List of sub-client names
* Since: 2015.09

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

Relative path to the text body template of the account creation email text client.

```
client/html/email/account/text/template-body = email/account/text-body-standard
```

* Default: email/account/text-body-standard
* Type: string - Relative path to the template creating code for the e-mail body
* Since: 2015.09

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

The email account text client allows to use a different template for
each account status value. You can create a template for each account
status and store it in the "email/account/<status number>/" directory
below the "templates" directory (usually in client/html/templates). If no
specific layout template is found, the common template in the
"email/account/" directory is used.

See also:

* client/html/email/account/text/template-header
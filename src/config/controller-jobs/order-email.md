
# delivery
## attachments

List of file paths whose content should be attached to all delivery e-mails

```
controller/jobs/order/email/delivery/attachments = Array
(
)
```

* Default: `Array
(
)
`
* Type: array - List of absolute file paths
* Since: 2016.10

This configuration option allows you to add files to the e-mails that are
sent to the customer when the delivery status changes, e.g. for the order
confirmation e-mail. These files can't be customer specific.

See also:

* controller/jobs/order/email/payment/attachments

## bcc-email

Hidden e-mail address all delivery e-mails should be also sent to

```
controller/jobs/order/email/delivery/bcc-email = Array
(
)
```

* Default: `Array
(
)
`
* Type: string|array - E-mail address or list of e-mail addresses
* Since: 2014.03

Using this option you can send a copy of all delivery related e-mails
to a second e-mail account. This can be handy for testing and checking
the e-mails sent to customers.

It also allows shop owners with a very small volume of orders to be
notified about delivery changes. Be aware that this isn't useful if the
order volumne is high or has peeks!


## cc-email

E-Mail address all delivery e-mails should be also sent to

```
controller/jobs/order/email/delivery/cc-email = 
```

* Type: string - E-mail address or list of e-mail addresses
* Since: 2023.10

Using this option you can send a copy of all delivery related e-mails
to a second e-mail account. This can be handy for testing and checking
the e-mails sent to customers.

It also allows shop owners with a very small volume of orders to be
notified about delivery changes. Be aware that this isn't useful if the
order volumne is high or has peeks!


## decorators/excludes

Excludes decorators added by the "common" option from the order email delivery controllers

```
controller/jobs/order/email/delivery/decorators/excludes = Array
(
)
```

* Default: `Array
(
)
`
* Type: array - List of decorator names
* Since: 2015.09

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"controller/jobs/common/decorators/default" before they are wrapped
around the job controller.

```
 controller/jobs/order/email/delivery/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Controller\Jobs\Common\Decorator\*") added via
"controller/jobs/common/decorators/default" to this job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/order/email/delivery/decorators/global
* controller/jobs/order/email/delivery/decorators/local

## decorators/global

Adds a list of globally available decorators only to the order email delivery controllers

```
controller/jobs/order/email/delivery/decorators/global = Array
(
)
```

* Default: `Array
(
)
`
* Type: array - List of decorator names
* Since: 2015.09

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Controller\Jobs\Common\Decorator\*") around the job controller.

```
 controller/jobs/order/email/delivery/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Controller\Jobs\Common\Decorator\Decorator1" only to this job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/order/email/delivery/decorators/excludes
* controller/jobs/order/email/delivery/decorators/local

## decorators/local

Adds a list of local decorators only to the order email delivery controllers

```
controller/jobs/order/email/delivery/decorators/local = Array
(
)
```

* Default: `Array
(
)
`
* Type: array - List of decorator names
* Since: 2015.09

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Controller\Jobs\Order\Email\Delivery\Decorator\*") around this job controller.

```
 controller/jobs/order/email/delivery/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Controller\Jobs\Order\Email\Delivery\Decorator\Decorator2" only to this job
controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/order/email/delivery/decorators/excludes
* controller/jobs/order/email/delivery/decorators/global

## limit-days

Only send delivery e-mails of orders that were created in the past within the configured number of days

```
controller/jobs/order/email/delivery/limit-days = 90
```

* Default: `90`
* Type: integer - Number of days
* Since: 2014.03

The delivery e-mails are normally send immediately after the delivery
status has changed. This option prevents e-mails for old order from
being send in case anything went wrong or an update failed to avoid
confusion of customers.

See also:

* controller/jobs/order/email/delivery/limit-days
* controller/jobs/service/delivery/process/limit-days

## name

Class name of the used order email delivery scheduler controller implementation

```
controller/jobs/order/email/delivery/name = Standard
```

* Default: `Standard`
* Type: string - Last part of the class name
* Since: 2014.03

Each default job controller can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the controller factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Controller\Jobs\Order\Email\Delivery\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Controller\Jobs\Order\Email\Delivery\Mydelivery
```

then you have to set the this configuration option:

```
 controller/jobs/order/email/delivery/name = Mydelivery
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyDelivery"!


## status

Only send order delivery notification e-mails for these delivery status values

```
controller/jobs/order/email/delivery/status = Array
(
    [0] => 2
    [1] => 3
    [2] => 6
    [3] => 7
)
```

* Default: `Array
(
    [0] => 2
    [1] => 3
    [2] => 6
    [3] => 7
)
`
* Type: integer - Delivery status constant
* Since: 2014.03

Notification e-mail about delivery status changes can be sent for these
status values:

* 0: deleted
* 1: pending
* 2: progress
* 3: dispatched
* 4: delivered
* 5: lost
* 6: refused
* 7: returned

User-defined status values are possible but should be in the private
block of values between 30000 and 32767.

See also:

* controller/jobs/order/email/payment/status
* controller/jobs/order/email/delivery/limit-days

## template-html

Relative path to the template for the HTML part of the delivery emails.

```
controller/jobs/order/email/delivery/template-html = order/email/delivery/html
```

* Default: `order/email/delivery/html`
* Type: string - Relative path to the template
* Since: 2022.04

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in templates/controller/jobs).
You can overwrite the template file configuration in extensions and
provide alternative templates.

See also:

* controller/jobs/order/email/delivery/template-text

## template-text

Relative path to the template for the text part of the delivery emails.

```
controller/jobs/order/email/delivery/template-text = order/email/delivery/text
```

* Default: `order/email/delivery/text`
* Type: string - Relative path to the template
* Since: 2022.04

The template file contains the text and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in templates/controller/jobs).
You can overwrite the template file configuration in extensions and
provide alternative templates.

See also:

* controller/jobs/order/email/delivery/template-html

# payment
## attachments

List of file paths whose content should be attached to all payment e-mails

```
controller/jobs/order/email/payment/attachments = Array
(
)
```

* Default: `Array
(
)
`
* Type: array - List of absolute file paths
* Since: 2016.10

This configuration option allows you to add files to the e-mails that are
sent to the customer when the payment status changes, e.g. for the order
confirmation e-mail. These files can't be customer specific.

See also:

* controller/jobs/order/email/delivery/attachments

## bcc-email

Hidden e-mail address all payment e-mails should be also sent to

```
controller/jobs/order/email/payment/bcc-email = Array
(
)
```

* Default: `Array
(
)
`
* Type: string|array - E-mail address or list of e-mail addresses
* Since: 2014.03

Using this option you can send a copy of all payment related e-mails
to a second e-mail account. This can be handy for testing and checking
the e-mails sent to customers.

It also allows shop owners with a very small volume of orders to be
notified about payment changes. Be aware that this isn't useful if the
order volumne is high or has peeks!


## cc-email

E-Mail address all payment e-mails should be also sent to

```
controller/jobs/order/email/payment/cc-email = 
```

* Type: string - E-mail address or list of e-mail addresses
* Since: 2023.10

Using this option you can send a copy of all payment related e-mails
to a second e-mail account. This can be handy for testing and checking
the e-mails sent to customers.

It also allows shop owners with a very small volume of orders to be
notified about payment changes. Be aware that this isn't useful if the
order volumne is high or has peeks!


## decorators/excludes

Excludes decorators added by the "common" option from the order email payment controllers

```
controller/jobs/order/email/payment/decorators/excludes = Array
(
)
```

* Default: `Array
(
)
`
* Type: array - List of decorator names
* Since: 2015.09

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"controller/jobs/common/decorators/default" before they are wrapped
around the job controller.

```
 controller/jobs/order/email/payment/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Controller\Jobs\Common\Decorator\*") added via
"controller/jobs/common/decorators/default" to this job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/order/email/payment/decorators/global
* controller/jobs/order/email/payment/decorators/local

## decorators/global

Adds a list of globally available decorators only to the order email payment controllers

```
controller/jobs/order/email/payment/decorators/global = Array
(
)
```

* Default: `Array
(
)
`
* Type: array - List of decorator names
* Since: 2015.09

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Controller\Jobs\Common\Decorator\*") around the job controller.

```
 controller/jobs/order/email/payment/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Controller\Jobs\Common\Decorator\Decorator1" only to this job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/order/email/payment/decorators/excludes
* controller/jobs/order/email/payment/decorators/local

## decorators/local

Adds a list of local decorators only to the order email payment controllers

```
controller/jobs/order/email/payment/decorators/local = Array
(
)
```

* Default: `Array
(
)
`
* Type: array - List of decorator names
* Since: 2015.09

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Controller\Jobs\Order\Email\Payment\Decorator\*") around this job controller.

```
 controller/jobs/order/email/payment/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Controller\Jobs\Order\Email\Payment\Decorator\Decorator2" only to this job
controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/order/email/payment/decorators/excludes
* controller/jobs/order/email/payment/decorators/global

## limit-days

Only send payment e-mails of orders that were created in the past within the configured number of days

```
controller/jobs/order/email/payment/limit-days = 30
```

* Default: `30`
* Type: integer - Number of days
* Since: 2014.03

The payment e-mails are normally send immediately after the payment
status has changed. This option prevents e-mails for old order from
being send in case anything went wrong or an update failed to avoid
confusion of customers.

See also:

* controller/jobs/order/email/delivery/limit-days
* controller/jobs/service/delivery/process/limit-days

## name

Class name of the used order email payment scheduler controller implementation

```
controller/jobs/order/email/payment/name = Standard
```

* Default: `Standard`
* Type: string - Last part of the class name
* Since: 2014.03

Each default job controller can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the controller factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Controller\Jobs\Order\Email\Payment\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Controller\Jobs\Order\Email\Payment\Mypayment
```

then you have to set the this configuration option:

```
 controller/jobs/order/email/payment/name = Mypayment
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyPayment"!


## pdf

Enables attaching the order confirmation PDF to the payment e-mail

```
controller/jobs/order/email/payment/pdf = 1
```

* Default: `1`
* Type: bool - TRUE to enable attaching the PDF, FALSE to skip the PDF
* Since: 2022.04

The order confirmation PDF contains the same information like the
HTML e-mail and can be also used as invoice if possible.


## pdf-partial

Location of the address partial template for the text e-mails

```
controller/jobs/order/email/payment/pdf-partial = order/email/summary-pdf
```

* Default: `order/email/summary-pdf`
* Type: string - Relative path to the address partial
* Since: 2020.07

To configure an alternative template for the address partial, you
have to configure its path relative to the template directory
(usually templates/controller/jobs/). It's then used to display the
payment or delivery address block in the text e-mails.


## status

Only send order payment notification e-mails for these payment status values

```
controller/jobs/order/email/payment/status = Array
(
    [0] => 3
    [1] => 4
    [2] => 5
    [3] => 6
)
```

* Default: `Array
(
    [0] => 3
    [1] => 4
    [2] => 5
    [3] => 6
)
`
* Type: integer - Payment status constant
* Since: 2014.03

Notification e-mail about payment status changes can be sent for these
status values:

* 0: deleted
* 1: canceled
* 2: refused
* 3: refund
* 4: pending
* 5: authorized
* 6: received
* 7: transferred

User-defined status values are possible but should be in the private
block of values between 30000 and 32767.

See also:

* controller/jobs/order/email/delivery/status
* controller/jobs/order/email/payment/limit-days

## template-html

Relative path to the template for the HTML part of the payment emails.

```
controller/jobs/order/email/payment/template-html = order/email/payment/html
```

* Default: `order/email/payment/html`
* Type: string - Relative path to the template
* Since: 2022.04

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in templates/controller/jobs).
You can overwrite the template file configuration in extensions and
provide alternative templates.

See also:

* controller/jobs/order/email/payment/template-text

## template-pdf

Relative path to the template for the PDF part of the payment emails.

```
controller/jobs/order/email/payment/template-pdf = order/email/payment/pdf
```

* Default: `order/email/payment/pdf`
* Type: string - Relative path to the template
* Since: 2022.10

The template file contains the text and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in templates/controller/jobs).
You can overwrite the template file configuration in extensions and
provide alternative templates.

See also:

* controller/jobs/order/email/payment/template-html
* controller/jobs/order/email/payment/template-text

## template-text

Relative path to the template for the text part of the payment emails.

```
controller/jobs/order/email/payment/template-text = order/email/payment/text
```

* Default: `order/email/payment/text`
* Type: string - Relative path to the template
* Since: 2022.04

The template file contains the text and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in templates/controller/jobs).
You can overwrite the template file configuration in extensions and
provide alternative templates.

See also:

* controller/jobs/order/email/payment/template-html

# subscription
## template-html

Relative path to the template for the HTML part of the subscription emails.

```
controller/jobs/order/email/subscription/template-html = order/email/subscription/html
```

* Default: `order/email/subscription/html`
* Type: string - Relative path to the template
* Since: 2022.04

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in templates/controller/jobs).
You can overwrite the template file configuration in extensions and
provide alternative templates.

See also:

* controller/jobs/order/email/subscription/template-text

## template-text

Relative path to the template for the text part of the subscription emails.

```
controller/jobs/order/email/subscription/template-text = order/email/subscription/text
```

* Default: `order/email/subscription/text`
* Type: string - Relative path to the template
* Since: 2022.04

The template file contains the text and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in templates/controller/jobs).
You can overwrite the template file configuration in extensions and
provide alternative templates.

See also:

* controller/jobs/order/email/subscription/template-html

# voucher
## decorators/excludes

Excludes decorators added by the "common" option from the order email voucher controllers

```
controller/jobs/order/email/voucher/decorators/excludes = Array
(
)
```

* Default: `Array
(
)
`
* Type: array - List of decorator names
* Since: 2015.09

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"controller/jobs/common/decorators/default" before they are wrapped
around the job controller.

```
 controller/jobs/order/email/voucher/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Controller\Jobs\Common\Decorator\*") added via
"controller/jobs/common/decorators/default" to this job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/order/email/voucher/decorators/global
* controller/jobs/order/email/voucher/decorators/local

## decorators/global

Adds a list of globally available decorators only to the order email voucher controllers

```
controller/jobs/order/email/voucher/decorators/global = Array
(
)
```

* Default: `Array
(
)
`
* Type: array - List of decorator names
* Since: 2015.09

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Controller\Jobs\Common\Decorator\*") around the job controller.

```
 controller/jobs/order/email/voucher/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Controller\Jobs\Common\Decorator\Decorator1" only to this job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/order/email/voucher/decorators/excludes
* controller/jobs/order/email/voucher/decorators/local

## decorators/local

Adds a list of local decorators only to the order email voucher controllers

```
controller/jobs/order/email/voucher/decorators/local = Array
(
)
```

* Default: `Array
(
)
`
* Type: array - List of decorator names
* Since: 2015.09

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Controller\Jobs\Order\Email\Voucher\Decorator\*") around this job controller.

```
 controller/jobs/order/email/voucher/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Controller\Jobs\Order\Email\Voucher\Decorator\Decorator2" only to this job
controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/order/email/voucher/decorators/excludes
* controller/jobs/order/email/voucher/decorators/global

## limit-days

Only send voucher e-mails of orders that were created in the past within the configured number of days

```
controller/jobs/order/email/voucher/limit-days = 30
```

* Default: `30`
* Type: integer - Number of days
* Since: 2014.03

The voucher e-mails are normally send immediately after the voucher
status has changed. This option prevents e-mails for old order from
being send in case anything went wrong or an update failed to avoid
confusion of customers.

See also:

* controller/jobs/order/email/delivery/limit-days
* controller/jobs/service/delivery/process/limit-days

## name

Class name of the used order email voucher scheduler controller implementation

```
controller/jobs/order/email/voucher/name = Standard
```

* Default: `Standard`
* Type: string - Last part of the class name
* Since: 2014.03

Each default job controller can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the controller factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Controller\Jobs\Order\Email\Voucher\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Controller\Jobs\Order\Email\Voucher\Myvoucher
```

then you have to set the this configuration option:

```
 controller/jobs/order/email/voucher/name = Myvoucher
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyVoucher"!


## pdf

Enables attaching a PDF to the voucher e-mail

```
controller/jobs/order/email/voucher/pdf = 1
```

* Default: `1`
* Type: bool - TRUE to enable attaching the PDF, FALSE to skip the PDF
* Since: 2022.10

The voucher PDF contains the same information like the HTML e-mail.


## status

Only send e-mails containing voucher for these payment status values

```
controller/jobs/order/email/voucher/status = 6
```

* Default: `6`
* Type: integer - Payment status constant
* Since: 2018.07

E-mail containing vouchers can be sent for these payment status values:

* 0: deleted
* 1: canceled
* 2: refused
* 3: refund
* 4: pending
* 5: authorized
* 6: received

See also:

* controller/jobs/order/email/voucher/limit-days

## template-html

Relative path to the template for the HTML part of the voucher emails.

```
controller/jobs/order/email/voucher/template-html = order/email/voucher/html
```

* Default: `order/email/voucher/html`
* Type: string - Relative path to the template
* Since: 2022.04

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in templates/controller/jobs).
You can overwrite the template file configuration in extensions and
provide alternative templates.

See also:

* controller/jobs/order/email/voucher/template-text

## template-pdf

Relative path to the template for the PDF part of the voucher emails.

```
controller/jobs/order/email/voucher/template-pdf = order/email/voucher/pdf
```

* Default: `order/email/voucher/pdf`
* Type: string - Relative path to the template
* Since: 2022.10

The template file contains the text and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in templates/controller/jobs).
You can overwrite the template file configuration in extensions and
provide alternative templates.

See also:

* controller/jobs/order/email/voucher/template-html
* controller/jobs/order/email/voucher/template-text

## template-text

Relative path to the template for the text part of the voucher emails.

```
controller/jobs/order/email/voucher/template-text = order/email/voucher/text
```

* Default: `order/email/voucher/text`
* Type: string - Relative path to the template
* Since: 2022.04

The template file contains the text and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in templates/controller/jobs).
You can overwrite the template file configuration in extensions and
provide alternative templates.

See also:

* controller/jobs/order/email/voucher/template-html
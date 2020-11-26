# Common

The Aimeos web shop can send out emails after for every payment and delivery status update which also includes the confirmation email. Some configuration options listed in this section are very important for shop owners as you should configure at least the email addresses!

The options that are shared and which you should keep an eye on:

client/html/email/logo
: Path to the logo image displayed in HTML emails

client/html/email/from-email
: Email address used when sending emails

client/html/email/from-name
: Name used when sending emails

client/html/email/reply-email
: Email address used by the customer when replying to emails

client/html/email/reply-name
: Recipient name displayed when the customer replies to emails

client/html/email/bcc-email
: Email address all emails should be also sent to (can be used as notification of the shop owner)

# Account

Aimeos is able to create customer accounts after placing an order automatically. The customers will get an email that contains the credentials for their new accounts created by the [customer/email/account job controller](../../config/controller-jobs/customer-email.md#account).

## Structure

Account emails consists of a [HTML](../../config/client-html/email-account.md#name) and a [text](../../config/client-html/email-account.md#name) part. They are sent in one email as alternative views and the mail clients will display the one that is preferred by the customer.

![Aimeos-email-account-html](Aimeos-email-account-html.png)
![Aimeos-email-account-text](Aimeos-email-account-text.png)

## Templates

You can adapt the templates for the HTML/text account emails itself and the included sections by overwriting them in your own extension or configuring alternative template names:

* [Header template](../../config/client-html/email-account.md#template-header)
* [Body template](../../config/client-html/email-account.md#template-body)
* [HTML email body](../../config/client-html/email-account.md#standard/standardtemplate-body)
* [Text email body](../../config/client-html/email-account.md#standard/standardtemplate-body_1)

If you want to change the HTML structure of one of the templates, please have a look at the original versions to ensure that you don't loose essential functionality.

# Delivery

Delivery emails are sent out by the [order/email/delivery job](../../cronjobs/index.md) after the delivery status of an order has changed. The available [order delivery status values](https://github.com/aimeos/aimeos-core/blob/master/lib/mshoplib/src/MShop/Order/Item/Base.php) are :

* STAT_UNFINISHED (-1)
* STAT_DELETED (0)
* STAT_PENDING (1)
* STAT_PROGRESS (2)
* STAT_DISPATCHED (3)
* STAT_DELIVERED (4)
* STAT_LOST (5)
* STAT_REFUSED (6)
* STAT_RETURNED (7)

For each of these delivery status values you are able to send out an email to the customers informing them about the delivery status change. For which status changes emails are sent is configured via the [controller/jobs/order/email/delivery/standard/status](../../config/controller-jobs/order-email.md#standardstatus) setting.

## Email settings

Shop owners have the possibility to configure specific email settings for the delivery emails that differ from the [common settings](#common). Each specific setting overwrites the correlated common setting for the delivery emails. The list of specific settings is:

[client/html/email/delivery/from-email](../../config/client-html/email-delivery.md#from-email)
: Email address used when sending delivery emails

[client/html/email/delivery/from-name](../../config/client-html/email-delivery.md#from-name)
: Name used when sending delivery emails

[client/html/email/delivery/reply-email](../../config/client-html/email-delivery.md#reply-email)
: Email address used by the customer when replying to delivery emails

[client/html/email/delivery/reply-name](../../config/client-html/email-delivery.md#reply-name)
: Recipient name displayed when the customer replies to delivery emails

[client/html/email/delivery/bcc-email](../../config/client-html/email-delivery.md#bcc-email)
: Email address all delivery emails should be also sent to (can be used as notification for the shop owner)

## Structure

Delivery emails consists of an [HTML](../../config/client-html/email-delivery.md#name) and a [text](../../config/client-html/email-delivery.md#name_2) part. They are sent in one email as alternative views and the mail clients will display the one that is preferred by the customer.

![Aimeos-email-service-html](Aimeos-email-service-html.png)
![Aimeos-email-service-text](Aimeos-email-service-text.png)

## Templates

You can adapt the templates for the HTML/text delivery emails itself and the included sections by overwriting them in your own extension or configuring alternative template names:

* [Header template](../../config/client-html/email-delivery.md#template-header)
* [Body template](../../config/client-html/email-delivery.md#template-body)
* [HTML email body](../../config/client-html/email-delivery.md#standardtemplate-body)
* [Text email body](../../config/client-html/email-delivery.md#standardtemplate-body_1)

If you want to change the HTML structure of one of the templates, please have a look at the original versions to ensure that you don't loose essential functionality.

# Payment

Payment emails are sent out by the [order/email/payment job](../../cronjobs/index.md) after the payment status of an order has changed. This is also used for the order confirmation emails which are sent when the payment status is "authorized" or "received". The available [order payment status values](https://github.com/aimeos/aimeos-core/blob/master/lib/mshoplib/src/MShop/Order/Item/Base.php) are :

* PAY_UNFINISHED (-1)
* PAY_DELETED (0)
* PAY_CANCELED (1)
* PAY_REFUSED (2)
* PAY_REFUND (3)
* PAY_PENDING (4)
* PAY_AUTHORIZED (5)
* PAY_RECEIVED (6)

For each of these payment status values you are able to send out an email to the customers informing them about the payment status change. For which status changes emails are sent is configured via the [controller/jobs/order/email/payment/standard/status](../../config/controller-jobs/order-email.md#standardstatus_1) setting.

## Email settings

Shop owners have the possibility to configure specific email settings for the payment emails that differ from the [common settings](#common). Each specific setting overwrites the correlated common setting for the payment emails. The list of specific settings is:

* [client/html/email/payment/from-email](../../config/client-html/email-payment.md#from-email)
: Email address used when sending payment emails

* [client/html/email/payment/from-name](../../config/client-html/email-payment.md#from-name)
: Name used when sending payment emails

* [client/html/email/payment/reply-email](../../config/client-html/email-payment.md#reply-email)
: Email address used by the customer when replying to payment emails

* [client/html/email/payment/reply-name](../../config/client-html/email-payment.md#reply-name)
: Recipient name displayed when the customer replies to payment emails

* [client/html/email/payment/bcc-email](../../config/client-html/email-payment.md#bcc-email)
: Email address all payment emails should be also sent to (can be used as notification for the shop owner)

## Structure

Payment emails consists of an [HTML](../../config/client-html/email-payment.md#name) and a [text](../../config/client-html/email-payment.md#name_3) part. They are sent in one email as alternative views and the mail clients will display the one that is preferred by the customer.

![Aimeos-email-service-html](Aimeos-email-service-html.png)
![Aimeos-email-service-text](Aimeos-email-service-text.png)

## Templates

You can adapt the templates for the HTML/text payment emails itself and the included sections by overwriting the templates in your own extension or configuring alternative template names:

* [Header template](../../config/client-html/email-payment.md#template-header)
* [Body template](../../config/client-html/email-payment.md#template-body)
* [HTML email body](../../config/client-html/email-payment.md#standardtemplate-body)
* [Text email body](../../config/client-html/email-payment.md#standardtemplate-body_2)

If you want to change the HTML structure of one of the templates, please have a look at the original versions to ensure that you don't loose essential functionality.

# Product watch

Notification emails for watched products are sent out by the [customer/email/watch job](../../cronjobs/index.md) after the product was updated. This includes both, price and stock level updates.

## Email settings

Shop owners have the possibility to configure specific email settings for the product notification emails that differ from the [common settings](#common). Each specific setting overwrites the correlated common setting for the watch emails. The list of specific settings is:

[client/html/email/watch/from-email](../../config/client-html/email-watch.md#from-email)
: Email address used when sending notification emails

[client/html/email/watch/from-name](../../config/client-html/email-watch.md#from-name)
: Name used when sending notification emails

[client/html/email/watch/reply-email](../../config/client-html/email-watch.md#reply-email)
: Email address used by the customer when replying to notification emails

[client/html/email/watch/reply-name](../../config/client-html/email-watch.md#reply-name)
: Recipient name displayed when the customer replies to notification emails

[client/html/email/watch/bcc-email](../../config/client-html/email-watch.md#bcc-email)
: Email address all notification emails should be also sent to (can be used for debug purposes or to explicitly remove a common BCC email address by setting it to NULL)

## Structure

Product notification emails consists of an [HTML](../../config/client-html/email-watch.md#name) and a [text](../../config/client-html/email-watch.md#name_2) part. They are sent in one email as alternative views and the mail clients will display the one that is preferred by the customer.

![Aimeos-email-watch-html](Aimeos-email-watch-html.png)
![Aimeos-email-watch-text](Aimeos-email-watch-text.png)

## Templates

You can adapt the templates for the HTML/text product notification emails itself and the included sections by overwriting them in your own extension or configuring alternative template names:

* [Header template](../../config/client-html/email-watch.md#template-header)
* [Body template](../../config/client-html/email-watch.md#template-body)
* [HTML email body](../../config/client-html/email-watch.md#standardtemplate-body)
* [Text email body](../../config/client-html/email-watch.md#standardtemplate-body_1)


If you want to change the HTML structure of one of the templates, please have a look at the original versions to ensure that you don't loose essential functionality.

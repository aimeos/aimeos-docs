# Installation

## Requirements

* Linux/Unix, WAMP/XAMP or MacOS environment
* PHP >= 7.1
* MySQL >= 5.7.8, MariaDB >= 10.2.2
* Web server (Apache, Nginx or integrated PHP web server for testing)

## Supported versions

For the list of Symfony versions that are supported by the Aimeos bundle, please have a look at the [support section in the repository](https://github.com/aimeos/aimeos-symfony#installation).

## Using Composer

**Symfony bundle** : Can be integrated into your own Symfony application. The installation is described here:

* <https://github.com/aimeos/aimeos-symfony#installation>

# Upgrade

## Guideline

The upgrade process depends on the version you want to upgrade to.

There are three types of releases:

* minor releases (bugfixes)
* stable releases (new features)
* major releases (breaking changes)

As a rule of thumb:

1. Update to the latest minor release, e.g. from 2020.04.1 to 2020.04.2 to get all bugfixes
2. Update to the latest stable release, e.g. from 2020.07 to 2020.10 to get long term support for your major version
3. Upgrade to the new major version e.g. from 2020.10 to 2021.10 if long term support has ended

Instead of upgrading to a new LTS version, you can also buy an [extended long term support](https://aimeos.com/support) from the Aimeos company. They guarantee up to **five years support** for your used version.

More information about the release schedule and the support periods is available on the Aimeos roadmap page: <https://aimeos.org/project/roadmap/>

## Process

If you want to upgrade from earlier versions, there are a few steps necessary to update your Symfony application:

* Follow the steps in the [installation guide](https://github.com/aimeos/aimeos-symfony#table-of-content)
* Update the database and clear all caches

```bash
php ./bin/console aimeos:setup
php ./bin/console cache:clear
php ./bin/console aimeos:clear
```

If you've created a custom Aimeos extension, please have a look into the Aimeos **changelog section** and search for changes that applies to your code.

# Cronjobs

Aimeos jobs are implemented for maintenance tasks like clean up or sending e-mails. Some of them need to be executed very often, others only once a day.

## Setup

A job should be executed by a regularly running cronjob. You can also execute jobs by hand at any time but some jobs need to run very often, e.g. every minute. Aimeos jobs can be executed on the command line using the Symfony "bin/console" command:

```bash
php bin/console aimeos:jobs "<jobs>" "<sites>"
```

jobs (mandatory)
: The jobs parameter can be the name of a single job or a list of job names separated by a white space. For a list of available jobs have a look at [job controller documentation](../../cronjobs/index.md)

sites (standard is "default")
: This must be one or more locale site codes that you have used in the administration interface. Several sites must be separated by a white space.

## Configuration

For some jobs (especially the tasks that are sending e-mails) a few configuration settings are required in the "aimeos_shop" section of the `./onfig/packages/aimeos_shop.yaml` file of your application. This includes the e-mail address of your shop, the name displayed in the "From:" line of all sent e-mails and the base URL to the product images:

```yaml
aimeos_shop:
    client:
        html:
            email:
                from-email: me@myshop.com
                from-name: 'My Shop'
            common:
                content:
                    baseurl: https://yourdomain.com/uploads
                template:
                    baseurl: '%kernel.root_dir%/../public/bundles/aimeosshop/themes/elegance'
```

To use another theme CSS for the sent e-mails, you can set the [client/html/common/template/baseurl](../../config/client-html/common-template#baseurl) parameter like shown above. As the job controller is executed via a cronjob, you must configure an **absolute path to the theme files**. The easiest way is to use the `%kernel.root_dir%` variable which always points to the `./bin/` directory of your Symfony application.

E-mails with products also contains links to these products on you web site. But e-mails are sent from the command line and Symfony can't guess the base URL in this case. This is solved by adding the following settings to your `./config/services.yml` file:

```yaml
parameters:
    router.request_context.host: yourhost.com
    router.request_context.scheme: https
    router.request_context.base_url:
```

!!! warning
    Don't add a slash behind the **router.request_context.base_url** setting if your Symfony `./public/` directory is located directly at the document root of your virtual host! This causes links whose paths begin with two slashes ("//") and Symfony doesn't reduce them to one, so the links won't work.

## Every minute

Some Aimeos jobs should run very often, like the job for sending order confirmation e-mails after an order was placed successfully. This task can also be used for other jobs that should also run frequently:

* Order CSV export (export of orders marked in the admin interface)
* Order delivery related e-mails (customer notification e-mails on delivery status changes)
* Order payment related e-mails (customer notification e-mails on payment status changes and order confirmation e-mails)
* Order voucher e-mails (e-mails to customers containing the code for the voucher they bought)
* Process order delivery services (send paid orders to ERP systems or logistic partners)
* Subscription CSV export (export of subscriptions marked in the admin interface)
* Customer account e-mails (create new customer accounts and send e-mails with password)

The appropriate cronjob command is:

```
* * * * * php /path/to/bin/console aimeos:jobs "order/export/csv order/email/delivery order/email/payment order/email/voucher order/service/delivery subscription/export/csv customer/email/account"
```

## Every hour

The same must be done for jobs that have to be executed every hour (or at least several times a day):

* Product notification e-mails (customer notification for price and stock updates)
* Removes unfinished orders (unblock product stock and coupon codes)
* Batch update of payment/delivery status (asynchronous updates via uploaded files)
* Capture authorized payments (if payments are first authorized and captured later)

The appropriate cronjob command is:

```
30 * * * * php /path/to/bin/console aimeos:jobs "customer/email/watch order/cleanup/unfinished order/service/async order/service/payment"
```

## Once a day

These jobs should be executed once a day (best at times of low traffic):

* Cache cleanup (remove old cache entries)
* Catalog import (import categories from CSV files)
* Log cleanup (remove old log entries)
* Removes unpaid orders (delete orders without payment)
* Product import (import products from CSV files)
* Products bought together (automatically generated product suggestions)
* Index rebuild (re-create the product index)
* Index optimize (optimizes the index for fastest query execution)
* Product sitemap (generate product sitemaps for search engines)
* Start subscription period (start subscription period and add permissions if applicable)
* Renew subscriptions (renew subscriptions on next date)
* End subscription period (finish subscriptions and revoke permissions if applicable)

The appropriate cronjob command is:

```
0 1 * * * php /path/to/bin/console aimeos:jobs "admin/cache admin/log catalog/import/csv order/cleanup/unpaid product/import/csv product/bought index/rebuild index/optimize product/export/sitemap subscription/process/begin subscription/process/renew subscription/process/end"
```

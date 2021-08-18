# Installation

## Requirements

* Linux/Unix, WAMP/XAMP or MacOS environment
* PHP >= 7.2
* MySQL >= 5.7.8, MariaDB >= 10.2.2
* Web server (Apache, Nginx or integrated PHP web server for testing)

## Supported versions

For the list of Laravel versions that are supported by the Aimeos package, please have a look at the [support section in the repository](https://github.com/aimeos/aimeos-laravel#supported-versions).

## Using Composer

**Laravel package** : Can be integrated into your own Laravel application. The installation is described here:

* <https://github.com/aimeos/aimeos-laravel#installation>

**stand-alone shop** : Can be installed using composer within five minutes to get a complete shop system:

* <https://github.com/aimeos/aimeos#installation>

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

More information about the release schedule and the support periods is available on the Aimeos roadmap page: <https://aimeos.org/roadmap>

## Process

If you want to upgrade from earlier versions, there are some steps necessary to update your Laravel application:

* Follow the steps in the [installation guide](https://github.com/aimeos/aimeos-laravel#installation)
* Copy the `vendor/aimeos/aimeos-laravel/src/config/shop.php` to `config/shop.php`
* Adapt the `shop.php` to your needs again
* Copy the `./vendor/aimeos/aimeos-laravel/src/views/` folder to `./resources/views/vendor/shop/`
* Adapt the views to your needs again
* Update the database and clear all caches

```bash
php ./artisan aimeos:setup
php ./artisan route:clear
php ./artisan view:clear
php ./artisan aimeos:clear
```

If you've created a custom Aimeos extension, please have a look into the Aimeos **Changelog** (left navigation) and search for changes that applies to your code.

## Upgrade to 2021.07+

Since 2021.07, installing Aimeos via composer requires composer 2.1+ and the official Aimeos extensions prefixed with "ai-" must be removed from the *./ext/* directory. Instead, they are installed into *./vendor/aimeos/* now. If you don't remove them with:

```bash
rm -rf ./ext/ai-*
```

from your installation after upgrading, you will get an error about these extensions are available twice (once in *./ext* and once in *./vendor/aimeos/*). Your custom extensions can still be placed in the ./ext directory to make development easier.

Due to splitting uploaded files by site, the directory structure changed and those file are now stored in subdirectories named by the site ID, e.g. *./public/aimeos/1./files/*. New uploaded files use that new structure automatically. The old paths were:

* ./public/files/...
* ./public/previews/...

In 2021.07+, the new paths are:

* ./public/aimeos/1./files/...
* ./public/aimeos/1./previews/...
* ./public/aimeos/2./files/...
* ./public/aimeos/2./previews/...

Thus, old uploaded files will be only found if you move the old paths to the new *./public/aimeos* sub-directory:

```bash
mv ./public/files/ ./public/aimeos/files
mv ./public/previews/ ./public/aimeos/previews
```

Furthermore, the themes directory for Laravel installation has changed from *./public/packages/shop* to *./public/vendor/shop* to comply to Laravel standards.

# Cronjobs

Aimeos jobs are implemented for maintenance tasks like clean up or sending e-mails. Some of them need to be executed very often, others only once a day.

## Setup

A job should be executed by a regularly running cronjob. You can also execute jobs by hand at any time but some jobs need to run very often, e.g. every minute. Aimeos jobs can be executed on the command line using the Laravel "artisan" command:

```bash
php artisan aimeos:jobs "<jobs>" "<sites>"
```

jobs (mandatory)
: The jobs parameter can be the name of a single job or a list of job names separated by a white space. For a list of available jobs have a look at [job controller documentation](../cronjobs/index.md)

sites (standard is "default")
: This must be one or more locale site codes that you have used in the administration interface. Several sites must be separated by a white space.

## Configuration

For some jobs (especially the tasks that are sending e-mails) a few configuration settings are required in the `config/shop.php` file of your application. This includes the e-mail address of your shop, the name displayed in the "From:" line of all sent e-mails and the base URL to the product images:

```php
'client' => array(
    'html' => array(
        'common' => array(
            'template' => array(
                 'baseurl' => public_path('vendor/shop/themes/elegance'),
            ),
        ),
        'email' => array(
            'from-email' => 'demo@aimeos.org',
            'from-name' => 'Demo shop',
        ),
        ...
    ),
),
```

To use another theme CSS for the sent e-mails, you can set the [client/html/common/template/baseurl](../config/client-html/common-template.md#baseurl) parameter like shown above. As the job controller is executed via a cronjob, you must configure an **absolute path to the theme files**. The easiest way is to use the `public_path()` helper function which creates absolute paths to the `./public/` directory of your Laravel application.

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
* * * * * php /path/to/artisan aimeos:jobs "order/export/csv order/email/delivery order/email/payment order/email/voucher order/service/delivery subscription/export/csv customer/email/account"
```

## Every hour

The same must be done for jobs that have to be executed every hour (or at least several times a day):

* Product notification e-mails (customer notification for price and stock updates)
* Removes unfinished orders (unblock product stock and coupon codes)
* Batch update of payment/delivery status (asynchronous updates via uploaded files)
* Capture authorized payments (if payments are first authorized and captured later)

The appropriate cronjob command is:

```
30 * * * * php /path/to/artisan aimeos:jobs "customer/email/watch order/cleanup/unfinished order/service/async order/service/payment"
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
0 1 * * * php /path/to/artisan aimeos:jobs "admin/cache admin/log catalog/import/csv order/cleanup/unpaid product/import/csv product/bought index/rebuild index/optimize product/export/sitemap subscription/process/begin subscription/process/renew subscription/process/end"
```

# Content Security Policy

Since 2021.07+, Aimeos enforces a strict Content Security Policy (CSP) by default to prevent cross-site scripting attacks. You won't notice that most of the time but if you need to include CSS, Javascript or images from other domains or try to add inline Javascript, you will see errors like this one in the browser console:

```
js.stripe.com/:1 Refused to frame 'https://js.stripe.com/'
because it violates the following Content Security Policy directive:
"default-src 'self' https://cdn.jsdelivr.net"
```

The default CSP is part of the [base.blade.php](https://github.com/aimeos/aimeos-laravel/blob/master/src/views/base.blade.php#L7) template and consists of:

```
default-src 'self' 'nonce-{{ app( 'aimeos.context' )->get()->nonce() }}' https://cdn.jsdelivr.net;
style-src 'unsafe-inline' 'self' https://cdn.jsdelivr.net;
img-src 'self' data: https://cdn.jsdelivr.net https://aimeos.org
```

This allows:

* CSS from own domain, Jsdelivr and as inline styles
* Images from own domain, Jsdeliver, Aimeos and as "data" content
* Everything else (incl. Javascript) from own domain and Jsdelivr

The random `nonce-...` value also allows inline Javascript when a *nonce* attribute is added to the script tag in the template, e.g.:

```
<script nonce="{{ app( 'aimeos.context' )->get()->nonce() }}">
var count = 1;
</script>
```

To add another domain to the CSP, first you have to copy the `base.blade.php` template from `./vendor/aimeos/aimeos-laravel/src/views/base.blade.php` to `./resources/views/vendor/shop/base.blade.php`. Then, your copy takes precedence over the template in the `./vendor` directory and you can change it according to your needs.

To add e.g. YouTube videos, you should add `https://youtube.com` to the *default-src* directive, e.g.:

```
default-src 'self' 'nonce-{{ app( 'aimeos.context' )->get()->nonce() }}' https://cdn.jsdelivr.net https://youtube.com; style-src 'unsafe-inline' 'self' https://cdn.jsdelivr.net; img-src 'self' data: https://cdn.jsdelivr.net https://aimeos.org
```

Sometimes, several subdomains are used e.g. by Stripe and then you should add `https://*.stripe.com` as wildcard:

```
default-src 'self' 'nonce-{{ app( 'aimeos.context' )->get()->nonce() }}' https://cdn.jsdelivr.net https://*.stripe.com; style-src 'unsafe-inline' 'self' https://cdn.jsdelivr.net; img-src 'self' data: https://cdn.jsdelivr.net https://aimeos.org
```

# Installation

## Requirements

* Linux/Unix, WAMP/XAMP or MacOS environment
* PHP >= 7.1
* MySQL >= 5.7.8, MariaDB >= 10.2.2
* Web server (Apache, Nginx or integrated PHP web server for testing)

## Supported versions

For the list of TYPO3 versions that are supported by the Aimeos extension, please have a look at the [support section in the repository](https://github.com/aimeos/aimeos-typo3#installation).

## Using Composer

**TYPO3 extension** : Can be integrated into your own TYPO3 application. The installation is described here:

* <https://github.com/aimeos/aimeos-typo3#installation>

**TYPO3 distribution** : Can be installed in a fresh TYPO3 instance within five minutes to get a complete shop system:

* <https://github.com/aimeos/aimeos-typo3-dist>

# Upgrade

## Guideline

The upgrade process depends on the version you want to upgrade to.

There are three types of releases:

* minor releases (bugfixes)
* stable releases (new features)
* major releases (breaking changes)

As a rule of thumb:

1. Update to the latest minor release, e.g. from 24.4.1 to 24.4.2 to get all bugfixes
2. Update to the latest stable release, e.g. from 24.7 to 24.10 to get long term support for your major version
3. Upgrade to the new major version e.g. from 23.10 to 24.10 if long term support has ended

Instead of upgrading to a new LTS version, you can also buy an [extended long term support](https://aimeos.com/support) from the Aimeos company. They guarantee up to **five years support** for your used version.

More information about the release schedule and the support periods is available on the Aimeos roadmap page: <https://aimeos.org/roadmap>

## Process

If you want to upgrade from earlier versions, there are a few steps necessary to update your TYPO3 application:

* Follow the steps in the [installation guide](https://github.com/aimeos/aimeos-typo3#table-of-content)
* Execute the Aimeos update script in the Extension manager (or from CLI)
* Clear all caches

If you've created a custom Aimeos extension, please have a look into the Aimeos **changelog section** and search for changes that applies to your code.

## Upgrade to 21.7+

Since 21.7, installing Aimeos via composer requires composer 2.1+ and the official Aimeos extensions prefixed with "ai-" must be removed from the *./ext/* directory. Instead, they are installed into *./vendor/aimeos/* now. If you don't remove them with:

```bash
rm -rf ./ext/ai-*
```

from your installation after upgrading, you will get an error about these extensions are available twice (once in *./ext* and once in *./vendor/aimeos/*). Your custom extensions can still be placed in the ./ext directory to make development easier.

# Cronjobs

The *Scheduler* extension has to be installed in TYPO3, before any tasks can be configured. Furthermore, the script for running the scheduler tasks needs to be executed regularly. The best way is using the Unix crontab by adding this line:

```
* * * * * /path/to/vendor/bin/typo3 scheduler:run
```

## Create Aimeos tasks

After installing the Aimeos TYPO3 extension, a new scheduler task named "Aimeos scheduler" is available. It's capable of executing one or more Aimeos jobs for one or more sites. Normally, you will need to add the Aimeos scheduler task several times with different jobs. To add a new task, click on the icon with the plus symbol (green one in the upper left corner / above the list of configured tasks):

![Aimeos scheduler task](Aimeos-scheduler.png)

Configure a task for them by

1. click on the plus sign above the list of configured tasks
2. new window *Scheduled tasks* opens:
    * Select "Aimeos Shop advanced scheduler"
    * set selection box *Type* to value "Recurring"
    * enter e.g. "* * * * *" in field *Frequency* to run the task every minute
    * configure the additional fields like page IDs if applicable
    * select the jobs (see below for details)
    * select the sites for which the jobs will be executed (at least "default")
3. click *Save and close.*

!!! warning
    Only the "Aimeos Shop advanced scheduler" is able to generate SEO friendly URLs!

## Every minute

Some Aimeos jobs should run very often, like the job for sending order confirmation e-mails after an order was placed successfully. This task can also be used for other jobs that should also run frequently:

* Customer account e-mails (create new customer accounts and send e-mails with password)
* Order delivery related e-mails (customer notification e-mails on delivery status changes)
* Order export CSV (export of orders marked in the admin interface)
* Order payment related e-mails (customer notification e-mails on payment status changes and order confirmation e-mails)
* Process order delivery services (send paid orders to ERP systems or logistic partners)
* Subscription export CSV (export of subscriptions marked in the admin interface)
* Voucher related e-mails (e-mails to customers containing the code for the voucher they bought)

## Every hour

The same must be done for jobs that have to be executed every hour (or at least several times a day):

* Product notification e-mails (customer notification for price and stock updates)
* Removes unfinished orders (unblock product stock and coupon codes)
* Batch update of payment/delivery status (asynchronous updates via uploaded files)
* Capture authorized payments (if payments are first authorized and captured later)

## Once a day

These jobs should be executed once a day (best at times of low traffic):

* Cache cleanup (remove old cache entries)
* Catalog import (import categories from CSV files)
* Catalog sitemap (generate sitemap with categories for search engines)
* Basket cleanup (remove old baskets)
* Log cleanup (remove old log entries)
* Removes unfinished orders (delete orders with payment status equals -1)
* Removes unpaid orders (delete orders without payment)
* Product import (import products from CSV files)
* Products bought together (automatically generated product suggestions)
* Index rebuild (re-create the product index)
* Index optimize (optimizes the index for fastest query execution)
* Product sitemap (generate product sitemaps for search engines)
* Subscription process start (start subscription period and add permissions if applicable)
* Subscription process renew (renew subscriptions on next date)
* Subscription process end (finish subscriptions and revoke permissions if applicable)

# SEO urls

For TYPO3 9.5 and later, you can define the routes for your shop in your `./config/sites/<sitename>/config.yaml` file for composer based installations so you get user and SEO friendly URLs for your Aimeos shop pages.

```yaml
routeEnhancers:
  Aimeos:
    type: Extbase
    namespace: ai
    defaultController: 'Catalog::list'
    routes:
      - { routePath: '/pin/{pin_action}/{pin_id}/{d_name}', _controller: 'Catalog::detail' }
      - { routePath: '/history/{his_action}/{his_id}', _controller: 'Account::history' }
      - { routePath: '/watch/{wat_action}/{wat_id}', _controller: 'Account::watch' }
      - { routePath: '/watch/{wat_action}', _controller: 'Account::watch' }
      - { routePath: '/fav/{fav_action}/{fav_id}', _controller: 'Account::favorite' }
      - { routePath: '/fav/{fav_action}', _controller: 'Account::favorite' }
      - { routePath: '/c/{f_name}~{f_catid}', _controller: 'Catalog::list' }
      - { routePath: '/t/{f_name}~{f_catid}', _controller: 'Catalog::tree' }
      - { routePath: '/p/{d_name}/{d_prodid}/{d_pos}', _controller: 'Catalog::detail' }
      - { routePath: '/d/{d_name}/{d_pos}', _controller: 'Catalog::detail' }
      - { routePath: '/lt/{l_type}', _controller: 'Catalog::list' }
      - { routePath: '/lp/{l_page}', _controller: 'Catalog::list' }
      - { routePath: '/ls/{f_sort}/{l_page}', _controller: 'Catalog::list' }
      - { routePath: '/l/{f_sort}', _controller: 'Catalog::list' }
      - { routePath: '/b/{b_action}', _controller: 'Basket::index' }
      - { routePath: '/co/{c_step}', _controller: 'Checkout::index' }
      - { routePath: '/s/{s_name}/{f_supid}', _controller: 'Supplier::detail' }
    defaults:
      b_action: ''
      c_step: ''
      f_name: 'c'
      f_sort: ''
      d_pos: ''
```

!!! warn
    Only use the latest TYPO3 10 and 11 releases as older releases have several route enhancer related bugs and the TYPO3 route enhancer implementation is still not bug free! Please watch for unexpected behavior and report them to the [TYPO3 project](https://forge.typo3.org/projects/typo3cms-core/issues)

# Backend access

TYPO3 administrators have full access to all panels and all sites in the Aimeos administration interface but sometimes this isn't desired. Instead, editors shouldn't be TYPO3 administrators and only see the parts of the Aimeos backend they need to see.

Therefore, access to the Aimeos backend can be given to non-admin users in the TYPO3 instance as well. For this, you have to create these backend user groups (names are case sensitive!):

super
: Same access level for non-admin users as for TYPO3 admin users (all panels and all sites)

admin
: Access to all panels in one site

editor
: Access to the panels editors need for their daily work in one site

To limit access for TYPO3 backend users in the Aimeos admin interface you have to:

* Create a new group with label "super", "admin" or "editor"
* Assign one of these groups to the TYPO3 backend user account that should have access to the Aimeos admin interface

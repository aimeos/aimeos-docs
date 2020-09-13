A shop needs to execute several tasks in an asynchronous manner, like sending out e-mails, importing or exporting data as well as rebuilding indexes. The tasks included in Aimeos that can be referred to by these keys:

admin/cache
: Remove old cache entries

admin/log
: Remove old log entries

catalog/import/csv
: Import categories from CSV files

customer/email/account
: Create new customer accounts and send e-mails

customer/email/watch
: Customer notification e-mails on product updates

index/optimize
: Optimize the product index for fastest access

index/rebuild
: Rebuilds the product index)

media/scale
: rescales the product images to the new sizes

order/cleanup/unfinished
: Removes unfinished orders

order/cleanup/unpaid
: Removes unpaid orders

order/email/delivery
: Order delivery related e-mails

order/email/payment
: Order payment related e-mails incl. order confirmation e-mails

order/email/voucher
: E-mails containing the voucher code

order/export/csv
: Export orders in admin interface

order/service/async
: Batch update of payment/delivery status

order/service/delivery
: Process order delivery services like sending orders to ERP systems

order/service/payment
: Capture authorized payments

product/bought
: Automatically generated product suggestions

product/export
: Export products

product/export/sitemap
: Generate product sitemaps for search engines

product/import/csv
: Import products from CSV files

subscription/export/csv
: Export subscriptions in admin interface

subscription/process/begin
: Start subscription period and add permissions if applicable

subscription/process/renew
: Renew subscriptions on next date

subscription/process/end
: Finish subscription period and revoke permissions if applicable

Each application and framework offers means to execute them directly:

* [Laravel](../laravel/setup.md#cronjobs)
* [Symfony](../symfony/setup.md#cronjobs)
* [TYPO3](../typo3/setup.md#scheduler)

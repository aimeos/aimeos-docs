# Databases

The Aimeos web shop is able to use different databases for its data domains. Thus, you can configure a separate database e.g. for all customer or order related data. If no specific database is configured for a data domain, the default database will be used.

The default database configuration is defined in the `config/shop.php` file of the Aimeos shop package and looks like:

```php
'resource' => [
    'db' => [
        'adapter' => 'mysql',
        'host' => '<from .env file>',
        'port' => '',
        'database' => '<from .env file>',
        'username' => '<from .env file>',
        'password' => '<from .env file>',
        'stmt' => ["SET NAMES 'utf8'", "SET SESSION sql_mode='ANSI'"],
        'limit' => 2,
        'opt-persistent' => 0,
    ],
],
```

It defines the database location and credentials as well as the default statements that are executed when opening a connection ("stmt"), the maximum allowed connections to this database for the request ("limit") and if the database connection should persist between connections ("opt-persistent").

You can define one database for each domain (e.g. order, customer, etc.) in the same way. To store all orders in a separate database, add another configuration block to your `./config/shop.php` file:

```php
'resource' => [
    'db-order' => [
        'adapter' => 'mysql',
        'host' => '<hostname or IP address>',
        'port' => '<server port>',
        'database' => '<database name>',
        'username' => '<database user>',
        'password' => '<user password>',
        'stmt' => ["
            SET NAMES 'utf8mb4';
            SET SESSION sql_mode='ANSI';
            SET SESSION sort_buffer_size=2097144;
            SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;
        "],
        'limit' => 2,
        'opt-persistent' => 0,
    ],
],
```

The important line contains the `db-order` key, which tells Aimeos that this resource configuration is for a database that should contain all data from the "order" domain (which includes all *mshop_order* tables).

# Enable APC

A big performance boost can be achieved by installing `APCu` (the APC user cache). It can cache all configuration and translation entries in the shared memory of the web server which can improve performance by 50%.

!!! warning
    Be aware that you have to clear the APC user cache manually each time after you've changed a configuration option or a translation!

In order to tell your application to use the APC user cache, you need to change the `apc_enabled` setting in the `./config/shop.php` file of your application:

```php
return [
    'apc_enabled' => true,
    'apc_prefix' => 'laravel:',
    // ....
);
```

!!! warning
    If you have more than one shop application on the same server, you must assign an **unique apc_prefix** for each instance!

# Caching

During development it's very useful to disable the internal content caching done by the Aimeos package. By default, the following output is cached:

* HTML header and body of each component by the Aimeos caching framework
* Small basket and last seen products in the session of the user

Thus, new content is only generated if you flush the caches and/or delete the frontend cookie in your browser.

To disable the content caching completely, add this to your `./config/shop.php` file:

```php
'madmin' => [
    'cache' => [
        'manager' => [
            'name' => 'None'
        ],
    ],
],
```

!!! warning
    Don't disable the content caching by default in production environments. This has a **severe performance impact**!

The basket is also updated automatically if you add products to or delete products from the basket resp. modifying the basket content in another way.

!!! tip
    You can also disable caching the basket content in the sessions for development using the [client/html/basket/cache/enable](../config/client-html/basket-cache#enable) configuration option.

# Cache distribution

The content cache is usually enabled by default if you haven't disabled it during development in your `./config/shop.php`.

If you have a high volume of products (50k+) and your database server gets slower due to the amount of queries executed, you can offload the content cache entries either to another database server or to an in-memory key/value store like [Redis](https://redis.io/).

To move the content cache entries to a Redis server, you have to install the [ai-cache extension](https://github.com/aimeos/ai-cache). The extension contains documentation how to configure your application for Redis support.

Alternatively, you can move the cached component content to another database server. In this case, you must add a `db-cache` resource block to your `./config/shop.php`:

```php
return [
    // ..
    'resource' => [
        // ..
        'db-cache' => [
            'adapter' => 'mysql',
            'host' => '...',
            'port' => '...',
            'database' => '...',
            'username' => '...',
            'password' => '...',
            'stmt' => ["SET NAMES 'utf8'", "SET SESSION sql_mode='ANSI'"],
            'opt-persistent' => 0,
            'limit' => 2,
        ],
    ],
    // ...
];
```

# Distribute static files

Browsers don't load all required files at once referenced inside a HTML document. Instead, they limit the number of concurrent requests for a single domain. To get around this, a common way is to make the files also available via a different domain, so the browsers will download more files in parallel. Thus, rendering the page is much faster for the user.

One way is to create a second virtual host configuration in your web server which uses a sub-domain like "static.example.com". The document root should point to the same directory as your main virtual host (e.g. example.com) in the file system to ease maintenance. Otherwise you would have to make sure that the files are in sync in both directories.

If the internet connection to your customers is short and fast and your server is able to handle the load, this way is the preferred one - especially, if you are able to serve the files from a memory-based cache like a [reverse Nginx proxy](https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/) or [Varnish](https://www.varnish-cache.org/).

Another option is to use a domain from a content delivery network (CDN) like [Amazon Cloudfront](https://aws.amazon.com/cloudfront/). Usually, you can configure these services to retrieve the static files on the first request from your host and deliver them from their caches afterwards.

The advantage of a CDN over a sub-domain on your own server is the load-balancing across many servers and the distribution from a server near to the visitors of your web site. Both can improve the speed of your web site a lot.

In both cases, you need to configure the Aimeos Laravel package to create links to the product pictures with a different domain. This can be done via an entry in the `config/shop.php` file:

```php
    'resource' => [
        'fs' => [
            'adapter' => 'Standard',
            'basedir' => public_path(),
            'tempdir' => storage_path( 'tmp' ),
            'baseurl' => 'https://static.example.com/media/',
        ],
    ],
```

You can also use the "aimeos/ai-filesystem" package to store files directly on another server. There are drivers for different services available and for details, please have a look at the readme file of the [ai-filesystem package](https://github.com/aimeos/ai-filesystem#installation). An example configuration for using an Amazon S3 storage would be:

```php
    'resource' => [
        'fs' => [
            'adapter' => 'FlyAwsS3',
            'credentials' => [
                'key'    => 'your-key',
                'secret' => 'your-secret',
            ],
            'region' => 'your-region',
            'version' => 'latest',
            'bucket' => 'your-bucket-name',
            'prefix' => 'your-prefix', // optional
            'baseurl' => 'https://your-bucket-name.s3.your-region.amazonaws.com/your-prefix/',
        ],
    ],
```

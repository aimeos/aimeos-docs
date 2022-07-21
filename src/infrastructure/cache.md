Caching already generated content for the next request is one of the main methods to increase performance. The Aimeos [context](context.md) contains a cache object which you can use to store, retrieve and remove cached entries:

```php
$cache = $context->cache();
```

# Available methods

## Add cache entries

Adding or overwriting a single cache entry can be done by calling the `set()` method with the key and the value parameters:

```php
$cache->set( 'product/id/100', '<string with product details>' );
```

The keys must be strings and can contain any UTF-8 character. For the best compatibility ASCII characters and only a few special characters like ".", ":", "-" and "/" should be preferred and the first character should always be an char between a-z or A-Z. Try to use a consistent schema for naming, e.g. `product/id/100/name` or `user:1000:name`. The maximum allowed length for keys is 255 bytes.

As only strings are allowed, list of values and objects must be serialized before they can be added to the cache. You can use `json_encode()` or the PHP `serialize()` method for this. Please remember to use `json_decode()` or `unserialize()` after retrieving the values for these keys to get back the list or object again. The maximum length of a value is 16 MB.

Additionally, one or more tags can be associated to each key/value pair in the cache:

```php
$tags = ['product/id/101', 'product/id/102'];
$cache->set( 'product/id/100', '<string>', null, $tags );
```

In this case, the tag `product/id/101` and `product/id/102` would be associated to the key. This can be extremely handy if you have entries that relates to several other items and should be deleted by `deleteByTags()`. The maximum allowed length for tags
is 255 bytes.

You can also specify an expiration date for the key:

```php
$cache->set( 'product/id/100', '<string>', '2100-01-01 12:00:00' );
```

In the example, `product/id/100` would stay in the cache till Jan. 1, 2100 at noon. The format of the date/time values is "YYYY-MM-DD HH:mm:ss" and the hour values are from 0-23. If no expiry date is given (a null value) then the cache entry will stay forever in the cache.

To add or overwrite multiple key/value pairs in the cache use `setMultiple()`, which is much more efficient than setting them one by one using the `set()` method. In the simplest form, you can use this method to add or overwrite several
key/value pairs at once in the cache:

```php
$pairs = [
	'product/id/100/name' => 'Product name for product with ID 100',
	'product/id/100/prices' => '{1:"10.00",5:"9.00",10:"7.50"}',
	'product/id/100/object' => '<output from serialize()>',
];
$cache->setMultiple( $pairs );
```

The keys must be strings and can contain any UTF-8 character and you should use a consistent schema for naming. The maximum allowed length for keys is 255 bytes.

As only strings are allowed, list of values and objects must be serialized before they can be added to the cache. You can use `json_encode()` or the PHP `serialize()` method for this. Please remember to use `json_decode()` or `unserialize()` after retrieving the values for these keys to get back the list or object again. The maximum length of a value is 512 MB.

You can also specify an expiration date by adding the date/time or TTL as value:

```php
$cache->setMultiple( $pairs, '2100-01-01 00:00:00' );
```

In the example, all passed cache entries will expire at Jan. 1, 2100 at noon. Additionally, one or more tags can be associated to all given cache entries:

```php
$cache->setMultiple( $pairs, null, ['product-100', 'price'], );
```

In this case, `product-100` and `price` would be associated to all cache entries. The maximum allowed length for tags is 255 bytes.

!!! warning
    You should keep the time on both servers in sync to get expected results. Also, the date/time values for expiration are sensitive to time zones. Make sure your web server and your cache server use the same time zone. Otherwise, cache entries will be dropped earlier or later than specified by the web server. The best option is to use UTC time zone on all servers especially if your visitors are accessing your content from all over the world. For example, you can use the `date_default_timezone_set()` function to set the timezone explicitely:

    ```php
    date_default_timezone_set( 'UTC' );
    ```

## Retrieve cached entries

To fetch an entry from the cache server, call the `get()` method with the key of the cached entry:

```php
$result = $cache->get( 'product/id/100' );
```

If the key doesn't exist in the cache, null is returned by default. To return an alternative default value, please use the second parameter:

```php
$result = $cache->get( 'product/id/100', '' );
```

This would return an empty string if the key isn't found in the cache. You can use any type for the default value, even objects or resources.

The default value should not be something that requires a lot of time to be created. Neither should it be the same that is expected to be returned by the `get()` method from the cache. In both cases, it would render the caching useless as the required amount of time for generating the content and asking the server adds up. Instead, use a check, generate and store workflow:

```php
if( ( $result = $cache->get( 'product/id/100' ) ) === null )
{
	$result = generateContent();
	$cache->set( 'product/id/100', $result );
}
```

In case you need to retrieve several cached entries, please use `getMultiple()` instead. It can combine fetching the entries into one request and saves the round trip time of a second or all further requests:

```php
$keys = [
	'product/id/100',
	'product/id/101',
];
$result = $cache->getMultiple( $keys );

// content of $result:
[
	'product/id/100' => '<cached string for product/id/100>',
	'product/id/101' => '<cached string for product/id/101>',
];
```

The result is an associative array of the keys used in the first parameter and the strings stored in the cache for these keys. If one of the keys is not used in the cache, the key is ignored and won't be part of the result array. No error or warning is returned in this case. If none of the keys is found in the cache, an empty array is returned.

You can also check whether an item is present in the cache by using the `has()` method:

```php
if( $cache->has( 'product/id/100' ) ) {
    // yes, we have!
}
```

!!! note
    It is recommended that `has()` is only to be used for cache warming type purposes and not to be used within your live applications operations for get/set, as this method is subject to a race condition where your `has()` will return true and immediately after, another script can remove it, making the state of your app out of date.

## Remove entries

To remove a single entry from the cache, use:

```php
$cache->delete( 'product/id/100' );
```

If the key doesn't exist in the cache, nothing happens and the method returns in the same way as if the key was found. When multiple keys should be deleted, use `deleteMultiple()` instead as it can delete the keys much faster by combining them into one request:

```php
$keys = [
	'product/id/100',
	'product/id/101',
];
$cache->deleteMultiple( $keys );
```

This is much faster than deleting them one by one as they are combined into a single request. If one of the keys is not part of the cache, it's ignored and no error or warning occurs.

If cache entries are tagged by one or more stings, these entries can also be deleted by their tags:

```php
$tags = [
	'product/code/abc',
	'product/code/def',
];
$cache->deleteByTags( $tags );
```

One tag can be associated to several cache entries, so tags are a fast way of deleting many entries at once that share the same tags. This is extremely handy if e.g. all cached entries that relates to one product should be deleted because the product has changed.

If no cache entry is tagged by one of the given tags, nothing will happen and no error or warning occurs.

In rare cases, you may want to wipe out the whole cache and `clear()` will do that:

```php
$cache->clear();
```

This method deletes all cached entries of a site from the cache server the client has access to. This method is primarily usefull to provide a clean start before new entries are added to the cache and you don't know which entries are still in the cache.

!!! warning
    Be careful because this can be a very long lasting operation which blocks your script and can also block all other requests which access the cache!

Finally, the `cleanup()` method will remove all expired cache entries:

```php
$cache->cleanup();
```

This method should be only called by a cronjob regularly to delete entries from the cache that are not valid any more because they have been already expired. The interval of calling this method depends on the expiration of the entries. If most of your cache entires expire after midnight, it's a good idea to clean up the cache a few minutes afterwards.

When the expiration occurs randomly distributed over the whole day, then a clean up every half hour, hour, two hours, etc. is better. The amount of time between each cleanup() call depends on the size of your cache and the amount of expired entries. The more entries has been expired, the more often `cleanup()` should be called. But if your cache size is very big it might be a good idea to remove the cache entries at a time of less activity because cleaning up the cache can be a long running task.

Implementations for cache servers that care about expiration themselves simply do nothing and return immediately.

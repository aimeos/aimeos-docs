
# force

Enforces content caching regardless of user logins

```
client/html/common/cache/force = 
```

* Default: ``
* Type: boolean - True to cache output regardless of login, false for no caching
* Since: 2015.08

Caching the component output is normally disabled as soon as the
user has logged in. This enables displaying user or user group
specific content without mixing standard and user specific output.

If you don't have any user or user group specific content
(products, categories, attributes, media, prices, texts, etc.),
you can enforce content caching nevertheless to keep response
times as low as possible.

See also:

* client/html/common/cache/tag-all

# tag-all

Adds tags for all items used in a cache entry

```
client/html/common/cache/tag-all = 1
```

* Default: `1`
* Type: boolean - True to add tags for all items, false to use only a domain tag
* Since: 2014.07

Each cache entry storing rendered parts for the HTML header or body
can be tagged with information which items like texts, media, etc.
are used in the HTML. This allows removing only those cache entries
whose content has really changed and only that entries have to be
rebuild the next time.

The standard behavior stores only tags for each used domain, e.g. if
a text is used, only the tag "text" is added. If you change a text
in the administration interface, all cache entries with the tag
"text" will be removed from the cache. This effectively wipes out
almost all cached entries, which have to be rebuild with the next
request.

Important: As a list or detail view can use several hundred items,
this configuration option will also add this number of tags to the
cache entry. When using a cache adapter that can't insert all tags
at once, this slows down the initial cache insert (and therefore the
page speed) drastically! It's only recommended to enable this option
if you use the DB, Mysql or Redis adapter that can insert all tags
at once.

See also:

* client/html/common/cache/force
* madmin/cache/manager/name
* madmin/cache/name
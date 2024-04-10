
# enable

Enables or disables caching of the basket content

```
client/html/basket/cache/enable = 1
```

* Default: `1`
* Type: boolean - True to enable, false to disable basket content caching
* Since: 2014.11

For performance reasons, the content of the small baskets is cached
in the session of the customer. The cache is updated each time the
basket content changes either by adding, deleting or editing products.

To ease development, the caching can be disabled but you shouldn't
disable it in your production environment!


# list

List of user action names that should be displayed in the catalog detail view

```
client/html/catalog/actions/list = Array
(
    [0] => pin
    [1] => watch
    [2] => favorite
)
```

* Default: `Array
(
    [0] => pin
    [1] => watch
    [2] => favorite
)
`
* Type: array - List of user action names
* Since: 2017.04

Users can add products to several personal lists that are either only
available during the session or permanently if the user is logged in. The list
of pinned products is session based while the watch list and the favorite
products are durable. For the later two lists, the user has to be logged in
so the products can be associated to the user account.

The order of the action names in the configuration determines the order of
the actions on the catalog detail page.


# salutations

List of salutions the customers can select from in the HTML frontend

```
client/html/common/address/salutations = Array
(
    [0] => 
    [1] => company
    [2] => mr
    [3] => ms
)
```

* Default: Array
* Type: array - List of available salutation codes
* Since: 2021.04

The following salutations are available:

* empty string for "unknown"
* company
* mr
* ms

You can modify the list of salutation codes and remove the ones
which shouldn't be used or add new ones.

See also:

* client/html/account/profile/address/salutations
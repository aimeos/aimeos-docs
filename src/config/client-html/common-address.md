
# billing
## disable-new

Disables the billing address form for a new address

```
client/html/common/address/billing/disable-new = 
```

* Default: 
* Type: boolean - True to disable the "new billing address" form, false to allow a new address
* Since: 2014.03

Normally, customers are allowed to enter a different billing address in the
checkout process that is only stored along with the current order. Registered
customers also have the possibility to change their current billing address
but this updates the existing one in their profile.

You can disable the address form for the new billing address by this setting
if it shouldn't be allowed to enter a different billing address.

See also:

* client/html/common/address/delivery/disable-new

# delivery
## disable-new

Disables the billing address form for a new address

```
client/html/common/address/delivery/disable-new = 
```

* Default: 
* Type: boolean - True to disable the "new delivery address" form, false to allow a new address
* Since: 2014.03

Normally, customers are allowed to enter new delivery addresses in the
checkout process which are stored in the current order. For registered
customers they are also added to the list of delivery addresses in their
profile.

You can disable the address form for the new delivery address by this setting
if it shouldn't be allowed to add another delivery address.

See also:

* client/html/common/address/billing/disable-new

# renew
## standard/use-coupons

Applies the coupons of the previous order also to the new one

```
controller/jobs/subcription/process/renew/standard/use-coupons = 
```

* Default: 
* Type: boolean - True to reuse coupon codes, false to remove coupons
* Since: 2018.10

Reuse coupon codes added to the basket by the customer the first time
again in new subcription orders. If they have any effect depends on
the codes still being active (status, time frame and count) and the
decorators added to the coupon providers in the admin interface.

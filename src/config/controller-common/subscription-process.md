
# payment-days

Number of days to wait for the payment until subscription is removed

```
controller/common/subscription/process/payment-days = 3
```

* Default: 3
* Type: float - Number of days
* Since: 2018.07

Subscriptions wait for the confiugrable number of days until the payment
status changes to a valid payment (by default: "authorized" and "received").
If the payment arrives within this time frame, the subscription is activated.
Otherwise, the subscription is removed from the list of subscriptions that
will be checked for activation.

See also:

* controller/common/subscription/process/processors
* controller/common/subscription/process/payment-status

# payment-ends

Subscriptions ends if payment couldn't be captured

```
controller/common/subscription/process/payment-ends = 1
```

* Default: 1
* Type: bool - TRUE if payment failures ends the subscriptions, FALSE if not
* Since: 2019.10

By default, a subscription ends automatically if the next payment couldn't
be captured. When setting this configuration to FALSE, the subscription job
controller will try to capture the payment at the next run again until the
subscription is deactivated manually.

See also:

* controller/common/subscription/process/processors
* controller/common/subscription/process/payment-days
* controller/common/subscription/process/payment-status

# payment-status

Minimum payment status that will activate the subscription

```
controller/common/subscription/process/payment-status = 5
```

* Default: 5
* Type: integer - Payment status constant
* Since: 2018.07

Subscriptions will be activated if the payment status of the order is
at least the configured payment constant. The default payment status
is "authorized" so orders with a payment status of "authorized" (5) and
"received" (6) will cause the subscription to be activated. Lower
payment status values, e.g. "pending" (4) won't activate the subscription.

See also:

* controller/common/subscription/process/processors
* controller/common/subscription/process/payment-days

# processor
## cgroup/groupids

```
controller/common/subscription/process/processor/cgroup/groupids = Array
(
)
```

* Default: Array


## cgroup/name

```
controller/common/subscription/process/processor/cgroup/name = Standard
```

* Default: Standard


# processors

List of processor names that should be executed for subscriptions

```
controller/common/subscription/process/processors = Array
(
    [0] => cgroup
)
```

* Default: Array
* Type: array - List of processor names
* Since: 2018.04
* Since: 2018.04

For each subscription a number of processors for different tasks can be executed.
They can for example add a group to the customers' account during the customer
has an active subscribtion.

See also:

* controller/common/subscription/process/payment-status
* controller/common/subscription/process/payment-days
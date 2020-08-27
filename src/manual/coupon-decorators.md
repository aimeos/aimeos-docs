A decorator can add additional features on top of coupons only by configuration. For example, if a fixed rebate should only be granted when the total basket value is above a certain limit, then this can be done by an additional decorator added to the configured coupon. The great advantage of decorators is that they can be reused in any combination with all coupons. It's like a set of rules that can be rearranged to create different rule sets only with a small amount of rules.

# Usage

Decorators are activated by adding their name comma separated after the coupon provider name in the "Provider" field in the detail view of a coupon item. If currently a fixed rebate (provided by the FixedRebate coupon provider) is configured like this:
```
FixedRebate
```

the decorator checking for a lower limit of the basket value is added via
```
FixedRebate,BasketValues
```

If you would like to restrict the coupon also to the availability of a certain product in the basket, you can additionally add the "Required" decorator:
```
FixedRebate,BasketValues,Required
```

The decorators are called from right to left, so at first the "Required" decorator is executed, afterwards the "BasketValues" decorator and at last the "FixedRebate" coupon provider. Therefore, it's a good idea to add the decorators requiring less resources at the end and the decorators using external sources just before the coupon provider.


# Built-in decorators

## BasketValues

Tests if the total value of the basket (including service costs for delivery and payment) is above or below the configured limits.

basketvalues.total-value-min (optional)
: The minimum value before the coupon has any effect. The format is a JSON encoded map of the currency ID and the value in x.xx format, e.g. *{"EUR":"1.00","USD":"1.00"}*

basketvalues.total-value-max (optional)
: The maximum value after the coupon has no effect any more. The format is a JSON encoded map of the currency ID and the value in x.xx format, e.g. *{"EUR":"1.00","USD":"1.00"}*

## Category

Tests if at least one product from the configured category or categories is in the basket of the customer. The decorator is available since 2017.10.

category.code (required)
: The category code or a list of category codes separated by comma (e.g. home,men,shirts)

category.only (optional)
: Apply the discount only to the configured categories, not to the whole basket

## Once

Tests if customers have already used the same coupon code in previous orders by checking their billing e-mail address. If this is the case, the customer is informed about that and the coupon code has no effect. This decorator doesn't require additional configuration and is available since 2017.10.

## Not

Negates the availability of the coupon depending on the previous decorators. It returns "true" for availability if the coupon shall not be available and false, if it would be available.

When adding this in the provider field:
```
PercentRebate,Category,Not
```
and configuring the "Category" decorator like this:
```
category.code : root
```
the coupon will be applied to the basket if the basket contains products not from the "root" category. The availabiliy is evaluated from left to right.

## Required

Tests if a certain product is in the basket of the customer.

required.productcode (required)
: The unique code of a product that must be in the basket before the action of the configured coupon is executed.

required.only (optional)
: Apply the discount only to the configured product, not to the whole basket

## Supplier

Restricts the coupons to a certain supplier that must have been selected by the customer in the delivery section of the checkout process. This is useful if you have several subsidaries in different locations.

supplier.code (required)
: Code of the required supplier

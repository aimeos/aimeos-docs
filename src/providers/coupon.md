Aimeos offers an extensible way to implement basket-related actions based on coupon codes. You can modify the basket content, add discount products or adapt any other property of the basket. The user manual contains the [built-in coupon providers](../manual/coupons.md), the available [coupon decorators](../manual/coupon-decorators.md) as well as how to [set up coupons](../manual/coupon-details.md).

# Create coupon providers

To create a new coupon provider, put this code snippet in a class file with the name *Mycoupon.php*:

```php
namespace Aimeos\MShop\Coupon\Provider;

class Mycoupon
	extends \Aimeos\MShop\Coupon\Provider\Factory\Base
	implements Iface, \Aimeos\MShop\Coupon\Provider\Factory\Iface
{
	public function update( \Aimeos\MShop\Order\Item\Base\Iface $base ) : \Aimeos\MShop\Coupon\Provider\Iface
	{
		$base->setCoupon( $this->getCode(), [] );
		return $this;
	}
}
```

The filename must be the same as the class name (here: *Mycoupon*). Of course you should use a more meaningful name for your class and file. Be aware that all names are case sensitive. The new coupon provider must be stored within your project specific [Aimeos extension](../developer/extensions.md) at this location:

```php
// Laravel, Symfony
./<yourext>/lib/custom/src/MShop/Coupon/Provider/Mycoupon.php
// TYPO3
./<yourext>/Resources/Private/Extensions/<yourext>/lib/custom/src/MShop/Coupon/Provider/Mycoupon.php
```

Now you can add a rebate of 1.00 EUR/USD/etc. to the basket for example:

```php
public function update( \Aimeos\MShop\Order\Item\Base\Iface $base ) : \Aimeos\MShop\Coupon\Provider\Iface
{
	$rebate = '1.00',
	$products = $this->createRebateProducts( $base, 'demo-rebate', $rebate );
	$base->setCoupon( $this->getCode(), $products );
	return $this;
}
```

The call to `$this->createRebateProducts()` returns an order product based on the product with the product code "demo-rebate" which must exist. The third parameter is the amount of rebate that will be added to the basket.

!!! note
    All discounts must be added as rebate products because they will be removed automatically, if the requirements for the coupon are not matched any more. This is not possible if you only change the price of a product in the basket.

For tax optimized rebates, you can get the (product) prices by tax rate:

```php
public function update( \Aimeos\MShop\Order\Item\Base\Iface $base ) : \Aimeos\MShop\Coupon\Provider\Iface
{
	$priceItem = current( $this->getPriceByTaxRate( $base ) ); // price for the biggest tax rate
	$product = $this->createProduct( 'demo-rebate' )->setPrice( $priceItem );
	$base->setCoupon( $this->getCode(), [$product] );
	return $this;
}
```

# Add coupon configuration

If you want to add configuration options to your coupon provider which can be modified by editors in the admin backend, you have to specify which configuration keys are used, what value types are allowed, if there's a default value and if it's required or optional as well as implement `checkConfigBE()` and `getConfigBE()` methods:

```php
private $beConfig = [
    'mycoupon.rebate' => [
        'code' => 'mycoupon.rebate',
        'internalcode' => 'mycoupon.rebate',
        'label' => 'Rebate amount',
        'type' => 'number',
        'internaltype' => 'string',
        'default '=> '0',
        'required' => true,
    ],
];

public function checkConfigBE( array $attributes ) : array
{
	return $this->checkConfig( $this->beConfig, $attributes );
}

public function getConfigBE() : array
{
	return $this->getConfigItems( $this->beConfig );
}

public function update( \Aimeos\MShop\Order\Item\Base\Iface $base ) : \Aimeos\MShop\Coupon\Provider\Iface
{
	$rebate = $this->getConfigValue( 'mycoupon.rebate', 0 );
	// ...
	return $this;
}
```

A definition is always identified by an unique key which is identical to its **code** and should contain the provider name in lower case as prefix ("myprovider.minprice" for example). This prevents collisions between keys of decorators named the same.

**Label** is just an arbitrary name to know what the option is for. It can be displayed by the administration interface to the editors to explain what they have to enter.

The **type** value must be one of the predefined strings that describe the allowed type. These types are available:

string
: Arbitrary string with 255 characters at maximum

boolean
: 0/1 value to enable or disable the option

integer
: An integer number (maybe negative)

number
:  A number that can include fractional digits

date
: An ISO date value (YYYY-MM-DD)

time
: A 24h time value (HH:mm)

datetime
: An ISO date and time value (YYYY-MM-DD HH:mm:ss)

select
: A list of values (defined via the "default" key, e.g. "['option1', 'option2']") where one must be chosen, rendered as select box

map
: Associative list of key/value pairs, e.g. "['option1' => 'Label1', 'option2' => 'Label2']") (back-end only)

All values for **internaltype** are most of the time closely related and describe how to store the values internally. Available internal types are:

array
: List of key/value pairs

string
: Arbitrary string with 255 characters at maximum

boolean
: 0/1 value to enable or disable the option

integer
: An integer number (maybe negative)

float
:  A number that can include fractional digits

datetime
: An ISO date and time value (YYYY-MM-DD HH:mm:ss)

For **default**, either a scalar value of any type (string, integer, float, boolean) is allowed or an associative array of key/value pairs in case of the "select" type.

If a setting have to be added, the **required** option must be set to true. Otherwise, it can be left out or set to false so it's optional and won't be enforced.

# Create coupon decorators

The skeleton for the most basic implementation of a coupon decorator would be:

```php
namespace Aimeos\MShop\Coupon\Provider\Decorator;

class Mydecorator
	extends \Aimeos\MShop\Coupon\Provider\Decorator\Base
	implements \Aimeos\MShop\Coupon\Provider\Decorator\Iface
{
}
```
The new coupon provider must be stored within your project specific [Aimeos extension](../developer/extensions.md) at this location:

```php
// Laravel, Symfony
./<yourext>/lib/custom/src/MShop/Coupon/Provider/Decorator/Mydecorator.php
// TYPO3
./<yourext>/Resources/Private/Extensions/<yourext>/lib/custom/src/MShop/Coupon/Provider/Decorator/Mydecorator.php
```

It's only important to extend from the base decorator class and implement the decorator interface. The base class already contains default implementations for all coupon provider methods.

A decorator without methods is totally valid but useless. Thus, you should add one or more methods that intercept the calls to the "onion" object and implement some additional functionality. You can intercept any **public method** that is implemented in a coupon provider:

```php
public function calcPrice( \Aimeos\MShop\Order\Item\Base\Iface $base ) : \Aimeos\MShop\Price\Item\Iface
{
    // do something before
    $priceItem = $this->getProvider()->calcPrice( $base );
    // do something after

    return $priceItem;
}
```

Thus, adding restrictions to the coupon is simple. To check if the user is logged in would consist of:

```php
public function isAvailable( \Aimeos\MShop\Order\Item\Base\Iface $base ) : bool
{
	if( $this->getContext()->getUserId() ) {
		return $this->getProvider()->isAvailable( $base );
	}

	return $false;
}
```

You can define [configuration options](#add-coupon-configuration) for decorators in the same way as for coupon providers.

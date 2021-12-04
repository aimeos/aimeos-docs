Since 2021.04, Aimeos offers an extensible way to implement dynamic pricing rules for products. You can modify the price of each product by creating [rules sets in the admin backend](../manual/rules.md). They consist of rule providers modifying the price and decorators restricting if a rule provider is applied to a price.

!!! tip
    Even if we only speak of modifying product prices by rules, it's also possible to modify other content of product items by rule providers.

# Create rule providers

To create a new catalog rule provider, put this code snippet in a class file with the name *Myprovider.php*:

```php
namespace Aimeos\MShop\Rule\Provider\Catalog;

class Myprovider
	extends \Aimeos\MShop\Rule\Provider\Base
	implements \Aimeos\MShop\Rule\Provider\Catalog\Iface, \Aimeos\MShop\Rule\Provider\Factory\Iface
{
	public function apply( \Aimeos\MShop\Product\Item\Iface $product ) : bool
    {
        return $this->isLast();
    }
}
```

The filename must be the same as the class name (here: *Myprovider*). Of course you should use a more meaningful name for your class and file. Be aware that all names are case sensitive. The new rule provider must be stored within your project specific [Aimeos extension](../developer/extensions.md) at this location:

```php
// Laravel, Symfony
./<yourext>/lib/custom/src/MShop/Rule/Provider/Catalog/Myprovider.php
// TYPO3
./<yourext>/Resources/Private/Extensions/<yourext>/lib/custom/src/MShop/Rule/Provider/Catalog/Myprovider.php
```

Once this is done, Aimeos detects the rule provider automatically and editors will now be able to add rules using the rule provider in the *Marketing* section of the *Aimeos* backend.

!!! warning
    In the `apply()` method, you have access to the product item and related items if they have been fetched from the database. Depending on the frontend configuration, only referenced items from those domains are available that have been passed to the `search()` method of the product manager. This means that not always all related items are available!

To reduce all product prices by 10% for example, use this code as example:

```php
public function apply( \Aimeos\MShop\Product\Item\Iface $product ) : bool
{
	foreach( $product->getRefItems( 'price' ) as $price )
	{
		$value = $price->getValue();
		$discount = $value * 10 / 100;
		$price->setValue( $value - $discount )->setRebate( $discount );
	}

	return $this->isLast();
}
```

The call to `$this->isLast()` returns true if this should be the last rule applied to that product and that depends on the configured value in the admin backend for that rule.

!!! note
    Keep the implementation of `apply()` as small and fast as possible because it's called for every product and every rule. If you send a request to a web service, this will slow down the performance of your shop drastically!

# Add rule configuration

To add configuration options for editors in the admin backend, you have to specify which configuration keys are used, what value types are allowed, if there's a default value and if it's required or optional as well as implement `checkConfigBE()` and `getConfigBE()` methods:

```php
private $beConfig = [
    'myprovider.minprice' => [
        'code' => 'myprovider.minprice',
        'internalcode' => 'myprovider.minprice',
        'label' => 'Minimum price',
        'type' => 'number',
        'internaltype' => 'string',
        'default '=> '0',
        'required' => true,
    ],
];

public function checkConfigBE( array $attributes ) : array
{
	$errors = parent::checkConfigBE( $attributes );
	return array_merge( $errors, $this->checkConfig( $this->beConfig, $attributes ) );
}

public function getConfigBE() : array
{
	return array_merge( parent::getConfigBE(), $this->getConfigItems( $this->beConfig ) );
}

public function apply( \Aimeos\MShop\Product\Item\Iface $product ) : bool
{
	$min = $this->getConfigValue( 'myprovider.minprice', 0 );
	return $product->getPrice()->getValue() > $min ? true : false;
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

# Create rule decorators

The skeleton for the most basic implementation of a rule decorator would be:

```php
namespace Aimeos\MShop\Rule\Provider\Catalog\Decorator;

class Mydecorator
	extends \Aimeos\MShop\Rule\Provider\Catalog\Decorator\Base
	implements \Aimeos\MShop\Rule\Provider\Catalog\Decorator\Iface
{
}
```
The new rule provider must be stored within your project specific [Aimeos extension](../developer/extensions.md) at this location:

```php
// Laravel, Symfony
./<yourext>/lib/custom/src/MShop/Rule/Provider/Catalog/Decorator/Mydecorator.php
// TYPO3
./<yourext>/Resources/Private/Extensions/<yourext>/lib/custom/src/MShop/Rule/Provider/Catalog/Decorator/Mydecorator.php
```

It's only important to extend from the base decorator class and implement the decorator interface. The base class already contains default implementations for all rule provider methods.

A decorator without methods is totally valid but useless. Thus, you should add one or more methods that intercept the calls to the "onion" object and implement some additional functionality. You can intercept any **public method** that is implemented in a rule provider:

```php
public function apply( \Aimeos\MShop\Product\Item\Iface $product ) : bool
{
    // do something before
    $result = $this->getProvider()->apply( $product );
    // do something after

    return $result;
}
```

Thus, adding restrictions to the rule is simple. To check if the user is logged in would consist of:

```php
public function apply( \Aimeos\MShop\Product\Item\Iface $product ) : bool
{
	if( $this->context()->getUserId() ) {
	    return $this->getProvider()->apply( $product )
	}

	return false;
}
```

You can define [configuration options](#add-rule-configuration) for decorators in the same way as for rule providers.

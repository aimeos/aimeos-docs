Delivery and payment handling are one of the most important tasks in a web shop. Most often this involves connecting to external systems and pushing data to them. Therefore it's vital that a shop system has a feature rich interface that is able to cope with all kinds of special requirements remote services demand.

In *Aimeos* the service providers are adapters between the shop interfaces for delivery and payment handling and any remote gateway. They can have arbitrary configurations, individually defined for each service provider. The base classes offer a rich set of methods that ease development and minimize the code that must be written.

Your service provider must be part of your project specific [*Aimeos* extension](../../developer/extensions.md) and be stored in

```
./<yourext>/src/MShop/Service/Provider/Delivery/<classname>.php
```
or
```
./<yourext>/src/MShop/Service/Provider/Payment/<classname>.php
```

to be available in your *Aimeos* installation.

For most service providers you need some configuration values like for username and password to authenticate against external web services. You can store arbitrary numbers of key/value pairs in the service items for each provider which can be checked against a given configuration definition to minimize errors.

!!! warning
    There are two kinds of configuration definitions: For the fields the customer has to fill out in the front-end and for the shop owner in the administration interface! Both use the same way and format for their definition, the only difference is by which method they are returned, either by `getConfigFE()` for the front-end or by `getConfigBE()` for the administration interface.

In order to make things as easy as possible, the base service provider class offers some common methods that are often used in provider implementations.

# Working with orders

By default, the complete order is passed to almost all service provider methods including the addresses, products and services. You can get the items inside an order using:

```php
$coupons = $order->getCoupons();
$products = $order->getProducts();

$paymentAddresses = $order->getAddress( 'payment' );
$deliveryAddresses = $order->getAddress( 'delivery' );

$paymentServices = $order->getService( 'payment' );
$deliveryServices = $order->getService( 'delivery' );
```

All passed orders are saved automatically by the calling object, which is usually a job controller. If you need to set the delivery/payment status of an order and throw an exception afterwards, you have to save the order yourself using:

```php
$this->saveOrder( $order );
```

This saves the order item including the complete order content and creates the necessary entries in the *mshop_order_status* table if one of the status values have been changed.

# Additonal data

## Retrieve data

In cases you need to fetch items from other domains, the context object is necessary to instantiate the appropriate managers. Use it only if you really need it! The complete order can be fetched much simpler with the other support methods and the service item for the provider is already available. To get the context object, use:

```php
$context = $this->context();
```

Afterwards, you can use the *Aimeos\MShop* class to create the manager you need:

```php
$manager = \Aimeos\MShop::create( $context, 'stock' );
```

The line above would create and return the stock manager using the given context.

## Store order data

When integrating external services you often want or have to store data returned by them for later or for reference. This may include transaction IDs, status codes or other related data. In these cases, you should store the data as service attributes attached to the delivery or payment service provider:

```php
$orderServiceItem->addAttributeItems( $this->attributes( $attributes ), $type );
```

It adds the key/value pairs in the `$attributes` parameter with the specified type to the given order service item. If the attribute key/type combination already exists, the attribute value will be updated. The type is an arbitrary string but it's best to use the service provider name in lower case to quickly identify to which service provider it belongs. You can save one or more attribute like this:

```php
$attributes = ['transactionid' => 123];

$serviceType = \Aimeos\MShop\Order\Manager\Base\Base::TYPE_PAYMENT;
$orderServiceItem = $order->getService( $serviceType );

$orderServiceItem->addAttributeItems( $$this->attributes( $attributes ), 'myprovider' );
```

To fetch the attribute again, you can use the *getAttribute()* or *getAttributeItem()* method of the order service item object:

```php
$serviceType = \Aimeos\MShop\Order\Item\Base\Service\Base::TYPE_PAYMENT;
$orderServiceItem = $$order->getService( $serviceType );

$value = $orderServiceItem->getAttribute( 'transactionid', 'myprovider' );
$attrItem = $orderServiceItem->getAttributeItem( 'transactionid', 'myprovider' );
```

## Store customer data

You can also store data related to a customer using the `setData()` method. It's a simple key/value store which can be used for e.g. tokens for repeated payments:

```php
$this->setData( $customerId, 'token', '...' );
```

The method expects the ID of the customer, the key and the associated value. Similarly, you can retrieve the data again using:

```php
$token = $this->data( $customerId, 'token' );
```

# Configuration

## Access configuration

To retrieve values from the configuration stored in the service item by the shop owner or injected by the application (like the self, success, failure, cancel or update URLs), the *getConfigValues()* method offers a common interface to access them:

```php
getConfigValue( array $keys, $default = null )
```

It accepts an array of configuration keys that are tested in the given order and returns the value of the first key that matches. If none of the keys was found, then the default value is returned.  The configuration keys are either defined by your service provider (we will come back to that later) or by the application in case of the URLs.

There are five URLs and the IP address that can be injected by the application:

payment.url-self
: The URL that points to the current page

payment.url-success
: The URL customers are redirected if the payment was successful

payment.url-failure (optional)
: The URL customers are redirected if the payment failed

payment.url-cancel (optional)
: The URL customers are redirected if they canceled the payment

payment.url-update
: The URL payment gateways should send their notifications to if the payment status has changed

client.ipaddress
: Remote IP address of the customer

The URLs for failure and cancellation are not available everywhere and in this case the success URL should be used instead. Therefore, the *getConfigValues()* method simplifies getting the value if you call it like this:

```php
$value = $this->getConfigValue( ['payment.url-failure', 'payment.url-success'] );
$value = $this->getConfigValue( ['username'], 'aimeos' );
```

The first call will either return the URL for "payment.url-failure" if available or the "payment.url-success" URL otherwise. The second call would return the value stored for the key "username" in the service item or "aimeos" if it's not configured.

## Add configuration

To make the available configuration settings known, you have to specify which configuration keys they use, what value types are allowed, if there's a default value and if it's required or optional:

```php
private $feconfig = [
    'myprovider.username' => [
        'code' => 'myprovider.username',
        'internalcode' => 'myprovider.username',
        'label' => 'Username',
        'type' => 'string',
        'internaltype' => 'string',
        'default' => '',
        'required' => true,
    ],
];
```

In the front-end you can also specify if the setting should be hidden or not:

```php
private $feconfig = [
    'myprovider.token' => [
        'code' => 'myprovider.token',
        'internalcode' => 'token',
        'label' => 'Authentication token',
        'type' => 'number',
        'internaltype' => 'integer',
        'default' => '1234',
        'required' => true,
        'public' => false,
   ],
];
```

A definition is always identified by an unique key which is identical to its **code** and should contain the provider name in lower case as prefix ("myprovider.token" for example). This prevents collisions between keys of decorators named the same.

The value for **internalcode** can be the name that is expected by the external service if you have to post the value directly to the gateway. Otherwise, it should be the same as the value for "code".

**Label** is just an arbitrary name to know what the option is for. It can be displayed by the administration interface to the editors to explain what they have to enter. You can add a translation for your new field (to show a specific value on the front-end) like this (Laravel `config/shop.php` example):

```
'i18n' => [
  'en' => [
    'client/code' => [
      'myprovider.username' => ['User name']
    ]
  ]
]
```

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

list
: Associative list of key/value pairs, e.g. "['option1' => 'Label1', 'option2' => 'Label2']") rendered as list of radio options

map
: Associative list of key/value pairs, e.g. "['option1' => 'Label1', 'option2' => 'Label2']") (back-end only)

All values for **internaltype** are most of the time closely related and describe how to store the values internally. Available internal types are:

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

The value for **public** is only evaluated if the configuration options are defined for the front-end. It will add a hidden input field instead of a visible one to the form with the string in "default" as value. In the administration interface it won't have an effect.

## Checkout process

The definitions of what is available will render a form in the front-end near the delivery/payment option. To inform the front-end about the field that should be displayed, the *getConfigFE()* method of your service provider implementation must return them as objects. This is done with these lines of code:


```php
public function getConfigFE( \Aimeos\MShop\Order\Item\Base\Iface $basket ) : array
{
    $list = [];

    foreach( $this->feconfig as $key => $config ) {
        $list[$key] = new \Aimeos\Base\Criteria\Attribute\Standard( $config );
    }

    return $list;
}
```

The *$this->feconfig* contains the front-end configuration definition in this example. In the *getConfigFE()* method, the basket is available too with all data that has been collected up to now. This usually includes at least the products and address(es) of the customers. Based on this information, you can modify the list of definitions as well as adding strings as default for things like the customers' name which was already entered.

If form fields are marked as public, then customers can or must fill out the fields - depending on the "required" flag. If customers forgot one field or entered invalid data, an error message will be shown and the form fields are highlighted where values are missing or invalid. To make this happen, implement the *checkConfigFE()* method in your service provider:

```php
public function checkConfigFE( array $attributes ) : array
{
    return $this->checkConfig( $this->feconfig, $attributes );
}
```

It will receive an associative list of key/value pairs with the "code" you've used in your definition and the value the customer entered. There's a helper method available that is able to check if the types of the values are the same as defined in your definition, e.g. if the value is an integer number, a date or one of the other supported types. *$this->feconfig* again holds your definitions. You can also do additional checks in this method like a range check to ensure the values are between an upper and lower limit.

After the values have been checked and no invalid data has been found, the values entered by customers into the fields should be stored as service attributes along with the selected delivery or payment option in the basket and afterwards in the order. Implement the *setConfigFE()* method to do this:

```php
public function setConfigFE( \Aimeos\MShop\Order\Item\Base\Service\Iface $orderServiceItem,
    array $attributes ) : \Aimeos\MShop\Order\Item\Base\Service\Iface
{
    $this->setAttributes( $orderServiceItem, $attributes, 'payment' );
}
```

In the example above, all given attributes would be added to the order service item in the basket as payment attributes. Use "delivery" for delivery service items instead. You can also use more specific types than "payment" and "delivery" like "payment/paypalexpress". Up to 32 characters are allowed for the attribute types.

In this method you can also modify the values before storing them. You could encrypt or scramble them for example, add the original value in a different attribute and replace the value of the original key with a scrambled one. The DirectDebit payment provider uses this to show only the last three digits of an account number.

All values can be used later on in the back-end systems but don't have any further effect in the web shop.

!!! note
    *Aimeos* don't offer a payment service provider that stores any credit card data. This was an explicit design decision to prevent credit card theft. Please use a payment gateway instead that processes credit card data in a PCI compliant environment.

If you need to retrieve data from the fields you defined at your feconfig you can use this code at your Payment Provider:

```php
public function process( \Aimeos\MShop\Order\Item\Iface $order,
    array $params = [] ) : \Aimeos\MShop\Order\Item\Iface
{
    $type = \Aimeos\MShop\Order\Item\Base\Service\Base::TYPE_PAYMENT;
    $code = $this->getServiceItem()->getCode(); // code of the service payment

    foreach( $$order->getService( $type, $code )->getAttributes() as $attr ) {
        // $attr->getCode() . ': ' . $attr->getValue();
    }
}
```

The `$code` parameter of *getService()* will return the *Aimeos\MShop\Order\Item\Base\Service\Standard* object the code belongs to. If you leave it out, you will get an array of all order service items of that type which have been added to the order during the checkout process.

## Payment form

Most payment gateways require some values to be posted to their servers like the amount the customer has to pay, the currency and a few other necessary ones. Redirecting the customer to the payment gateways and handing over these values is done after the customer clicked on the "Buy now" button at the end of the checkout process.

In the same way you've defined the front-end configuration, you can specify the form fields of the payment form too. Only the way how to pass them to the front-end is different because they have to be returned as part of a [form helper object](https://github.com/aimeos/aimeos-core/blob/master/src/MShop/Common/Helper/Form/Iface.php) by the *process()* method of your payment service provider. This doesn't apply to delivery service providers!

```php
public function process( \Aimeos\MShop\Order\Item\Iface $order,
    array $params = [) ) : ?\Aimeos\MShop\Common\Helper\Form\Iface
{
    $attr = [];

    foreach( $this->payconfig as $key => $config ) {
        $attr[$key] = new \Aimeos\Base\Criteria\Attribute\Standard( $config );
    }

    $url = $this->getConfigValue( 'payment.url-self' );
    return new \Aimeos\MShop\Common\Item\Helper\Form\Standard( $url, 'POST', $attr, false );
}
```

For example, the [OmniPay service provider](https://github.com/aimeoscom/ai-payments/blob/master/src/MShop/Service/Provider/Payment/OmniPay.php) makes heavy use of this. The *process()* method is a "dual use" method in the sense that it can return the definition of a payment form but also push the data forward to the payment gateway if the gateway uses a API reachable via an URL.

## Admin interface

To support editors when configuring your service provider, you must define the configuration possibilities of your implementation:

```php
private $beconfig = [
    'myprovider.myoption' => [
        'code' => 'myprovider.myoption',
        'internalcode'=> 'myprovider.myoption',
        'label'=> 'My option',
        'type'=> 'string',
        'internaltype'=> 'string',
        'default'=> '',
        'required'=> true,
    ],
];
```

They will be informed about what options are available and which one have to be added before the service provider will work. Similar to the front-end, there's a *getConfigBE()* method that must return the available settings as attribute objects:

```php
public function getConfigBE() : array
{
    $list = parent::getConfigBE();

    foreach( $this->beconfig as $key => $config ) {
        $list[$key] = new \Aimeos\Base\Criteria\Attribute\Standard( $config );
    }

    return $list;
}
```

There are some global back-end configurations available (especially for payment providers) like the URLs for success, failure, cancellation and updating a payment. Therefore, you should call the parent function before you add your own definition to the list (*$this->beconfig* contains your own definition in this example).

In the back-end, the "public" flag has no meaning while the "required" flag enforces a configuration value to be set. The editor is informed after pressing the "Save" button what settings are missing or invalid. The check if that is the case is done by the *checkConfigBE()* method:

```php
public function checkConfigBE( array $attributes ) : array
{
    $errors = parent::checkConfigBE( $attributes );
    return array_merge( $errors, $this->checkConfig( $this->beconfig, $attributes ) );
}
```

The parameter passed is again an associative list of key/value pairs with the "code" you've used in your definition and the value as entered by the editor. You should call its parent method to check the global settings first. Afterwards, you can use the *checkConfig()* method as for the front-end to validate your own settings. Keep in mind that this is only a type check! To check for a specific range or other limits, you have to add that checks in this method yourself.

All settings entered by the editor are added automatically to the configuration array of the service item so there's no need to do anything. In your service provider, the easiest way to access those settings is via the *getConfigValues()* method.

Both, delivery and payment service provider can implement some methods that are used to determine if the service provider is available at all, what it supports and to calculate an additional fee if the provider is used. All methods described here are optional and default implementations exist.

# Error handling

In case of an error, you often want to log an error message:

```php
$this->log( 'Error message' );
```

You can also log the result of an operation if it returns an array or object:

```php
$this->log( ['error' => 'Message', 'details' => [/* ... */]] );
```

If the message or object should be logged as warning or debug message, you can pass the log level as second parameter:

```php
$this->log( 'A warning', \Aimeos\Base\Logger\Iface::WARN );
$this->log( 'Some debug stuff', \Aimeos\Base\Logger\Iface::DEBUG );
```

Most often, you also want to inform the user about the error in the frontend. Then, you should throw an exception:

```php
$this->throw( 'Item not found' );
```

To translate the message automatically to the language of the user, pass the translation domain as second parameter:

```php
$this->throw( 'Item not found', 'mshop' );
```

!!! note
    When adding custom error messages, you have to care yourself about translating them to different languages! Check the pages for adding translations in [Laravel](../../laravel/customize.md#overwrite-translations) and [TYPO3](../../typo3/customize.md#overwrite-translations).

Logging and throwing an exception can be combined too but keep care of the order:

```php
$this->log( 'Error message' )->throw( 'Item not found' );
```

# Most often used

## Show or hide option

By default, all delivery and payment options are displayed to all customers without any restrictions. On the other side, there's often the case that single options are only available in specific countries if you sell worldwide. For this, it's possible to restrict each option via the *isAvailable()* method. What are the criteria for the restriction is totally up to you. The complete basket including everything that was added up to now is available.

```php
public function isAvailable( \Aimeos\MShop\Order\Item\Base\Iface $basket ) : bool
{
    if( $basket->getPrice()->getTotal() > 1000 ) {
        return false;
    }
    return true;
}
```

In the example method above, the delivery or payment option would only be available if the total value of the basket is less or equal than 1000. Above that value, the service option won't be shown to the customer. Usually, the customer address was already added before the delivery and payment methods will be displayed, so you can use those data as well.

!!! tip
    There are already decorators implemented that can hide service options based on the [country](https://github.com/aimeos/aimeos-core/blob/master/src/MShop/Service/Provider/Decorator/Country.php) or the [number of previous orders](https://github.com/aimeos/aimeos-core/blob/master/src/MShop/Service/Provider/Decorator/OrderCheck.php) of the customers.

## Calculate a service fee

For each delivery and payment option, a service fee can be charged. By default, the fixed fee that was associated to the service item by the shop owner is added to the total price of the basket. If you need a variable service fee depending on the value of the basket, you have to overwrite the *calcPrice()* method and calculate the fee value yourself:

```php
public function calcPrice( \Aimeos\MShop\Order\Item\Base\Iface $basket ) : \Aimeos\MShop\Price\Item\Iface
{
    $productTotal = ...; // Sum up the price of all products in $basket
    $manager = \Aimeos\MShop::create( $this->context(), 'price' );

    $price = $manager->create();
    $price->setCosts( '0.10' * $productTotal );

    return $price;
}
```

The example implementation above would add a service fee of 10% based on the total price of all products. You have access to the complete basket including all information that has been added up to now. This usually includes the customer address too, so it's possible to calculate fees based on the country or address of the customer.

This method must return a price item with the service fee set via the *setCosts()* method. If you add the service fee via the *setValue()* method of the price item, the amount will be displayed along with the product prices instead in the service section between the sub-total and the total price!

!!! tip
    There are already decorators implemented that can add percentage based service [costs](https://github.com/aimeos/aimeos-core/blob/master/src/MShop/Service/Provider/Decorator/Costs.php) and [reductions](https://github.com/aimeos/aimeos-core/blob/master/src/MShop/Service/Provider/Decorator/Reduction.php) for all delivery and payment providers.

## Check available methods

Both, delivery and payment service provider can implement optional methods where no useful default implementation is available. Instead, the default implementations will throw an exception that the method isn't supported.

For payment providers these include:

cancel
: Cancel the payment of an order

capture
: Capture payment after authorization

query
: Ask for the current payment status of an order

refund
: Refund the payment

Delivery provider implementations can support:

query
: Ask for the current delivery status of an order


To avoid the need to call the method and catch the exception afterwards, the *isImplemented()* method simplifies the handling in this case. There are `FEAT_*` constants defined for the methods that can be supported in the [delivery class](https://github.com/aimeos/aimeos-core/blob/master/src/MShop/Service/Provider/Delivery/Base.php) and the [payment class](https://github.com/aimeos/aimeos-core/blob/master/src/MShop/Service/Provider/Payment/Base.php). These constants must be fed to the *isImplemented()* method to determine if the feature is supported or not:

```php
public function isImplemented( int $what ) : bool
{
    switch( $what )
    {
        case \Aimeos\MShop\Service\Provider\Payment\Base::FEAT_CAPTURE:
        case \Aimeos\MShop\Service\Provider\Payment\Base::FEAT_REFUND:
            return true;
    }
    return false;
}
```

This method would tell the caller that the *capture()* and *refund()* payment methods are supported while all other optional payment methods (*cancel()* and *query()*) would throw an exception if they are called. For delivery service providers, only *query()* is optional and can be checked.

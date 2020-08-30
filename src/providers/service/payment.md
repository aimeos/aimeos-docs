Handling the customers' payment after ordering is one of the vital tasks of every web shop system. From simply storing payment related data, to sending those data to a payment gateway or redirecting the user to the payment gateway - every kind of payment and payment gateway has its own requirements and interface for processing those payments.

Aimeos offers a powerful interface for integrating all kinds of payments into the web shop. It supports not only immediate payments but also authorization and capturing, cancellation, refunds, querying and updating the payment status synchronously and asynchronously.

Moreover, shop owners can recalculate the total price based on the used payment method or limit the payment options depending on the address of the customer or other criteria.

!!! tip
    Before thinking about implementing an Aimeos specific payment provider, please have a look at the [Omnipay payment library](https://omnipay.thephpleague.com/) if it already supports the payment gateway you need. If not, try to implement a new Omnipay gateway. You can use these gateways by adding the [Aimeos ai-payments extension](https://github.com/aimeoscom/ai-payments) to your shop. Only if you need features that are not supported by Omnipay (like batch status updates), you must create your own Aimeos payment provider.

# Basic skeleton

The skeleton for the most basic implementation of a payment service provider would be:

```php
namespace Aimeos\MShop\Service\Provider\Payment;

class Myprovider
    extends \Aimeos\MShop\Service\Provider\Payment\Base
    implements \Aimeos\MShop\Service\Provider\Payment\Iface
{
    /**
     * Tries to get an authorization or captures the money immediately for the given
     * order if capturing isn't supported or not configured by the shop owner.
     *
     * @param \Aimeos\MShop\Order\Item\Iface $order Order invoice object
     * @param array $params Request parameter if available
     * @return \Aimeos\MShop\Common\Helper\Form\Standard Form object with URL, action
     *  and parameters to redirect to    (e.g. to an external server of the payment
     *  provider or to a local success page)
     */
    public function process( \Aimeos\MShop\Order\Item\Iface $order, array $params = [] )
    {
        // perform your actions
        return parent::process( $order, $params );
    }
}
```

You should implement the *process()* method so your payment service provider does something useful even if a default implementation exists that redirects the customer to the confirmation page.

If you need some configuration values set by the shop owner like the remote payment gateway, there's a section for [adding and checking settings](index.md#configuration). You should also have a look into the [support methods](index.md) to fully understand the example code below.

Payment service providers also [share some methods](index.md#most-often-used) with delivery service providers. They allow you to control the visibility of the payment options, calculate variable service fees and check if certain methods are implemented.

# Process the payment

The main method of every payment service provider is the *process()* method and it should be implemented so the provider can perform anything useful. There's a default implementation available but that only redirects the customer to the confirmation page, so the payment status will remain "unfinished".

The method will be called during the checkout process after the customer clicked on "Buy now" by the "process" subpart of the checkout component. There you can either display a payment form to collect the payment information from the customer, redirect the customer to the payment gateway or use the API of the payment gateway to execute the payment directly.

The first example lists the steps to use a direct API call to a remote server for executing the payment. When *process()* is called, the order item of the order that should be processed is passed as argument. It can be used to retrieve the rest of the order data and to update the payment status afterwards:

```php
public function process( \Aimeos\MShop\Order\Item\Iface $order, array $params = [] )
{
    $basket = $this->getOrderBase( $order->getBaseId() );
    $total = $basket->getPrice()->getValue() + $basket->getPrice()->getCosts();

    // send the payment details to an external payment gateway

    $status = \Aimeos\MShop\Order\Item\Base::PAY_RECEIVED;
    $order->setPaymentStatus( $status );
    $this->saveOrder( $order );

    return parent::process( $order, $params );
}
```

In the first line, the [basic order information](index.md#retrieve-complete-order) is fetched from the database. It contains the price details and the currency, which is required by almost all payment gateways.

In this example, you would use the API of the payment gateways to execute the payment directly and get an immediate response back from the gateway. Afterwards, you must update the payment status and [persist the change](index.md#save-order-items) in the database. This will automatically log the status change in the *mshop_order_status* table.

The call to the parent *process()* method will return the [form helper object](https://github.com/aimeos/aimeos-core/blob/master/lib/mshoplib/src/MShop/Common/Helper/Form/Iface.php) to redirect the customer to the confirmation page.


There are several [payment status values](https://github.com/aimeos/aimeos-core/blob/master/lib/mshoplib/src/MShop/Order/Item/Base.php) available:

PAY_UNFINISHED
: The default status when nothing has happend

PAY_DELETED
: The payment for the order was deleted manually

PAY_CANCELED
: The payment was canceled by the customer

PAY_REFUSED
: The payment gateway declined the customers' payment attempt

PAY_REFUND
: The payment was refunded after it was successfully captured

PAY_PENDING
: The payment is currently pending and a new status will be received later

PAY_AUTHORIZED
: The payment was authorized but not yet captured

PAY_RECEIVED
: The payment has been received and was added to the account of the shop owner

Instead of an API call, you can also redirect the customer directly to the payment gateway and hand over the required data via GET or POST:

```php
public function process( \Aimeos\MShop\Order\Item\Iface $order, array $params = [] )
{
    $basket = $this->getOrderBase( $order->getBaseId() );
    $total = $basket->getPrice()->getValue() + $basket->getPrice()->getCosts();

    // define the payment information that should be sent to the external payment gateway
    $list = [
        'myprovider.orderid' => new \Aimeos\MW\Criteria\Attribute\Standard( [
            'label' => 'Order ID',
            'code' => 'myprovider.orderid',
            'internalcode' => 'x_ref',
            'internaltype' => 'string',
            'type' => 'string',
            'default' => $order->getId(),
            'public' => false,
        ] ),
        'myprovider.total' => new \Aimeos\MW\Criteria\Attribute\Standard( [
            'label' => 'Total value',
            'code' => 'myprovider.total',
            'internalcode' => 'x_total',
            'internaltype' => 'float',
            'type' => 'float',
            'default' => $total,
            'public' => false,
        ] ),
    ];

    $gatewayUrl = $this->getConfigValue( 'myprovider.url', 'https://gateway.com' );
    return new \Aimeos\MShop\Common\Helper\Form\Standard( $gatewayUrl, 'POST', $list );
}
```

This example would generate a form in the checkout process with two hidden input fields (because "public" is false) that contain the order ID and the total value named as the payment gateway expects them ("x_ref" and "x_total").

As soon as the customer clicks on "Proceed", the form values will be posted to the payment gateway given in the first parameter of the form helper. For more details about generating the payment form, please have a look into the article about [configurations](index.md#payment-form).

If you redirect the customers to the payment provider where they can enter their payment data (like credit card details), the payment providers need to redirect the customers back to your web site. When supported, you can hand over two URLs to the payment provider:

payment.url-success
: URL to the thank you page (also for failed payments but a suitable text will be displayed instead)

payment.url-update
: Page where the checkout update component is placed and waits for asynchronous notifications from the payment provider

You can retrieve these URLs using:

```php
$url = $this->getConfigValue( 'payment.url-success' );
$url = $this->getConfigValue( 'payment.url-update' );
```

The last way the *process()* method could be implemented is to collect the payment data locally. Therefore, you have to generate a form first and retrieve the data entered by the customer afterwards. In this case, the "params" argument will contain the GET/POST parameters that have been posted:

```php
public function process( \Aimeos\MShop\Order\Item\Iface $order, array $params = [] )
{
    if( !isset( $params['myprovider.accountno'] ) || $params['myprovider.accountno'] * )
    {
        // define the form to collect the payment data from the customer
        $list = [
            'myprovider.accountno' => new \Aimeos\MW\Criteria\Attribute\Standard( [
                'label' => 'Account number',
                'code' => 'myprovider.accountno',
                'internalcode' => 'myprovider.accountno',
                'internaltype' => 'string',
                'type' => 'string',
                'default' => *,
                'public' => true,
            ] ),
        ];

        $selfUrl = $this->getConfigValue( 'payment.url-self' );
        return new \Aimeos\MShop\Common\Helper\Form\Standard( $selfUrl, 'POST', $list );
    }

    $type = \Aimeos\MShop\Order\Item\Base\Service\Base::TYPE_PAYMENT;
    $baseItem = $this->getOrderBase( $order->getBaseId() );
    $orderServiceItem = $baseItem->getService( $type );

    $this->setAttributes( $orderServiceItem, $params, 'myprovider' );
    $this->saveOrderBase( $baseItem );

    return parent::process( $order, $params );
}
```

If there's no parameter named "myprovider.accountno" available, a form will be generated and returned as [form helper object](https://github.com/aimeos/aimeos-core/blob/master/lib/mshoplib/src/MShop/Common/Helper/Form/Iface.php).

After the customers entered their data, the information will be posted to the same page ("payment.url-self"), so the *process()* method of your payment service provider will be called again, now with the entered value passed in the "params" argument. This value or values can be saved as attribute along with the payment service data in the order.

!!! tip
You can also combine the different ways shown, e.g. collect the payment data locally like in the last example but sent it via API call to a remote server.

# Status updates

## Direct update

Many payment gateways collect the payment related data on their server, process the payment and redirect the customer to the shop afterwards. Within this redirect, they usually send the payment status as GET or POST parameter, so the payment service provider can update the order status immediately. Thus, customers see if their payment and order was accepted on the confirmation page.

These status updates sent directly within the redirect are handled by the *updateSync()* method. In the payment service provider, all data (GET/POST parameters as well as the request body) from the payment gateway is available in the [PSR-7 request object](https://www.php-fig.org/psr/psr-7/) passed to the method. Furthermore, the second argument is the order item representing the invoice of the order which contains the current payment status.

```php
public function updateSync( \Psr\Http\Message\ServerRequestInterface $request, \Aimeos\MShop\Order\Item\Iface $order )
{
    // extract status from the request
    // map the status value to one of the Aimeos payment status values

    $order->setPaymentStatus( $status );
    $this->saveOrder( $order );

    return $order;
}
```

You need to extract the status value either from the given GET/POST parameters or from the request body. The way to extract this information totally depends on the external system sending the request.

Based on this data, you can map the status value sent by the payment gateway to one of the [Aimeos payment status values](https://github.com/aimeos/aimeos-core/blob/master/lib/mshoplib/src/MShop/Order/Item/Base.php) also used in the *process()* method and [save the modified order](index.md#save-order-items) back to the database afterwards.

## Push update

It's desirable to keep the payment status in the shop up to date to have one central, authoritative system, even if the handling is done by external systems. Therefore, those external systems must be able to update the payment status of orders in the shop system and the *updatePush()* method of payment providers accepts those status updates.

To be more precise, status updates sent synchronously via HTTP(S) are accepted by the *updatePush()* method. For updates sent via [asynchronous batch file transfers](#batch-update), use the *updateAsync()* method instead.

The *updatePush()* method is called by the application as soon as a status update request via HTTP(S) arrives. This happen on the update page which accepts asynchronous update notifications sent by the payment gateways later on. The sent GET/POST parameters as well as the request body are available in the [PSR-7 request object](https://www.php-fig.org/psr/psr-7/):

```php
public function updatePush( \Psr\Http\Message\ServerRequestInterface $request, \Psr\Http\Message\ResponseInterface $response )
{
    // extract the order ID and latest status from the request
    $order = $this->getOrder( $orderid );
    // map the status value to one of the Aimeos payment status values

    $order->setPaymentStatus( $status );
    $this->saveOrder( $order );

    return $response;
}
```

First, you need to retrieve the order ID and the corresponding status value either from the given GET/POST parameters or from the request body. The way to extract this information totally depends on the external system sending the request.

Based on this data, you can retrieve the order item from the database, map the status value sent by the payment gateway to one of the [Aimeos payment status values](https://github.com/aimeos/aimeos-core/blob/master/lib/mshoplib/src/MShop/Order/Item/Base.php) also used in the *process()* method and [save the modified order](index.md#save-order-items) back to the database afterwards.

If the payment gateway needs more or a different acknowledgement then a HTTP status 200, then you can add any valid HTTP header and an appropriate response body to the *$response* parameter. The content of the response body can totally depend on what the external system expects and can be any string, XML or whatever format.

## Batch update

Keeping the payment status of each order up to date can not only be done [[#Update_status|via HTTP(S) by using the *updateSync()* method]] but also asynchronously via batch file transfer or similar methods. In this case, you have to implement the *updateAsync()* method instead.

The *updateAsync()* method is called regularly by a job controller. Thus, there are no parameters passed to this method and your service provider needs to know where to look after the batch files. The information could be available in the [configuration](index.md#configuration) added by the shop owner when setting up the service option/provider.

```php
public function updateAsync()
{
    // extract the order IDs and latest status values from the file

    foreach( $entries as $orderid => $status )
    {
        // map the status value to one of the Aimeos payment status values

        $order = $this->getOrder( $orderid );
        $order->setPaymentStatus( $status );
        $this->saveOrder( $order );
    }
}
```

As batch files usually contain several updates at once, e.g. one at each line, extracting the list, looping over the entries and retrieving/updating each order item is a regular task. Also, you need to map the status value sent by the external system to one of the [Aimeos payment status values](https://github.com/aimeos/aimeos-core/blob/master/lib/mshoplib/src/MShop/Order/Item/Base.php) and [save the modified order](#index.md#save-order-items) back to the database.

!!! tip
    If your batch file contains some kind of CSV data, the easiest way to extract those data is by using the [container/content utility classes](../../infrastructure/read-write-files.md).

# Optional methods

The methods described in this section are optional methods where no useful default implementation exists and an exception is thrown when called nevertheless.

## Query current status

To enable querying the current payment status, you have to implement the *query()* method in your payment service provider. If it exists, the *query()* method should ask its payment gateway for the actual status of the order passed as argument to the method and update the payment status of that order accordingly:

```php
public function query( \Aimeos\MShop\Order\Item\Iface $order )
{
    $orderid = $order->getId();
    // ask the external service for the current payment status for the given order

    $order->setPaymentStatus( $status );
    $this->saveOrder( $order );
}
```

The available [payment status values](https://github.com/aimeos/aimeos-core/blob/master/lib/mshoplib/src/MShop/Order/Item/Base.php) are the same as described in the *process()* method and you have to save the order item too for persisting the [changed order item data](index.md#save-order-items) in the storage.

As the *query()* method isn't available by default, you have to tell the application using the service provider that your implementation supports it. Thus, you have to [overwrite the *isImplemented()* method](index.md#check-available-methods) and return true for the query feature:

```php
public function isImplemented( $what )
{
    switch( $what )
    {
        case \Aimeos\MShop\Service\Provider\Payment\Base::FEAT_QUERY:
            return true;
    }
    return false;
}
```

This example implementation will tell the application that the query feature is available and the *query()* method can be called without throwing an exception because its not implemented.

## Capture the money

If the payment gateway supports getting an authorization for the payment first (a reservation of the money) and your payment service provider allows to configure this, you must implement the *capture()* method as well to receive the money afterwards.

If the method exists, it should tell the payment gateway to capture the money for the order passed as argument to the method and update the payment status of that order accordingly:


```php
public function capture( \Aimeos\MShop\Order\Item\Iface $order )
{
    $orderid = $order->getId();
    // ask the payment gateway to capture the money for the given order

    $status = \Aimeos\MShop\Order\Item\Base::PAY_RECEIVED;
    $order->setPaymentStatus( $status );
    $this->saveOrder( $order );
}
```


Use the "PAY_RECEIVED" payment status after capturing the money and save the order item to [store the changed payment status](index.md#save-order-items) in the database. If an error occurs, leave the current payment status as is.

As the *capture()* method isn't available by default, you have to tell the application using the service provider that your implementation supports it. Thus, you have to [overwrite the *isImplemented()* method](index.md#check-available-methods) and return true for the capture feature:

```php
public function isImplemented( $what )
{
    switch( $what )
    {
        case \Aimeos\MShop\Service\Provider\Payment\Base::FEAT_CAPTURE:
            return true;
    }
    return false;
}
```

This example implementation will tell the application that the capture feature is available and the *capture()* method can be called without throwing an exception because the method isn't implemented.

## Cancel the payment

If the payment gateway supports cancellations, you should implement the *cancel()* method. If the method exists, it should ask the payment gateway to cancel the payment for the order passed as argument to the method if possible and update the payment status of the order accordingly:

```php
public function cancel( \Aimeos\MShop\Order\Item\Iface $order )
{
    $orderid = $order->getId();
    // ask the payment gateway to cancel the payment for the given order

    $status = \Aimeos\MShop\Order\Item\Base::PAY_DELETED;
    $order->setPaymentStatus( $status );
    $this->saveOrder( $order );
}
```

Use the "PAY_DELETED" payment status after canceling the payment and save the order item to [persist the payment status](index.md#save-order-items) in the storage. If an error occurs, leave the current payment status as is.

!!! warning
    For canceled payment you should set the payment status "PAY_DELETED" and NOT "PAY_CANCELED" because the later one is for situations when the customers cancel the payment themselves while being at the payment gateway site.

As the *cancel()* method isn't available by default, you have to tell the application using the service provider that your implementation supports it. Thus, you must [overwrite the *isImplemented()* method](index.md#check-available-methods) and return true for the cancel feature:

```php
public function isImplemented( $what )
{
    switch( $what )
    {
        case \Aimeos\MShop\Service\Provider\Payment\Base::FEAT_CANCEL:
            return true;
    }
    return false;
}
```

This example implementation will tell the application that the capture feature is available and the *cancel()* method can be called without throwing an exception because the method isn't implemented.

## Refund the money

If the payment gateway supports refunding payments, you should implement the *refund()* method. If the method exists, it should ask the payment gateway to refund the complete payment for the order passed as argument to the method and update the payment status of the order accordingly:

```php
public function refund( \Aimeos\MShop\Order\Item\Iface $order )
{
    $orderid = $order->getId();
    // ask the payment gateway to refund the complete payment for the given order

    $status = \Aimeos\MShop\Order\Item\Base::PAY_REFUND;
    $order->setPaymentStatus( $status );
    $this->saveOrder( $order );
}
```

Use the "PAY_REFUND" payment status after refunding the payment and save the order item to [store the payment status](index.md#save-order-items) in the database. If an error occurs, leave the current payment status as is.

As the *refund()* method isn't available by default, you have to tell the application using the service provider that your implementation supports it. Thus, you have to [overwrite the *isImplemented()* method](index.md#check-available-methods) and return true for the refund feature:


```php
public function isImplemented( $what )
{
    switch( $what )
    {
        case \Aimeos\MShop\Service\Provider\Payment\Base::FEAT_REFUND:
            return true;
    }
    return false;
}
```


This example implementation will tell the application that the refund feature is available and the *refund()* method can be called without throwing an exception because the method isn't implemented.

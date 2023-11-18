Regarding deliveries, shop owners are usually offering several delivery methods a customer can choose from but the shop owners also need to make sure that the orders are pushed to their back-end systems. Both is possible with delivery service providers which are the base for the configured delivery methods.

A delivery method can be anything like delivering by courier service, mail, DHL, UPS or any other transportation company. What's displayed in the list of delivery methods the customers can select from is independent of the implementation of the delivery service provider underneath. This means that you can name the delivery method in the checkout process "Express delivery" but the configured delivery service provider class behind is "Manual" which only implies the orders will be exported from the shop database by hand.

Depending on the delivery service provider implementation, it may send the orders in the required format to the ERP system of the shop owner or to a fulfillment company in a format understood by them. As sending orders is an asynchronous process started regularly in the background, it doesn't depend on any action of the customers besides their successful payment.

Also the format is totally up to the other side: It can be CSV, XML or any other format you implement and delivered via HTTP, batch file transfer or another arbitrary protocol.

Examples of imaginable delivery configurations could be:

* Delivery by mail, manual order export from the shop
* Delivery by a courier service, order sent automatically to the ERP system of the shop owner
* Delivery by a parcel service, orders sent automatically to an Amazon logistic center

# Basic skeleton

The location of your new delivery service provider must be:

```
./<yourext>/src/MShop/Service/Provider/Delivery/<classname>.php
```

The skeleton for the most basic implementation of a delivery service provider would be:

```php
namespace Aimeos\MShop\Service\Provider\Delivery;

class Myprovider
    extends \Aimeos\MShop\Service\Provider\Delivery\Base
    implements \Aimeos\MShop\Service\Provider\Delivery\Iface
{
    /**
     * Sends the order details to the ERP system for further processing.
     *
     * @param \Aimeos\MShop\Order\Item\Iface $order Order invoice object to process
     */
    public function push( iterable $orders ) : \Aimeos\Map
    {
        return map( $orders );
    }
}
```

The only method that must be implemented is the *push()* method that will be called regularly by the job controller for exporting the orders. Anything else is optional. How to access configuration or which supporting methods are available is described in the [basics article](index.md).

Delivery service providers also [share some methods](index.md#most-often-used) with payment service providers. They allow you to control the visibility of the delivery options, calculate variable service fees and check if certain methods are implemented.

# Process an order

The main methods of every delivery service provider are the *processBatch()* and *push()* methods, and they must be implemented so the provider can perform anything useful.

The *processBatch()* method will be called by the job controller regularly for all orders that have been paid (or at least where the payment have been authorized) and should be sent to the next step. This can contain exporting the order to a file, pushing it to the ERP system or forwarding it to the fulfillment company.

When called, the item(s) of the orders that should be processed are passed as argument. It can be used to retrieve the rest of the order data and to update the delivery status afterwards:

```php
public function push( iterable $orders ) : \Aimeos\Map
{
    // send the order details to an external system

    $status = \Aimeos\MShop\Order\Item\Base::STAT_PROGRESS;
    return map( $orders )->setStatusDelivery( $status );
}
```

In the first line you can add your own implementation to send all details to the system that will care about the next steps.

Afterwards, you should update the order status so the order won't be passed again to the *push()* method and persist the change in the database. This will automatically log the status change in the *mshop_order_status* table.

There are several [delivery status values](https://github.com/aimeos/aimeos-core/blob/master/src/MShop/Order/Item/Base.php) available:

STAT_UNFINISHED
: Delivery is open and waiting for manual action

STAT_DELETED
: The delivery of the order was canceled manually

STAT_PENDING
: The delivery is currently pending

STAT_PROGRESS
: Delivery is in progress, e.g. sent to the next system

STAT_DISPATCHED
: The parcel was handed over to the transportation company

STAT_DELIVERED
: The transportation company has delivered the parcel to the customer

STAT_REFUSED
: The parcel was lost by the transportation company

STAT_RETURNED
: The parcel was returned either by the customer or the transportation company

Most of the time, *STAT_PROGRESS* is the best option after the pushing the order to the next system. The other status values are mainly used if external systems report back the actual status of the delivery to keep the orders in the shop database up to date.

# Notification status updates

It's desirable to keep the delivery status in the shop up to date to have one central, authoritative system, even if the handling is done by external systems. Therefore, those external systems must be able to update the delivery status of orders in the shop system and the *updatePush()* method of delivery providers accepts those status updates.

To be more precise, status updates sent synchronously via HTTP(S) are accepted by the *updatePush()* method. For updates sent via [asynchronous batch file transfers](#batch-updates), use the *updateAsync()* method instead.

The *updatePush()* method is called by the application as soon as a status update request via HTTP(S) arrives. The sent GET/POST parameters as well as the request body are available in the [PSR-7 request](https://www.php-fig.org/psr/psr-7/) object:

```php
public function updatePush( \Psr\Http\Message\ServerRequestInterface $request,
    \Psr\Http\Message\ResponseInterface $response ) : \Psr\Http\Message\ResponseInterface
{
    // extract the order ID and latest status from the request
    $order = \Aimeos\MShop::create( $this->context(), 'order' )->get( $orderid );
    // map the status value to one of the Aimeos delivery status values

    $order->setStatusDelivery( $status );
    $this->save( $order );

    return $response;
}
```

**Note**: The URL forwarding requests to `updatePush()` depends on the host system and your configuration. For Laravel its `https://<domain>/update` and for TYPO3 `https://<domain>/shop/update` by default. As a minimum the parameter `code` must be passed as GET or POST parameter with the code value of your provider as set in the Service panel of the admin backend.

First, you need to retrieve the order ID and the corresponding status value either from the given GET/POST parameters or from the request body. The way to extract this information totally depends on the external system sending the request.

Based on this data, you can retrieve the order item from the database, map the status value sent by the external system to one of the [Aimeos delivery status values](https://github.com/aimeos/aimeos-core/blob/master/src/MShop/Order/Item/Base.php) also used in the *push()* method and save the modified order back to the database afterwards.

If the external system needs more or a different acknowledgement then a HTTP status 200, then you can add any valid HTTP header and an appropriate response body to the `$response` argument. The content of the response body can totally depend on what the external system expects and can be any string, XML or whatever format.

!!! tip
    It's not necessary to send only one order status update after another to the *updatePush()* method. The external system can also push bunches of status updates at once to the shop system. Your service provider only needs to loop over the list of data and update each order accordingly.

# Batch status updates

Keeping the delivery status of each order up to date can not only be done via HTTP(S) by using the [*updatePush()* method](#update-status) but also asynchronously via batch file transfer or similar methods. In this case, you have to implement the *updateAsync()* method instead.

The *updateAsync()* method is called regularly by a job controller. Thus, there are no parameters passed to this method and your service provider needs to know where to look after the batch files. The information could be available in the configuration added by the shop owner when setting up the service option/provider.

```php
public function updateAsync() : bool
{
    $manager = \Aimeos\MShop::create( $this->context(), 'order' );

    // extract the order IDs and latest status values from the file

    foreach( $entries as $orderid => $status )
    {
        // map the status value to one of the Aimeos delivery status values

        $order = $manager->get( $orderid );
        $order->setStatusDelivery( $status );
        $this->save( $order );
    }

    return true;
}
```

As batch files usually contain several updates at once, e.g. one at each line, extracting the list, looping over the entries and retrieving/updating each order item is a regular task. Also, you need to map the status value sent by the external system to one of the [Aimeos delivery status values](https://github.com/aimeos/aimeos-core/blob/master/src/MShop/Order/Item/Base.php) used in the *push()* method too and save the modified order back to the database afterwards.

# Query current status

To enable querying the current delivery status, you have to implement the *query()* method in your delivery service provider. This method is one of the optional methods where no default implementation exists and an exception is thrown when called nevertheless.

If it exists, the *query()* method should ask its remote service for the actual delivery status of the order, which is passed as an argument to the method, and update the delivery status of the order accordingly:

```php
public function query( \Aimeos\MShop\Order\Item\Iface $order ) : \Aimeos\MShop\Order\Item\Iface
{
    $orderid = $order->getId();
    // ask the external service for the current delivery status for the given order

    $status = \Aimeos\MShop\Order\Item\Base::STAT_DISPATCHED;
    $order->setStatusDelivery( $status );
    $this->save( $order );

    return $order;
}
```

The available [delivery status values](https://github.com/aimeos/aimeos-core/blob/master/src/MShop/Order/Item/Base.php) are the same as described in the *push()* method and you have to save the order item too for persisting the changed order item data in the storage.


As the *query()* method isn't available by default, you have to tell the application using the service provider that your implementation supports it. Thus, you have to [index.md#check-available-methods|overwrite the *isImplemented()* method]] as well and return true for the query feature:


```php
public function isImplemented( int $what ) : bool
{
    switch( $what )
    {
        case \Aimeos\MShop\Service\Provider\Delivery\Base::FEAT_QUERY:
            return true;
    }
    return false;
}
```


This example implementation will tell the application that the query feature is available and the *query()* method can be called without throwing an exception immediately.

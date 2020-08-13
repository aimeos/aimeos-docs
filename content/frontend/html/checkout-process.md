The checkout process is one of the hearts of a web shop. Aimeos contains a full-featured checkout component that can be customized to very wide degree. The illustration below contains the complete checkout process including payment and asynchronous payment notifications if they are used:

![Checkout process](Checkout-process.png)

* Checkout
    1. Enter billing (and delivery) address
    2. Choose delivery option
    3. Choose payment option
    4. Show detailed summary page
    5. Start order process
* Confirmation
    1. Show order confirmation or enable retry
* Update notification
    1. Receive payment status updates

# Checkout steps

All steps are implemented as subparts of the "checkout standard" component. The difference between this component and others is that only the subpart is shown that matches the step in the URL parameter or the first one that requires attention if the page is called without parameter.

Moving through the steps is done by instantiating all subparts, calling their `process()` methods and the one that requires some input will set the *standardStepActive* view variable to its own subpart name. This subpart is rendered afterwards and the [process() method of the address subpart](https://github.com/aimeos/ai-client-html/blob/master/client/html/src/Client/Html/Checkout/Standard/Address/Standard.php) is a good place to see how this works.

If a customer is already logged in and the [Autofill basket plug-in](../../manual/plugins.md#autofill) is configured, then the address data as well as the chosen delivery and payment options are used from the last order. The steps that doesn't require any input are skipped and the [configured destination page](../../config/client-html/checkout-standard.md#step-active) (the summary page by default) is displayed directly to the customer.

# Payment processing

Afterwards, the order is stored in the database and the product stock and coupon code(s) are blocked (their count is decreased). If the payment fails or the customer leaves the shop before completing the order, the order stays in the database and products and coupon codes won't be available for other customers.

!!! tip
     There's a job controller ("Remove unpaid orders") available for unblock reserved stock and coupon codes of unpaid orders after a configurable amount of time. Also, unfinished orders can be deleted safely after some time using the "Remove unfinished orders" job controller.

A new delivery address is also saved in the customer address table. To prevent this, you have to remove the "address" subpart from the [process subparts configuration](../../config/client-html/checkout-standard.md#standardsubparts_3). This applies also to creating a new customer account based on the e-mail address.

If the customer has chosen a payment provider which requires no redirect to an external payment gateway (like pre-payments), the customer is directly forwarded to the order confirmation page which must contain the "checkout confirm" component.

Otherwise, a form is shown which asks for the required data like credit card information. Submitting the form (done automatically if no further data is required and Javascript is available) will forward the customer to the payment gateway where acquiring the payment takes place.

The payment gateway must redirect the customer back to the confirmation page afterwards to complete the order. Additionally, it's possible to accept order status updates via the "checkout update" component sent by the payment gateway later on.

# Confirmation page

The "checkout confirm" component displays the placed order and the current payment status of that order.

If possible, it updates the payment status depending on the parameters sent by the payment gateways or queries the payment provider for the current status. It asks each configured payment provider for the current shop site to update the payment status until one of them succeeds.

Thus, and for usability reasons it's best to place the most commonly used [payment option](../../manual/services.md#built-in-payment-services) at the top of the list of payment options using a low number (or zero) for the [position value](../../manual/service-details.md#basic-details).

Sometimes, payments of customers are declined by the payment provider or the payment fails for other reasons. In this case, the buttons for retrying the payment are displayed. The customer can use the same payment option or choosing another one.

# Update notifications

The payment status of an order can change due to external reasons like the payment was pending first and succeeds afterwards or it was declined by the credit card provider. It's important for a shop to get notified about these changes. For example, Aimeos shops hold back orders as long as their payment is neither "authorized" nor "received".

The notifications about payment status updates can happen every time and are therefore not bound to any direct customer action. Instead, the payment provider gateways may send them as soon as they occur or maybe only once a day. Thus, they are distinguished into two types:

* real-time/synchronous update
* batch/asynchronous updates

All real-time updates are sent directly to the "checkout update" component of your Aimeos shop. Some payment service provider implementations are able to hand over the URL created by using the [configured destination page or route](../../config/client-html/checkout-update.md#url) automatically to the payment gateway. In the other cases, you need to add the absolute URL to your page containing the "checkout update" component in the management backend of the payment gateway.

Batch updates work in a different way. Usually, files are uploaded via FTP to your server or you have to fetch the files from the server of your payment gateway. Afterwards, the Aimeos service provider can import the file and updated the payment status of the order in the database.

You have to configure the Aimeos  payment service provider which is responsible for these files to import them. This is explicitly stated in the [service provider documentation](../../manual/services.md#built-in-payment-services) if necessary.

!!! note
    If one of the payment provider you are using sends batched payment status updates, you have to set up the "Batch update of payment/delivery status" job for processing those files

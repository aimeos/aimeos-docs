The service panel is dedicated to the delivery and payment options that should be available during the checkout process. A service item configures the delivery or payment provider which are responsible for the further handling of the order (i.e. the payment).

The list view provides a paged list of all available delivery and payment options in the system, which can be [filtered](filtering-lists.md) by various criteria. The most important columns are shown by default but the list of columns can be adapted via the list header. Delivery and payment options can be added, edited or deleted using the buttons in the list. A click on the entry also opens the detail view for editing the delivery or payment item.

![List of delivery/payment options](Admin-backend-service-list.png)

# Services explained

## Delivery

During the checkout process, the customer might be able to choose between several delivery options (e.g. UPS, TNT, etc.) if they are made available by the shop owner. Each delivery option can have its own description, picture, and price. You can add as many delivery options as you like.

Every delivery option needs a delivery provider configured with the necessary parameter. A delivery provider implements the handling of the order after the payment was successful. This can be either a completely manual handling, a transfer of the order to the logistic partner, or an automated process for providing a customized download file to the customer. Everything that can be implemented in an algorithm is possible within a provider.

## Payment

Just as shop customers can select one of many delivery options, customers can select one of several payment options, but only if provided by the shop owner. Payment options can also have their own description, picture, and price.

For each payment option there must also be a configured payment provider to take care of the payment. There are two different payment processes: Local and remote payments. A local payment process collects the required payment data (if any additional data is necessary) and stores it locally in the shop system. Alternatively, a remote payment provider redirects the customer to a payment gateway, which handles the payment and notifies the shop system about the result of the payment process (usually success or failure).

Extensions implementing payment providers are available, especially those using payment gateways to handle payments of customers.

!!! note
    Please don't use any payment provider that stores credit card details locally in the shop system as long as you aren't certified as PCI-compliant. For more information take a look at the website of the [PCI Security Standards Council](https://www.pcisecuritystandards.org/).


# Built-in delivery services

## Standard

Completely manual handling of orders without any notifications. It only sets the status of the order to "in progress". This service requires no further configuration.

## Xml

XML based transfer of orders to a web service understanding the content of the XML.

xml.backupdir (optional)
: Relative or absolute path of the backup directory (with strftime() placeholders)

xml.exportpath (required)
: Relative or absolute path and name of the XML files (with strftime() placeholders)

xml.template (optional)
: Relative path of the template file name

xml.updatedir (optional)
: Relative or absolute path and name of the order update XML files


# Built-in payment services

## DirectDebit

If you want to offer payments via an automatic bank transfer from the bank account of the customer, you should configure the **DirectDebit** payment service provider. The customer is asked for the necessary details like bank name, bank account, etc. which are stored along with the order in your database. This service doesn't have any options.

## PayPalExpress

Payments via PalPal are available by the **PayPalExpress** payment service provider. It provides all possibilities PayPal is offering. The required configuration options are:

paypalexpress.AccountEmail
: The e-mail address of the account that will receive the money, usually the one you've used for registration

paypalexpress.ApiUsername
: User name of the account that should be used for the automatic communication with the shop. This is not the name of your own user account!

paypalexpress.ApiPassword
: The password you have assigned the the API user name. This is not the password of your own user account!

paypalexpress.ApiSignature
: The shared secret that is created by PayPal for the API user

## PrePay

The **PrePay** provider is used for payments that must be done in advance and before the delivery of the ordered products is started, like a bank transfer in advance. This service doesn't have any options.

## PostPay

The **PostPay** provider is useful for all payments where the customers pay after placing their order. This allows payment by invoice or payment by cash on delivery. This service doesn't have any options.


# Supported by ai-payments

Service providers for many payment gateways are available by the Aimeos [ai-payments extension](https://github.com/aimeoscom/ai-payments). This includes:


## Authorize.net AIM

The [Authorize.net](https://www.authorize.net/) gateway for the [AIM method](http://www.authorize.net/support/AIM_guide.pdf) (collect payment details locally and send them to the payment gateway) is available via the **AuthorizeAIM** payment service provider since 2015.07.

```
composer req "omnipay/authorizenet:~3.0"
```

It supports authorization/capture and offers these configuration options:

apiLoginId (string, required)
: The API login ID from your Authorize.net account

transactionKey (string, required)
: The transaction key generated for your Authorize.net account

authorizenet.address (boolean, optional)
: A value of "1" will send the customer address to Authorize.net

authorizenet.authorize (boolean, optional)
: Use "1" if you want to get an authorization first and capture the payment after the parcel has been dispatched or the product delivered according to the delivery status of the order. Leave this setting out for immediate payments

testMode (boolean, optional)
: Use "1" for test payments without real money


## Authorize.net SIM

The [Authorize.net](https://www.authorize.net/) gateway for the [SIM method](http://www.authorize.net/support/SIM_guide.pdf) (collect payment details at the payment gateway site) is available via the **AuthorizeSIM** payment service provider since 2015.07.

```
composer req "omnipay/authorizenet:~3.0"
```

It supports authorization/capture and offers these configuration options:

apiLoginId (string, required)
: The API login ID from your Authorize.net account

transactionKey (string, required)
: The transaction key generated for your Authorize.net account

hashSecret (string, optional)
: A secret string you've entered in your Authorize.net account that offers additional protection for payment status notifications

authorizenet.address (boolean, optional)
: A value of "1" will send the customer address to Authorize.net

authorizenet.authorize (boolean, optional)
: Use "1" if you want to get an authorization first and capture the payment after the parcel has been dispatched or the product delivered according to the delivery status of the order. Leave this setting out for immediate payments

authorizenet.header (string, optional)
: The HTTP header sent by the checkout update component after updating the order successfully ("Location: <URL to confirm page>" by default)

authorizenet.body (string, optional)
: The HTTP body sent by the checkout update component after updating the order successfully ("success" by default). This could be a complete HTML page too that is shown to the customer and offering a link to the confirm page (authorizenet.header must be a empty value in this case)

testMode (boolean, optional)
: Use "1" for test payments without real money


## Authorize.net DPM

The [Authorize.net](https://www.authorize.net/) gateway for the [DPM method](http://www.authorize.net/support/SIM_guide.pdf) (collect payment details locally but pass them to the payment gateway directly) is available via the **AuthorizeDPM** payment service provider since 2015.07.

```
composer req "omnipay/authorizenet:~3.0"
```

It supports authorization/capture and offers these configuration options:

apiLoginId (string, required)
: The API login ID from your Authorize.net account

transactionKey (string, required)
: The transaction key generated for your Authorize.net account

hashSecret (string, optional)
: A secret string you've entered in your Authorize.net account that offers additional protection for payment status notifications

authorizenet.address (boolean, optional)
: A value of "1" will send the customer address to Authorize.net

authorizenet.authorize (boolean, optional)
: Use "1" if you want to get an authorization first and capture the payment after the parcel has been dispatched or the product delivered according to the delivery status of the order. Leave this setting out for immediate payments

authorizenet.header (string, optional)
: The HTTP header sent by the checkout update component after updating the order successfully ("Location: <URL to confirm page>" by default)

authorizenet.body (string, optional)
: The HTTP body sent by the checkout update component after updating the order successfully ("success" by default). This could be a complete HTML page too that is shown to the customer and offering a link to the confirm page (authorizenet.header must be a empty value in this case)

testMode (boolean, optional)
: Use "1" for test payments without real money


## CardSave

The [CardSave](http://www.cardsave.net/) payment gateway is available via the **CardSave** payment service provider since 2015.07.

```
composer req "omnipay/cardsave:~3.0"
```

It supports authorization/capture and offers these configuration options:

merchantId (string, required)
: The merchant ID sent to you by CardSave

password (string, required)
: The password for the merchant ID sent to you by CardSave

cardsave.address (boolean, optional)
: A value of "1" will send the customer address to CardSave for additional verification

cardsave.authorize (boolean, optional)
: Use "1" if you want to get an authorization first and capture the payment after the parcel has been dispatched or the product delivered according to the delivery status of the order. Leave this setting out for immediate payments

testMode (boolean, optional)
: Use "1" for test payments without real money


## Mollie

The [Mollie](https://www.mollie.com/en/) payment gateway is available via the **Mollie** payment service provider since 2015.07. It supports all on-line payment methods (e.g. credit card) but no off-line payments (e.g. SEPA) and no authorization before capture.

```
composer req "omnipay/mollie:~3.0"
```

The available configuration options are:

apiKey (string, required)
: The API key string from your Mollie account

mollie.address (boolean, optional)
: A value of "1" will send the customer address to the Mollie server for additional verification

testMode (boolean, optional)
: Use "1" for test payments without real money


## Omnipay (generic)

[Omnipay](http://omnipay.thephpleague.com/) is a library offering a common interface for 100+ different payment gateways. It's available via the **OmniPay** payment service provider since 2015.07.

!!! note
    If you use composer, you have to add the [Omnipay payment driver](https://github.com/thephpleague/omnipay#payment-gateways) you want to use to your composer.json and run *composer update*.

It supports these configuration options:

omnipay.type (string, required)
: Gateway name as defined by the [https://github.com/thephpleague/omnipay#payment-gateways Omnipay driver] (stated in the documentation of the driver)

omnipay.address (boolean, optional)
: A value of "1" will send the customer address to the Stripe server for additional verification

omnipay.authorize (boolean, optional)
: Use "1" if you want to get an authorization first and capture the payment after the parcel has been dispatched or the product delivered according to the delivery status of the order. Leave this setting out for immediate payments

omnipay.onsite (boolean, optional)
: Use "1" if payment gateway requires that payment details are collected locally

testMode (boolean, optional)
: Use "1" for test payments without real money

!!! note
    You need to add the credentials for each payment gateway you want to use. There is no common naming for the credentials, so you have to look into the *./src/Gateway.php* of each [payment gateway](https://github.com/thephpleague/omnipay#payment-gateways) to find out what's required. They are listed in the *getDefaultParameters()* method of each Gateway class, e.g. in the [2Checkout class](https://github.com/thephpleague/omnipay-2checkout/blob/master/src/Gateway.php).

!!! tip
    Some payment gateways offered by Omnipay requires special handling. Sub-classing from the Omnipay provider and overwriting the existing methods if required can support even special payment gateways interfaces. Please drop us a not if you got a provider working in your shop.


## OPPWA

OPPWA is a white label platform for payments used by several payment providers like:
* Hobex
* HyperPay
* Pay.ON
* PaySquare
* Peach Payments
* Qualife
* ZooPay

```
composer req "vdbelt/omnipay-oppwa:~3.0"
```

It supports these configuration options:

omnipay.type (string, required)
: Must be "Oppwa"

omnipay.onsite (boolean, required)
: Must be "1"

userId (string, required)
: User identifier to authenticate against the payment gateway

password (string, required)
: Password to authenticate against the payment gateway

entityId (string, required)
: Unique identifier for the payment account

omnipay.address (boolean, optional)
: A value of "1" will send the customer address to the OPPWA server for additional verification

omnipay.authorize (boolean, optional)
: Use "1" if you want to get an authorization first and capture the payment after the parcel has been dispatched or the product delivered according to the delivery status of the order. Leave this setting out for immediate payments

testMode (boolean, optional)
: Use "1" for test payments without real money


## Payone

The [Payone](https://www.payone.de/en/) payment gateways are available via the Omnipay payment service provider.

```
composer req "academe/omnipay-payone:~3.0"
```

The available configuration options are:

omnipay.type (string, required)
: Gateway name, "Payone_ShopFrontend" without quotation marks

omnipay.address (boolean, optional)
: A value of "1" to pass the billing address to the payment gateway

merchantId (string, required)
: Your merchant ID available in your Payone account

portalId (string, required)
: Portal ID you've created in the Payone backend

portalKey (string, required)
: Hexadecimal string for authentication created in the Payone backend

subAccountId (string, required)
: ID of the sub-account you've created in the Payone backend

clearingtype (string, optional)
: Code from the Payone documentation (default: "cc" for credit cards)

testMode (boolean, optional)
: Use "1" for test payments without real money. Requires activating the test mode in your payone account too


## Postfinance

!!! warning
    The *bummzack/omnipay-postfinance* driver is currently available for the outdated Omnipay 2.0 only and will not work in Aimeos 2019.x+ releases!

The [Postfinance](https://e-payment.postfinance.ch) payment gateways are available via the Omnipay payment service provider. If you use composer, add this to your composer.json and run *composer update*:

```
composer req "bummzack/omnipay-postfinance:~0.1"
```

The available configuration options are:

omnipay.type (string, required)
: Gateway name, "Postfinance" without quotation marks

omnipay.address (boolean, optional)
: A value of "1" to pass the billing address to the payment gateway

pspId (string, required)
: Your merchant ID you use to log into your Postfinance account

shaIn (string, required)
: SHA-IN key

shaOut (string, required)
: SHA-OUT key

testMode (boolean, optional)
: Use "1" for test payments without real money. Requires activating the test mode in your payone account too

!!! note
    Please configure your Postfinance account according to this documenation: [Required Postfinance settings] (https://github.com/bummzack/omnipay-postfinance#configuration-in-the-postfinance-backend)

![Parameter hashing configuration](Postfinance-global.png)
![Send feedback parameters](Postfinance-feedback.png)


## Sofort

The [Sofort](https://sofort.com/) payment gateway is available via the Omnipay payment service provider since 2016.07.

```
composer req "aimeoscom/omnipay-sofort:~3.0"
```

The available configuration options are:

projectId (string, required)
: Project ID from Projects -> My Projects -> <project name> -> General settings

username (string, required)
: Customer ID from Projects -> My Projects -> <project name> -> General settings

password (string, required)
: API key from Projects -> My Projects -> <project name> -> General settings

omnipay.type (string, required)
: Gateway name, "Sofort" without quotation marks

omnipay.authorize (boolean, required)
: Always use "1" because the Sofort driver only supports this mode

omnipay.address (boolean, optional)
: A value of "1" will send the customer address to the Sofort server for additional verification

testMode (boolean, optional)
: Use "1" for test payments without real money. Requires activating the test mode in your sofort.com account too


## Stripe

The [Stripe](https://stripe.com) payment gateway is available via the **Stripe** payment service provider since 2015.07. It supports credit card payments and authorization before capture.

```
composer req "omnipay/stripe:~3.0"
```

The available configuration options are:

apiKey (string, required)
: The secret API key string from your Stripe account

publishableKey (string, requires)
: Public key used in the JS frontend code to authenticate to Stripe

stripe.address (boolean, optional)
: A value of "1" will send the customer address to the Stripe server for additional verification

stripe.authorize (boolean, optional)
: Use "1" if you want to get an authorization first and capture the payment after the parcel has been dispatched or the product delivered according to the delivery status of the order. Leave this setting out for immediate payments

testMode (boolean, optional)
: Use "1" for test payments without real money

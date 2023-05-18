Creating orders requires a complete basket, i.e. it contains at least one product, the billing address and a payment and delivery entry. Then it's a three-way step to create the required database entries and redirect to the payment gateway or the "Thank You" page.

# Save basket

The first step to create an order is to persist the basket of the customer. This is done by a POST request to the basket URL. You obtain this URL either from the resource list of an OPTIONS response or from the basket response.

=== "CURL"
    ```bash
    curl -b cookies.txt -c cookies.txt \
    -X POST 'http://localhost:8000/jsonapi/basket?_token=...'
    ```
=== "jQuery"
    ```javascript
    // basket URL returned from OPTIONS response
    var url = response['meta']['resources']['basket'];
    // or basket URL returned from basket response
    var url = response['links']['self']['href'];

    if(response['meta']['csrf']) { // add CSRF token if available and therefore required
        var csrf = {};
        csrf[response['meta']['csrf']['name']] = response['meta']['csrf']['value'];
        url += (url.indexOf('?') === -1 ? '?' : '&') + $.param(csrf);
    }

    $.ajax({
        url: url,
        method: "POST",
        dataType: "json"
    }).done( function( result ) {
        console.log( result );
    });
    ```

The response will then contain a basket ID value which is equivalent to the "order.id" attribute. Furthermore, it contains the link to create the order invoice in **response['links']['order']['href']**:

```json
{
    "meta": {
        "total": 1,
        "prefix": null,
        "content-baseurl": "/"
    },
    "links": {
        "self": {
            "href": "http://localhost:8000/jsonapi/basket",
            "allow": ["GET"]
        },
        "order": {
            "href": "http://localhost:8000/jsonapi/order",
            "allow": ["POST"]
        }
    },
    "data": {
        "id": "123",
        "type": "basket",
        "links": {
            "self": {
                "href": "http://localhost:8000/jsonapi/basket?id=123",
                "allow": ["GET"]
            }
        },
        "attributes": {
            "order.id": "123",
            "order.customerid": "321",
            "order.sitecode": "default",
            "order.languageid": "en",
            "order.currencyid": "EUR",
            "order.price": "1.00",
            "order.costs": "0.00",
            "order.rebate": "0.00",
            "order.status": 0,
            "order.comment": "just a comment"
        },
        "relationships": {
        }
    },
    "included": [
    ]
}
```

To mitigate DoS attacks, you can only create a limited number of orders from one IP address. The default configuration is 5 orders within 15 minutes. If you try to create more orders within this time frame, an error will be returned.

* [controller/frontend/basket/limit-count](../../config/controller-frontend/basket.md#limit-count)
* [controller/frontend/basket/limit-seconds](../../config/controller-frontend/basket.md#limit-seconds)

# Redirect to payment gateway

After saving the basket, you may need to redirect the customer to an external payment gateway. For this, you must send a POST request to the "order" link listed in the response of the saved basket. In that request, the ID of the saved basket needs to be added as "order.id" value within the parameters sent with the POST request:

=== "CURL"
    ```bash
    curl -b cookies.txt -c cookies.txt \
    -X POST 'http://localhost:8000/jsonapi/order?_token=...' \
    -H 'Content-Type: application/json' \
    -d '{"data": {
        "attributes": {
            "order.id": "..."
        }
    }}'
    ```
=== "jQuery"
    ```javascript
    var params = {'data': {
        'attributes': {
            "order.id": response["data"]["id"], // generated ID returned in the basket POST response
        }
    }};

    // basket URL returned from basket response
    var url = response['links']['order']['href'];

    if(response['meta']['csrf']) { // add CSRF token if available and therefore required
        var csrf = {};
        csrf[response['meta']['csrf']['name']] = response['meta']['csrf']['value'];
        url += (url.indexOf('?') === -1 ? '?' : '&') + $.param(csrf);
    }

    $.ajax({
        url: url,
        method: "POST",
        dataType: "json",
        data: JSON.stringify(params)
    }).done( function( result ) {
        console.log( result );
    });
    ```

The response will contain the data with a link to the next step. This can either be the URL to the payment gateway or to the "Thank You" page and can be found in **response['links']['process']['href']**:

```json
{
    "meta": {
        "total": 1,
        "prefix": null,
        "content-baseurl": "/"
    },
    "links": {
        "self": { "href": "http://localhost:8000/jsonapi/order" }
    },
    "data": {
        "id": "123",
        "type": "order",
        "links": {
            "self": {
                "href": "http://localhost:8000/jsonapi/order?id=321",
                "allow": [ "GET"]
            }
            "process": {
                "href": "https://payment-gateway.com/creditcard",
                "allow": [ "POST"],
                "meta": {
                    "invoiceid": {
                        "code": "invoiceid",
                        "required": true,
                        "default": 321,
                        "public": false,
                        "type": "string"
                    },
                    "language": {
                        "code": "language",
                        "required": true,
                        "default": en,
                        "public": false,
                        "type": "string"
                    }
                }
            }
        },
        "attributes": {
            "order.id": "123",
            "order.customerid": "321",
            "order.statusdelivery": -1,
            "order.statuspayment": -1,
            "order.currencyid": "EUR",
            "order.datepayment": "2000-01-01 00:00:00",
            "order.datedelivery": null,
            "order.relatedid": null
        }
    }
}
```

Depending on the chosen payment, the response contains a description of all necessary information in the **response['links']['process']['meta']** section that is required by the payment gateway.

As you can see in the response above, the description of the required parameters looks like this:

```json
"invoiceid": {
    "code": "invoiceid",
    "required": true,
    "default": 123,
    "public": false,
    "type": "string"
},
```

Possible values for "type" are:

boolean
: True/false value (input of type "checkbox")

string
: Short text field (input)

integer
: Integer value (input of type "number" and no decimal places)

date
: Date selector (input of type "date")

select
: Select drop-down (with options from "default" property)


The "code" contains the form parameter name and the "default" property value that should be sent to the payment gateway. For all entries in the "meta" section with "public" equals "true", you have to show the customer a corresponding input field where they can enter e.g. their credit card number. All entries with "public" is "false" must be added as hidden input elements:

=== "jQuery"
    ```javascript
    var form = $('<form/>');

    // process URL returned in order POST response
    form.attr('action', response['links']['process']['href']);
    // from the order POST response
    form.attr('method', response['links']['process']['allow'][0]);

    for(entry in response["data"]["links"]["process"]["meta"]) {
        // todo: translate code to readable string
        $('<label>' + entry['code'] + '</label>').appendTo(form);

        var input = $('<input/>');
        if(entry['public'] == false) {
            input.attr('type', 'hidden');
        }
        input.attr('name', entry['code']);
        input.attr('value', entry['default']);
        input.appendTo(form);
    }

    $('<button type="submit">Submit</button>').appendTo(form);
    ```

# Retrieve orders

To get orders for a customer, the customer must be logged in.

!!! tip
    How to authenticate the user depends on the used PHP framework. Please have a look into the documentation of your used framework, e.g. at Laravel [Passport](https://laravel.com/docs/master/passport)/[Sanctum](https://laravel.com/docs/master/sanctum) or Symfony [Guard](https://symfony.com/doc/current/security/guard_authentication.html).

Then, you can retrieve the list of orders using the "order" endpoint:

=== "CURL"
    ```bash
    curl -b cookies.txt -c cookies.txt \
    -X GET 'http://localhost:8000/jsonapi/order'
    ```
=== "jQuery"
    ```javascript
    $.ajax({
        method: "GET",
        dataType: "json",
        url: options.meta.resources['order'] // returned from OPTIONS call
    }).done( function( result ) {
        console.log( result );
    });
    ```

To retrieve a single order only, you need to use the "self" link of the order item returned by the previous response. You can get the full order details by passing:

```
order/address,order/coupon,order/product,order/service
```

as *include* parameter:

=== "CURL"
    ```bash
    curl -X GET 'http://localhost:8000/jsonapi/order?id=...&include=order/address,order/coupon,order/product,order/service'
    ```
=== "jQuery"
    ```javascript
    var args = {
        include: "order/address,order/coupon,order/product,order/service"
    };
    var params = {};

    if(options.meta.prefix) { // returned from OPTIONS call
        params[options.meta.prefix] = args;
    } else {
        params = args;
    }

    $.ajax({
        method: "GET",
        dataType: "json",
        url: options.meta.resources['order'], // returned from OPTIONS call
        data: params
    }).done( function( result ) {
        console.log( result );
    });
    ```

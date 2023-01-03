Most of the time you want to offer some shipping and/or payment options to your customers. Even if you don't show the shipping or payment options, you need to add it to the basket so the process after creating the order continues as expected.

# List options

At first you need to get the available delivery and payment options from the service's resource URL listed in the OPTIONS request. With that URL you can query for the available services, either all together in one request or separated by their type ("delivery" or "payment"). The example code below will return all payment options:

=== "CURL"
    ```bash
    curl -b cookies.txt -c cookies.txt \
    -X GET 'http://localhost:8000/jsonapi/service?filter[cs_type]=payment&include=text,price,media'
    ```
=== "jQuery"
    ```javascript
    var args = {
        'filter': {
            'cs_type': 'payment' // or "delivery" (optional)
        },
        'include': 'text,price,media'
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
        url: options.meta.resources['service'], // returned from OPTIONS call
        data: params
    }).done( function( result ) {
        console.log( result );
    });
    ```

This returns the list of payment or delivery options (or both if the "filter" parameter is omitted) including the associated texts, prices and images due to the "included" parameter:

```json
{
    "meta": {
        "total": 5,
        "prefix": null,
        "content-baseurl": "http://localhost:8000/",
        "csrf": {
            "name": "_token",
            "value": "..."
        }
    },
    "links": {
        "self": "http://localhost:8000/jsonapi/service?filter%5Bcs_type%5D=delivery&include=text%2Cprice%2Cmedia"
    },
    "data": [{
        "id": "1",
        "type": "service",
        "links": {
            "self": {
                "href": "http:\/\/localhost:8000\/jsonapi\/service?id=1",
                "allow": ["GET"]
            },
            "basket.service": {
                "href": "http:\/\/localhost:8000\/jsonapi\/basket?id=default&related=service&relatedid=delivery",
                "allow": ["POST"],
                "meta": {
                    "time.hourminute": {
                        "code": "time.hourminute",
                        "type": "time",
                        "label": "Delivery time",
                        "public": true,
                        "default": "07:15",
                        "required": true
                    },
                    "supplier.code": {
                        "code": "supplier.code",
                        "type": "list",
                        "label": "Pick-up address",
                        "public": true,
                        "default": {
                            "demo-test1": "Test supplier 1\nTest company\nTest street 1\n10000 Test city\nNY US\ndemo1@example.com\n",
                            "demo-test2": "Test supplier 2\nTest company\nTest road 10\n20000 Test town\nNY US\ndemo2@example.com\n"
                        },
                        "required": true
                    }
                }
            }
        },
        "attributes": {
            "service.id": "1",
            "service.type": "delivery",
            "service.code": "demo-pickup",
            "service.label": "Click & Collect",
            "service.provider": "Standard,Time,Supplier",
            "service.position": 0,
            "service.datestart": null,
            "service.dateend": null,
            "service.status": 1,
            "price": {
                "price.id": "27",
                "price.type": "default",
                "price.currencyid": "EUR",
                "price.domain": "service",
                "price.quantity": 1,
                "price.value": "0.00",
                "price.costs": "0.00",
                "price.rebate": "0.00",
                "price.taxvalue": "0.0000",
                "price.taxrates": {
                    "": "0.00"
                },
                "price.taxrate": "0.00",
                "price.taxflag": true,
                "price.status": 1,
                "price.label": "Demo: DHL"
            }
        },
        "relationships": {
            "media": {
                "data": [{
                    "id": "18",
                    "type": "media",
                    "attributes": {
                        "service.lists.id": "1",
                        "service.lists.domain": "media",
                        "service.lists.refid": "18",
                        "service.lists.datestart": null,
                        "service.lists.dateend": null,
                        "service.lists.config": [],
                        "service.lists.position": 0,
                        "service.lists.status": 1,
                        "service.lists.type": "default"
                    }
                }]
            },
            "price": {
                "data": [{
                    "id": "27",
                    "type": "price",
                    "attributes": {
                        "service.lists.id": "2",
                        "service.lists.domain": "price",
                        "service.lists.refid": "27",
                        "service.lists.datestart": null,
                        "service.lists.dateend": null,
                        "service.lists.config": [],
                        "service.lists.position": 0,
                        "service.lists.status": 1,
                        "service.lists.type": "default"
                    }
                }]
            },
            "text": {
                "data": [{
                    "id": "86",
                    "type": "text",
                    "attributes": {
                        "service.lists.id": "6",
                        "service.lists.domain": "text",
                        "service.lists.refid": "86",
                        "service.lists.datestart": null,
                        "service.lists.dateend": null,
                        "service.lists.config": [],
                        "service.lists.position": 3,
                        "service.lists.status": 1,
                        "service.lists.type": "default"
                    }
                }]
            }
        }
    }],
    "included": [{
        "id": "18",
        "type": "media",
        "attributes": {
        "media.id": "18",
        "media.domain": "service",
        "media.label": "Demo: dhl.png",
        "media.languageid": null,
        "media.mimetype": "image\/png",
        "media.type": "icon",
        "media.preview": "http:\/\/demo.aimeos.org\/media\/service\/pickup.png",
        "media.previews": {
        "1": "http:\/\/demo.aimeos.org\/media\/service\/pickup.png"
        },
        "media.url": "http:\/\/demo.aimeos.org\/media\/service\/pickup.png",
        "media.status": 1
        }
    },{
        "id": "27",
        "type": "price",
        "attributes": {
            "price.id": "27",
            "price.type": "default",
            "price.currencyid": "EUR",
            "price.domain": "service",
            "price.quantity": 1,
            "price.value": "0.00",
            "price.costs": "0.00",
            "price.rebate": "0.00",
            "price.taxvalue": "0.0000",
            "price.taxrates": {
                "": "0.00"
            },
            "price.taxrate": "0.00",
            "price.taxflag": true,
            "price.status": 1,
            "price.label": "Demo: Click&Collect"
        }
    },{
        "id": "86",
        "type": "text",
        "attributes": {
            "text.id": "86",
            "text.languageid": "en",
            "text.type": "short",
            "text.label": "Demo short\/en: Local pick-up",
            "text.domain": "service",
            "text.content": "Local pick-up",
            "text.status": 1
        }
    }]
}
```

# Add delivery/payment

To add a service to the basket you need the "basket/service" URL from the service resource response. In our previous example, the URL of the first delivery option that would add this service to the basket is:

```
http://localhost:8000/jsonapi/basket?id=default&related=service&relatedid=delivery
```

To add this service as delivery option to the current basket you should use:

=== "CURL"
    ```bash
    curl -b cookies.txt -c cookies.txt \
    -X POST 'http://localhost:8000/jsonapi/basket?id=default&related=service&relatedid=delivery&_token=...' \
    -H 'Content-Type: application/json' \
    -d '{"data": [{
        "id": "delivery",
        "attributes": {
            "service.id": "1",
            "time.hourminute": "15:00",
            "supplier.code": "demo-test2"
        }
    }]}'
    ```
=== "jQuery"
    ```javascript
    var params = {'data': [{
        'id': 'payment',
        'attributes': {
            'service.id': '1', // from service response
            'time.hourminute': '15:00', // key/value pairs of data entered by the customer
            'supplier.code': 'demo-test2'
        }
    }]};

    var url = response['data'][0]['links']['basket/service']['href']; // from service response

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

It's important to add the **id: "delivery"** (or **"payment"**) and the service ID in the attributes section of the parameters sent to the server. The value for "id" is the service type while the value for "service.id" must be the ID of the service option that should be added as delivery or payment entry to the basket.

The response to this request would be similar to this:

```json
{
    "meta": {
        "total": 1,
        "prefix": null,
        "content-baseurl": "http://localhost:8000/",
        "csrf": {
            "name": "_token",
            "value": "..."
        }
    },
    "links": {
        "self": {
            "href": "http://localhost:8000/jsonapi/basket?id=default&related=service&relatedid=delivery",
            "allow": ["DELETE","GET","PATCH","POST"]
        },
        "basket/product": {
            "href": "http://localhost:8000/jsonapi/basket?id=default&related=product",
            "allow": ["POST"]
        },
        "basket/service": {
            "href": "http://localhost:8000/jsonapi/basket?id=default&related=service",
            "allow": ["POST"]
        },
        "basket/address": {
            "href": "http://localhost:8000/jsonapi/basket?id=default&related=address",
            "allow": ["POST"]
        },
        "basket/coupon": {
            "href": "http://localhost:8000/jsonapi/basket?id=default&related=coupon",
            "allow": ["POST"]
        }
    },
    "data": {
        "id": "default",
        "type": "basket",
        "links": {
            "self": {
                "href": "http:\/\/localhost:8000\/jsonapi\/basket?id=default",
                "allow": ["DELETE","GET","PATCH","POST"]
            }
        },
        "attributes": {
            "order.id": null,
            "order.sitecode": "",
            "order.customerid": "",
            "order.languageid": "en",
            "order.currencyid": "EUR",
            "order.price": "0.00",
            "order.costs": "0.00",
            "order.rebate": "0.00",
            "order.taxvalue": "0.0000",
            "order.taxflag": true,
            "order.customerref": "",
            "order.comment": ""
        },
        "relationships": {
            "basket.service": {
                "data": [{
                    "type": "basket.service",
                    "id": "delivery"
                }]
            }
        }
    },
    "included": [{
        "id": "delivery",
        "type": "basket.service",
        "attributes": {
            "order.service.id": null,
            "order.service.price": "0.00",
            "order.service.costs": "0.00",
            "order.service.rebate": "0.00",
            "order.service.taxrate": "0.00",
            "order.service.taxrates": {
                "": "0.00"
            },
            "order.service.type": "delivery",
            "order.service.code": "demo-pickup",
            "order.service.name": "Click & Collect",
            "order.service.position": null,
            "order.service.mediaurl": "",
            "attribute": [{
                "order.service.attribute.id": null,
                "order.service.attribute.type": "delivery",
                "order.service.attribute.name": "",
                "order.service.attribute.code": "time.hourminute",
                "order.service.attribute.value": "15:00",
                "order.service.attribute.quantity": 1
            },{
                "order.service.attribute.id": null,
                "order.service.attribute.type": "delivery",
                "order.service.attribute.name": "",
                "order.service.attribute.code": "supplier.address",
                "order.service.attribute.value": "Test supplier 1\nTest company\nTest street 1\n10000 Test city\nNY US\ndemo1@example.com\n",
                "order.service.attribute.quantity": 1
            }]
        },
        "links": {
            "self": {
                "href": "http:\/\/localhost:8000\/jsonapi\/basket?id=default&related=service&relatedid=delivery",
                "allow": ["DELETE", "PATCH"]
            }
        }
    }]
}
```

It contains an additional "relationships" entry for the basket which points to the basket service entry in the "included" section.

!!! note
    If you perform the same request again, **existing options** in the basket are **NOT overwritten** but an additional option added! Thus you can add several delivery or payment options in one order.

## Passing additional data

The "attributes" section in "data" can contain additional key/value pairs whose values are entered by the customer. Here the "pickup time" and "location" are passed. The available keys are listed in the "meta" section of the "basket/service" link of each entry returned by the service response:

```json
"meta": {
    "time.hourminute": {
        "code": "time.hourminute",
        "type": "time",
        "label": "Pick-up time",
        "public": true,
        "default": "07:15",
        "required": true
    },
    "supplier.code": {
        "code": "supplier.code",
        "type": "list",
        "label": "Pick-up address",
        "public": true,
        "default": {
            "demo-test1": "Test supplier 1\nTest company\nTest street 1\n10000 Test city\nNY US\ndemo1@example.com\n",
            "demo-test2": "Test supplier 2\nTest company\nTest road 10\n20000 Test town\nNY US\ndemo2@example.com\n"
        },
        "required": true
    }
}
```

Only values for these keys will be accepted and if the "required" property is true, they must be passed in the request!

Each of these additional service attributes contains a type property which can be one of these:

boolean
: True/false value (input of type "checkbox")

string
: Short text field (input)

text
: Long text field (textarea)

integer
: Integer value (input of type "number" and no decimal places)

number
: Decimal value (input of type "number" with two decimal places)

date
: Date selector (input of type "date")

time
: Time selector (input of type "time")

datetime
: Date and time selector (input of type datetime-local)

select
: Select drop-down (with options from "default" property)

list
: List of values (input elements of type "radio" for value in "default" property)

map
: Key/value pairs (select drop-down with keys as option value and values as option labels)

The additional service attributes are then stored in the "attribute" section of the service option in the basket ("included" section):

```json
"attribute": [{
    "order.service.attribute.id": null,
    "order.service.attribute.type": "delivery",
    "order.service.attribute.name": "",
    "order.service.attribute.code": "time.hourminute",
    "order.service.attribute.value": "15:00",
    "order.service.attribute.quantity": 1
},{
    "order.service.attribute.id": null,
    "order.service.attribute.type": "delivery",
    "order.service.attribute.name": "",
    "order.service.attribute.code": "supplier.address",
    "order.service.attribute.value": "Test supplier 2\nTest company\nTest road 10\n20000 Test town\nNY US\ndemo2@example.com\n",
    "order.service.attribute.quantity": 1
}]
```

# Update services

Replacing existing delivery/payment services in the basket with only one request is possible since 2022.07 by using the PATCH request of the basket service resource. It will remove the already available delivery or payment option (depending on the `relatedid` parameter) and add the new options afterwards from the body sent with the request.

From the previous GET request or the response returned for your last request you know that the URL for modifying the basket delivery service options is e.g.:

```
http://localhost:8000/jsonapi/basket?id=default&related=service&relatedid=delivery
```

To update the delivery service in the current basket you should use:

=== "CURL"
    ```bash
    curl -b cookies.txt -c cookies.txt \
    -X PATCH 'http://localhost:8000/jsonapi/basket?id=default&related=service&relatedid=delivery&_token=...' \
    -H 'Content-Type: application/json' \
    -d '{"data": [{
        "id": "delivery",
        "attributes": {
            "service.id": "1",
            "time.hourminute": "17:00",
            "supplier.code": "demo-test1"
        }
    }]}'
    ```
=== "jQuery"
    ```javascript
    var params = {'data': [{
        'id': 'payment',
        'attributes': {
            'service.id': '1', // from service response
            'time.hourminute': '17:00', // key/value pairs of data entered by the customer
            'supplier.code': 'demo-test1'
        }
    }]};

    var url = response['data'][0]['links']['basket/service']['href']; // from service response

    if(response['meta']['csrf']) { // add CSRF token if available and therefore required
        var csrf = {};
        csrf[response['meta']['csrf']['name']] = response['meta']['csrf']['value'];
        url += (url.indexOf('?') === -1 ? '?' : '&') + $.param(csrf);
    }

    $.ajax({
        url: url,
        method: "PATCH",
        dataType: "json",
        data: JSON.stringify(params)
    }).done( function( result ) {
        console.log( result );
    });
    ```

It's important to add the **id: "delivery"** (or **"payment"**) and the service ID in the attributes section of the parameters sent to the server. The value for "id" is the service type while the value for "service.id" must be the ID of the service option that should be added as delivery or payment entry to the basket.

The response to this request would be similar to this:

```json
{
    "meta": {
        "total": 1,
        "prefix": null,
        "content-baseurl": "http://localhost:8000/",
        "csrf": {
            "name": "_token",
            "value": "..."
        }
    },
    "links": {
        "self": {
            "href": "http://localhost:8000/jsonapi/basket?id=default&related=service&relatedid=delivery",
            "allow": ["DELETE","GET","PATCH","POST"]
        },
        "basket/product": {
            "href": "http://localhost:8000/jsonapi/basket?id=default&related=product",
            "allow": ["POST"]
        },
        "basket/service": {
            "href": "http://localhost:8000/jsonapi/basket?id=default&related=service",
            "allow": ["POST"]
        },
        "basket/address": {
            "href": "http://localhost:8000/jsonapi/basket?id=default&related=address",
            "allow": ["POST"]
        },
        "basket/coupon": {
            "href": "http://localhost:8000/jsonapi/basket?id=default&related=coupon",
            "allow": ["POST"]
        }
    },
    "data": {
        "id": "default",
        "type": "basket",
        "links": {
            "self": {
                "href": "http:\/\/localhost:8000\/jsonapi\/basket?id=default",
                "allow": ["DELETE","GET","PATCH","POST"]
            }
        },
        "attributes": {
            "order.id": null,
            "order.sitecode": "",
            "order.customerid": "",
            "order.languageid": "en",
            "order.currencyid": "EUR",
            "order.price": "0.00",
            "order.costs": "0.00",
            "order.rebate": "0.00",
            "order.taxvalue": "0.0000",
            "order.taxflag": true,
            "order.customerref": "",
            "order.comment": ""
        },
        "relationships": {
            "basket.service": {
                "data": [{
                    "type": "basket.service",
                    "id": "delivery"
                }]
            }
        }
    },
    "included": [{
        "id": "delivery",
        "type": "basket.service",
        "attributes": {
            "order.service.id": null,
            "order.service.price": "0.00",
            "order.service.costs": "0.00",
            "order.service.rebate": "0.00",
            "order.service.taxrate": "0.00",
            "order.service.taxrates": {
                "": "0.00"
            },
            "order.service.type": "delivery",
            "order.service.code": "demo-pickup",
            "order.service.name": "Click & Collect",
            "order.service.position": null,
            "order.service.mediaurl": "",
            "attribute": [{
                "order.service.attribute.id": null,
                "order.service.attribute.type": "delivery",
                "order.service.attribute.name": "",
                "order.service.attribute.code": "time.hourminute",
                "order.service.attribute.value": "17:00",
                "order.service.attribute.quantity": 1
            },{
                "order.service.attribute.id": null,
                "order.service.attribute.type": "delivery",
                "order.service.attribute.name": "",
                "order.service.attribute.code": "supplier.address",
                "order.service.attribute.value": "Test supplier 2\nTest company\nTest road 10\n20000 Test town\nNY US\ndemo2@example.com\n",
                "order.service.attribute.quantity": 1
            }]
        },
        "links": {
            "self": {
                "href": "http:\/\/localhost:8000\/jsonapi\/basket?id=default&related=service&relatedid=delivery",
                "allow": ["DELETE", "PATCH"]
            }
        }
    }]
}
```

Aimeos also allows several delivery or payment option within the basket and there can be more than one delivery or payment option sent in the PATCH request. You can also mix delivery and payment option within one PATCH request but only the type passed in `relatedid` ("delivery" or "payment") is removed before the new ones are added.

# Delete services

Delivery or payment options added to the basket can also be removed again. For this you need the URL from the basket service entry, which is returned in the basket response. For the example above it is:

```
http://localhost:8000/jsonapi/basket?id=default&related=service&relatedid=delivery
```

Executing a DELETE request using this URL will remove the service option from the basket again:

=== "CURL"
    ```bash
    curl -b cookies.txt -c cookies.txt \
    -X DELETE 'http://localhost:8000/jsonapi/basket?id=default&related=service&relatedid=delivery&_token=...'
    ```
=== "jQuery"
    ```javascript
    // basket service URL returned from basket response
    var url = response['included'][0]['links']['self']['href'];

    if(response['meta']['csrf']) { // add CSRF token if available and therefore required
        var csrf = {};
        csrf[response['meta']['csrf']['name']] = response['meta']['csrf']['value'];
        url += (url.indexOf('?') === -1 ? '?' : '&') + $.param(csrf);
    }

    $.ajax({
        url: url
        method: "DELETE",
        dataType: "json"
    }).done( function( result ) {
        console.log( result );
    });
    ```

!!! note
    In the default configuration, the "Autofill" plugin will automatically add a delivery option after removing the delivery option from the basket.

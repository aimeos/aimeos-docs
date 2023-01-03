By default you can add a billing and delivery address to the basket. While the delivery address is optional, setting the billing address is almost always mandatory.

# Add addresses

To add one or more addresses you have to pass the data including the "id" and the attributes in a POST request to the server. The "id" is in that case the type of the address, i.e. "payment" for the billing address and "delivery" for the corresponding address.

There are some address attributes that are required when adding or replacing an address:

* order.base.address.lastname (last name or full name)
* order.base.address.address1 (most of the time the street name)
* order.base.address.city (town or city name)
* order.base.address.languageid (language the customer prefers)
* order.base.address.email (account e-mail address)

The request for creating a new address in the basket could look like this:

=== "CURL"
    ```bash
    curl -b cookies.txt -c cookies.txt \
    -X POST 'http://localhost:8000/jsonapi/basket?id=default&related=address&_token=...' \
    -H 'Content-Type: application/json' \
    -d '{"data": [{
        "id": "payment",
        "attributes": {
            "order.base.address.addressid": "...",
            "order.base.address.salutation": "mr",
            "order.base.address.company": "Example company",
            "order.base.address.vatid": "DE123456789",
            "order.base.address.title": "Dr.",
            "order.base.address.firstname": "Test",
            "order.base.address.lastname": "User",
            "order.base.address.address1": "Test street",
            "order.base.address.address2": "1",
            "order.base.address.address3": "",
            "order.base.address.postal": "12345",
            "order.base.address.city": "Test city",
            "order.base.address.state": "HH",
            "order.base.address.countryid": "DE",
            "order.base.address.languageid": "de",
            "order.base.address.telephone": "+4912345678",
            "order.base.address.telefax": "+49123456789",
            "order.base.address.email": "test@example.com",
            "order.base.address.website": "https://example.com",
            "order.base.address.longitude": 10.0,
            "order.base.address.latitude": 50.0
        }
    }]}'
    ```
=== "jQuery"
    ```javascript
    var params = {'data': [{
        'id': 'payment', // or 'delivery'
        'attributes': {
            'order.base.address.addressid': '...', // customer address ID (optional)
            'order.base.address.salutation': 'mr', // 'mr', 'mrs', 'miss', 'company' or empty (optional)
            'order.base.address.company': 'Example company', // (optional)
            'order.base.address.vatid': 'DE123456789', // (optional)
            'order.base.address.title': 'Dr.', // (optional)
            'order.base.address.firstname': 'Test', // (optional)
            'order.base.address.lastname': 'User', // (required)
            'order.base.address.address1': 'Test street', // (required)
            'order.base.address.address2': '1', // (optional)
            'order.base.address.address3': '', // (optional)
            'order.base.address.postal': '12345', // (optional)
            'order.base.address.city': 'Test city', // (required)
            'order.base.address.state': 'HH', // (optional)
            'order.base.address.countryid': 'DE', // (optional)
            'order.base.address.languageid': 'de', // (required by many payment gateways)
            'order.base.address.telephone': '+4912345678', // (optional)
            'order.base.address.telefax': '+49123456789', // (optional)
            'order.base.address.email': 'test@example.com', // (required)
            'order.base.address.website': 'https://example.com', // (optional)
            'order.base.address.longitude': 10.0, // (optional, float value)
            'order.base.address.latitude': 50.0 // (optional, float value)
        }
    }]};

    var url = response['links']['basket/address']['href']; // from basket response

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

The response will then contain an additional "relationships" section in the basket data that points to the new address in the "included" section:

```json
{
    "meta": {
        "total": 1,
        "prefix": null,
        "content-baseurl": "/"
    },
    "links": {
        "self": {
            "href": "http://localhost:8000/jsonapi/basket?id=default&related=address",
            "allow": ["DELETE","GET"]
        },
    },
    "data": {
        "id": "default",
        "type": "basket",
        "links": {
            "self": {
                "href": "http://localhost:8000/jsonapi/basket?id=default",
                "allow": ["DELETE", "GET", "PATCH", "POST"]
            }
        },
        "attributes": {
            "order.base.id": null,
            "order.base.customerid": "",
            "order.base.sitecode": "",
            "order.base.languageid": "en",
            "order.base.currencyid": "EUR",
            "order.base.price": "0.00",
            "order.base.costs": "0.00",
            "order.base.rebate": "0.00",
            "order.base.comment": ""
        },
        "relationships": {
            "basket.address": {
                "data": [{
                    "type": "basket.address",
                    "id": "payment"
                }]
            }
        }
    },
    "included": [{
        "id": "payment",
        "type": "basket.address",
        "attributes": {
            "order.base.address.id": null,
            "order.base.address.addressid": "...",
            "order.base.address.salutation": "mr",
            "order.base.address.company": "Example company",
            "order.base.address.vatid": "DE12345678",
            "order.base.address.title": "Dr.",
            "order.base.address.firstname": "Test",
            "order.base.address.lastname": "User",
            "order.base.address.address1": "Test street",
            "order.base.address.address2": "1",
            "order.base.address.address3": "",
            "order.base.address.postal": "12345",
            "order.base.address.city": "Test city",
            "order.base.address.state": "HH",
            "order.base.address.countryid": "DE",
            "order.base.address.languageid": "de",
            "order.base.address.telephone": "+4912345678",
            "order.base.address.telefax": "+49123456789",
            "order.base.address.email": "test@example.com",
            "order.base.address.website": "https://example.com",
            "order.base.address.longitude": 10.0,
            "order.base.address.latitude": 50.0,
            "order.base.address.position": 0,
            "order.base.address.type": "payment"
        },
        "links": {
            "self": {
                "href": "http://localhost:8000/jsonapi/basket?id=default&related=address&relatedid=payment",
                "allow": ["DELETE"]
            }
        }
    }]
}
```

Depending on the activated basket plugins, the content of the response can be modified more than that. Especially since the address is often the basis for the available delivery options.

# Update addresses

Replacing existing delivery/payment addresses in the basket with only one request is possible since 2022.07 by using the PATCH request of the basket address resource. It will remove the already available delivery or payment addresses (depending on the `relatedid` parameter) and add the new addresses afterwards from the body sent with the request.

From the previous GET request or the response returned for your last request you know that the URL for modifying the basket delivery address is e.g.:

```
http://localhost:8000/jsonapi/basket?id=default&related=address&relatedid=payment
```

To update the payment address in the current basket you should use:

=== "CURL"
    ```bash
    curl -b cookies.txt -c cookies.txt \
    -X POST 'http://localhost:8000/jsonapi/basket?id=default&related=address&relatedid=payment&_token=...' \
    -H 'Content-Type: application/json' \
    -d '{"data": [{
        "id": "payment",
        "attributes": {
            "order.base.address.addressid": "...",
            "order.base.address.salutation": "mr",
            "order.base.address.company": "Example company",
            "order.base.address.vatid": "DE123456789",
            "order.base.address.title": "Dr.",
            "order.base.address.firstname": "Test",
            "order.base.address.lastname": "User",
            "order.base.address.address1": "Test way",
            "order.base.address.address2": "2",
            "order.base.address.address3": "",
            "order.base.address.postal": "54321",
            "order.base.address.city": "Test town",
            "order.base.address.state": "HH",
            "order.base.address.countryid": "DE",
            "order.base.address.languageid": "de",
            "order.base.address.telephone": "+4912345678",
            "order.base.address.telefax": "+49123456789",
            "order.base.address.email": "test@example.com",
            "order.base.address.website": "https://example.com",
            "order.base.address.longitude": 10.0,
            "order.base.address.latitude": 50.0
        }
    }]}'
    ```
=== "jQuery"
    ```javascript
    var params = {'data': [{
        'id': 'payment', // or 'delivery'
        'attributes': {
            'order.base.address.addressid': '...', // customer address ID (optional)
            'order.base.address.salutation': 'mr', // 'mr', 'mrs', 'miss', 'company' or empty (optional)
            'order.base.address.company': 'Example company', // (optional)
            'order.base.address.vatid': 'DE123456789', // (optional)
            'order.base.address.title': 'Dr.', // (optional)
            'order.base.address.firstname': 'Test', // (optional)
            'order.base.address.lastname': 'User', // (required)
            'order.base.address.address1': 'Test way', // (required)
            'order.base.address.address2': '2', // (optional)
            'order.base.address.address3': '', // (optional)
            'order.base.address.postal': '54321', // (optional)
            'order.base.address.city': 'Test town', // (required)
            'order.base.address.state': 'HH', // (optional)
            'order.base.address.countryid': 'DE', // (optional)
            'order.base.address.languageid': 'de', // (required by many payment gateways)
            'order.base.address.telephone': '+4912345678', // (optional)
            'order.base.address.telefax': '+49123456789', // (optional)
            'order.base.address.email': 'test@example.com', // (required)
            'order.base.address.website': 'https://example.com', // (optional)
            'order.base.address.longitude': 10.0, // (optional, float value)
            'order.base.address.latitude': 50.0 // (optional, float value)
        }
    }]};

    var url = response['included'][0]['links']['self']['href']; // from basket response

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

It's important to add the **id: "delivery"** (or **"payment"**) sent to the server because the value for "id" is the address type.

The response to this request would be similar to this:

```json
{
    "meta": {
        "total": 1,
        "prefix": null,
        "content-baseurl": "/"
    },
    "links": {
        "self": {
            "href": "http://localhost:8000/jsonapi/basket?id=default&related=address",
            "allow": ["DELETE","GET"]
        },
    },
    "data": {
        "id": "default",
        "type": "basket",
        "links": {
            "self": {
                "href": "http://localhost:8000/jsonapi/basket?id=default",
                "allow": ["DELETE", "GET", "PATCH", "POST"]
            }
        },
        "attributes": {
            "order.base.id": null,
            "order.base.customerid": "",
            "order.base.sitecode": "",
            "order.base.languageid": "en",
            "order.base.currencyid": "EUR",
            "order.base.price": "0.00",
            "order.base.costs": "0.00",
            "order.base.rebate": "0.00",
            "order.base.comment": ""
        },
        "relationships": {
            "basket.address": {
                "data": [{
                    "type": "basket.address",
                    "id": "payment"
                }]
            }
        }
    },
    "included": [{
        "id": "payment",
        "type": "basket.address",
        "attributes": {
            "order.base.address.id": null,
            "order.base.address.addressid": "...",
            "order.base.address.salutation": "mr",
            "order.base.address.company": "Example company",
            "order.base.address.vatid": "DE12345678",
            "order.base.address.title": "Dr.",
            "order.base.address.firstname": "Test",
            "order.base.address.lastname": "User",
            "order.base.address.address1": "Test way",
            "order.base.address.address2": "2",
            "order.base.address.address3": "",
            "order.base.address.postal": "54321",
            "order.base.address.city": "Test town",
            "order.base.address.state": "HH",
            "order.base.address.countryid": "DE",
            "order.base.address.languageid": "de",
            "order.base.address.telephone": "+4912345678",
            "order.base.address.telefax": "+49123456789",
            "order.base.address.email": "test@example.com",
            "order.base.address.website": "https://example.com",
            "order.base.address.longitude": 10.0,
            "order.base.address.latitude": 50.0,
            "order.base.address.position": 0,
            "order.base.address.type": "payment"
        },
        "links": {
            "self": {
                "href": "http://localhost:8000/jsonapi/basket?id=default&related=address&relatedid=payment",
                "allow": ["DELETE"]
            }
        }
    }]
}
```

Aimeos also allows several delivery or payment addresses within the basket and there can be more than one delivery or payment address sent in the PATCH request. You can also mix delivery and payment addresses within one PATCH request but only the type passed in `relatedid` ("delivery" or "payment") is removed before the new ones are added.

# Delete addresses

You can also remove addresses from the basket again by using a DELETE request to the URL of the address in the basket. In our example above the URL is:

```
http://localhost:8000/jsonapi/basket?id=default&related=address&relatedid=payment
```

The DELETE request can be constructed in that way:

=== "CURL"
    ```bash
    curl -b cookies.txt -c cookies.txt \
    -X DELETE 'http://localhost:8000/jsonapi/basket?id=default&related=address&relatedid=payment&_token=...'
    ```
=== "jQuery"
    ```javascript
    // basket address URL returned from basket response
    var url = response['included'][0]['links']['self']['href'];

    if(response['meta']['csrf']) { // add CSRF token if available and therefore required
        var csrf = {};
        csrf[response['meta']['csrf']['name']] = response['meta']['csrf']['value'];
        url += (url.indexOf('?') === -1 ? '?' : '&') + $.param(csrf);
    }

    $.ajax({
        url: url,
        method: "DELETE",
        dataType: "json"
    }).done( function( result ) {
        console.log( result );
    });
    ```

This request will remove the address entry from the basket, and the response won't contain the address in the "included" section neither the corresponding "relationships" entry anymore.

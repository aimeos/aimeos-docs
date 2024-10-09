By default you can add a billing and delivery address to the basket. While the delivery address is optional, setting the billing address is almost always mandatory.

# Add addresses

To add one or more addresses you have to pass the data including the "id" and the attributes in a POST request to the server. The "id" is in that case the type of the address, i.e. "payment" for the billing address and "delivery" for the corresponding address.

There are some address attributes that are required when adding or replacing an address:

* order.address.lastname (last name or full name)
* order.address.address1 (most of the time the street name)
* order.address.city (town or city name)
* order.address.languageid (language the customer prefers)
* order.address.email (account e-mail address)

The request for creating a new address in the basket could look like this:

=== "CURL"
    ```bash
    curl -b cookies.txt -c cookies.txt \
    -X POST 'http://localhost:8000/jsonapi/basket?id=default&related=address&_token=...' \
    -H 'Content-Type: application/json' \
    -d '{"data": [{
        "id": "payment",
        "attributes": {
            "order.address.addressid": "...",
            "order.address.salutation": "mr",
            "order.address.company": "Example company",
            "order.address.vatid": "DE123456789",
            "order.address.title": "Dr.",
            "order.address.firstname": "Test",
            "order.address.lastname": "User",
            "order.address.address1": "Test street",
            "order.address.address2": "1",
            "order.address.address3": "",
            "order.address.postal": "12345",
            "order.address.city": "Test city",
            "order.address.state": "HH",
            "order.address.countryid": "DE",
            "order.address.languageid": "de",
            "order.address.telephone": "+4912345678",
            "order.address.telefax": "+49123456789",
            "order.address.email": "test@example.com",
            "order.address.website": "https://example.com",
            "order.address.longitude": 10.0,
            "order.address.latitude": 50.0
        }
    }]}'
    ```
=== "Javascript"
    ```javascript
    const params = {'data': [{
        'id': 'payment', // or 'delivery'
        'attributes': {
            'order.address.addressid': '...', // customer address ID (optional)
            'order.address.salutation': 'mr', // 'mr', 'mrs', 'miss', 'company' or empty (optional)
            'order.address.company': 'Example company', // (optional)
            'order.address.vatid': 'DE123456789', // (optional)
            'order.address.title': 'Dr.', // (optional)
            'order.address.firstname': 'Test', // (optional)
            'order.address.lastname': 'User', // (required)
            'order.address.address1': 'Test street', // (required)
            'order.address.address2': '1', // (optional)
            'order.address.address3': '', // (optional)
            'order.address.postal': '12345', // (optional)
            'order.address.city': 'Test city', // (required)
            'order.address.state': 'HH', // (optional)
            'order.address.countryid': 'DE', // (optional)
            'order.address.languageid': 'de', // (required by many payment gateways)
            'order.address.telephone': '+4912345678', // (optional)
            'order.address.telefax': '+49123456789', // (optional)
            'order.address.email': 'test@example.com', // (required)
            'order.address.website': 'https://example.com', // (optional)
            'order.address.longitude': 10.0, // (optional, float value)
            'order.address.latitude': 50.0 // (optional, float value)
        }
    }]};

    let url = response['links']['basket.address']['href']; // from basket response

    if(response['meta']['csrf']) { // add CSRF token if available and therefore required
        const csrf = {}
        csrf[response['meta']['csrf']['name']] = response['meta']['csrf']['value']
        url += (url.indexOf('?') === -1 ? '?' : '&') + window.param(csrf) // from https://github.com/knowledgecode/jquery-param
    }

    fetch(url, {
        method: "POST",
        body: JSON.stringify(params)
    }).then(result => {
        if(!result.ok) {
            throw new Error(`Response error: ${response.status}`)
        }
        return result.json()
    }).then(result => {
        console.log(result.data)
    })
    ```
=== "jQuery"
    ```javascript
    var params = {'data': [{
        'id': 'payment', // or 'delivery'
        'attributes': {
            'order.address.addressid': '...', // customer address ID (optional)
            'order.address.salutation': 'mr', // 'mr', 'mrs', 'miss', 'company' or empty (optional)
            'order.address.company': 'Example company', // (optional)
            'order.address.vatid': 'DE123456789', // (optional)
            'order.address.title': 'Dr.', // (optional)
            'order.address.firstname': 'Test', // (optional)
            'order.address.lastname': 'User', // (required)
            'order.address.address1': 'Test street', // (required)
            'order.address.address2': '1', // (optional)
            'order.address.address3': '', // (optional)
            'order.address.postal': '12345', // (optional)
            'order.address.city': 'Test city', // (required)
            'order.address.state': 'HH', // (optional)
            'order.address.countryid': 'DE', // (optional)
            'order.address.languageid': 'de', // (required by many payment gateways)
            'order.address.telephone': '+4912345678', // (optional)
            'order.address.telefax': '+49123456789', // (optional)
            'order.address.email': 'test@example.com', // (required)
            'order.address.website': 'https://example.com', // (optional)
            'order.address.longitude': 10.0, // (optional, float value)
            'order.address.latitude': 50.0 // (optional, float value)
        }
    }]};

    var url = response['links']['basket.address']['href']; // from basket response

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
        "content-baseurl": "http://localhost:8000/",
        "content-baseurls": {
            "fs-media": "http://localhost:8000/aimeos",
            "fs-mimeicon": "http://localhost:8000/vendor/shop/mimeicons",
            "fs-theme": "http://localhost:8000/vendor/shop/themes"
        }
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
            "order.id": null,
            "order.customerid": "",
            "order.sitecode": "",
            "order.languageid": "en",
            "order.currencyid": "EUR",
            "order.price": "0.00",
            "order.costs": "0.00",
            "order.rebate": "0.00",
            "order.comment": ""
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
            "order.address.id": null,
            "order.address.addressid": "...",
            "order.address.salutation": "mr",
            "order.address.company": "Example company",
            "order.address.vatid": "DE12345678",
            "order.address.title": "Dr.",
            "order.address.firstname": "Test",
            "order.address.lastname": "User",
            "order.address.address1": "Test street",
            "order.address.address2": "1",
            "order.address.address3": "",
            "order.address.postal": "12345",
            "order.address.city": "Test city",
            "order.address.state": "HH",
            "order.address.countryid": "DE",
            "order.address.languageid": "de",
            "order.address.telephone": "+4912345678",
            "order.address.telefax": "+49123456789",
            "order.address.email": "test@example.com",
            "order.address.website": "https://example.com",
            "order.address.longitude": 10.0,
            "order.address.latitude": 50.0,
            "order.address.position": 0,
            "order.address.type": "payment"
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
            "order.address.addressid": "...",
            "order.address.salutation": "mr",
            "order.address.company": "Example company",
            "order.address.vatid": "DE123456789",
            "order.address.title": "Dr.",
            "order.address.firstname": "Test",
            "order.address.lastname": "User",
            "order.address.address1": "Test way",
            "order.address.address2": "2",
            "order.address.address3": "",
            "order.address.postal": "54321",
            "order.address.city": "Test town",
            "order.address.state": "HH",
            "order.address.countryid": "DE",
            "order.address.languageid": "de",
            "order.address.telephone": "+4912345678",
            "order.address.telefax": "+49123456789",
            "order.address.email": "test@example.com",
            "order.address.website": "https://example.com",
            "order.address.longitude": 10.0,
            "order.address.latitude": 50.0
        }
    }]}'
    ```
=== "Javascript"
    ```javascript
    const params = {'data': [{
        'id': 'payment', // or 'delivery'
        'attributes': {
            'order.address.addressid': '...', // customer address ID (optional)
            'order.address.salutation': 'mr', // 'mr', 'ms', 'miss', 'company' or empty (optional)
            'order.address.company': 'Example company', // (optional)
            'order.address.vatid': 'DE123456789', // (optional)
            'order.address.title': 'Dr.', // (optional)
            'order.address.firstname': 'Test', // (optional)
            'order.address.lastname': 'User', // (required)
            'order.address.address1': 'Test street', // (required)
            'order.address.address2': '1', // (optional)
            'order.address.address3': '', // (optional)
            'order.address.postal': '12345', // (optional)
            'order.address.city': 'Test city', // (required)
            'order.address.state': 'HH', // (optional)
            'order.address.countryid': 'DE', // (optional)
            'order.address.languageid': 'de', // (required by many payment gateways)
            'order.address.telephone': '+4912345678', // (optional)
            'order.address.telefax': '+49123456789', // (optional)
            'order.address.email': 'test@example.com', // (required)
            'order.address.website': 'https://example.com', // (optional)
            'order.address.longitude': 10.0, // (optional, float value)
            'order.address.latitude': 50.0 // (optional, float value)
        }
    }]};

    let url = response['included'][0]['links']['self']['href']; // from basket response

    if(response['meta']['csrf']) { // add CSRF token if available and therefore required
        const csrf = {}
        csrf[response['meta']['csrf']['name']] = response['meta']['csrf']['value']
        url += (url.indexOf('?') === -1 ? '?' : '&') + window.param(csrf) // from https://github.com/knowledgecode/jquery-param
    }

    fetch(url, {
        method: "PATCH",
        body: JSON.stringify(params)
    }).then(result => {
        if(!result.ok) {
            throw new Error(`Response error: ${response.status}`)
        }
        return result.json()
    }).then(result => {
        console.log(result.data)
    })
    ```
=== "jQuery"
    ```javascript
    var params = {'data': [{
        'id': 'payment', // or 'delivery'
        'attributes': {
            'order.address.addressid': '...', // customer address ID (optional)
            'order.address.salutation': 'mr', // 'mr', 'mrs', 'miss', 'company' or empty (optional)
            'order.address.company': 'Example company', // (optional)
            'order.address.vatid': 'DE123456789', // (optional)
            'order.address.title': 'Dr.', // (optional)
            'order.address.firstname': 'Test', // (optional)
            'order.address.lastname': 'User', // (required)
            'order.address.address1': 'Test way', // (required)
            'order.address.address2': '2', // (optional)
            'order.address.address3': '', // (optional)
            'order.address.postal': '54321', // (optional)
            'order.address.city': 'Test town', // (required)
            'order.address.state': 'HH', // (optional)
            'order.address.countryid': 'DE', // (optional)
            'order.address.languageid': 'de', // (required by many payment gateways)
            'order.address.telephone': '+4912345678', // (optional)
            'order.address.telefax': '+49123456789', // (optional)
            'order.address.email': 'test@example.com', // (required)
            'order.address.website': 'https://example.com', // (optional)
            'order.address.longitude': 10.0, // (optional, float value)
            'order.address.latitude': 50.0 // (optional, float value)
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
        "content-baseurl": "http://localhost:8000/",
        "content-baseurls": {
            "fs-media": "http://localhost:8000/aimeos",
            "fs-mimeicon": "http://localhost:8000/vendor/shop/mimeicons",
            "fs-theme": "http://localhost:8000/vendor/shop/themes"
        }
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
            "order.id": null,
            "order.customerid": "",
            "order.sitecode": "",
            "order.languageid": "en",
            "order.currencyid": "EUR",
            "order.price": "0.00",
            "order.costs": "0.00",
            "order.rebate": "0.00",
            "order.comment": ""
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
            "order.address.id": null,
            "order.address.addressid": "...",
            "order.address.salutation": "mr",
            "order.address.company": "Example company",
            "order.address.vatid": "DE12345678",
            "order.address.title": "Dr.",
            "order.address.firstname": "Test",
            "order.address.lastname": "User",
            "order.address.address1": "Test way",
            "order.address.address2": "2",
            "order.address.address3": "",
            "order.address.postal": "54321",
            "order.address.city": "Test town",
            "order.address.state": "HH",
            "order.address.countryid": "DE",
            "order.address.languageid": "de",
            "order.address.telephone": "+4912345678",
            "order.address.telefax": "+49123456789",
            "order.address.email": "test@example.com",
            "order.address.website": "https://example.com",
            "order.address.longitude": 10.0,
            "order.address.latitude": 50.0,
            "order.address.position": 0,
            "order.address.type": "payment"
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
=== "Javascript"
    ```javascript
    // basket address URL returned from basket response
    let url = response['included'][0]['links']['self']['href'];

    if(response['meta']['csrf']) { // add CSRF token if available and therefore required
        const csrf = {}
        csrf[response['meta']['csrf']['name']] = response['meta']['csrf']['value']
        url += (url.indexOf('?') === -1 ? '?' : '&') + window.param(csrf) // from https://github.com/knowledgecode/jquery-param
    }

    fetch(url, {
        method: "DELETE",
    }).then(result => {
        if(!result.ok) {
            throw new Error(`Response error: ${response.status}`)
        }
        return result.json()
    }).then(result => {
        console.log(result.data)
    })
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

You can store arbitrary key/language/value pairs in each customer account for different purposes. The JSON REST API allows you to manage them for the authenticated user.

!!! tip
    The way how a user is authenticated depends very much on the PHP framework you use. Please have a look into the documentation of your framework of choice, e.g. at Laravel [Passport](https://laravel.com/docs/master/passport)/[Sanctum](https://laravel.com/docs/master/sanctum) or Symfony [Guard](https://symfony.com/doc/current/security/guard_authentication.html)).

The customer response returns the URLs for managing properties:

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
        },
        "csrf": {
            "name": "_token",
            "value": "..."
        }
    },
    "links": {
        "self": "http://localhost:8080/jsonapi/customer",
        "customer/property": {
            "href": "http://localhost:8000/jsonapi/customer?id=2&related=property",
            "allow": ["GET","POST"]
        }
    }
}
```

# Fetch properties

Retrieving the properties of a customer requires a GET request to the *customer/property* endpoint returned by the GET request for the [customer](customer.md), e.g.:

=== "CURL"
    ```bash
    curl -b cookies.txt -c cookies.txt \
    -X GET 'http://localhost:8000/jsonapi/customer?related=property'
    ```
=== "Javascript"
    ```javascript
    // from customer response
    fetch(response['links']['customer/property']['href']).then(result => {
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
    $.ajax({
        method: "GET",
        dataType: "json",
        url: response['links']['customer/property']['href'] // from customer response
    }).done( function( result ) {
        console.log( result.data );
    });
    ```

When at least one property is available, the response will be similar to this one:

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
        },
        "csrf": {
            "name": "_token",
            "value": "..."
        }
    },
    "links": {
        "self": "http://localhost:8000/jsonapi/customer?related=property"
    },
    "data": [{
        "id": "1",
        "type": "customer.property",
        "links": {
            "self": {
                "href": "http:\/\/localhost:8000\/jsonapi\/customer?id=2&related=property&relatedid=1",
                "allow": ["DELETE","GET","PATCH"]
            }
        },
        "attributes": {
            "customer.property.id": "1",
            "customer.property.languageid": null,
            "customer.property.value": "1000",
            "customer.property.type": "limit"
        }
    }]
}
```

# Add properties

To add one or more properties to an authenticated customer, use a POST request including the property data. The URL for that request is returned by the GET request to the [customer endpoint](customer.md) and contains a *customer/property* entry in the *links* section:

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
        },
        "csrf": {
            "name": "_token",
            "value": "..."
        }
    },
    "links": {
        "self": "http://localhost:8080/jsonapi/customer",
        "customer/property": {
            "href": "http://localhost:8080/jsonapi/customer?related=property",
            "allow": ["GET","POST"]
        }
    }
}
```

These are the property fields you can use:

* customer.property.type (arbitrary type code, up to 64 bytes)
* customer.property.value (value string , up to 255 bytes)
* customer.property.languageid (two letter ISO language code or null)

The request for creating a new property looks similar to this one:

=== "CURL"
    ```bash
    curl -b cookies.txt -c cookies.txt \
    -X POST 'http://localhost:8000/jsonapi/customer?related=property&_token=...' \
    -H 'Content-Type: application/json' \
    -d '{"data": [{
        "attributes": {
            "customer.property.type": "crm-id",
            "customer.property.languageid": null,
            "customer.property.value": "1234"
        }
    }]}'
    ```
=== "Javascript"
    ```javascript
    let params = {'data': [{
        'attributes': {
            "customer.property.type": "crm-id", // arbitrary type
            "customer.property.languageid": null, // optional
            "customer.property.value": "1234" // string up to 255 bytes
        }
    }]}

    let url = response['links']['customer/property']['href']; // from customer response

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
        'attributes': {
            "customer.property.type": "crm-id", // arbitrary type
            "customer.property.languageid": null, // optional
            "customer.property.value": "1234" // string up to 255 bytes
        }
    }]};

    var url = response['links']['customer/property']['href']; // from customer response

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

# Modify property

Changing one property of an authenticated customer is possible by executing a PATCH request. The URL for updating the property is returned to the response of the GET request which fetches all properties. You can add all property fields or only the modified ones in the PATCH request:

=== "CURL"
    ```bash
    curl -b cookies.txt -c cookies.txt \
    -X PATCH 'http://localhost:8000/jsonapi/customer?related=property&relatedid=...&_token=...' \
    -H 'Content-Type: application/json' \
    -d '{"data": {
        "attributes": {
            "customer.property.value": "4321"
        }
    }}'
    ```
=== "Javascript"
    ```javascript
    let params = {'data': [{
        'attributes': {
            "customer.property.value": "4321"
        }
    }]}

    let url = response['data'][0]['links']['self']['href'] // from customer property response

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
    var params = {'data': {
        'attributes': {
            "customer.property.value": "4321"
        }
    }};

    var url = response['data'][0]['links']['self']['href']; // from customer property response

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

# Delete properties

Removing properties from the user account is also possible by executing a DELETE request to the URL of the property. In our first response above, the URL is:

```
http://localhost:8000/jsonapi/customer?id=2&related=property&relatedid=1
```

The DELETE request can be constructed like this:

=== "CURL"
    ```bash
    curl -b cookies.txt -c cookies.txt \
    -X DELETE 'http://localhost:8000/jsonapi/customer?related=property&relatedid=...&_token=...'
    ```
=== "Javascript"
    ```javascript
    let url = response['data'][0]['links']['self']['href'] // from customer property response

    if(response['meta']['csrf']) { // add CSRF token if available and therefore required
        const csrf = {}
        csrf[response['meta']['csrf']['name']] = response['meta']['csrf']['value']
        url += (url.indexOf('?') === -1 ? '?' : '&') + window.param(csrf) // from https://github.com/knowledgecode/jquery-param
    }

    fetch(url, {
        method: "DELETE"
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
    var url = response['data'][0]['links']['self']['href']; // from customer property response

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

Then, the property entry identified by its ID is removed from the customer account.

To be able to retrieve the basket, you need the basket resource endpoint from the OPTIONS request. Depending on the used routes it might be something like this:

=== "CURL"
    ```bash
    curl -b cookies.txt -c cookies.txt \
    -X OPTIONS 'http://localhost:8000/jsonapi'
    ```
=== "jQuery"
    ```javascript
    $.ajax({
        method: "GET",
        dataType: "json",
        url: 'http://localhost:8000/jsonapi'
    }).done( function( result ) {
        console.log( result.data );
    });
    ```

This will return a response like:

```json
{
    "meta": {
        "csrf": {
            "name": "_token",
            "value": "..."
        },
        "prefix": "ai",
        "resources": {
            "attribute": "http://localhost:8000/jsonapi/attribute",
            "basket": "http://localhost:8000/jsonapi/basket",
            ...
        }
    }
}
```

The "csrf" section in "meta" will be important when you want to modify the basket. Each response will contain such a "csrf" section if the host application supports tokens against cross-site request forgery attacks. If available, you need to send them with every DELETE, PATCH and POST request.

!!! warning
    Don't take the resource URLs in the OPTIONS response as granted! They will change depending on the routes and the application. Thus, your client needs the OPTIONS URL of the JSON REST API as configuration parameter. Its response will define the next possibilities.

# Fetch the basket

To retrieve the current basket content you need to send a GET request to the basket resource like this:

=== "CURL"
    ```bash
    curl -b cookies.txt -c cookies.txt \
    -X GET 'http://localhost:8000/jsonapi/basket'
    ```
=== "jQuery"
    ```javascript
    $.ajax({
        method: "GET",
        dataType: "json",
        url: response.meta.resources['basket'] // returned from OPTIONS request
    }).done( function( result ) {
        console.log( result.data );
    });
    ```

If the basket is empty, it will return only the basic basket properties but no products, addresses, service items or coupons. It is very important that the same session cookie is sent with each request. Otherwise an empty basket is returned for every request regardless of which action you've performed before. The response would be for example:

```json
{
    "meta": {
        "total": 1,
        "prefix": null,
        "content-baseurl": "/",
        "csrf": {
            "name": "_token",
            "value": "..."
        }
    },
    "links": {
        "self": {
            "href": "http://localhost:8000/jsonapi/basket",
            "allow": ["DELETE","GET","PATCH"]
        }
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
            "order.taxvalue": "0.0000",
            "order.taxflag": true,
            "order.comment": "",
            "order.customerref": ""
        },
        "relationships": []
    },
    "included": []
}
```

!!! tip
    You can create multiple baskets by passing different values for the "id" parameter, e.g.
    ```bash
    curl -b cookies.txt -c cookies.txt \
    -X GET 'http://localhost:8000/jsonapi/basket?id=second'
    ```

# Modifiy the basket

There are three values that you can update using a PATCH request to the basket:

* order.customerid (ID of the customer to show the order in her/his account history)
* order.comment (customer comment for this order)
* order.customerref (own reference of the customer for this order)

To update the basket you have to use the "self" link from a previous GET request:

=== "CURL"
    ```bash
    curl -X PATCH 'http://localhost:8000/jsonapi/basket?id=default&_token=...' \
    -H 'Content-Type: application/json' \
    -b cookies.txt -c cookies.txt \
    -d '{"data": {
        "attributes": {
            "order.customerid": "...",
            "order.comment": "test comment",
            "order.customerref": "ABCD-1234"
        }
    }}'
    ```
=== "jQuery"
    ```javascript
    var params = {'data': {
        'attributes': {
            'order.customerid': '...', // from customer response (optional)
            'order.comment': 'test comment', // (optional)
            'order.customerref': 'ABCD-1234' // (optional)
        }
    }};

    var url = response.links.self.href; // from basket response

    if(response['meta']['csrf']) { // add CSRF token if available and therefore required
        var csrf = {};
        csrf[response['meta']['csrf']['name']] = response['meta']['csrf']['value'];
        url += (url.indexOf('?')= -1 ? '?' : '&') + $.param(csrf);
    }

    $.ajax({
        url: url, // returned from OPTIONS request
        method: "PATCH",
        dataType: "json",
        data: params
    }).done( function( result ) {
        console.log( result.data );
    });
    ```

The response will be the same as for the GET request but the attributes are updated to the new values.

# Clear the basket

Removing all items and properties from the basket (effectively wiping out the basket content) is done by sending a DELETE request to the basket resource:

=== "CURL"
    ```bash
    curl -b cookies.txt -c cookies.txt \
    -X DELETE 'http://localhost:8000/jsonapi/basket?id=default&_token=...'
    ```
=== "jQuery"
    ```javascript
    var url = response.links.self.href; // from basket response

    if(response['meta']['csrf']) { // add CSRF token if available and therefore required
        var csrf = {};
        csrf[response['meta']['csrf']['name']] = response['meta']['csrf']['value'];
        url += (url.indexOf('?')= -1 ? '?' : '&') + $.param(csrf);
    }

    $.ajax({
        url: url, // returned from OPTIONS request
        method: "DELETE",
        dataType: "json"
    }).done( function( result ) {
        console.log( result.data );
    });
    ```

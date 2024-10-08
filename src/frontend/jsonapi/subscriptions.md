Customers can view and delete their own subscriptions using the JSON REST API, but they need to authenticate themselves first. Creating subscriptions is only possible by buying a subscription product. Modifying subscriptions by the user is not allowed for security reasons.

!!! tip
    The way how a user is authenticated depends very much on the PHP framework you use. Please have a look into the documentation of your framework of choice, e.g. at Laravel [Passport](https://laravel.com/docs/master/passport)/[Sanctum](https://laravel.com/docs/master/sanctum) or Symfony [Guard](https://symfony.com/doc/current/security/guard_authentication.html).

Before you can retrieve the available subscriptions, you must get the resource endpoint via the OPTIONS request. Depending on the used routes it might be something like this:

```bash
curl -X OPTIONS 'http://localhost:8000/jsonapi'
```

The customer response returns the URLs for managing subscriptions:

```json
{
    "meta": {
        "prefix": null,
        "resources": {
            "subscription": "http://localhost:8000/jsonapi/subscription"
        }
    }
}
```

# Fetch subscriptions

Retrieving the subscriptions of the customer requires a GET request to the *subscription* endpoint, e.g.:

=== "CURL"
    ```bash
    curl -b cookies.txt -c cookies.txt \
    -X GET 'http://localhost:8000/jsonapi/subscription'
    ```
=== "Javascript"
    ```javascript
    fetch(response['links']['subscription']['href']).then(result => {
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
        url: response['links']['subscription']['href']
    }).done( function( result ) {
        console.log( result.data );
    });
    ```

When at least one subscription is available, the response will be similar to this one:

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
        "self": "http://localhost:8000/jsonapi/subscription"
    },
    "data": [{
        "id": "1",
        "type": "subscription",
        "links": {
            "self": {
                "href": "http://localhost:8000/jsonapi/subscription?id=1",
                "allow": ["DELETE","GET"]
            }
        },
        "attributes": {
            "subscription.orderid": "1",
            "subscription.ordprodid": "2",
            "subscription.productid": "3",
            "subscription.datenext": "2000-01-01 00:00:00",
            "subscription.dateend": null,
            "subscription.interval": "P0Y1M0D0H",
            "subscription.period": 1,
            "subscription.status": 1,
            "subscription.reason": null
        }
    }]
}
```

# Delete subscriptions

Removing subscriptions from the user account is also possible by executing a DELETE request to the URL of the subscription. In the response from the GET request, the URL is:

```
http://localhost:8000/jsonapi/subscription?id=1
```

You can build a DELETE request like this:

=== "CURL"
    ```bash
    curl -b cookies.txt -c cookies.txt \
    -X DELETE 'http://localhost:8000/jsonapi/subscription?id=1&_token=...'
    ```
=== "Javascript"
    ```javascript
    let url = response['data'][0]['links']['self']['href'] // from customer subscription response

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
    var url = response['data'][0]['links']['self']['href']; // from customer subscription response

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

Then, the subscription identified by its ID is removed from the customer's account.

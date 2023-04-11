# Add coupons

Coupon (or voucher) codes can be added to the basket by using the "basket.coupon" URL that is sent with every basket response. The data objects only need the code passed in the "id" parameter like this:

=== "CURL"
    ```bash
    curl -b cookies.txt -c cookies.txt \
    -X POST 'http://localhost:8000/jsonapi/basket?id=default&related=coupon&_token=...' \
    -H 'Content-Type: application/json' \
    -d '{"data": [{
        "id": "fixed"
    }]}'
    ```
=== "jQuery"
    ```javascript
    var params = {"data": [{
        "id": "fixed", // coupon code entered by the customer
    }]};

    var url = response['links']['basket.coupon']['href']; // from basket response

    if(response['meta']['csrf']) { // add CSRF token if available and therefore required
        var csrf = {};
        csrf[response['meta']['csrf']['name']] = response['meta']['csrf']['value'];
        url += (url.indexOf('?') === -1 ? '?' : '&') + $.param(csrf);
    }

    $.ajax({
        url: url,
        method: "POST",
        dataType: "json",
        data: JSON.stringify(data)
    }).done( function( result ) {
        console.log( result );
    });
    ```

The response will then contain a new "relationships" section in the basket data as well as a new entry with the coupon code in the "included" section:

```json
{
    "meta": {
        "total": 1,
        "prefix": null,
        "content-baseurl": "/"
    },
    "links": {
        "self": {
            "href": "http://localhost:8000/jsonapi/basket?id=default&related=coupon",
            "allow": ["DELETE","GET"]
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
            "order.status": 0,
            "order.comment": ""
        },
        "relationships": {
            "basket.coupon": {
                "data": [{
                    "type": "basket.coupon",
                    "id": "fixed"
                }]
            }
        }
    },
    "included": [{
        "id": "fixed",
        "type": "basket.coupon"
        },
        "links": {
            "self": {
                "href": "http://localhost:8000/jsonapi/basket?id=default&related=coupon&relatedid=fixed",
                "allow": ["DELETE"]
            }
        }
    }]
}
```

Depending on the coupon code, there will be more changes to the basket. They can modify the shipping costs, add rebate products that reduce the price or perform other modifications to the basket.

If a coupon code does require one or more prerequisites, and they aren't matched, only the coupon entry will be part of the basket response. As soon as changes to the basket content fulfill the coupon requirements, the changes implemented by the corresponding coupon provider are automatically applied to the basket.

# Delete coupons

Removing coupons from the basket is done by using a DELETE request to the URL of the coupon entry in the basket. In our example above the URL is:

```
http://localhost:8000/jsonapi/basket?id=default&related=coupon&relatedid=fixed
```

Deleting the coupon again would be:


=== "CURL"
    ```bash
    curl -b cookies.txt -c cookies.txt \
    -X DELETE 'http://localhost:8000/jsonapi/basket?id=default&related=coupon&relatedid=fixed&_token=...'
    ```
=== "jQuery"
    ```javascript
    // basket coupon URL returned from basket response
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

This will remove the coupon entry from the basket and revert all changes that have been done by the corresponding coupon provider.

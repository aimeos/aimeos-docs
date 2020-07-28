To be able to retrieve the basket, you need the basket resource endpoint from the OPTIONS request. Depending on the used routes it might be something like:

```bash
curl -X OPTIONS https://localhost:8000/jsonapi
```

```json
{
    "meta": {
        "csrf": {
            "name": "_token",
            "value": "..."
        },
        "prefix": "ai",
        "resources": {
            "attribute": "https://localhost:8000/jsonapi/attribute",
            "basket": "https://localhost:8000/jsonapi/basket",
            ...
        }
    }
}
```


The "csrf" section in "meta" will be important when you want to modify the basket. Each response will contain such a "csrf" section if the host application supports tokens against cross-site request forgery attacks. If available, you need to send them with every DELETE, PATCH and POST request.

!!! warning
    Don't take the resource URLs in the OPTIONS response as granted! They will change depending on the routes and the application. Thus, your client needs the OPTIONS URL of the JSON REST API as configuration parameter. It's response will define the next possibilities.

# Fetch the basket

To retrieve the current basket content, you need to send a GET request to the basket resource like this:

=== "CURL"
	```bash
	curl -X GET https://localhost:8000/jsonapi/basket?id=default
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

If the basket is empty, it will return only the basic basket properties but no products, addresses, service items or coupons. Important is that the same session cookie is sent with each request, which is normally the case. Otherwise, an empty basket is returned for every request. The response would be for example:

```json
{
    "meta": {
        "total": 1,
        "prefix": null,
        "content-baseurl": "/",
        "csrf": {
                "name": "_token",
                "value": ""
            }
    },
    "links": {
        "self": {
            "href": "http://localhost:8000/jsonapi/basket",
            "allow": ["DELETE","GET","PATCH"]
        },
        // ...
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
            "order.base.taxvalue": "0.0000",
            "order.base.taxflag": true,
            "order.base.comment": "",
            "order.base.customerref": ""
        },
        "relationships": []
    },
    "included": []
}
```

!!! tip
    You can create multiple baskets by passing different values for the "id" parameter, e.g.
	```bash
	curl -X GET https://localhost:8000/jsonapi/basket?id=second
	```

# Modifiy the basket

There are three values that you can update using a PATCH request to the basket:

* order.base.customerid (ID of the customers to show the order in their account history)
* order.base.comment (customer comment for this order)
* order.base.customerref (own reference of the customer for this order)

The update the basket, you have to use the "self" link from a previous GET request:

=== "CURL"
	```bash
	curl -X PATCH https://localhost:8000/jsonapi/basket?id=default&_token=... \
	-H "Content-Type: application/json"
	-d '{data: { \
		attributes: { \
			"order.base.customerid": '...', \
			"order.base.comment": "test comment", \
			"order.base.customerref": "ABCD-1234" \
		} \
	}}'
	```
=== "jQuery"
	```javascript
	var params = {data: {
		attributes: {
			"order.base.customerid": '...', // from customer response (optional)
			"order.base.comment": "test comment", // (optional)
			"order.base.customerref": "ABCD-1234" // (optional)
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

Removing all items and properties from the basket (effectively wiping out the basket content) is done by doing a DELETE request to the basket resource:

=== "CURL"
	```bash
	curl -X DELETE https://localhost:8000/jsonapi/basket?id=default&_token=...
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

Products can be added and removed from the basket as well as some attributes of each product entry in the basket changed. For the start, you need to [fetch one or more products](basics.md) using the product resource from the [OPTIONS response](index.md):

```bash
curl -X GET http://localhost:8000/jsonapi/product
```

Each listed product will contain the link how it could be added to the basket:

```json
{
    "meta": {
        // ...
    },
    "links": {
        "self": "http://localhost/jsonapi/product"
    },
    "data": [{
        "id": "1",
        "type": "product",
        "links": {
            "self": {
                "href": "http://localhost/default/jsonapi/product?id=1",
                "allow": ["GET"]
            },
            "basket\/product": {
                "href": "http://localhost/default/jsonapi/basket?id=default&related=product",
                "allow": ["POST"]
            }
        },
        "attributes": {
            // ...
        }
}
```

The URL to add the product to the basket is in

```javascript
data[0]['links']['basket/product']['href']
```

!!! warning
    Don't take these URLs for granted! They change depending on the route configration and the application.

# Add products

When adding a product to the basket, you can specify some more attributes than just the product ID. Besides the quantity (amount of products in the basket), there are a number of optional attributes:

stocktype
: Warehouse or local store where the product is available

variant
: List of product attribute IDs that uniquely determine the article of a selection product

config
: Additional options the customer can buy for this product

custom
: Map of attribute ID and custom value pairs for data entered by the customer (e.g. text)

To add a product to the basket may look like this:

=== "CURL"
	```bash
	curl -X POST http://localhost:8000/jsonapi/basket?id=default&_token=... \
	-H "Content-Type: application/json"
	-d '{data: [{ \
		attributes: { \
			"product.id": "...", \
			quantity: 1, \
			stocktype: "default" \
		} \
	}]}'
	```
=== "jQuery"
	```javascript
	var data = {data: [{
		attributes: {
			"product.id": '...', // from product response
			quantity: 1, // optional
			stocktype: "default", // warehouse code (optional)
		}
	}]};

	var url = response['data'][0]['links']['basket/product']['href']; // from product response

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

Then, the response will contain an additional "relationships" entry in the basket data that points to the order product entry in the "included" section:

```json
{
    "meta": {
        "total": 1,
        "prefix": null,
        "content-baseurl": "/"
    },
    "links": {
        "self": {
            "href": "http://127.0.0.1:8000/jsonapi/basket/default/product/",
            "allow": ["DELETE","GET","PATCH"]
        },
        // ...
    },
    "data": {
        "id": "default",
        "type": "basket",
        "links": {
            "self": {
                "href": "http://127.0.0.1:8000/jsonapi/basket/default",
                "allow": ["DELETE", "GET", "PATCH", "POST"]
            }
        },
        "attributes": {
            "order.base.id": null,
            "order.base.customerid": "",
            "order.base.sitecode": "",
            "order.base.languageid": "en",
            "order.base.currencyid": "EUR",
            "order.base.price": "100.00",
            "order.base.costs": "5.00",
            "order.base.rebate": "0.00",
            "order.base.status": 0,
            "order.base.comment": ""
        },
        "relationships": {
            "basket\/product": {
                "data": [{
                    "type": "basket\/product",
                    "id": 0
                }]
            }
        }
    },
    "included": [{
        "id": 0,
        "type": "basket\/product",
        "attributes": {
            "order.base.product.id": null,
            "order.base.product.type": "default",
            "order.base.product.stocktype": "default",
            "order.base.product.suppliercode": "",
            "order.base.product.productid": "7",
            "order.base.product.prodcode": "demo-article",
            "order.base.product.name": "Demo article",
            "order.base.product.mediaurl": "http:\/\/demo.aimeos.org\/media\/1.jpg",
            "order.base.product.position": null,
            "order.base.product.price": "100.00",
            "order.base.product.costs": "5.00",
            "order.base.product.rebate": "0.00",
            "order.base.product.taxrate": "20.00",
            "order.base.product.quantity": 1,
            "order.base.product.status": -1,
            "order.base.product.flags": 0
        },
        "links": {
            "self": {
                "href": "http://localhost:8000/jsonapi/basket?id=default&related=product&relatedid=0",
                "allow": ["DELETE", "PATCH"]
            }
        }
    }]
}
```

For selection products, you have to pass the IDs of the variant attributes too, so the concrete article can be identified:

=== "CURL"
	```bash
	curl -X POST http://localhost:8000/jsonapi/basket?id=default&_token=... \
	-H "Content-Type: application/json"
	-d '{data: [{ \
		attributes: { \
			"product.id": "...", \
			variant: ["...", "..."], \
		} \
	}]}'
	```
=== "jQuery"
	```javascript
	var data = {data: [{
		attributes: {
			"product.id": '...', // from product response
			variant: [], // variant attribute IDs for selection products
		}
	}]};

	var url = response['data'][0]['links']['basket/product']['href']; // from product response

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

If the product contains configurable attributes which the customer can optionally choose from, the IDs of these configurable attributes and their quantities must be passed like this:

=== "CURL"
	```bash
	curl -X POST http://localhost:8000/jsonapi/basket?id=default&_token=... \
	-H "Content-Type: application/json"
	-d '{data: [{ \
		attributes: { \
			"product.id": "...", \
			config: {"...": 2, "...": 1}, \
		} \
	}]}'
	```
=== "jQuery"
	```javascript
	var data = {data: [{
		attributes: {
			"product.id": '...', // from product response
			config: { // config attribute IDs/quantity pairs
				"...": 2,
				"...": 1
			},
		}
	}]};

	var url = response['data'][0]['links']['basket/product']['href']; // from product response

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

Custom attributes are a way to add values like a date, a text or even a custom price to an ordered product. The IDs and values of custom attribute must be passed as key/value pairs:

=== "CURL"
	```bash
	curl -X POST http://localhost:8000/jsonapi/basket?id=default&_token=... \
	-H "Content-Type: application/json"
	-d '{data: [{ \
		attributes: { \
			"product.id": "...", \
			custom: { \
				"...", "2020-01-01", \
				"...", "100.00", \
				"...", "Happy birthday" \
			}, \
		} \
	}]}'
	```
=== "jQuery"
	```javascript
	var data = {data: [{
		attributes: {
			"product.id": '...', // from product response
			custom: { // custom attribute ID/value pairs
				"...", "2020-01-01",
				"...", "100.00",
				"...", "Happy birthday"
			}
		}
	}]};

	var url = response['data'][0]['links']['basket/product']['href']; // from product response

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

The attributes will also be updated to reflect the price of the products in the basket.

# Edit products

To edit already added products in the basket, you can send a PATCH request to the URL listed in the links section of the ordered product. In the response before it's:

```
http://localhost:8000/jsonapi/basket?id=default&related=product&relatedid=0
```

Based on this URL, you can change the quanity of the product in the basket:

quantity
: Amount of products that should be bought

Editing products in the basket should be similar to this one:

=== "CURL"
	```bash
	curl -X PATCH http://localhost:8000/jsonapi/basket?id=default&related=product&relatedid=0&_token=... \
	-H "Content-Type: application/json"
	-d '{data: [{ \
		attributes: { \
			quantity: 2 \
			stocktype: "default" \
		} \
	}]}'
	```
=== "jQuery"
	```javascript
	var params = {data: {
		attributes: {
			quantity: 2,
			stocktype: "default" // optional
		}
	}};

	// basket product URL returned from basket response
	var url = response['included'][0]['links']['self']['href'],

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

The PATCH requests will change primarily the product data in the basket. Depending on the activated basket plugins, they can also lead to additional or less entries in the response:

```json
{
    "meta": {
        "total": 1,
        "prefix": "null",
        "content-baseurl": "/"
    },
    "links": {
        "self": {
            "href": "http://127.0.0.1:8000/jsonapi/basket/default/product/",
            "allow": ["DELETE","GET","PATCH"]
        },
        // ...
    },
    "data": {
        "id": "default",
        "type": "basket",
        "links": {
            "self": {
                "href": "http://127.0.0.1:8000/jsonapi/basket/default",
                "allow": ["DELETE", "GET", "PATCH", "POST"]
            }
        },
        "attributes": {
            "order.base.id": null,
            "order.base.customerid": "",
            "order.base.sitecode": "",
            "order.base.languageid": "en",
            "order.base.currencyid": "EUR",
            "order.base.price": "200.00",
            "order.base.costs": "10.00",
            "order.base.rebate": "0.00",
            "order.base.status": 0,
            "order.base.comment": ""
        },
        "relationships": {
            "basket\/product": {
                "data": [{
                    "type": "basket\/product",
                    "id": 0
                }]
            }
        }
    },
    "included": [{
        "id": 0,
        "type": "basket\/product",
        "attributes": {
            "order.base.product.id": null,
            "order.base.product.type": "default",
            "order.base.product.stocktype": "default",
            "order.base.product.suppliercode": "",
            "order.base.product.productid": "7",
            "order.base.product.prodcode": "demo-article",
            "order.base.product.name": "Demo article",
            "order.base.product.mediaurl": "http:\/\/demo.aimeos.org\/media\/1.jpg",
            "order.base.product.position": null,
            "order.base.product.price": "100.00",
            "order.base.product.costs": "5.00",
            "order.base.product.rebate": "0.00",
            "order.base.product.taxrate": "20.00",
            "order.base.product.quantity": 2,
            "order.base.product.status": -1,
            "order.base.product.flags": 0
        },
        "links": {
            "self": {
                "href": "http://localhost:8000/jsonapi/basket?id=default&related=product&relatedid=0",
                "allow": ["DELETE", "PATCH"]
            }
        }
    }]
}
```


The response only contains the updated product and basket details in this example.

# Delete products

Removing product entries from the basket is done by using a DELETE request to the URL of the ordered product. In our example before, the URL is:

```
http://localhost:8000/jsonapi/basket?id=default&related=product&relatedid=0
```

The code for the DELETE request itself is fairly simple:

=== "CURL"
	```bash
	curl -X DELETE http://localhost:8000/jsonapi/basket?id=default&related=product&relatedid=0&_token=...
	```
=== "jQuery"
	```javascript
	// basket product URL returned from basket response
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


Afterwards, the product in the basket identified by the URL is removed from the basket. Depending on the activated basket plugins, more changes might have happened.

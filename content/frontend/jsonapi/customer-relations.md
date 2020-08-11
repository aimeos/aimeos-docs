Each customer account can store relations to other domains for different purposes, e.g. for favorite or watched products . The JSON REST API allows you to manage them for the authenticated user.

!!! tip
    How to authenticate the user depends on the used PHP framework. Please have a look into the documentation of your used framework, e.g. at [Laravel Passport](https://laravel.com/docs/master/passport).

The customer response can return more than the URLs for managing relations, it can also include the related items itself. Add the *include* parameter with the domain of the items you want to fetch, e.g. *&include=product* to get:

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
		"self": "http://localhost:8080/jsonapi/customer",
		"customer/relationships": {
			"href": "http://localhost:8000/jsonapi/customer?id=2&related=relationships",
			"allow": ["GET","POST"]
		},
		// ...
	},
	"data": {
		"id": "2",
		"type": "customer",
		"links": {
			"self": {
				"href": "http:\/\/localhost:8000\/jsonapi\/customer?id=2",
				"allow": ["DELETE","GET","PATCH"]
			}
		},
		"attributes": {
			// ...
		},
		"relationships": {
			// ...
			"product": {
				"data": [{
					"id": "1",
					"type": "product",
					"attributes": {
						"customer.lists.id": "1",
						"customer.lists.domain": "product",
						"customer.lists.refid": "1",
						"customer.lists.datestart": null,
						"customer.lists.dateend": null,
						"customer.lists.config": [],
						"customer.lists.position": 0,
						"customer.lists.status": 1,
						"customer.lists.type": "favorite"
					},
					"links": {
						"self": {
							"href": "http:\/\/localhost:8000\/jsonapi\/product?id=2&related=relationships&relatedid=1",
							"allow": ["DELETE","PATCH"]
						}
					}
				}]
			}
		}
	},
	"included": [{
		"id": "1",
		"type": "product",
		"attributes": {
			"product.id": "1",
			"product.type": "default",
			"product.code": "demo-article",
			"product.label": "Demo article",
			"product.status": 1,
			"product.dataset": "",
			"product.datestart": null,
			"product.dateend": null,
			"product.config": [],
			"product.target": "",
			"product.ctime": "2020-07-28 08:41:18"
		}
	}]
}
```

# Fetch relations

To get the relations only, use a GET request to the *customer/relationships* endpoint returned by the reponse of the [customer](customer.md) request, e.g.:

=== "CURL"
	```bash
	curl -b cookies.txt -c cookies.txt \
	-X GET 'http://localhost:8000/jsonapi/customer?related=relationships&include=product'
	```
=== "jQuery"
	```javascript
	var url = response['links']['customer/relationships']['href']; // from customer response
	var $params = {include: "product"};

	if(options.meta.prefix) { // returned from OPTIONS call
		params[options.meta.prefix] = params;
	}

	$.ajax({
		url: url,
		method: "GET",
		dataType: "json"
	}).done( function( result ) {
		console.log( result.data );
	});
	```

!!! note
    Don't forget to add the *include* parameter to specify which domain items you want to retrieve. If you forget that parameter, no relations are returned even if there are items referenced by the customer account!

The response will look like this one if at least one relationship is available:

```json
{
	"meta": {
		"total": 2,
		"prefix": null,
		"content-baseurl": "http://localhost:8000/",
		"csrf": {
			"name": "_token",
			"value": "pKauLfPXgUoMbsxtrRwRi43BsfVHYgjzBtQqPQXI"
		}
	},
	"links": {
		"self": "http://localhost:8000/jsonapi/customer?related=relationships&include=product",
		"related": "http://localhost:8000/jsonapi/customer?related=relationships&include=product"
	},
	"data": [{
		"id": "1",
		"type": "customer\/lists",
		"links": {
			"self": {
				"href": "http:\/\/localhost:8000\/jsonapi\/customer?id=2&related=relationships&relatedid=1",
				"allow": ["DELETE","GET","PATCH"]
			}
		},
		"attributes": {
			"customer.lists.id": "3",
			"customer.lists.domain": "product",
			"customer.lists.refid": "1",
			"customer.lists.datestart": null,
			"customer.lists.dateend": null,
			"customer.lists.config": [],
			"customer.lists.position": 0,
			"customer.lists.status": 1,
			"customer.lists.type": "favorite"
		}
	}]
}
```

# Add relations

To add one or more relations to the authenticated customer, use a POST request including the relationship data, i.e. the data for the list item. The URL for that request is returned by the GET request to the [customer endpoint](customer.md) and contains a *customer/relationships* entry in the *links* section:

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
		"self": "http://localhost:8080/jsonapi/customer?id=2",
		"customer/relationships": {
			"href": "http://localhost:8000/jsonapi/customer?id=2&related=relationships",
			"allow": ["GET","POST"]
		},
		// ...
	},
	// ...
```

The fields that can be populated are:

customer.lists.domain
: Domain code up to 32 bytes, required

customer.lists.type
: Type code up to 64 bytes, "default" if no value is passed

customer.lists.refid
: ID of the referenced domain item up to 36 bytes, required

customer.lists.datestart
: ISO datetime in "YYYY-MM-DD HH:mm:ss" format or null

customer.lists.dateend
: ISO datetime in "YYYY-MM-DD HH:mm:ss" format or null

customer.lists.config
: Object of key/value pairs up to 64k bytes

customer.lists.position
: Position in the list of relations, integer value

customer.lists.status
: Status of the relation, integer value (-2:archived, -1:review, 0:disabled, 1:enabled)

The request for creating a new relation looks similar to this one:

=== "CURL"
	```bash
	curl -b cookies.txt -c cookies.txt \
	-X POST 'http://localhost:8000/jsonapi/customer?related=relationships&_token=...' \
	-H 'Content-Type: application/json' \
	-d '{"data": [{
		"attributes": {
			"customer.lists.domain": "service",
			"customer.lists.type": "default",
			"customer.lists.refid": "1234",
			"customer.lists.datestart": null,
			"customer.lists.dateend": "2022-01-01 00:00:00",
			"customer.lists.config": {
				"token": "..."
			},
			"customer.lists.position": 0,
			"customer.lists.status": 1
		}
	}]}'
	```
=== "jQuery"
	```javascript
	var params = {'data': [{
		'attributes': {
			"customer.lists.domain": "service",
			"customer.lists.type": "default",
			"customer.lists.refid": "1234",
			"customer.lists.datestart": null,
			"customer.lists.dateend": "2022-01-01 00:00:00",
			"customer.lists.config": {
				"token": "..."
			},
			"customer.lists.position": 0,
			"customer.lists.status": 1
		}
	}]};

	var url = response['links']['customer/relationships']['href']; // from customer response

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

!!! note
    If you want to get the created relationship back, add the *include* parameter with the domain you have added the item for.

## Favorite products

To add a product as favorite to the customer account, use:

=== "CURL"
	```bash
	curl -b cookies.txt -c cookies.txt \
	-X POST 'http://localhost:8000/jsonapi/customer?related=relationships&_token=...' \
	-H 'Content-Type: application/json' \
	-d '{"data": [{
		"attributes": {
			"customer.lists.domain": "product",
			"customer.lists.type": "favorite",
			"customer.lists.refid": "123",
			"customer.lists.datestart": null,
			"customer.lists.dateend": null,
			"customer.lists.config": {},
			"customer.lists.position": 0,
			"customer.lists.status": 1
		}
	}]}'
	```
=== "jQuery"
	```javascript
	var params = {'data': [{
		'attributes': {
			"customer.lists.domain": "product",
			"customer.lists.type": "favorite",
			"customer.lists.refid": "123",
			"customer.lists.datestart": null,
			"customer.lists.dateend": null,
			"customer.lists.config": {},
			"customer.lists.position": 0,
			"customer.lists.status": 1
		}
	}]};

	var url = response['links']['customer/relationships']['href']; // from customer response

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

## Watched product

Customers can register themselves to get notified by e-mail when the price of a product decreases or if the product is back in stock again. The key/value pairs required in the *customer.lists.config* for watched products are:

timeframe
: Maximum number of days the customer wants to get notified

stock
: "1" to notify the customer when the product is back in stock

price
: "1" to notify the customer when the price of the product decreases

currency
: Three letter ISO currency code of the price limit

pricevalue
: Value of the price limit for the currency

=== "CURL"
	```bash
	curl -b cookies.txt -c cookies.txt \
	-X POST 'http://localhost:8000/jsonapi/customer?related=relationships&_token=...' \
	-H 'Content-Type: application/json' \
	-d '{"data": [{
		"attributes": {
			"customer.lists.domain": "product",
			"customer.lists.type": "watch",
			"customer.lists.refid": "123",
			"customer.lists.datestart": null,
			"customer.lists.dateend": null,
			"customer.lists.config": {
				"timeframe": "7",
				"stock": "1",
				"price": "1",
				"currency": "EUR",
				"pricevalue": "100.00"
			},
			"customer.lists.position": 0,
			"customer.lists.status": 1
		}
	}]}'
	```
=== "jQuery"
	```javascript
	var params = {'data': [{
		'attributes': {
			"customer.lists.domain": "product",
			"customer.lists.type": "watch",
			"customer.lists.refid": "123",
			"customer.lists.datestart": null,
			"customer.lists.dateend": null,
			"customer.lists.config": {
				"timeframe": "7",
				"stock": "1",
				"price": "1",
				"currency": "EUR",
				"pricevalue": "100.00"
			},
			"customer.lists.position": 0,
			"customer.lists.status": 1
		}
	}]};

	var url = response['links']['customer/relationships']['href']; // from customer response

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

# Modify relations

To change a relation of the authenticated customer, perform a PATCH request. The URL for updating the relation is returned in the response of the GET request which fetches all relations. You can add all fields or only the modified ones of a relation in the PATCH request:

=== "CURL"
	```bash
	curl -b cookies.txt -c cookies.txt \
	-X PATCH 'http://localhost:8000/jsonapi/customer?related=relationships&relatedid=...&_token=...' \
	-H 'Content-Type: application/json' \
	-d '{"data": {
		"attributes": {
			"customer.lists.config": {
				"timeframe": "28",
				"stock": "1",
				"price": "1",
				"currency": "EUR",
				"pricevalue": "100.00"
			}
		}
	}}'
	```
=== "jQuery"
	```javascript
	var params = {'data': {
		'attributes': {
			"customer.lists.config": {
				"timeframe": "28",
				"stock": "1",
				"price": "1",
				"currency": "EUR",
				"pricevalue": "100.00"
			}
		}
	}};

	var url = response['data'][0]['links']['self']['href']; // from customer relationships response

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

!!! note
    Be aware that the *customer.lists.ctime" value is used as start point for the number of days a product is watched. If a customer wants to renew getting notified for changes, it's better to remove and add the relation again.

# Delete relations

Removing relations from the user account is possible by performing a DELETE request to the URL of the relation. In our first response above, the URL is:

```
http://localhost:8000/jsonapi/customer?id=2&related=relationships&relatedid=1
```

A DELETE request is performed by:


=== "CURL"
	```bash
	curl -b cookies.txt -c cookies.txt \
	-X DELETE 'http://localhost:8000/jsonapi/customer?related=relationships&relatedid=...&_token=...'
	```
=== "jQuery"
	```javascript
	var url = response['data'][0]['links']['self']['href']; // from customer relationships response

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

Then, the relation entry identified by its ID is removed from the customer account.

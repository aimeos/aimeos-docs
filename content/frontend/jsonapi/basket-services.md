Most of the time, you want to offer some delivery and payment options to your customers or at least one. Even if you don't show the only delivery or payment option, you need to add it to the basket so the process after creating the order continues as expected.

# List shipping/payment options

At first, you need to get the available delivery and payment options from the services resource URL listed in the OPTIONS request. With URL, you can query for the available services, either all together in one request or separated by their type ("delivery" or "payment"). The example code below will return all payment options:

=== "CURL"
	```bash
	curl -X GET http://localhost:8000/jsonapi/service?filter[cs_type]=payment&include=text,price,media
	curl -X GET http://localhost:8000/jsonapi/service?ai[filter][cs_type]=payment&ai[include]=text,price,media
	```
=== "jQuery"
	```javascript
	var params = {
		filter: {
			cs_type: "payment" // or "delivery" (optional)
		},
		include: "text,price,media"
	};

	if(options.meta.prefix) { // returned from OPTIONS call
		params[options.meta.prefix] = params;
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

This returns the list of payment or delivery options (or both if the "filter" parameter is omitted) including the associated texts, price and images due to the "included" parameter:

```json
{
	"meta": {
		"total": 9,
		"prefix": "null",
		"content-baseurl": "/"
	},
	"links": {
		"self": "http://localhost:8000/jsonapi/service"
	},
	"data": [{
		"id": "10",
		"type": "service",
		"links": {
			"self": {
				"href": "http://localhost:8000/jsonapi/service?id=10",
				"allow": ["GET"]
			},
			"basket/service": {
				"href": "http://localhost:8000/jsonapi/basket?id=default&related=service",
				"allow": ["POST"],
				"meta": []
			}
		},
		"attributes": {
			"service.id": "10",
			"service.typename": "Delivery",
			"service.type": "delivery",
			"service.code": "demo-dhl",
			"service.label": "DHL",
			"service.provider": "Manual,Reduction",
			"service.position": 0,
			"service.status": 1,
			"price": {
				"price.id": "71",
				"price.type": "default",
				"price.typename": "Standard",
				"price.currencyid": "EUR",
				"price.domain": "service",
				"price.quantity": 1,
				"price.value": "0.00",
				"price.costs": "5.90",
				"price.rebate": "0.00",
				"price.taxvalue": "0.9833",
				"price.taxrate": "20.00",
				"price.taxflag": true,
				"price.status": 1,
				"price.label": "Demo: DHL"
			}
		},
		"relationships": {
			"media": {
				"data": [{
					"id": "43",
					"type": "media",
					"attributes": {
						"service.lists.id": "68",
						"service.lists.domain": "media",
						"service.lists.refid": "43",
						"service.lists.datestart": null,
						"service.lists.dateend": null,
						"service.lists.config": [],
						"service.lists.position": 0,
						"service.lists.status": 1,
						"service.lists.typename": "Standard",
						"service.lists.type": "default"
					}
				}]
			},
			"price": {
				"data": [{
					"id": "71",
					"type": "price",
					"attributes": {
					"service.lists.id": "69",
					"service.lists.domain": "price",
					"service.lists.refid": "71",
					"service.lists.datestart": null,
					"service.lists.dateend": null,
					"service.lists.config": [],
					"service.lists.position": 0,
					"service.lists.status": 1,
					"service.lists.typename": "Standard",
					"service.lists.type": "default"
					}
				}]
			},
			"text": {
				"data": [{
					"id": "174",
					"type": "text",
					"attributes": {
					"service.lists.id": "73",
					"service.lists.domain": "text",
					"service.lists.refid": "174",
					"service.lists.datestart": null,
					"service.lists.dateend": null,
					"service.lists.config": [],
					"service.lists.position": 3,
					"service.lists.status": 1,
					"service.lists.typename": "Standard",
					"service.lists.type": "default"
					}
				}]
			}
		}
	}, {
		// ...
	}],
	"included": [{
		"id": "43",
		"type": "media",
		"attributes": {
			"media.id": "43",
			"media.domain": "service",
			"media.label": "Demo: dhl.png",
			"media.languageid": null,
			"media.mimetype": "image/png",
			"media.type": "default",
			"media.typename": "Standard",
			"media.preview": "http://demo.aimeos.org/media/service/dhl.png",
			"media.url": "http://demo.aimeos.org/media/service/dhl.png",
			"media.status": 1
		}
	}, {
		"id": "71",
		"type": "price",
		"attributes": {
			"price.id": "71",
			"price.type": "default",
			"price.typename": "Standard",
			"price.currencyid": "EUR",
			"price.domain": "service",
			"price.quantity": 1,
			"price.value": "0.00",
			"price.costs": "5.90",
			"price.rebate": "0.00",
			"price.taxvalue": "0.9833",
			"price.taxrate": "20.00",
			"price.taxflag": true,
			"price.status": 1,
			"price.label": "Demo: DHL"
		}
	}, {
		"id": "174",
		"type": "text",
		"attributes": {
			"text.id": "174",
			"text.languageid": "en",
			"text.typename": "Short description",
			"text.type": "short",
			"text.label": "Demo short/en: Delivery within three days",
			"text.domain": "service",
			"text.content": "Delivery within three days",
			"text.status": 1
		}
	}, {
		// ...
	}]
}
```

# Set services

To add a service to the basket or replace an existing one, you need the "basket/service" URL from the service resource response. In our previous example, the URL of the first delivery option that would add this service to the basket was:

```
http://localhost:8000/jsonapi/basket?id=default&related=service
```

To set this service as delivery option in the current basket, you should use some code like this:

=== "CURL"
	```bash
	curl -X POST http://localhost:8000/jsonapi/basket?id=default&related=service&_token=... \
	-H "Content-Type: application/json"
	-d '{data: [{ \
		id: "delivery", \
		attributes: { \
			"service.id": "...",
			"...": "...", \
		} \
	}]}'
	```
=== "jQuery"
	```javascript
	var params = {data: [{
		type: "basket/service",
		id: "delivery",
		attributes: {
			"service.id": "...",
			// key/value pairs of data entered by the customer, e.g. bank account data
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

Important is to add the **id: "delivery"** and the service option ID in the attributes section of the parameters that are sent to the server.  The value for "id" is the type ("delivery" or "payment") while the value for "service.id" points to the service option that should be used as delivery or payment entry in the basket.

The "attributes" section in the parameter object can contain additional key/value pairs whose values are entered by the customer, e.g. the payment related data for direct debit. The available keys will be listed in the "attributes" section of each entry returned by the service resource response and only values for these keys will be accepted.

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
            "href": "http://localhost:8000/jsonapi/basket?id=default&related=service",
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
            "order.base.costs": "5.90",
            "order.base.rebate": "0.00",
            "order.base.status": 0,
            "order.base.comment": ""
        },
        "relationships": {
            "basket/service": {
                "data": [{
                    "type": "basket/service",
                    "id": "delivery"
                }]
            }
        }
    },
    "included": [{
        "id": "delivery",
        "type": "basket/service",
        "attributes": {
            "order.base.service.id": null,
            "order.base.service.code": "demo-dhl",
            "order.base.service.serviceid": "10",
            "order.base.service.name": "DHL",
            "order.base.service.mediaurl": "http://demo.aimeos.org/media/service/dhl.png",
            "order.base.service.type": "delivery",
            "order.base.service.price": "0.00",
            "order.base.service.costs": "5.90",
            "order.base.service.rebate": "0.00",
            "order.base.service.taxrate": "20.00"
        },
        "links": {
            "self": {
                "href": "http://localhost:8000/jsonapi/basket?id=default&related=service&relatedid=delivery",
                "allow": ["DELETE"]
            }
        }
    }]
}
```

It contains an additional "relationships" entry for the basket which points to the basket service entry in the "included" section.

# Delete services

Delivery or payment options added to the basket can also be removed again. For this, you need the URL from the basket service entry that is returned in the basket response. For the example above, it's:

```
http://localhost:8000/jsonapi/basket?id=default&related=service&relatedid=delivery
```

Executing a DELETE request using this URL will remove the service option from the basket again:

=== "CURL"
	```bash
	curl -X DELETE http://localhost:8000/jsonapi/basket?id=default&related=service&relatedid=delivery&_token=...
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

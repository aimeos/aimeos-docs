Aimeos allows several delivery addresses for each customer but customers must be authenticated before they can add, delete, retrieve and update their addresses.

!!! tip
    How to authenticate the user depends on the used PHP framework. Please have a look into the documentation of your used framework, e.g. at [Laravel Passport](https://laravel.com/docs/master/passport).

The customer response returnes the URLs for managing addresses:

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
		"customer/address": {
			"href": "http://localhost:8080/jsonapi/customer?related=address",
			"allow": ["GET","POST"]
		}
	}
}
```

# Fetch adresses

To retrieve the delivery addresses of the customer, you have to send a GET request to the *customer/address* endpoint returned by the GET request for the [customer](customer.md), e.g.:

=== "CURL"
	```bash
	curl -b cookies.txt -c cookies.txt \
	-X GET 'http://localhost:8000/jsonapi/customer?related=address'
	```
=== "jQuery"
	```javascript
	$.ajax({
		method: "GET",
		dataType: "json",
		url: response['links']['customer/address']['href'] // from customer response
	}).done( function( result ) {
		console.log( result.data );
	});
	```

If there's at least one delivery address available, the response looks like:

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
		"self": "http://localhost:8000/jsonapi/customer?related=address"
	},
	"data": [{
		"id": "2",
		"type": "customer\/address",
		"links": {
			"self": {
				"href": "http:\/\/localhost:8000\/jsonapi\/customer?id=2&related=address&relatedid=2",
				"allow": ["DELETE","GET","PATCH"]
			},
			"basket\/address": {
				"href": "http:\/\/localhost:8000\/jsonapi\/basket?id=default&related=address&relatedid=delivery",
				"allow": ["POST"]
			}
		},
		"attributes": {
			"customer.address.id": "2",
			"customer.address.salutation": "mr",
			"customer.address.company": "",
			"customer.address.vatid": "",
			"customer.address.title": "",
			"customer.address.firstname": "Test",
			"customer.address.lastname": "User",
			"customer.address.address1": "Test street",
			"customer.address.address2": "1",
			"customer.address.address3": "",
			"customer.address.postal": "12345",
			"customer.address.city": "Test city",
			"customer.address.state": "",
			"customer.address.countryid": "DE",
			"customer.address.languageid": "en",
			"customer.address.telephone": "",
			"customer.address.telefax": "",
			"customer.address.email": "",
			"customer.address.website": "",
			"customer.address.longitude": null,
			"customer.address.latitude": null,
			"customer.address.position": 0
		}
	}]
}
```

# Add addresses

You can add one or more addresses to the account of the currently authenticated customer by using a POST request. The URL for that request is returned by the GET request to the [customer endpoint](customer.md) and contains a *customer/address* entry in the *links* section:

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
		"customer/address": {
			"href": "http://localhost:8080/jsonapi/customer?related=address",
				"allow": ["GET","POST"]
		}
	}
}
```

There are some address attributes that are suggested when adding an address:

* customer.address.lastname (last name or full name)
* customer.address.address1 (most of the time the street name)
* customer.address.city (town or city name)
* customer.address.languageid (language the customer prefers)

The request for creating a new delivery address could look like:

=== "CURL"
	```bash
	curl -b cookies.txt -c cookies.txt \
	-X POST 'http://localhost:8000/jsonapi/customer?related=address&_token=...' \
	-H 'Content-Type: application/json' \
	-d '{"data": [{
		"attributes": {
			"customer.address.salutation": "mr",
			"customer.address.company": "Example company",
			"customer.address.vatid": "DE123456789",
			"customer.address.title": "Dr.",
			"customer.address.firstname": "Test",
			"customer.address.lastname": "User",
			"customer.address.address1": "Test street",
			"customer.address.address2": "1",
			"customer.address.address3": "",
			"customer.address.postal": "12345",
			"customer.address.city": "Test city",
			"customer.address.state": "HH",
			"customer.address.countryid": "DE",
			"customer.address.languageid": "de",
			"customer.address.telephone": "+4912345678",
			"customer.address.telefax": "+49123456789",
			"customer.address.email": "test@example.com",
			"customer.address.website": "https://example.com",
			"customer.address.longitude": 10.0,
			"customer.address.latitude": 50.0
		}
	}]}'
	```
=== "jQuery"
	```javascript
	var params = {'data': [{
		'attributes': {
			'customer.address.salutation': 'mr', // 'mr', 'mrs', 'miss', 'company' or empty (optional)
			'customer.address.company': 'Example company', // (optional)
			'customer.address.vatid': 'DE123456789', // (optional)
			'customer.address.title': 'Dr.', // (optional)
			'customer.address.firstname': 'Test', // (optional)
			'customer.address.lastname': 'User', // (required)
			'customer.address.address1': 'Test street', // (required)
			'customer.address.address2': '1', // (optional)
			'customer.address.address3': '', // (optional)
			'customer.address.postal': '12345', // (optional)
			'customer.address.city': 'Test city', // (required)
			'customer.address.state': 'HH', // (optional)
			'customer.address.countryid': 'DE', // (optional)
			'customer.address.languageid': 'de', // (required by many payment gateways)
			'customer.address.telephone': '+4912345678', // (optional)
			'customer.address.telefax': '+49123456789', // (optional)
			'customer.address.email': 'test@example.com', // (required)
			'customer.address.website': 'https://example.com', // (optional)
			'customer.address.longitude': 10.0, // (optional, float value)
			'customer.address.latitude': 50.0 // (optional, float value)
		}
	}]};

	var url = response['links']['customer/address']['href']; // from customer response

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

# Modify address

In the same way you can add address, you can change one or more address fields of the authenticated customer using a PATCH request. The URL for updating an address is returned by the GET response containing the customer delivery addresses. You can add all address fields or only the modified ones in the PATCH request:

=== "CURL"
	```bash
	curl -b cookies.txt -c cookies.txt \
	-X PATCH 'http://localhost:8000/jsonapi/customer?related=address&relatedid=...&_token=...' \
	-H 'Content-Type: application/json' \
	-d '{"data": {
		"attributes": {
			"customer.address.address2": "2",
			"customer.address.address3": "2. floor"
		}
	}}'
	```
=== "jQuery"
	```javascript
	var params = {'data': {
		'attributes': {
			'customer.address.address2': '2',
			'customer.address.address3': '2. floor'
		}
	}};

	var url = response['data'][0]['links']['self']['href']; // from customer address response

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

# Delete addresses

You can also remove delivery addresses from the customer account by using a DELETE request to the URL of the customer address. In our first response above, the URL is:

```
http://localhost:8000/jsonapi/customer?id=2&related=address&relatedid=2
```

Use code like that to contruct the DELETE request:


=== "CURL"
	```bash
	curl -b cookies.txt -c cookies.txt \
	-X DELETE 'http://localhost:8000/jsonapi/customer?id=2&related=address&relatedid=2&_token=...'
	```
=== "jQuery"
	```javascript
	var url = response['data'][0]['links']['self']['href']; // from customer address response

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

This request will remove the address entry from the user account and an additional GET request to retrieve the addresses won't contain the address any more.

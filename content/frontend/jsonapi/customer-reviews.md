Customers can view, add and update their own reviews using the JSON RESt API but they need to authenticate themselves first.

!!! tip
    How to authenticate the user depends on the used PHP framework. Please have a look into the documentation of your used framework, e.g. at [Laravel Passport](https://laravel.com/docs/master/passport).

The customer response returnes the URLs for managing reviews:

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
		"customer/review": {
			"href": "http://localhost:8000/jsonapi/customer?id=2&related=review",
			"allow": ["GET","POST"]
		},
		// ...
	},
```

# Fetch reviews

Retrieving the reviews of the customer requires a GET request to the *customer/review* endpoint returned by the GET request for the [customer](customer.md), e.g.:

=== "CURL"
	```bash
	curl -b cookies.txt -c cookies.txt \
	-X GET 'http://localhost:8000/jsonapi/customer?related=review'
	```
=== "jQuery"
	```javascript
	$.ajax({
		method: "GET",
		dataType: "json",
		url: response['links']['customer/review']['href'] // from customer response
	}).done( function( result ) {
		console.log( result.data );
	});
	```

When at least one review is available, the response will be similar to this one:

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
		"self": "http://localhost:8000/jsonapi/customer?id=2&related=review",
		"related": "http://localhost:8000/jsonapi/customer?id=2&related=review"
	},
	"data": [{
		"id": "1",
		"type": "customer\/review",
		"links": {
			"self": {
				"href": "http:\/\/localhost:8000\/jsonapi\/customer?id=2&related=review&relatedid=1",
				"allow": ["DELETE","GET","PATCH"]
			}
		},
		"attributes": {
			"review.id": "1",
			"review.refid": "1",
			"review.domain": "product",
			"review.response": "test response",
			"review.comment": "test comment",
			"review.rating": 5,
			"review.status": 1,
			"review.name": "test user"
		}
	}]
}
```

# Add reviews

To add one or more reviews to the authenticated customer, use a POST request including the review data. The URL to add reviews is returned by the GET request to the [customer endpoint](customer.md), which contains a *customer/review* entry in the *links* section.

The available fields for reviews are:

review.domain
: Domain of the reviewed item, e.g. "product" (required, up to 32 bytes)

review.refid
: ID of the reviewed item (required, up to 36 bytes)

review.name
: Name of the reviewer (required, up to 32 bytes)

review.rating
: Rating value, i.e. number of stars (required, integer value 0, 1, 2, 3, 4 or 5)

review.comment
: Reviewer comment (optional, up to 64k bytes)

The request for creating a new review looks similar to this one:

=== "CURL"
	```bash
	curl -b cookies.txt -c cookies.txt \
	-X POST 'http://localhost:8000/jsonapi/customer?related=review&_token=...' \
	-H 'Content-Type: application/json' \
	-d '{"data": [{
		"attributes": {
			"review.domain": "product",
			"review.refid": "1",
			"review.name": "Test User",
			"review.rating": 5,
			"review.comment": "Exactly fits my needs"
		}
	}]}'
	```
=== "jQuery"
	```javascript
	var params = {'data': [{
		'attributes': {
			"review.domain": "product",
			"review.refid": "1",
			"review.name": "Test User",
			"review.rating": 5,
			"review.comment": "Exactly fits my needs"
		}
	}]};

	var url = response['links']['customer/review']['href']; // from customer response

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

# Modify reviews

Changing one review of the authenticated customer is possible by performing a PATCH request. The URL for updating the review is returned by the GET response fetching all reviews. You can add all review fields or only the modified ones in the PATCH request:

=== "CURL"
	```bash
	curl -b cookies.txt -c cookies.txt \
	-X PATCH 'http://localhost:8000/jsonapi/customer?related=review&relatedid=8&_token=sTVVJGBtJyarXfgrYOxL5hpGADLbYOMb1azBn79V' \
	-H 'Content-Type: application/json' \
	-d '{"data": {
		"attributes": {
			"review.rating": 0,
			"review.comment": "Got broken after two weeks"
		}
	}}'
	```
=== "jQuery"
	```javascript
	var params = {'data': {
		'attributes': {
			"review.rating": 0,
			"review.comment": "Got broken after two weeks"
		}
	}};

	var url = response['data'][0]['links']['self']['href']; // from customer review response

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

# Delete reviews

Removing reviews from the user account is also possible by executing a DELETE request to the URL of the review. In the response from the GET request, the URL is:

```
http://localhost:8000/jsonapi/customer?id=2&related=review&relatedid=1
```

You can build a DELETE request using:


=== "CURL"
	```bash
	curl -b cookies.txt -c cookies.txt \
	-X DELETE 'http://localhost:8000/jsonapi/customer?related=review&relatedid=8&_token=sTVVJGBtJyarXfgrYOxL5hpGADLbYOMb1azBn79V'
	```
=== "jQuery"
	```javascript
	var url = response['data'][0]['links']['self']['href']; // from customer review response

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

Then, the review identified by its ID is removed from the customer account.

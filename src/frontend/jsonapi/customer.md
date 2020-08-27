To create a customer or modify his data, you need the customer resource endpoint from the OPTIONS request. Depending on the used routes it might be something like:

```bash
curl -b cookies.txt -c cookies.txt \
-X OPTIONS 'http://localhost:8000/jsonapi'
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
            "customer": "http://localhost:8000/jsonapi/customer",
            ...
        }
    }
}
```


The "csrf" section in "meta" is important to modify the customer data. Each response will contain such a "csrf" section if the host application supports tokens against cross-site request forgery attacks. If available, you have to send them with every DELETE, PATCH and POST request.

!!! warning
    Don't take the resource URLs in the OPTIONS response as granted! They will change depending on the routes and the application. Thus, your client needs the OPTIONS URL of the JSON REST API as configuration parameter. It's response will define the next possibilities.

# Fetch customer data

To get the customer entry, you have to send a GET request to the customer endpoint returned by the OPTIONS request:

=== "CURL"
	```bash
	curl -b cookies.txt -c cookies.txt \
	-X GET 'http://localhost:8000/jsonapi/customer'
	```
=== "jQuery"
	```javascript
	$.ajax({
		method: "GET",
		dataType: "json",
		url: response.meta.resources['customer'] // returned from OPTIONS request
	}).done( function( result ) {
		console.log( result.data );
	});
	```

If the customer didn't authenticate himself yet, an empty customer item is returned:

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
		},
		"customer/property": {
			"href": "http://localhost:8000/jsonapi/customer?id=2&related=property",
			"allow": ["GET","POST"]
		},
		"customer/relationships": {
			"href": "http://localhost:8000/jsonapi/customer?id=2&related=relationships",
			"allow": ["GET","POST"]
		}
	},
	"data": {
		"id": null,
		"type": "customer",
		"links": {
			"self": {
				"href": "http:\/\/localhost:8080\/jsonapi\/customer",
				"allow": ["DELETE","GET","PATCH"]
			}
		},
		"attributes": {
			"customer.id": null,
			"customer.salutation": "",
			"customer.company": "",
			"customer.vatid": "",
			"customer.title": "",
			"customer.firstname": "",
			"customer.lastname": "",
			"customer.address1": "",
			"customer.address2": "",
			"customer.address3": "",
			"customer.postal": "",
			"customer.city": "",
			"customer.state": "",
			"customer.languageid": "",
			"customer.countryid": "",
			"customer.telephone": "",
			"customer.email": "",
			"customer.telefax": "",
			"customer.website": "",
			"customer.longitude": null,
			"customer.latitude": null,
			"customer.label": "",
			"customer.code": "",
			"customer.birthday": null,
			"customer.status": 1,
			"customer.groups": []
		}
	},
	"included": []
}
```

!!! tip
    How to authenticate the user depends on the used PHP framework. Please have a look into the documentation of your used framework, e.g. at Laravel [Passport](https://laravel.com/docs/master/passport)/[Sanctum](https://laravel.com/docs/master/sanctum) or Symfony [Guard](https://symfony.com/doc/current/security/guard_authentication.html).

For an authenticated user, the response will contain the account data and the groups assigned to the user:

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
		"self": "http://localhost:8000/jsonapi/customer",
		"customer/address": {
			"href": "http://localhost:8000/jsonapi/customer?id=2&related=address",
			"allow": ["GET","POST"]
		},
		"customer/property": {
			"href": "http://localhost:8000/jsonapi/customer?id=2&related=property",
			"allow": ["GET","POST"]
		},
		"customer/relationships": {
			"href": "http://localhost:8000/jsonapi/customer?id=2&related=relationships",
			"allow": ["GET","POST"]
		}
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
			"customer.id": "2",
			"customer.salutation": "mr",
			"customer.company": "Test company",
			"customer.vatid": "DE12345678",
			"customer.title": "Dr.",
			"customer.firstname": "Test",
			"customer.lastname": "User",
			"customer.address1": "Test street",
			"customer.address2": "1",
			"customer.address3": "2. floor",
			"customer.postal": "12345",
			"customer.city": "Test city",
			"customer.state": "HH",
			"customer.languageid": "de",
			"customer.countryid": "DE",
			"customer.telephone": "+49012345678",
			"customer.email": "example@aimeos.org",
			"customer.telefax": "+490123456789",
			"customer.website": "https://aimeos.org",
			"customer.longitude": 10.0,
			"customer.latitude": 50.0,
			"customer.label": "Test User",
			"customer.code": "example@aimeos.org",
			"customer.birthday": "2000-01-01",
		},
		"relationships": {
			"customer\/group": {
				"data": [{
					"id": "1",
					"type": "customer\/group",
					"attributes": {
						"customer.lists.id": "1",
						"customer.lists.domain": "customer\/group",
						"customer.lists.refid": "1",
						"customer.lists.datestart": null,
						"customer.lists.dateend": null,
						"customer.lists.config": [],
						"customer.lists.position": 0,
						"customer.lists.status": 1,
						"customer.lists.type": "default"
					},
					"links": {
						"self": {
							"href": "http:\/\/localhost:8000\/jsonapi\/customer\/group?id=2&related=relationships&relatedid=1",
							"allow": []
						}
					}
				}]
			}
		}
	},
	"included": [{
		"id": "1",
		"type": "customer\/group",
		"attributes": {
			"customer.group.id": "1",
			"customer.group.code": "admin",
			"customer.group.label": "Administrator"
		}
	}]
}
```

If you don't need all data, you can [limit the fields](basics.md#return-specific-fields-only) returned by adding *&fields[customer]=...* to the URL, e.g. "&fields[customer]=customer.code,customer.email".

To fetch addresses or other [related data](basics.md#include-related-resources) too, you can add *&include=...* to the URL so the related data is returned in the response too. Available related resources are:

* *customer/address* : List of delivery addresses
* *customer/property* : List of properties stored for the user
* *product* : List of products from the favorite or watch list

# Create new customer

If the user isn't logged in, it's possible to create a new customer by sending the user data within a POST request to the customer endpoint from the OPTIONS response. The **e-mail address** is the only absolutely required field for new entries but it's a good idea to send data for these fields as well:

* customer.lastname (required in admin backend)
* customer.address1 (required in admin backend)
* customer.city (required in admin backend)
* customer.languageid (required by many payment gateways)

=== "CURL"
	```bash
	curl-b cookies.txt -c cookies.txt \
	-X POST 'http://localhost:8000/jsonapi/customer?_token=...' \
	-H 'Content-Type: application/json' \
	-d '{"data": {
		"attributes": {
			"customer.code": "testuser@example.com",
			"customer.label": "Test user",
			"customer.salutation": "mr",
			"customer.company": "Example company",
			"customer.vatid": "DE123456789",
			"customer.title": "Dr.",
			"customer.firstname": "Test",
			"customer.lastname": "User",
			"customer.address1": "Test street",
			"customer.address2": "1",
			"customer.address3": "",
			"customer.postal": "12345",
			"customer.city": "Test city",
			"customer.state": "HH",
			"customer.countryid": "DE",
			"customer.languageid": "de",
			"customer.telehone": "+4912345678",
			"customer.telefax": "+49123456789",
			"customer.email": "testuser@example.com",
			"customer.website": "https://example.com",
			"customer.longitude": 10.0,
			"customer.latitude": 50.0,
			"customer.birthday": "2000-01-01",
			"customer.password": "secret123"
		}
	}}'
	```
=== "jQuery"
	```javascript
	var params = {data: {
		attributes: {
			"customer.code": "testuser@example.com", // (optional, customer.email is used if empty)
			"customer.label": "Test user", // (optional, will be generated if empty)
			"customer.salutation": "mr", // "mr", "mrs", "miss", "company" or empty (optional)
			"customer.company": "Example company", // (optional)
			"customer.vatid": "DE123456789", // (optional)
			"customer.title": "Dr.", // (optional)
			"customer.firstname": "Test", // (optional)
			"customer.lastname": "User", // (required)
			"customer.address1": "Test street", // (required)
			"customer.address2": "1", // (optional)
			"customer.address3": "", // (optional)
			"customer.postal": "12345", // (optional)
			"customer.city": "Test city", // (required)
			"customer.state": "HH", // (optional)
			"customer.countryid": "DE", // (optional)
			"customer.languageid": "de", // (required by many payment gateways)
			"customer.telehone": "+4912345678", // (optional)
			"customer.telefax": "+49123456789", // (optional)
			"customer.email": "testuser@example.com", // (required)
			"customer.website": "https://example.com", // (optional)
			"customer.longitude": 10.0, // (optional, float value)
			"customer.latitude": 50.0, // (optional, float value)
			"customer.birthday": "2000-01-01", // (optional)
			"customer.password": "secret123" // (optional, generated if empty)
		}
	}};

	var url = response['links']['customer']['href']; // from OPTIONS response

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

You can't set the "customer.status" and "customer.groups" properties for an account using the JSON API. If you do so, they will be ignored because obviously, this would enable attackers to re-enable their disabled account or gain additional privileges.

In case the new account has been successfully created, the response will be similar to this one:

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
		"self": "http://localhost:8000/jsonapi/customer"
	},
	"data": {
		"id":"6",
		"type":"customer",
		"links":{
			"self":{
				"href":"http:\/\/localhost:8000\/jsonapi\/customer?id=6",
				"allow":["DELETE","GET","PATCH"]
			}
		},
		"attributes":{
			"customer.id":"6"
		}
	},
	"included": []
}
```

Only the ID of the newly created user account is returned for security reasons. Also, the number of user accounts that can be created from one IP address is limited to three accounts within four hours. You can change the limits using these settings:

* [controller/frontend/customer/limit-count](../../config/controller-frontend/customer.md#limit-count)
* [controller/frontend/customer/limit-seconds](../../config/controller-frontend/customer.md#limit-seconds)

# Change customer data

Once an account has been created and the user is logged in, the JSON API allows you to update the data in the user account.

!!! tip
    How to authenticate the user depends on the used PHP framework. Please have a look into the documentation of your used framework, e.g. at Laravel [Passport](https://laravel.com/docs/master/passport)/[Sanctum](https://laravel.com/docs/master/sanctum) or Symfony [Guard](https://symfony.com/doc/current/security/guard_authentication.html).

The request for changing data is very similar to creating a new user but it requires a PATCH request:

=== "CURL"
	```bash
	curl-b cookies.txt -c cookies.txt \
	-X PATCH 'http://localhost:8000/jsonapi/customer?_token=...' \
	-H 'Content-Type: application/json' \
	-d '{"data": {
		"attributes": {
			"customer.code": "testuser@example.com",
			"customer.label": "Test user",
			"customer.salutation": "mr",
			"customer.company": "Example company",
			"customer.vatid": "DE123456789",
			"customer.title": "Dr.",
			"customer.firstname": "Test",
			"customer.lastname": "User",
			"customer.address1": "Test street",
			"customer.address2": "2",
			"customer.address3": "",
			"customer.postal": "12345",
			"customer.city": "Test city",
			"customer.state": "HH",
			"customer.countryid": "DE",
			"customer.languageid": "de",
			"customer.telehone": "+4912345678",
			"customer.telefax": "+49123456789",
			"customer.email": "testuser@example.com",
			"customer.website": "https://example.com",
			"customer.longitude": 10.0,
			"customer.latitude": 50.0,
			"customer.birthday": "2000-01-01",
			"customer.password": "very+secret"
		}
	}}'
	```
=== "jQuery"
	```javascript
	var params = {data: {
		attributes: {
			"customer.code": "testuser@example.com", // (optional, customer.email is used if empty)
			"customer.label": "Test user", // (optional, will be generated if empty)
			"customer.salutation": "mr", // "mr", "mrs", "miss", "company" or empty (optional)
			"customer.company": "Example company", // (optional)
			"customer.vatid": "DE123456789", // (optional)
			"customer.title": "Dr.", // (optional)
			"customer.firstname": "Test", // (optional)
			"customer.lastname": "User", // (required)
			"customer.address1": "Test street", // (required)
			"customer.address2": "2", // (optional)
			"customer.address3": "", // (optional)
			"customer.postal": "12345", // (optional)
			"customer.city": "Test city", // (required)
			"customer.state": "HH", // (optional)
			"customer.countryid": "DE", // (optional)
			"customer.languageid": "de", // (required by many payment gateways)
			"customer.telehone": "+4912345678", // (optional)
			"customer.telefax": "+49123456789", // (optional)
			"customer.email": "testuser@example.com", // (required)
			"customer.website": "https://example.com", // (optional)
			"customer.longitude": 10.0, // (optional, float value)
			"customer.latitude": 50.0, // (optional, float value)
			"customer.birthday": "2000-01-01", // (optional)
			"customer.password": "very+secret" // (optional, generated if empty)
		}
	}};

	var url = response['links']['customer']['href']; // from OPTIONS response

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

The response will include the basic customer data including groups like in this example:

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
		"self": "http://localhost:8000/jsonapi/customer?id=1"
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
			"customer.id": "2",
			"customer.code": "testuser@example.com",
			"customer.label": "Test user",
			"customer.salutation": "mr",
			"customer.company": "Example company",
			"customer.vatid": "DE123456789",
			"customer.title": "Dr.",
			"customer.firstname": "Test",
			"customer.lastname": "User",
			"customer.address1": "Test street",
			"customer.address2": "2",
			"customer.address3": "",
			"customer.postal": "12345",
			"customer.city": "Test city",
			"customer.state": "HH",
			"customer.countryid": "DE",
			"customer.languageid": "de",
			"customer.telehone": "+4912345678",
			"customer.telefax": "+49123456789",
			"customer.email": "testuser@example.com",
			"customer.website": "https://example.com",
			"customer.longitude": 10.0,
			"customer.latitude": 50.0,
			"customer.birthday": "2000-01-01",
			"customer.status": 1,
			"customer.groups": ["1"]
		},
		"relationships": {
			"customer\/group": {
				"data": [{
					"id": "1",
					"type": "customer\/group",
					"attributes": {
						"customer.lists.id": "1",
						"customer.lists.domain": "customer\/group",
						"customer.lists.refid": "1",
						"customer.lists.datestart": null,
						"customer.lists.dateend": null,
						"customer.lists.config": [],
						"customer.lists.position": 0,
						"customer.lists.status": 1,
						"customer.lists.type": "default"
					},
					"links": {
						"self": {
							"href": "http:\/\/localhost:8000\/jsonapi\/customer\/group?id=2&related=relationships&relatedid=1",
							"allow": ["DELETE","PATCH"]
						}
					}
				}]
			}
		}
	},
	"included": [{
		"id": "1",
		"type": "customer\/group",
		"attributes": {
		"customer.group.id": "1",
		"customer.group.code": "customer",
		"customer.group.label": "Customer"
		}
	}]
}
```

It's not necessary to pass all customer fields along with the PATCH request. Instead, you can only add those fields with new or changed data. All other customer fields will remain unchanged.

!!! warning
    In most frameworks, the e-mail address is used as unique identifier and therefore, **customer.code** and **customer.email** should contain the same value if both are sent within the request. Otherwise, this may lead to inconsistencies when using different frameworks as host application.

# Delete customer

It's also possible to delete a user account and remove all associated data like addresses but except orders. All order related data will stay untouched because it's only loosely related to customer accounts and must be available for accounting reasons.

Every user can only delete his own account and he must be logged in to do so.

!!! tip
    How to authenticate the user depends on the used PHP framework. Please have a look into the documentation of your used framework, e.g. at Laravel [Passport](https://laravel.com/docs/master/passport)/[Sanctum](https://laravel.com/docs/master/sanctum) or Symfony [Guard](https://symfony.com/doc/current/security/guard_authentication.html).

For deleting the account use e.g.:

=== "CURL"
	```bash
	curl -b cookies.txt -c cookies.txt \
	-X DELETE 'http://localhost:8000/jsonapi/customer?id=...&_token=...'
	```
=== "jQuery"
	```javascript
	var url = response.links.self.href; // from customer response

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

!!! note
    Deleting a user returns a successful response even if the user doesn't exist or you are not allowed to delete that user for security reasons. If you want to be sure the users' own account is deleted, perform a GET request to the customer endpoint. It will return an empty customer item with no *customer.id* value if the account doesn't exist any more.

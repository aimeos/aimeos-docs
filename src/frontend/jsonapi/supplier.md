!!! tip
    You can fetch the suppliers together with the products in a single request too by using *&include=supplier*. This should be preferred for product detail pages. For generating a list of available suppliers, requests to the supplier endpoint as described in this articel are appropriate.

Before you can retrieve the available suppliers (can be used for brands, manufacturers, distributors or vendors), you must get the resource endpoint via the OPTIONS request. Depending on the used routes it might be something like this:

```bash
curl -X OPTIONS 'http://localhost:8000/jsonapi'
```

The response will contain the required endpoints you have to use:

```json
{
    "meta": {
        "prefix": null,
        "resources": {
            "supplier": "http://localhost:8000/jsonapi/supplier"
        }
    }
}
```

# Fetch suppliers

Now you can retrieve all available language/currency combinations via the "supplier" resource you've just received from the OPTIONS response. The response of the "supplier" endpoint contains the list of the available suppliers, e.g.:

=== "CURL"
    ```bash
    curl -X GET 'http://localhost:8000/jsonapi/supplier'
    ```
=== "Javascript"
    ```javascript
    // returned from OPTIONS call
    fetch(options.meta.resources['supplier']).then(result => {
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
        url: options.meta.resources['supplier'], // returned from OPTIONS call
    }).done( function( result ) {
        console.log( result );
    });
    ```

This response contains all available suppliers for the current site:

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
        "self": "http://localhost:8000/jsonapi/supplier"
    },
    "data": [
    {
        "id":"9",
        "type":"supplier",
        "links":{
            "self":{
                "href":"http://localhost:8000/jsonapi/supplier?id=9",
                "allow":["GET"]
            }
        },
        "attributes":{
            "supplier.id":"9",
            "supplier.code":"demo-hr",
            "supplier.label":"H&R",
            "supplier.status":1,
            "supplier.position":0
        }
    },
    {
        "id":"10",
        "type":"supplier",
        "links":{
            "self":{
                "href":"http://localhost:8000/jsonapi/supplier?id=10",
                "allow":["GET"]
            }
        },
        "attributes":{
            "supplier.id":"10",
            "supplier.code":"demo-cstory",
            "supplier.label":"C-Story",
            "supplier.status":1,
            "supplier.position":0
        }
    },
    {
        "id":"11",
        "type":"supplier",
        "links":{
            "self":{
                "href":"http://localhost:8000/jsonapi/supplier?id=11",
                "allow":["GET"]
            }
        },
        "attributes":{
            "supplier.id":"11",
            "supplier.code":"demo-sb",
            "supplier.label":"Sergio Blunic",
            "supplier.status":1,
            "supplier.position":0
        }
    },
    {
        "id":"12",
            "type":"supplier",
            "links":{
                "self":{
                    "href":"http://localhost:8000/jsonapi/supplier?id=12",
                    "allow":["GET"]
                }
            },
            "attributes":{
                "supplier.id":"12",
                "supplier.code":"demo-ballroom",
                "supplier.label":"Ballroom",
                "supplier.status":1,
                "supplier.position":0
            }
        }
    ]
}
```

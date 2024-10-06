Before you can retrieve the available locales (language and currency combinations for the current site), you must get the resource endpoint via the OPTIONS request. Depending on the used routes it might be something like this:

```bash
curl -X OPTIONS 'http://localhost:8000/jsonapi'
```

The response will contain the required endpoints you have to use:

```json
{
    "meta": {
        "prefix": null,
        "resources": {
            "locale": "http://localhost:8000/jsonapi/locale"
        }
    }
}
```

# Fetch locales

Now you can retrieve all available language/currency combinations via the "locale" resource you've just received from the OPTIONS response. The response of the "locale" endpoint contains the list of the available locales, e.g.:

=== "CURL"
    ```bash
    curl -X GET 'http://localhost:8000/jsonapi/locale'
    ```
=== "Javascript"
    ```javascript
    // returned from OPTIONS call
    fetch(options.meta.resources['locale']).then(result => {
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
        url: options.meta.resources['locale'], // returned from OPTIONS call
    }).done( function( result ) {
        console.log( result );
    });
    ```

This response contains all available locale combinations for the current site:

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
        "self": "http://localhost:8000/jsonapi/locale"
    },
    "data": [
        {
            "id":"1",
            "type":"locale",
            "links":{
                "self":{
                    "href":"http://localhost:8000/jsonapi/locale?id=1",
                    "allow":["GET"]
                },
                "resources":{
                    "href":"http://localhost:8000/jsonapi?locale=en&currency=USD",
                    "allow":["OPTIONS"]
                }
            },
            "attributes":{
                "locale.id":"1",
                "locale.currencyid":"USD",
                "locale.languageid":"en",
                "locale.position":0,
                "locale.sitecode":"default",
                "locale.siteid":"1.",
                "locale.status":1
            }
        },{
            "id":"2",
            "type":"locale",
            "links":{
                "self":{
                    "href":"http://localhost:8000/jsonapi/locale?id=2",
                    "allow":["GET"]
                },
                "resources":{
                    "href":"http://localhost:8000/jsonapi?locale=de&currency=EUR",
                    "allow":["OPTIONS"]
                }
            },
            "attributes":{
                "locale.id":"2",
                "locale.currencyid":"EUR",
                "locale.languageid":"de",
                "locale.position":1,
                "locale.sitecode":"default",
                "locale.siteid":"1.",
                "locale.status":1
            }
        }
    ]
}
```

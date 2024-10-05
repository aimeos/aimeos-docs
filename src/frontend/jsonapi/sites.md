Before you can retrieve the site which contains the seller/vendor information, you must get the resource endpoint via the OPTIONS request. Depending on the used routes it might be something like this:

```bash
curl -X OPTIONS 'http://localhost:8000/jsonapi'
```

The response will contain the required endpoints you have to use:

```json
{
    "meta": {
        "prefix": null,
        "resources": {
            "site": "http://localhost:8000/jsonapi/site"
        }
    }
}
```

# Fetch site

Now you can retrieve site via the "site" resource you've just received from the OPTIONS response. The response of the "site" endpoint contains the data of the current site, e.g.:

=== "CURL"
    ```bash
    curl -X GET 'http://localhost:8000/jsonapi/site'
    ```
=== "Javascript"
    ```javascript
    // returned from OPTIONS call
    fetch(options.meta.resources['site']).then(result => {
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
        url: options.meta.resources['site'], // returned from OPTIONS call
    }).done( function( result ) {
        console.log( result );
    });
    ```

This response contains all available site data for the current site:

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
        "self": "http://localhost:8000/jsonapi/site"
    },
    "data": {
        "id":"1",
        "type":"locale/site",
        "links":{
            "self":{
                "href":"https://localhost/jsonapi/site?id=1",
                "allow":["GET"]
            }
        },
        "attributes":{
            "locale.site.id":"1",
            "locale.site.code":"default",
            "locale.site.icon":"1.d\/icon.png",
            "locale.site.logo":{"200":"1.d\/logo200.webp"},
            "locale.site.theme":null,
            "locale.site.label":"Aimeos",
            "locale.site.status":1,
            "locale.site.refid":"123",
            "locale.site.ratings":5,
            "locale.site.rating":"4.75"
        }
    }
}
```

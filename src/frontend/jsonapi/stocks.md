!!! tip
    You can fetch the stock levels together with the products in a single request too by using *&include=stock*. For initial requests, this should be preferred to speed up rendering. As stock levels are very volatile, they shouldn't be cached like other product data and should be retrieved each time the product is re-rendered using the requests described in this article.

Before you can retrieve the available product stock entries, you must get the resource endpoint via the OPTIONS request. Depending on the used routes it might be something like this:

```bash
curl -X OPTIONS 'http://localhost:8000/jsonapi'
```

The response will contain the required endpoints you have to use:

```json
{
    "meta": {
        "prefix": null,
        "resources": {
            "stock": "http://localhost:8000/jsonapi/stock"
        }
    }
}
```

Have a look at [retrieving an OPTIONS request](index.md#retrieve-meta-data) for more details. An OPTIONS request to the stock endpoint also reveals the supported filters:

```bash
curl -X OPTIONS 'http://localhost:8000/jsonapi/stock'
```

It also returns the [prefix](index.md#nested-parameters) you have to use if the value is not `null`:

```json
{
    "meta": {
        "prefix": null,
        "content-baseurl": "http://localhost:8000",
		"content-baseurls": {
			"fs-media": "http://localhost:8000/aimeos",
			"fs-mimeicon": "http://localhost:8000/vendor/shop/mimeicons",
			"fs-theme": "http://localhost:8000/vendor/shop/themes"
		},
        "csrf": {
            "name": "_token",
            "value": "..."
        },
        "filter": {
            "s_prodid": {
                "label": "List of product IDs for which the stock level should be returned",
                "type": "array",
                "default": "[]",
                "required": false
            },
            "s_typecode": {
                "label": "List of warehouse/location codes (stock type)",
                "type": "array",
                "default": "[]",
                "required": false
            }
        }
    }
}
```

# Fetch stocks

Now you can retrieve stock levels via the "stock" resource you've just received from the OPTIONS response. The response of the "stock" endpoint contains the list of stock entries for the requested product IDs, e.g.:

=== "CURL"
    ```bash
    curl -X GET 'http://localhost:8000/jsonapi/stock?filter[s_prodid][]=1234'
    ```
=== "Javascript"
    ```javascript
    const args = {
        'filter': {
            's_prodid': ['1234']
        }
    }
    let params = {}

    if(options.meta.prefix) { // returned from OPTIONS call
        params[options.meta.prefix] = args
    } else {
        params = args
    }

    // returned from OPTIONS call
    const url = options.meta.resources['stock']
        + (options.meta.resources['stock'].includes('?') ? '&' : '?')
        + window.param(params) // from https://github.com/knowledgecode/jquery-param

    fetch(url).then(result => {
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
    var args = {
        'filter': {
            's_prodid': ['1234']
        }
    };
    var params = {};

    if(options.meta.prefix) { // returned from OPTIONS call
        params[options.meta.prefix] = args;
    } else {
        params = args;
    }

    $.ajax({
        method: 'GET',
        dataType: 'json',
        url: options.meta.resources['stock'], // returned from OPTIONS call
        data: params
    }).done( function( result ) {
        console.log( result );
    });
    ```

This response contains the list of stock entries (limited to 25 by default) for the current site:

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
        "self": "http://localhost:8000/jsonapi/stock"
    },
    "data": [
        {
            "id":"35",
            "type":"stock",
            "links":{
                "self":{
                    "href":"http://localhost:8000/jsonapi/stock?id=35",
                    "allow":["GET"]
                }
            },
            "attributes":{
                "stock.id":"35",
                "stock.productid":"35",
                "stock.stocklevel":null,
                "stock.timeframe":"",
                "stock.dateback":null,
                "stock.type":"default"
            }
        },
        {
            "id":"36",
            "type":"stock",
            "links":{
                "self":{
                    "href":"http://localhost:8000/jsonapi/stock?id=36",
                    "allow":["GET"]
                }
            },
            "attributes":{
                "stock.id":"36",
                "stock.productid":"35",
                "stock.stocklevel":0,
                "stock.timeframe":"",
                "stock.dateback":"2015-01-01 12:00:00",
                "stock.type":"warehouse2"
            }
        }
    ]
}
```

# Filter stocks

Additionally, you can filter stocks by stock type using the *s_typecode* parameter:

=== "CURL"
    ```bash
    curl -X GET 'http://localhost:8000/jsonapi/stock?filter[s_prodid][]=35&filter[s_prodid][]=36&filter[s_typecode]=default'
    ```
=== "Javascript"
    ```javascript
    const args = {
        'filter': {
            's_prodid': [35, 36],
            's_typecode': 'default'
        }
    }
    let params = {}

    if(options.meta.prefix) { // returned from OPTIONS call
        params[options.meta.prefix] = args
    } else {
        params = args
    }

    // returned from OPTIONS call
    const url = options.meta.resources['stock']
        + (options.meta.resources['stock'].includes('?') ? '&' : '?')
        + window.param(params) // from https://github.com/knowledgecode/jquery-param

    fetch(url).then(result => {
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
    var args = {
        'filter': {
            's_prodid': [35, 36],
            's_typecode': 'default'
        }
    };
    var params = {};

    if(options.meta.prefix) { // returned from OPTIONS call
        params[options.meta.prefix] = args;
    } else {
        params = args;
    }

    $.ajax({
        method: 'GET',
        dataType: 'json',
        url: options.meta.resources['stock'], // returned from OPTIONS call
        data: params
    }).done( function( result ) {
        console.log( result );
    });
    ```

Before you can retrieve the reviews, you must get the resource endpoint via the OPTIONS request. Depending on the used routes it might be something like this:

```bash
curl -X OPTIONS 'http://localhost:8000/jsonapi'
```

The response will contain the required endpoints you have to use:

```json
{
    "meta": {
        "prefix": null,
        "resources": {
            "review": "http://localhost:8000/jsonapi/review"
        }
    }
}
```

Have a look at [retrieving an OPTIONS request](index.md#retrieve-meta-data) for more details. An OPTIONS request to the review endpoint also reveals the supported filters:

```bash
curl -X OPTIONS 'http://localhost:8000/jsonapi/review'
```

It also returns the [prefix](index.md#nested-parameters) you have to use if the value is not `null`:

```json
{
    "meta": {
        "prefix": null,
        "filter": {
            "f_domain": {
                "label": "Return reviews for that domain, e.g. 'product'",
                "type": "string",
                "default": "product",
                "required": false
            },
            "f_refid": {
                "label": "Return reviews for the item from the domain with that ID",
                "type": "string",
                "default": null,
                "required": false
            }
        },
        "sort": {
            "ctime": {
                "label": "Sort reviews by creation date/time",
                "type": "string",
                "default": true,
                "required": false
            },
            "rating": {
                "label": "Sort reviews by rating",
                "type": "string",
                "default": false,
                "required": false
            }
        }
    }
}
```

# Fetch reviews

Now you can retrieve reviews via the "review" resource you've just received from the OPTIONS response. By default, the list of all product reviews is returned and you should filter them by the ID of the product the user requested, e.g.:

=== "CURL"
    ```bash
    curl -X GET 'http://localhost:8000/jsonapi/review?filter[f_refid]=1'
    ```
=== "Javascript"
    ```javascript
    const args = {
        filter: {
            'f_refid': '1'
        }
    };
    let params = {};

    if(options.meta.prefix) { // returned from OPTIONS call
        params[options.meta.prefix] = args;
    } else {
        params = args;
    }

    // returned from OPTIONS call
    fetch(options.meta.resources['review']).then(result => {
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
        filter: {
            'f_refid': '1'
        }
    };
    var params = {};

    if(options.meta.prefix) { // returned from OPTIONS call
        params[options.meta.prefix] = args;
    } else {
        params = args;
    }

    $.ajax({
        method: "GET",
        dataType: "json",
        url: options.meta.resources['review'], // returned from OPTIONS call
        data: params
    }).done( function( result ) {
        console.log( result );
    });
    ```

This response contains all reviews for the product with the ID "1":

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
        "next": "http://localhost:8000/default/jsonapi/review?f_refid=1&page%5Boffset%5D=10",
        "last": "http://localhost:8000/default/jsonapi/review?f_refid=1&page%5Boffset%5D=10",
        "self": "http://localhost:8000/default/jsonapi/review?f_refid=1"
    },
    "data": [{
        "id": "1",
        "type": "review",
        "links": {
            "self": {
                "href": "http://localhost:8000/default/jsonapi/review?id=1",
                "allow": ["GET"]
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

!!! tip
    It's also possible to retrive reviews for other domains than *product* by using the *f_domain* parameter, e.g. *&f_domain=customer*. You can also filter by additional fields using the [*filter* parameter](basics.md).

# Sort reviews

In addition to the generic filter possibilities, you can sort reviews by these keys:

* "ctime" (asc) or "-ctime" (desc)
* "rating" (asc) or "-rating" (desc)

=== "CURL"
    ```bash
    curl -X GET 'http://localhost:8000/jsonapi/review?sort=-rating'
    ```
=== "Javascript"
    ```javascript
    const args = {
        'sort': '-rating'
    };
    let params = {};

    if(options.meta.prefix) { // returned from OPTIONS call
        params[options.meta.prefix] = args;
    } else {
        params = args;
    }

    // returned from OPTIONS call
    fetch(options.meta.resources['review']).then(result => {
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
    var args = {'sort': '-rating'};
    var params = {};

    if(options.meta.prefix) { // returned from OPTIONS call
        params[options.meta.prefix] = params;
    } else {
        params = args;
    }

    $.ajax({
        method: "GET",
        dataType: "json",
        url: options.meta.resources['review'], // returned from OPTIONS call
        data: params
    }).done( function( result ) {
        console.log( result );
    });
    ```

!!! tip
    You can also sort by other fields, e.g. by the last modification date of the reviews using *&sort=review.mtime*

# Count ratings

You can get the rating counts for the reviews by using the **aggregate** key and the corresponding *review.rating* search key:

=== "CURL"
    ```bash
    curl -X GET 'http://localhost:8000/jsonapi/review?aggregate=review.rating'
    ```
=== "Javascript"
    ```javascript
    const args = {
        'aggregate': 'review.rating'
    };
    let params = {};

    if(options.meta.prefix) { // returned from OPTIONS call
        params[options.meta.prefix] = args;
    } else {
        params = args;
    }

    // returned from OPTIONS call
    fetch(options.meta.resources['review']).then(result => {
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
    var args = {'aggregate': 'review.rating'};
    var params = {};

    if(options.meta.prefix) { // returned from OPTIONS call
        params[options.meta.prefix] = args;
    } else {
        params = args;
    }

    $.ajax({
        method: 'GET',
        dataType: 'json',
        url: options.meta.resources['review'], // returned from OPTIONS call
        data: params
    }).done( function( result ) {
        console.log( result );
    });
    ```

This will return a list of "id" and "attributes" pairs where the value of "id" is the rating value and "attributes" is the number of reviews with that rating:

```javascript
{
    "meta": {
        "total": 1
    },
    "data": [
        {"id":1,"type":"review.rating","attributes":"0"},
        {"id":2,"type":"review.rating","attributes":"2"},
        {"id":3,"type":"review.rating","attributes":"3"},
        {"id":4,"type":"review.rating","attributes":"5"},
        {"id":5,"type":"review.rating","attributes":"10"}
    ]
}
```

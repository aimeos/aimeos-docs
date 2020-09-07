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
            "ctime": {
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
        "csrf": {
            "name": "_token",
            "value": "..."
        }
    },
    "links": {
        "self": "http://localhost:8000/default/jsonapi/review?f_refid=1"
    },
    "data": [{
        "id": "1",
        "type": "review",
        "links": {
            "self": {
                "href": "http:\/\/localhost:8000\/default\/jsonapi\/review?id=1",
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

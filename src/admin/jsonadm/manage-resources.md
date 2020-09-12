You can also create new items and update or delete existing ones using the Admin JSON API for management.

# Passing tokens

Some frameworks and applications require a CSRF token to prevent unauthorized modification of the data. This token change with every request and has to be sent back to the server each time if available. If a CSRF token must be sent back, it will be available in the meta section of each response:

```json
{
    "meta": {
        "prefix": null,
        "csrf": {
            "name": "<token name>",
            "value": "<token value>"
        }
    }
}
```

The token must be passed with each request as GET parameter to the server:

=== "CURL"
    ```bash
    curl -b cookies.txt -c cookies.txt \
    -X POST '<resource URL>?_token=...' \
    -H 'Content-Type: application/json' \
    -d '{...}'
    ```
=== "jQuery"
    ```javascript
    // returned from OPTIONS response
    var url = options.meta.resources['product'];

    var params = {
        // ...
    };

    if(options['meta']['csrf']) {
        var csrf = {};
        csrf[options['meta']['csrf']['name']] = options['meta']['csrf']['value'];
        url += (url.indexOf('?')= -1 ? '?' : '&') + $.param(csrf);
    }

    $.ajax({
        method: "POST",
        dataType: "json",
        url: url,
        data: params
    }).done( function( result ) {
        console.log( result.data );
    });
    ```

!!! warning
    Don't forget to [nest the parameters](metadata.md#nested-parameter) if a prefix is sent in the meta data!

# Create items

Adding new items to a list of resources is done by sending a POST request to the resource URL returned by the initial OPTIONS request. You need to send the data of the new item JSON encoded in the body of the request.

=== "CURL"
    ```bash
    curl -b cookies.txt -c cookies.txt \
    -X POST 'http://localhost:8000/jsonadm/default/product?_token=...' \
    -H 'Content-Type: application/json' \
    -d '{"data": {
        "type": "product",
        "attributes": {
            "product.code": "test",
            "product.label": "Test product",
            "product.status": "0"
        }
    }}'
    ```
=== "jQuery"
    ```javascript
    // returned from OPTIONS response
    var url = options.meta.resources['product'];

    var params = {"data": {
        "type": "product",
        "attributes": {
            "product.code": "test",
            "product.label": "Test product",
            "product.status": "0"
        }
    }};

    if(options['meta']['csrf']) {
        var csrf = {};
        csrf[options['meta']['csrf']['name']] = options['meta']['csrf']['value'];
        url += (url.indexOf('?')= -1 ? '?' : '&') + $.param(csrf);
    }

    $.ajax({
        method: "POST",
        dataType: "json",
        url: url,
        data: params
    }).done( function( result ) {
        console.log( result.data );
    });
    ```

The JSON encoded request body must contain a "data" section that specifies the resource type ("product" in this case) and the list of attributes that should be set in the new item:

```json
{
    "data": {
        "type": "product",
        "attributes": {
            "product.code": "test",
            "product.label": "Test product",
            "product.status": "0"
        }
    }
}
```

It's also possible to create several new items at once. Simply send a list of resource items within the request body and use the resource URL returned by the initial OPTIONS response instead:

```json
{
    "data": [{
        "type": "product",
        "attributes": {
            "product.code": "test",
            "product.label": "Test product",
            "product.status": "0"
        }
    }, {
        "type": "product",
        "attributes": {
            "product.code": "example",
            "product.label": "Example product",
            "product.status": "1"
        }
    }]
}
```

All resource types sent in the request body must be the same (product in this example) because you are pushing them to the server using a single resource URL.

If you want to associate items to the newly created item immediately, you can use the "relationships" section. It works for all items that can be referenced via the list table provided there is one for the domain the item will be created for.

```json
{
    "data": {
        "type": "product",
        "attributes": {
            "product.code": "test",
            "product.status": "0"
        },
        "relationships": {
            "text": {
                "data": [{
                    "id": "10",
                    "type": "text",
                    "attributes": {
                        "product.lists.typeid": "1",
                        "product.lists.config": {}
                    }
                }]
            }
        }
    }
}
```

Within the `relationships` section, there can be one or more keys for the domain of the referenced items ("text" in this example). The `id` within the `data` section is the unique ID of the referenced item (e.g. from the text domain) and the `type` is the same as the domain. The key/value pairs in the `attributes` section can be anything that is returned by the *fromArray()* method of a lists item.

The response of all POST requests will contain the same data structure as in the request. Also, the "meta" section including the "total" property is included which counts the number of created items:

```json
{
    "meta": {
        "total": 1
    },
    "data": {
        "id": "1",
        "type": "product",
        "attributes": {
            "product.id": "1",
            "product.code": "test",
            "product.label": "Test product",
            "product.status": "0",
            "product.editor": "admin"
        }
    }
}
```

It also contains the ID generated by the server and all attributes of the elements that were not sent with the request. The same is returned as list if several items have been sent in the request.

# Update items

You can also update the attributes of existing items via PATCH requests. As URLs, you have to use the "self" URLs sent back by a GET request before. You need to send the updated data encoded as JSON in the body of the request.

=== "CURL"
    ```bash
    curl -b cookies.txt -c cookies.txt \
    -X PATCH 'http://localhost:8000/jsonadm/default/product?id=1&_token=...' \
    -H 'Content-Type: application/json' \
    -d '{"data": {
        "id": "1",
        "type": "product",
        "attributes": {
            "product.label": "My test product",
            "product.status": "1"
        }
    }}'
    ```
=== "jQuery"
    ```javascript
    // returned in "self" link from products response
    var url = 'http://localhost:8000/jsonadm/default/product?id=1';

    var params = {"data": {
        "id": "1",
        "type": "product",
        "attributes": {
            "product.label": "My test product",
            "product.status": "1"
        }
    }};

    if(options['meta']['csrf']) {
        var csrf = {};
        csrf[options['meta']['csrf']['name']] = options['meta']['csrf']['value'];
        url += (url.indexOf('?')= -1 ? '?' : '&') + $.param(csrf);
    }

    $.ajax({
        method: "POST",
        dataType: "json",
        url: url,
        data: params
    }).done( function( result ) {
        console.log( result.data );
    });
    ```

The JSON encoded request body must contain a "data" section that contains the resource ID, its type ("product" in this case) and the list of attributes that should be updated:

```json
{
    "data": {
        "id": "1",
        "type": "product",
        "attributes": {
            "product.label": "My test product",
            "product.status": "1"
        }
    }
}
```

It's also possible to update several new items at once. Simply send a list inside the "data" section and use the resource URL returned by the initial OPTIONS response instead:

```json
{
    "data": [{
        "id": "1",
        "type": "product",
        "attributes": {
            "product.label": "My test product",
            "product.status": "1"
        }
    }, {
        "id": "2",
        "type": "product",
        "attributes": {
            "product.label": "My example product",
            "product.status": "0"
        }
    }]
}
```

All resource types sent in the request body must be the same (product in this example) because you are patching them using a single resource URL.

!!! note
    Use the ".../lists" resource URLs (e.g. for "product/lists") to update and delete list items instead.

The response of all PATCH requests will contain the same data structure as in the request. Also, the "meta" section including the "total" property is included which counts the number of updated items:

```json
{
    "meta": {
        "total": 1
    },
    "data": {
        "id": "1",
        "type": "product",
        "attributes": {
            "product.id": "1",
            "product.label": "My test product",
            "product.status": "1",
            "product.editor": "admin"
        }
    }
}
```

Additionally, all attributes of the items are included that haven't been sent with the PATHCH request. The same is returned as list if several items have been sent in the request:

```json
{
    "meta": {
        "total": 1
    },
    "data": [{
        "id": "1",
        "type": "product",
        "attributes": {
            "product.id": "1",
            "product.label": "My test product",
            "product.status": "1",
            "product.editor": "admin"
        }
    }, {
        "id": "2",
        "type": "product",
        "attributes": {
            "product.id": "2",
            "product.label": "My example product",
            "product.status": "0",
            "product.editor": "admin"
        }
    }]
}
```

# Delete items

Resources can also be deleted. To perform this operation, you have to send a DELETE request to the server using the "self" URL listed in the "links" section of a resource returned by a previous request.


=== "CURL"
    ```bash
    curl -b cookies.txt -c cookies.txt \
    -X DELETE 'http://localhost:8000/jsonadm/default/product?id=...&_token=...'
    ```
=== "jQuery"
    ```javascript
    // returned in "self" link from resource response
    var url = 'http://localhost:8000/jsonadm/default/product?id=...';

    if(options['meta']['csrf']) {
        var csrf = {};
        csrf[options['meta']['csrf']['name']] = options['meta']['csrf']['value'];
        url += (url.indexOf('?')= -1 ? '?' : '&') + $.param(csrf);
    }

    $.ajax({
        method: "DELETE",
        dataType: "json",
        url: url,
        data: {}
    }).done( function( result ) {
        console.log( result.data );
    });
    ```

The server will return a HTTP status code 200 if the request was OK. In the "meta" section of the response, the number of items requested for deletion is assigned to the "total" property:

```json
{
    "meta": {
        "total": 1
    }
}
```

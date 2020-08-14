Inserting and updating items that are part of a hierarchical tree like categories or locale site item must be handled a bit different than regular resources.

# Insert items

Adding a new catalog or locale site item is done by sending a POST request to the resource URL returned by the initial OPTIONS request. You need to send the data of the new item JSON encoded in the body of the request.

=== "CURL"
    ```bash
	curl -b cookies.txt -c cookies.txt \
    -X POST 'http://localhost:8000/jsonadm/default/catalog?_token=...' \
    -H 'Content-Type: application/json' \
    -d '{"data": {
        "type": "catalog",
        "targetid": "1",
        "refid": null,
        "attributes": {
            "catalog.code": "test",
            "catalog.label": "Test category"
        }
    }}'
    ```
=== "jQuery"
    ```javascript
    // returned from OPTIONS response
    var url = options.meta.resources['catalog'];

    var params = {"data": {
        "type": "catalog",
        "targetid": "1",
        "refid": null,
        "attributes": {
            "catalog.code": "test",
            "catalog.label": "Test category"
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

The JSON encoded request body must contain a "data" section that specifies the resource type ("catalog" in this case) and the list of attributes that should be set in the new item. Up to now that's exactly the same procedure like for regular items. Additionally, you have to add two more properties to the "data" section:

```json
{
    "data": {
        "type": "catalog",
        "targetid": "1",
        "refid": null,
        "attributes": {
            "catalog.code": "test",
            "catalog.label": "Test category"
        }
    }
}
```

The `targetid` is the ID of the parent node where the new item will be inserted below. The `refid` property hands over the ID of the node before which the new item will be inserted. It's value can be *null* and in this case the new item will be appended at the end.

It's also possible to create several new items at once. Simply send a list of resource items within the request body and use the resource URL returned by the initial OPTIONS response instead:

```json
{
    "data": [{
        "type": "catalog",
        "targetid": "1",
        "refid": "5",
        "attributes": {
            "catalog.code": "test",
            "catalog.label": "Test category"
        }
    }, {
        "type": "catalog",
        "parentid": "1",
        "refid": null,
        "attributes": {
            "catalog.code": "test2",
            "catalog.label": "Second category"
        }
    }]
}
```

If you want to associate items to the newly created item immediately, you can use the "relationships" section. For more details about this topic and the returned response, please have a look into the article about [managing items](manage-resources.md).

# Move items

Updating items works like described in the article about [managing items](manage-resources.md). In a hierarchical tree of resource items, you can move them around within the tree too by using the PATCH request.

As URL, you have to use the "self" URL of a catalog or locale site item returned by a GET request before. You need to send the updated data encoded as JSON in the body of the request.

=== "CURL"
    ```bash
	curl -b cookies.txt -c cookies.txt \
    -X PATCH 'http://localhost:8000/jsonadm/default/catalog?id=1&_token=...' \
    -H 'Content-Type: application/json' \
    -d '{"data": {
        "id": "10",
        "type": "catalog",
        "parentid": "1",
        "targetid": "3",
        "refid": "5",
        "attributes": {
            "catalog.label": "My test category",
            "catalog.status": "1"
        }
    }}'
    ```
=== "jQuery"
    ```javascript
    // returned in "self" link from catalog response
    var url = 'http://localhost:8000/jsonadm/default/catalog?id=1';

    var params = {"data": {
        "id": "10",
        "type": "catalog",
        "parentid": "1",
        "targetid": "3",
        "refid": "5",
        "attributes": {
            "catalog.label": "My test category",
            "catalog.status": "1"
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

The JSON encoded request body must contain a "data" section that specifies the resource ID and its type ("catalog" in this case). You can add a list of attributes too. They will be used to update the resource item within the same request. Additionally, you need to add the `parentid`, the "targetid" and the `refid` properties:

```json
{
    "data": {
        "id": "10",
        "type": "catalog",
        "parentid": "1",
        "targetid": "3",
        "refid": "5",
        "attributes": {
            "catalog.label": "My test category",
            "catalog.status": "1"
        }
    }
}
```

This will update the catalog item and move it from it's current parent with the ID "1" (`parentid`) to it's new parent node with the ID "3" ("targetid") and insert it before the node with the ID "5" (`refid`). Also, the value for `refid` can be *null* so the resource item will be appended at the end of the child list below the parent with the ID "3".

It's also possible to update several new items at once. Simply send a list inside the "data" section and use the resource URL returned by the initial OPTIONS response instead:

```json
{
    "data": [{
        "id": "1",
        "type": "catalog",
        "parentid": "1",
        "targetid": "3",
        "refid": "5",
        "attributes": {
            "catalog.label": "My test category",
            "catalog.status": "1"
        }
    }, {
        "id": "2",
        "type": "catalog",
        "parentid": "1",
        "targetid": "3",
        "refid": null,
        "attributes": {
            "catalog.label": "My example category",
            "catalog.status": "0"
        }
    }]
}
```

For more details about the returned response, please have a look into the article about [managing items](manage-resources.md).

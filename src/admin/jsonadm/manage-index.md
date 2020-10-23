Using the JsonAdm API, you can also manage the product index und update or delete entries after changing/removing products without doing a full index rebuild.

# Update index

After you've changed product details (esp. attributes, prices, supplliers, texts and categories), you must update the index to avoid serving old data for product list views. This is also required to get the correct results when performing a full text search based on the search string entered by the user.

=== "CURL"
    ```bash
    curl -b cookies.txt -c cookies.txt \
    -X POST 'http://localhost:8000/jsonadm/default/index?_token=...' \
    -H 'Content-Type: application/json' \
    -d '{"data": "123"}'
    ```
=== "jQuery"
    ```javascript
    // returned from OPTIONS response
    var url = options.meta.resources['index'];

    var params = {"data": "123"};

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

The JSON encoded request body must contain a "data" attribute which is set to the product ID. Then, the index will be updated for the product identified by that ID:

```json
{
    "data": "123"
}
```

It's also possible to update several products at once. Simply send a list of product IDs as part of the "data" attribute within the request body:

```json
{
    "data": ["123", "456", "789"]
}
```

The last JSON example body will update the product index for all three products listed identified by their ID at once.

# Delete from index

If you delete a product from the database or disable it, the product should not be part of the index any more. You can't use the POST request in that case because the product shouldn't be updated but completely removed instead from the product index. Thus, you have to perform a DELETE request instead:

=== "CURL"
    ```bash
    curl -b cookies.txt -c cookies.txt \
    -X DELETE 'http://localhost:8000/jsonadm/default/index?id=...&_token=...'
    ```
=== "jQuery"
    ```javascript
    var url = 'http://localhost:8000/jsonadm/default/index?id=...';

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

You can also remove several products at once from the index if you pass the IDs in the request body:

=== "CURL"
    ```bash
    curl -b cookies.txt -c cookies.txt \
    -X DELETE 'http://localhost:8000/jsonadm/default/index?_token=...' \
    -H 'Content-Type: application/json' \
    -d '{"data": ["123", "456", "789"]}'
    ```
=== "jQuery"
    ```javascript
    // returned from OPTIONS response
    var url = options.meta.resources['index'];

    var params = {"data": ["123", "456", "789"]};

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

The server will return a HTTP status code 200 if the request was OK. In the "meta" section of the response, the number of items requested for deletion is assigned to the "total" property:

```json
{
    "meta": {
        "total": 1
    }
}
```


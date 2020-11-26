Aimeos contains a front-end JSON API modeled after the guidelines of <https://jsonapi.org/>. It enables you to view and order products via mobile apps or create JavaScript applications to access to any Aimeos based online shop using a single look and feel.

The entry point to access the Aimeos JSON API depends on the host application you use (Laravel, Symfony, TYPO3). You have to retrieve the initial base URL from a configuration setting or somewhere else. The resource URLs are different depending on the environment, but you can get the available ones by querying the meta data from the base URL (via the HTTP OPTIONS method).

# Retrieve meta data

The offered URLs to the resources depend on the application that hosts the Aimeos components. Therefore, you can't use fixed URLs like `http://localhost:8000/jsonapi/product?id=1`. Instead you need to configure the base URL to the Aimeos JSON API of the instance you want to connect to in your client application. Afterwards you must use the OPTIONS method to retrieve the service description with the list of resources and their URLs, e.g.

=== "CURL"
    ```bash
    curl -X OPTIONS 'http://localhost:8000/jsonapi'
    ```
=== "jQuery"
    ```javascript
    var url = 'http://localhost:8000/jsonapi'; // Base URL from config

    var promise = $.ajax( url, {
        method: "OPTIONS",
        dataType: "json"
    });

    promise.done( function( options ) {
        var args = {};
        var params = {};

        if(options.meta.prefix) { // returned from OPTIONS call
            params[options.meta.prefix] = args;
        } else {
            params = args;
        }

        var result = $.ajax({
            method: "GET",
            dataType: "json",
            url: options.meta.resources['product'],
            data: params
        });

        result.done( function( result ) {
            console.log( result.data );
        });
    });
    ```

It returns a JSON object containing the resources (those names are always the same and you can rely on them) and the corresponding URLs, for example:

```json
{
    "meta": {
        "prefix": null,
        "resources": {
            "attribute": "http://localhost:8000/jsonapi/attribute",
            ...
            "product": "http://localhost:8000/jsonapi/product",
            ...
            "stock": "http://localhost:8000/jsonapi/stock",
        }
    }
}
```

To access the products for example, you must lookup the URL for the "product" resource key. Similarly, you can use every key defined in the `resources` object to retrieve the corresponding items.

!!! warning
    Don't take the resource URLs in the OPTIONS response as granted! They will change depending on the routes and the application. Thus, your client needs the OPTIONS URL of the JSON REST API as configuration parameter. Its response will define the next possibilities.

# Nested parameters

Some host applications need nested GET parameters, so they are recognized as part of the JSON request. In this case, a product resource URL can look like:

```
http://localhost:8000/jsonapi?ai[resource]=product/type&ai[id]=1
```

To handle this case correctly, you must embed the GET parameters into another object if the "prefix" attribute from the service description is not empty, e.g. by:

=== "Javascript"
    ```javascript
    var args = {'resource': 'product', 'id': '1'};
    var params = {};

    if( options.meta.prefix ) {
        params[options.meta.prefix] = args;
    } else {
        params = args
    }
    ```

!!! warning
    If you don't check if the parameters must be nested, your client application won't work with all applications supported by Aimeos!

# Error handling

Errors can and will occur sooner or later. The [JSON:API standard](https://jsonapi.org/format/#errors) like every REST protocol uses the HTTP status codes to signal error conditions. Used HTTP status codes are:

* 2xx : Successful operation
    * 200 : Operation was performed successfully
    * 201 : Resource has been created
* 4xx : Bad request
    * 401 : Authentication required
    * 403 : Operation is forbidden/unsupported
    * 404 : The resource wasn't found
* 5xx : Internal server error
    * 500 : A non-recoverable error occurred
    * 501 : Operation not implemented

Also, the JSON API standard specifies an "errors" section in the JSON response that can contain error hints for one or more operations:

```json
{
    "errors": [
        {
            "title": "No product with ID 1 available",
            "detail": "<stack trace where the error occured>"
        },
        ...
    ]
}
```

Each error item contains a "title" attribute that contains the error message for the user and the "detail" attribute including the stack trace for developers. You should show the error details because they are only helpful for developers.

!!! note
    The stack trace is only included if you enable debugging by configuring:
    ```
    client/jsonapi/debug = 1
    ```

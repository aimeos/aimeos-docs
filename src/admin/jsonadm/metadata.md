The offered URLs to the resources depend on the application that hosts the Aimeos components. Therefore, you can't use fixed URLs like `https://mydomain.com/admin/default/jsonadm/product/1`. Instead, you need to configure the base URL to the Aimeos JSON API of the instance you  want to connect to in your client application.

# Resource list

Afterwards, you must use the OPTIONS method to retrieve the service description with the list of resources and their URLs, e.g.

=== "CURL"
    ```bash
    curl -b cookies.txt -c cookies.txt \
    -X OPTIONS 'https://localhost:8000/admin/default/jsonadm'
    ```
=== "jQuery"
    ```javascript
    // Base URL from config
    var url = 'https://localhost:8000/admin/default/jsonadm';

    var options = $.ajax( url, {
        method: "OPTIONS",
        dataType: "json"
    });

    options.done( function( result ) {
        console.log( result.data );
    });
    ```

It returns a JSON object containing the resources (those names are always the same and you can rely on them) and the corresponding URLs. An example response would be:

```json
{
    "meta": {
        "resources": {
            "attribute": "http://localhost:8000/admin/default/jsonadm/attribute",
            "attribute/lists": "http://localhost:8000/admin/default/jsonadm/attribute/lists",
            "attribute/property": "http://localhost:8000/admin/default/jsonadm/attribute/property",
            "catalog": "http://localhost:8000/admin/default/jsonadm/catalog"
        }
    }
}
```

To access the products for example, you must lookup the URL for the "product" resource key:

=== "CURL"
    ```bash
    curl -b cookies.txt -c cookies.txt \
    -X GET 'http://localhost:8000/admin/default/jsonadm/product'
    ```
=== "jQuery"
    ```javascript
    var params = {};

    var result = $.ajax({
        method: "GET",
        dataType: "json",
        url: options.meta.resources['product'], // from OPTIONS response
        data: {}
    });

    result.done( function( result ) {
        console.log( result.data );
    });
    ```

Similarly, you can use every key defined in the "resources" object to retrieve the corresponding items.

# Item attributes

The response from the OPTIONS request also contains the attributes of all items:

```json
{
    "meta": {
        "attributes": {
            "catalog.id": {
                "code": "catalog.id",
                "type": "integer",
                "label": "ID",
                "public": false,
                "default": null,
                "required": true
            },
            "catalog.label": {
                "code": "catalog.label",
                "type": "string",
                "label": "Label",
                "public": true,
                "default": null,
                "required": true
            },
            ...
        }
    }
}
```

You can use that to build filters for the user interface. The `public` property of each item attribute states if it should be shown to the user or not.

# Nested parameters

Some host applications need nested GET parameters so they are recognized as part of the JSON request. In this case, a product resource URL can look like:

```
http://localhost:8000/admin/default/jsonadm?ai[resource]=product&ai[id]=1
```

To handle this case correctly, you must embed the GET parameters into another object if the `prefix` attribute from the OPTIONS response is not empty:

```json
{
    "meta": {
        "prefix": "ai"
    }
}
```

The following code handles embedding parameters depending on the availability of a prefix:

```javascript
var params;

if( options.meta.prefix ) {
    params[options.meta.prefix] = {resource: "product", id: "1"};
} else {
    params = {resource: "product", id: '1'};
}
```

Otherwise, your client application won't work with all applications supported by Aimeos!

Before you can retrieve the product items, you have to get to know the product resource endpoint via the OPTIONS request. Depending on the used routes it might be something like:

```bash
curl -X OPTIONS 'http://localhost:8000/jsonapi'
```

The response will contain the required endpoints you have to use:

```json
{
    "meta": {
        "prefix": "ai",
        "resources": {
            "attribute": "http://localhost:8000/jsonapi/attribute",
            "catalog": "http://localhost:8000/jsonapi/catalog",
            "product": "http://localhost:8000/jsonapi/product",
            "stock": "http://localhost:8000/jsonapi/stock",
            ...
        }
    }
}
```

Have a look at [retrieving an OPTIONS request](index.md#retrieve-meta-data) for more details.

For each endpoint you can use an OPTIONS request to get the supported filter and sort keys:

```bash
curl -X OPTIONS 'http://localhost:8000/jsonapi/product'
```

It also returns the [prefix](index.md#nested-parameters) you have to use, if the value is not `null`, and the base URL for media files:

```json
{
"meta": {
    "prefix": null,
    "content-baseurl": "http://localhost:8000/",
    "content-baseurls": {
        "fs-media": "http://localhost:8000/aimeos",
        "fs-mimeicon": "http://localhost:8000/vendor/shop/mimeicons",
        "fs-theme": "http://localhost:8000/vendor/shop/themes"
    },
    "filter": {
        "f_search": {
            "label": "Return products whose text matches the user input",
            "type": "string",
            "default": "",
            "required": false
        },
    },
    "sort": {
        "relevance": {
            "label": "Sort products by their category position",
            "type": "string",
            "default": true,
            "required": false
        }
    }
}
```

# Fetch products

Now you can retrieve product data directly via the "product" resource you get from the OPTIONS response. As the full, unsorted list of products isn't very helpful for users, you should offer the possibilities to search for products, list them by categories and filter them by their attributes in a faceted search.

Independent of how you filter products, you will always get back a JSON object like this if you use:

```bash
# include attribute, media, price, product, product/property, text
# as well as category, supplier and stock items
curl -X GET 'http://localhost:8000/jsonapi/product?include=attribute,media,price,product,product/property,text,catalog,supplier,stock'
```

```json
{
    "meta": {
        "total": 3
    },
    "links": {
        "self": "http:\/\/localhost:8000\/jsonapi\/product?include=attribute%2Cmedia%2Cprice%2Cproduct%2Cproduct%2Fproperty%2Ctext&page%5Boffset%5D=0"
    },
    "data": [{
        "id": "13",
        "type": "product",
        "links": {
            "self": {
                "href": "http:\/\/localhost:8000\/jsonapi\/product\/13",
                "allow": ["GET"]
            },
            "basket\/product": {
                "href": "http:\/\/localhost:8000\/jsonapi\/basket\/default\/product",
                "allow": ["POST"]
            }
        },
        "attributes": {
            "product.id": "13",
            "product.type": "default",
            "product.code": "demo-article",
            "product.label": "Demo article",
            "product.status": 1,
            "product.datestart": null,
            "product.dateend": null,
            "product.config": []
        },
        "relationships": {
            "product.property": {
                "data": [
                    {"id": "12", "type": "product.property"}
                ]
            },
            "attribute": {
                "data": [{
                    "id": "25", "type": "attribute",
                    "attributes": {"product.lists.type": "default", ...}
                }]
            },
            "media": {
                "data": [{
                    "id": "55", "type": "media",
                    "attributes": {"product.lists.type": "default", .... }
                }]
            },
            "price": {
                "data": [{
                    "id": "93", "type": "price",
                    "attributes": {"product.lists.type": "default", ...}
                }]
            },
            "text": {
                "data": [{
                    "id": "228", "type": "text",
                    "attributes": {"product.lists.type": "default", ...}
                }]
            },
            "catalog": {
                "data": [{
                    "id": "1", "type": "catalog"
                }]
            },
            "supplier": {
                "data": [{
                    "id": "2", "type": "supplier"
                }]
            },
            "stock": {
                "data": [{
                    "id": "1", "type": "stock"
                }]
            }
        }
    }],
    "included": [{
        "id": "12",
        "type": "product.property",
        "attributes": {
            "product.property.id": "12",
            "product.property.languageid": null,
            "product.property.value": "20.00",
            "product.property.type": "package-length"
        }
    }, {
        "id": "25",
        "type": "attribute",
        "attributes": {
            "attribute.id": "25",
            "attribute.domain": "product",
            "attribute.code": "demo-black",
            "attribute.status": 1,
            "attribute.type": "color",
            "attribute.position": 1,
            "attribute.label": "Demo: Black"
        }
    }, {
        "id": "55",
        "type": "media",
        "attributes": {
            "media.id": "55",
            "media.domain": "product",
            "media.label": "Demo: Article 1.jpg",
            "media.languageid": null,
            "media.mimetype": "image\/jpeg",
            "media.type": "default",
            "media.preview": "http:\/\/demo.aimeos.org\/media\/1.jpg",
            "media.url": "http:\/\/demo.aimeos.org\/media\/1-big.jpg",
            "media.status": 1
        }
    }, {
        "id": "93",
        "type": "price",
        "attributes": {
            "price.id": "93",
            "price.type": "default",
            "price.currencyid": "EUR",
            "price.domain": "product",
            "price.quantity": 1,
            "price.value": "100.00",
            "price.costs": "5.00",
            "price.rebate": "20.00",
            "price.taxvalue": "21.0000",
            "price.taxrate": "20.00",
            "price.taxflag": false,
            "price.status": 1,
            "price.label": "Demo: Article from 1"
        }
    }, {
        "id": "228",
        "type": "text",
        "attributes": {
            "text.id": "228",
            "text.languageid": "en",
            "text.type": "short",
            "text.label": "Demo short\/en: This is the short description",
            "text.domain": "product",
            "text.content": "This is the short description of the demo article.",
            "text.status": 1
        }
    }, {
        "id": "1",
        "type": "catalog",
        "attributes": {
            "catalog.id": "1",
            "catalog.code": "home",
            "catalog.label": "Home",
            "catalog.config": [],
            "catalog.status": 1,
            "catalog.target": "",
            "catalog.hasChildren": true
        }
    }, {
        "id": "2",
        "type": "supplier",
        "attributes": {
            "supplier.id": "2",
            "supplier.code": "demo-test2",
            "supplier.label": "Test supplier 2",
            "supplier.status": 1
        }
    }, {
        "id": "1",
        "type": "stock",
        "attributes": {
            "stock.id": "1",
            "stock.productcode": "demo-article",
            "stock.stocklevel": null,
            "stock.timeframe": "",
            "stock.dateback": null,
            "stock.type": "default"
        }
    }]
}
```

!!! note
    Returning categories, suppliers and stock items in the product response is available since 2020.07.

# Sort product lists

In addition to the generic filter possibilities, the product lists can be sorted easily by these keys:

* "relevance" (asc) or "-relevance" (desc)
* "name" (asc) or "-name" (desc)
* "price" (asc) or "-price" (desc)
* "ctime" (asc) or "-ctime" (desc)

=== "CURL"
    ```bash
    curl -X GET 'http://localhost:8000/jsonapi/product?sort=-ctime'
    ```
=== "Javascript"
    ```javascript
    const args = {
        'sort': '-ctime'
    }
    let params = {}

    if(options.meta.prefix) { // returned from OPTIONS call
        params[options.meta.prefix] = args
    } else {
        params = args
    }

    // returned from OPTIONS call
    const url = options.meta.resources['product']
        + (options.meta.resources['product'].includes('?') ? '&' : '?')
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
    var args = {'sort': '-ctime'};
    var params = {};

    if(options.meta.prefix) { // returned from OPTIONS call
        params[options.meta.prefix] = args;
    } else {
        params = args;
    }

    $.ajax({
        method: 'GET',
        dataType: 'json',
        url: options.meta.resources['product'], // returned from OPTIONS call
        data: params
    }).done( function( result ) {
        console.log( result );
    });
    ```

Sorting by "relevance" is the default sorting parameter if no other is passed to the server. You can also sort by other product fields, e.g. by the start date of the products using *&sort=product.datestart*

# Search products by text

If you offer users a search field for products, you have to add the entered text as query parameter to the URL of the product resource you got from the OPTIONS response:

=== "CURL"
    ```bash
    curl -X GET 'http://localhost:8000/jsonapi/product?filter[f_search]=demo'
    ```
=== "Javascript"
    ```javascript
    const args = {
        'filter': {
            'f_search': 'demo'
        }
    }
    let params = {}

    if(options.meta.prefix) { // returned from OPTIONS call
        params[options.meta.prefix] = args
    } else {
        params = args
    }

    // returned from OPTIONS call
    const url = options.meta.resources['product']
        + (options.meta.resources['product'].includes('?') ? '&' : '?')
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
            'f_search': 'demo'
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
        url: options.meta.resources['product'], // returned from OPTIONS call
        data: params
    }).done( function( result ) {
        console.log( result );
    });
    ```

# Filter products by price

To enable users to filter products by price, you need to use the *index.price:value* filter as well as the three letter currency code as parameter in round brackets and quotation marks ("). To return only products with a price of less than e.g. 99.50 Euro, you need:

=== "CURL"
    ```bash
    curl -X GET 'http://localhost:8000/jsonapi/product?filter[<][index.price:value("EUR")]=99.50'
    ```
=== "Javascript"
    ```javascript
    const args = {
        'filter': {
            '<': {'index.price:value("EUR")': 99.50}
        }
    }
    let params = {}

    if(options.meta.prefix) { // returned from OPTIONS call
        params[options.meta.prefix] = args
    } else {
        params = args
    }

    // returned from OPTIONS call
    const url = options.meta.resources['product']
        + (options.meta.resources['product'].includes('?') ? '&' : '?')
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
            '<': {'index.price:value("EUR")': 99.50}
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
        url: options.meta.resources['product'], // returned from OPTIONS call
        data: params
    }).done( function( result ) {
        console.log( result );
    });
    ```

Usually, you want to filter for a price range, so you need to pass an upper and a lower value:

=== "CURL"
    ```bash
    # filter[&&][][>][index.price:value("EUR")]=100
    # &filter[&&][][<][index.price:value("EUR")]=200
    curl -X GET 'http://localhost:8000/jsonapi/product?filter[%26%26][][%3E][index.price:value("EUR")]=100&filter[%26%26][][%3C][index.price:value("EUR")]=200'
    ```
=== "Javascript"
    ```javascript
    const args = {
        'filter': {
            '&&': [
                {'>': {'index.price:value("EUR")': 100}},
                {'<': {'index.price:value("EUR")': 200}}
            ]
        }
    }
    let params = {}

    if(options.meta.prefix) { // returned from OPTIONS call
        params[options.meta.prefix] = args
    } else {
        params = args
    }

    // returned from OPTIONS call
    const url = options.meta.resources['product']
        + (options.meta.resources['product'].includes('?') ? '&' : '?')
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
            '&&': [
                {'>': {'index.price:value("EUR")': 100}},
                {'<': {'index.price:value("EUR")': 200}}
            ]
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
        url: options.meta.resources['product'], // returned from OPTIONS call
        data: params
    }).done( function( result ) {
        console.log( result );
    });
    ```

# Retrieve categories

To display the category tree, you have to use the "catalog" resource returned by the OPTIONS method:

=== "CURL"
    ```bash
    curl -X GET 'http://localhost:8000/jsonapi/catalog?include=catalog,media,text'
    ```
=== "Javascript"
    ```javascript
    const args = {
        'include': 'catalog,media,text'
    }
    let params = {}

    if(options.meta.prefix) { // returned from OPTIONS call
        params[options.meta.prefix] = args
    } else {
        params = args
    }

    // returned from OPTIONS call
    const url = options.meta.resources['product']
        + (options.meta.resources['product'].includes('?') ? '&' : '?')
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
    var args = {'include': 'catalog,media,text'};
    var params = {};

    if(options.meta.prefix) { // returned from OPTIONS call
        params[options.meta.prefix] = args;
    } else {
        params = args;
    }

    $.ajax({
        method: 'GET',
        dataType: 'json',
        url: options.meta.resources['catalog'], // returned from OPTIONS call
        data: params
    }).done( function( result ) {
        console.log( result );
    });
    ```

This will return the root catalog node and its direct children as well as their related texts and images:

```json
{
    ...,
    "data": {
        "id": "201",
        "type": "catalog",
        "links": {
            "self": {
                "href": "http:\/\/localhost:8000\/jsonapi\/catalog?id=201",
                "allow": ["GET"]
            },
            "product": {"
                href": "http:\/\/localhost:8000\/jsonapi\/product?filter%5Bf_catid%5D=201",
                "allow": ["GET"]
            }
        },
        "attributes": {
            "catalog.id": "201",
            "catalog.code": "root",
            "catalog.label": "Root",
            "catalog.status": 1,
            "catalog.config": {"css-class": "home"},
            "catalog.hasChildren": true
        },
        "relationships": {
            "catalog": {
                "data": [{
                    "id": "203", "type": "catalog",
                    "attributes": {"catalog.list.type": "default"}
                }]
            }
        }
    },
    "included": [{
        "id": "203",
        "type": "catalog",
        "links": {
            "self": {
                "href": "http:\/\/localhost:8000\/jsonapi\/catalog?id=203",
                "allow": ["GET"]}
        },
        "attributes": {
            "catalog.id": "203",
            ...
        },
        "relationships": {
            "media": {
                "data": [
                    {
                        "id": "360",
                        "type": "media",
                        "attributes": {
                            "catalog.lists.type": "icon",
                            ...
                        }
                    }
                ]
            }
        }
    },
    {
        "id": "360",
        "type": "media",
        "attributes": {
            "media.id": "360",
            "media.preview": "example4.jpg",
            "media.url": "path\/to\/folder\/example4.jpg",
            ...
        }
    }
]}
```

If you wish to display the children's children of a specific category, use the URL that is provided by the **links[self]** key in the "included" section.

!!! tip
    To retrieve the whole category tree instead of just the children, use the [client/jsonapi/catalog/deep](../../config/client-jsonapi/catalog.md#deep) setting but beware: Allow retrieving all categories only if your category tree contains only a limited number of nodes! Otherwise, malicious users can easily create denial of service attacks!

# Get products by category

To get the products for a category, use the *f_catid* filter parameter:

=== "CURL"
    ```bash
    curl -X GET 'http://localhost:8000/jsonapi/product?filter[f_catid]=1'
    ```
=== "Javascript"
    ```javascript
    const args = {
        'filter': {
            'f_catid': '1'
        }
    }
    let params = {}

    if(options.meta.prefix) { // returned from OPTIONS call
        params[options.meta.prefix] = args
    } else {
        params = args
    }

    // returned from OPTIONS call
    const url = options.meta.resources['product']
        + (options.meta.resources['product'].includes('?') ? '&' : '?')
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
            'f_catid': '1'
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
        url: options.meta.resources['product'], // returned from OPTIONS call
        data: params
    }).done( function( result ) {
        console.log( result );
    });
    ```

By default, all the found products use "default" as the category list type. You can change the list type searched for by adding the *f_listtype* parameter to e.g. **promotion** to get promotional products:

=== "CURL"
    ```bash
    curl -X GET 'http://localhost:8000/jsonapi/product?filter[f_catid]=1&filter[f_listtype]=promotion'
    ```
=== "Javascript"
    ```javascript
    const args = {
        'filter': {
            'f_catid': '1',
            'f_listtype': 'promotion'
        }
    }
    let params = {}

    if(options.meta.prefix) { // returned from OPTIONS call
        params[options.meta.prefix] = args
    } else {
        params = args
    }

    // returned from OPTIONS call
    const url = options.meta.resources['product']
        + (options.meta.resources['product'].includes('?') ? '&' : '?')
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
            'f_catid': '1',
            'f_listtype': 'promotion'
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
        url: options.meta.resources['product'], // returned from OPTIONS call
        data: params
    }).done( function( result ) {
        console.log( result );
    });
    ```

# Attributes for faceted search

The product attributes for building the faceted search can be retrieved using the "attribute" resource returned by the OPTIONS method:

=== "CURL"
    ```bash
    curl -X GET 'http://localhost:8000/jsonapi/attribute?include=media,text'
    ```
=== "Javascript"
    ```javascript
    const args = {
        'include': 'media,text'
    }
    let params = {}

    if(options.meta.prefix) { // returned from OPTIONS call
        params[options.meta.prefix] = args
    } else {
        params = args
    }

    // returned from OPTIONS call
    const url = options.meta.resources['attribute']
        + (options.meta.resources['attribute'].includes('?') ? '&' : '?')
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
    var args = {'include': 'media,text'};
    var params = {};

    if(options.meta.prefix) { // returned from OPTIONS call
        params[options.meta.prefix] = args;
    } else {
        params = args;
    }

    $.ajax({
        method: 'GET',
        dataType: 'json',
        url: options.meta.resources['attribute'], // returned from OPTIONS call
        data: params
    }).done( function( result ) {
        console.log( result );
    });
    ```

This will return the first slice of attribute items as well as their related texts and images:

```json
{
    ...,
    "data": [{
        "id": "32",
        "type": "attribute",
        "links": {
            "self": {
                "href": "http:\/\/localhost:8000\/jsonapi\/attribute?id=32",
                "allow": ["GET"]
            }
        },
        "attributes": {
            "attribute.id": "32",
            "attribute.domain": "product",
            "attribute.code": "demo-beige",
            "attribute.status": 1,
            "attribute.type": "color",
            "attribute.position": 0,
            "attribute.label": "Demo: Beige"
        },
        "relationships": {
            "media": {
                "data": [{
                    "id": "60", "type": "media",
                    "attributes": {"attribute.list.type": "default", ...}
                }]
            },
            "text": {
                "data": [{
                    "id": "241", "type": "text",
                    "attributes": {"attribute.list.type": "default", ...}
                }]
            }
        }
    }],
    "included": [{
        "id": "60",
        "type": "media",
        "attributes": {
            "media.id": "60",
            "media.domain": "attribute",
            "media.label": "Demo: beige.gif",
            "media.languageid": null,
            "media.mimetype": "image\/gif",
            "media.type": "default",
            "media.previews": {
                "1": "relative\/path\/to\/preview.jpg",
                "250": "relative\/path\/to\/250-preview.jpg"
            },
            "media.preview": "relative\/path\/to\/preview.jpg",
            "media.url": "relative\/path\/to\/original.jpg",
            "media.status": 1
        }
    }, {
        "id": "241",
        "type": "text",
        "attributes": {
            "text.id": "241",
            "text.languageid": "en",
            "text.type": "name",
            "text.label": "Demo name\/en: Beige",
            "text.domain": "attribute",
            "text.content": "Beige",
            "text.status": 1
        }
    }]
}
```

Group the attributes by their "attribute.code" and sort them by "attribute.position" to make it easy for users to find the product attributes.

# Get products by attributes

If the user selects one or more of the attributes, you can get the corresponding products by adding a *f_attrid* to the product URL:

=== "CURL"
    ```bash
    curl -X GET 'http://localhost:8000/jsonapi/product?filter[f_attrid][]=1&filter[f_attrid][]=3'
    ```
=== "Javascript"
    ```javascript
    const args = {
        'filter': {
            'f_attrid': ['1','3']
        }
    }
    let params = {}

    if(options.meta.prefix) { // returned from OPTIONS call
        params[options.meta.prefix] = args
    } else {
        params = args
    }

    // returned from OPTIONS call
    const url = options.meta.resources['product']
        + (options.meta.resources['product'].includes('?') ? '&' : '?')
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
            'f_attrid': ['1','3']
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
        url: options.meta.resources['product'], // returned from OPTIONS call
        data: params
    }).done( function( result ) {
        console.log( result );
    });
    ```

Instead of *f_attrid* which combines all attributes with an **AND** condition, you can also use *f_optid* which uses an **OR** condition:

=== "CURL"
    ```bash
    curl -X GET 'http://localhost:8000/jsonapi/product?filter[f_optid][]=1&filter[f_optid][]=3'
    ```
=== "Javascript"
    ```javascript
    const args = {
        'filter': {
            'f_optid': ['1','3']
        }
    }
    let params = {}

    if(options.meta.prefix) { // returned from OPTIONS call
        params[options.meta.prefix] = args
    } else {
        params = args
    }

    // returned from OPTIONS call
    const url = options.meta.resources['product']
        + (options.meta.resources['product'].includes('?') ? '&' : '?')
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
            'f_optid': ['1','3']
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
        url: options.meta.resources['product'], // returned from OPTIONS call
        data: params
    }).done( function( result ) {
        console.log( result );
    });
    ```

Or you can use *f_oneid* with pairs of attribute types and list of attribute IDs to filter for products that contain **at least one** of the attributes per type:

=== "CURL"
    ```bash
    curl -X GET 'http://localhost:8000/jsonapi/product?filter[f_oneid][color][]=1&filter[f_oneid][length][]=3'
    ```
=== "Javascript"
    ```javascript
    const args = {
        'filter': {
            'f_oneid': {
                'color': ['1'],
                'size': ['3']
            }
        }
    }
    let params = {}

    if(options.meta.prefix) { // returned from OPTIONS call
        params[options.meta.prefix] = args
    } else {
        params = args
    }

    // returned from OPTIONS call
    const url = options.meta.resources['product']
        + (options.meta.resources['product'].includes('?') ? '&' : '?')
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
            'f_oneid': {
                'color': ['1'],
                'size': ['3']
            }
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
        url: options.meta.resources['product'], // returned from OPTIONS call
        data: params
    }).done( function( result ) {
        console.log( result );
    });
    ```

# Suppliers for faceted search

To fetch the suppliers for building the supplier facet, use the "supplier" resource returned by the OPTIONS method:

=== "CURL"
    ```bash
    curl -X GET 'http://localhost:8000/jsonapi/supplier?include=media,text'
    ```
=== "Javascript"
    ```javascript
    const args = {
        'include': 'media,text'
    }
    let params = {}

    if(options.meta.prefix) { // returned from OPTIONS call
        params[options.meta.prefix] = args
    } else {
        params = args
    }

    // returned from OPTIONS call
    const url = options.meta.resources['supplier']
        + (options.meta.resources['supplier'].includes('?') ? '&' : '?')
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
    var args = {'include': 'media,text'};
    var params = {};

    if(options.meta.prefix) { // returned from OPTIONS call
        params[options.meta.prefix] = args;
    } else {
        params = args;
    }

    $.ajax({
        method: 'GET',
        dataType: 'json',
        url: options.meta.resources['supplier'], // returned from OPTIONS call
        data: params
    }).done( function( result ) {
        console.log( result );
    });
    ```

This will return the first slice of supplier items as well as their associated texts and images:

```json
{
    ...,
    "data": [{
        "id": "1",
        "type": "supplier",
        "links": {
            "self": {
                "href": "http:\/\/localhost:8000\/jsonapi\/supplier?id=32",
                "allow": ["GET"]
            }
        },
        "attributes": {
            "supplier.id": "1",
            "supplier.code": "demo-test1",
            "supplier.label": "Test supplier 1",
            "supplier.status": 1
        },
        "relationships": {
            "media": {
                "data": [{
                    "id": "8", "type": "media",
                    "attributes": {"attribute.list.type": "default", ...}
                }]
            },
            "text": {
                "data": [{
                    "id": "34", "type": "text",
                    "attributes": {"attribute.list.type": "default", ...}
                }]
            }
        }
    }],
    "included": [{
        "id": "8",
        "type": "media",
        "attributes": {
            "media.id": "8",
            "media.domain": "supplier",
            "media.label": "Supplier logo",
            "media.languageid": null,
            "media.mimetype": "image\/jpg",
            "media.type": "default",
            "media.previews": {
                "1": "relative\/path\/to\/preview.jpg",
                "250": "relative\/path\/to\/250-preview.jpg"
            },
            "media.preview": "relative\/path\/to\/preview.jpg",
            "media.url": "relative\/path\/to\/original.jpg",
            "media.status": 1
        }
    }, {
        "id": "34",
        "type": "text",
        "attributes": {
            "text.id": "34",
            "text.languageid": "en",
            "text.type": "name",
            "text.label": "Demo supplier",
            "text.domain": "supplier",
            "text.content": "Demo supplier LLC",
            "text.status": 1
        }
    }]
}
```

# Get products by supplier

If the user selects a supplier, you can get the corresponding products by adding a *f_supid* to the product URL:

=== "CURL"
    ```bash
    curl -X GET 'http://localhost:8000/jsonapi/product?filter[f_supid]=1'
    ```
=== "Javascript"
    ```javascript
    const args = {
        'filter': {
            'f_supid': '1'
        }
    }
    let params = {}

    if(options.meta.prefix) { // returned from OPTIONS call
        params[options.meta.prefix] = args
    } else {
        params = args
    }

    // returned from OPTIONS call
    const url = options.meta.resources['product']
        + (options.meta.resources['product'].includes('?') ? '&' : '?')
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
            'f_supid': '1'
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
        url: options.meta.resources['product'], // returned from OPTIONS call
        data: params
    }).done( function( result ) {
        console.log( result );
    });
    ```

# Count matching products

For a real faceted search, you need the number of matching products per attribute and category.

## Attribute count

You can get the attribute counts by using the **aggregate** key and the corresponding *index.attribute.id* search key:

=== "CURL"
    ```bash
    curl -X GET 'http://localhost:8000/jsonapi/product?aggregate=index.attribute.id'
    ```
=== "Javascript"
    ```javascript
    const args = {
        'aggregate': 'index.attribute.id'
    }
    let params = {}

    if(options.meta.prefix) { // returned from OPTIONS call
        params[options.meta.prefix] = args
    } else {
        params = args
    }

    // returned from OPTIONS call
    const url = options.meta.resources['product']
        + (options.meta.resources['product'].includes('?') ? '&' : '?')
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
    var args = {'aggregate': 'index.attribute.id'};
    var params = {};

    if(options.meta.prefix) { // returned from OPTIONS call
        params[options.meta.prefix] = args;
    } else {
        params = args;
    }

    $.ajax({
        method: 'GET',
        dataType: 'json',
        url: options.meta.resources['product'], // returned from OPTIONS call
        data: params
    }).done( function( result ) {
        console.log( result );
    });
    ```

This will return a list of "id" and "attributes" pairs where the value of "id" is the attribute ID and "attributes" is the number of products that contain that attribute:

```javascript
{
    "meta": {
        "total": 12
    },
    "data": [
        {"id":25, "type":"index.attribute.id", "attributes":"2"},
        {"id":26, "type":"index.attribute.id","attributes":"2"},
        {"id":29, "type":"index.attribute.id","attributes":"1"}
    ]
}
```

## Categories count

In the same way you can get the product counts for the categories by using the **aggregate** key and the corresponding *index.catalog.id* search key:

=== "CURL"
    ```bash
    curl -X GET 'http://localhost:8000/jsonapi/product?aggregate=index.catalog.id'
    ```
=== "Javascript"
    ```javascript
    const args = {
        'aggregate': 'index.catalog.id'
    }
    let params = {}

    if(options.meta.prefix) { // returned from OPTIONS call
        params[options.meta.prefix] = args
    } else {
        params = args
    }

    // returned from OPTIONS call
    const url = options.meta.resources['product']
        + (options.meta.resources['product'].includes('?') ? '&' : '?')
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
    var args = {'aggregate': 'index.catalog.id'};
    var params = {};

    if(options.meta.prefix) { // returned from OPTIONS call
        params[options.meta.prefix] = args;
    } else {
        params = args;
    }

    $.ajax({
        method: 'GET',
        dataType: 'json',
        url: options.meta.resources['product'], // returned from OPTIONS call
        data: params
    }).done( function( result ) {
        console.log( result );
    });
    ```

This will return a list of "id" and "attributes" pairs where the value of "id" is the category ID and "attributes" is the number of products that are associated to the category:

```javascript
{
    "meta": {
        "total": 1
    },
    "data": [
        {"id":1,"type":"index.catalog.id","attributes":"3"}
    ]
}
```

## Supplier count

To get the product counts for the suppliers, use the **aggregate** key and the corresponding *index.supplier.id* search key:

=== "CURL"
    ```bash
    curl -X GET 'http://localhost:8000/jsonapi/product?aggregate=index.supplier.id'
    ```
=== "Javascript"
    ```javascript
    const args = {
        'aggregate': 'index.supplier.id'
    }
    let params = {}

    if(options.meta.prefix) { // returned from OPTIONS call
        params[options.meta.prefix] = args
    } else {
        params = args
    }

    // returned from OPTIONS call
    const url = options.meta.resources['product']
        + (options.meta.resources['product'].includes('?') ? '&' : '?')
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
    var args = {'aggregate': 'index.supplier.id'};
    var params = {};

    if(options.meta.prefix) { // returned from OPTIONS call
        params[options.meta.prefix] = args;
    } else {
        params = args;
    }

    $.ajax({
        method: 'GET',
        dataType: 'json',
        url: options.meta.resources['product'], // returned from OPTIONS call
        data: params
    }).done( function( result ) {
        console.log( result );
    });
    ```

This will return a list of "id" and "attributes" pairs where the value of "id" is the supplier ID and "attributes" is the number of products that are associated to the supplier:

```javascript
{
    "meta": {
        "total": 1
    },
    "data": [
        {"id":1,"type":"index.supplier.id","attributes":"2"}
    ]
}
```

# Stock levels for products

If you don't fetch the stock levels together with the products using *&include=stock*, you can retrieve the stock levels separately by using the value of the "product.id" attribute:

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

It returns the list of stock items for the given product IDs:

```json
{
    "data": [{
        "id": "12",
        "type": "stock",
        "links": {
            "self": {
                "href": "http:\/\/localhost:8000\/jsonapi\/stock\/12",
                "allow": ["GET"]
            }
        },
        "attributes": {
            "stock.id": "12",
            "stock.productid": "1234",
            "stock.stocklevel": null,
            "stock.dateback": null,
            "stock.type": "default"
        }
    }
]}
```

If the shop has different warehouses or local stores where customers can pick up their ordered products, you can use the *s_stocktype* parameter to fetch stock levels for different locations than the "default" one:

=== "CURL"
    ```bash
    curl -X GET 'http://localhost:8000/jsonapi/stock?filter[s_prodid][]=1234&filter[s_stocktype]=berlin'
    ```
=== "Javascript"
    ```javascript
    const args = {
        'filter': {
            's_prodid': ['1234'],
            's_stocktype': 'berlin'
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
            's_prodid': ['1234'],
            's_stocktype': 'berlin'
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

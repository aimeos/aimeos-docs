To fetch items from a resource, you need a GET request with the URL from the resource definition:

```bash
# resource URL returned by the OPTIONS request
curl -X GET 'http://localhost:8000/jsonapi/product'
```

Please have a look at [retrieving an OPTIONS request](index.md#retrieve-meta-data) for more details.

# Response structure

All GET requests will return a JSON object with the structure defined by [jsonapi.org](https://jsonapi.org/):

```json
{
    "meta": {
         "total": 100
    },
    "links": {
        "first": "http://localhost:8000/jsonapi/product?page[offset]=0",
        "prev": "http://localhost:8000/jsonapi/product?page[offset]=0",
        "next": "http://localhost:8000/jsonapi/product?page[offset]=25",
        "last": "http://localhost:8000/jsonapi/product?page[offset]=75",
        "self": "http://localhost:8000/jsonapi/product?page[offset]=0"
    },
    "data": [ {
        "type": "product",
        "id": "1",
        "attributes": {
             "product.id": "1",
             "product.status": "1"
        },
        "links": {
            "self": "http://localhost:8000/jsonapi/product/1"
        },
        "relationships": {
            "product.property": [{
                "data": {
                    "id": "12",
                    "type": "product.property"
                }
            }],
            "text": [{
                "data": {
                    "id": "9",
                    "type": "text",
                    "attributes": {
                        "product.lists.id": "5",
                        "product.lists.refid": "9"
                    }
                }
            }]
        }
    }],
    "included": [{
        "id": "12",
        "type": "product.property",
        "attributes": {
            "product.property.id": "12",
            "product.property.value": "1234-ABCD-5678"
    }, {
        "type": "text",
        "id": "9",
        "attributes": {
            "text.id": "9",
            "text.content": "My product name"
        }
    }]
}
```

The **"meta"** section will always contain a "total" property on success. Its value is the number of items found in total for the current search filter.

In the **"links"** section, all necessary links for navigating through the result set are listed including the link for the current request.

**"data"** contains the product items, and each item always contains the ID and the resource type. In the attributes section, you will find the same data as returned by the *toArray()* method for every item. An URL referencing the unique resource is included in "links". If related items are included, they will be referenced by their ID and type in the "relationships" section. Items that are associated via lists will also contain an "attributes" section with the data for the list table.

In the **"included"** section all related items are listed if you told the server to hand them over in the same request as well. Its structure is the same as for the "data" section. For more information, please have a look into the [related resources](#include-related-resources) section.

By default, the first 48 items available will be returned if no further GET parameters are sent along with the request. There are three parameters to modify that behavior:

* filter (conditions to retrieve specific items)
* sort (defines the order of the items in the result set)
* page (contains "start" and "limit" for getting slices of the result set)

!!! tip
    For debugging, you can get a more human-readable output if you add *&pretty=1* at the end of the URLs.

# Filtering the result

Each resource offers custom search parameters to retrieve data for common use cases. Please have a look into the articles about products, basket, etc. for details about these parameters.

Additionally, you can use custom filters for each resource. The JSON API standard defines a parameter named "filter" that can contain arbitrary conditions. In the Aimeos API you can use conditions for comparing values and combining them. E.g. to get all product items which are selections, you can do this:

=== "CURL"
    ```bash
    # filter[>][product.type]=select
    curl -X GET 'http://localhost:8000/jsonapi/product?filter[%3E][product.type]=select'
    ```
=== "Javascript"
    ```javascript
    const args = {
        'filter': {
            '>': {'product.type': 'select'}
        }
    }
    let params = {}

    if(options.meta.prefix) { // returned from OPTIONS call
        params[options.meta.prefix] = args
    } else {
        params = args
    }

    const url = options.meta.resources['product']
        + (options.meta.resources['product'].includes('?') ? '&' : '?')
        + window.param(params) // from https://github.com/knowledgecode/jquery-param

    // returned from OPTIONS call
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
            '>': {'product.type': 'select'}
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
        url: options.meta.resources['product'], // returned from OPTIONS call
        data: params
    }).done( function( result ) {
        console.log( result.data );
    });
    ```

This is known as the ["Polish"](https://en.wikipedia.org/wiki/Polish_notation) notation because the operator comes first, then the two operands (key and value). There are several operators available:

**=~** (%3D%7E)
: Strings that start with the given value

**~=** (%7E%3D)
: Strings that contain the given value

**>** (%3E)
: Greater than for date, date&time, integer and float values

**>=** (%3E%3D)
: Greater than and equal for date, date&time, integer and float values

**<** (%3C)
: Smaller than for date, date&time, integer and float values

**<=** (%3C%3D)
: Smaller than and equal for date, date&time, integer and float values

**==** (%3D%3D)
: Equal for boolean, date, date&time, integer, float and string values

**!=** (%21%3D)
: Not equal for boolean, date, date&time, integer, float and string values

!!! warning
    Don't forget to [nest the parameters](index.md#nested-parameters) if a prefix is sent in the meta data!

To combine several conditions into one request, you can combine two or more "compare" expressions by using a "combine" expression:

=== "CURL"
    ```bash
    # filter[&&][][>][product.type]=select
    # &filter[&&][][=~][product.label]=demo
    curl -X GET 'http://localhost:8000/jsonapi/product?filter[%26%26][][%3E][product.type]=select&filter[%26%26][][%3D%7E][product.label]=demo'
    ```
=== "Javascript"
    ```javascript
    const args = {
        'filter': {
            '&&': [
                {'>': {'product.type': 'select'}},
                {'=~': {'product.label': 'demo'}}
            ]
        }
    }
    let params = {}

    if(options.meta.prefix) { // returned from OPTIONS call
        params[options.meta.prefix] = args
    } else {
        params = args
    }

    const url = options.meta.resources['product']
        + (options.meta.resources['product'].includes('?') ? '&' : '?')
        + window.param(params) // from https://github.com/knowledgecode/jquery-param

    // returned from OPTIONS call
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
                {'>': {'product.type': 'select'}},
                {'=~': {'product.label': 'demo'}}
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
        method: "GET",
        dataType: "json",
        url: options.meta.resources['product'], // returned from OPTIONS call
        data: params
    }).done( function( result ) {
        console.log( result.data );
    });
    ```

That would search for all product items which are selections AND whose labels starts with "demo". The available "combine" expressions are:

**&&** (%26%26)
: Combines expressions using an AND operator

**||** (%7C%7C)
: Combines expressions using an OR operator

**!** (%21)
: Negates an expression

The negation is a special case because it only accepts one "compare" condition while the others require more than one condition. Nevertheless the value of the negation operator must be an array like the other "combine" operators:

=== "CURL"
    ```bash
    # filter[!][][=~][product.code]=demo-s
    curl -X GET 'http://localhost:8000/jsonapi/product?filter[%21][][%3D%7E][product.code]=demo-s'
    ```
=== "Javascript"
    ```javascript
    const args = {
        'filter': {
            '!': [
                {'=~': {'product.code': 'demo-s'}}
            ]
        }
    }
    let params = {}

    if(options.meta.prefix) { // returned from OPTIONS call
        params[options.meta.prefix] = args
    } else {
        params = args
    }

    const url = options.meta.resources['product']
        + (options.meta.resources['product'].includes('?') ? '&' : '?')
        + window.param(params) // from https://github.com/knowledgecode/jquery-param

    // returned from OPTIONS call
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
            '!': [
                {'=~': {'product.code': 'demo-s'}}
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
        method: "GET",
        dataType: "json",
        url: options.meta.resources['product'], // returned from OPTIONS call
        data: params
    }).done( function( result ) {
        console.log( result.data );
    });
    ```

You can also create more complicated statements by nesting them like:

=== "CURL"
    ```bash
    # filter[&&][0][!][][=~][product.label]=demo
    # &filter[&&][1][||][][==][product.datestart]=
    # &filter[&&][1][||][][>][product.datestart]=2000-01-01 00:00:00
    curl -X GET 'http://localhost:8000/jsonapi/product?filter[%26%26][0][%21][][%3D%7E][product.label]=demo&filter[%26%26][1][%7C%7C][][%3D%3D][product.datestart]=&filter[%26%26][1][%7C%7C][][%3E][product.datestart]=2000-01-01%2000:00:00'
    ```
=== "Javascript"
    ```javascript
    const args = {
        'filter': {
            '&&': [
                {'!': [
                    {'=~': {'product.label': 'demo'}}
                ]},
                {'||': [
                    {'==': {'product.datestart': null}},
                    {'>': {'product.datestart': '2000-01-01 00:00:00'}}
                }
            ]
        }
    }
    let params = {}

    if(options.meta.prefix) { // returned from OPTIONS call
        params[options.meta.prefix] = args
    } else {
        params = args
    }

    const url = options.meta.resources['product']
        + (options.meta.resources['product'].includes('?') ? '&' : '?')
        + window.param(params) // from https://github.com/knowledgecode/jquery-param

    // returned from OPTIONS call
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
                {'!': [
                    {'=~': {'product.label': 'demo'}}
                ]},
                {'||': [
                    {'==': {'product.datestart': null}},
                    {'>': {'product.datestart': '2000-01-01 00:00:00'}}
                }
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
        method: "GET",
        dataType: "json",
        url: options.meta.resources['product'], // returned from OPTIONS call
        data: params
    }).done( function( result ) {
        console.log( result.data );
    });
    ```

It combines all three expressions by using the AND operator. In the first expression we tell the server that we want to get all items whose code doesn't start with "demo-s". The second expression in this case is an OR expression that specifies that "product.datestart" can either be a null value or the start date must be a date after the beginning of the year 2000.

!!! warning
    Don't forget to [nest the parameters](index.md#nested-parameters) if a prefix is sent in the meta data!

# Sorting the result set

Some resources, e.g. for products, offer specific sorting like "price", "name" or "relevance". Others, like those for services, use an implicit default sorting. Please have a look at the available sort criteria for the respective resources.

Additionally, you can use the sort parameter and the items keys for generic sorting. In the JSON API standard, the URL parameter "sort" is used to define the sorting of the result set:

=== "CURL"
    ```bash
    curl -X GET 'http://localhost:8000/jsonapi/product?sort=product.label'
    ```
=== "Javascript"
    ```javascript
    const args = {
        'sort': 'product.label'
    }
    let params = {}

    if(options.meta.prefix) { // returned from OPTIONS call
        params[options.meta.prefix] = args
    } else {
        params = args
    }

    const url = options.meta.resources['product']
        + (options.meta.resources['product'].includes('?') ? '&' : '?')
        + window.param(params) // from https://github.com/knowledgecode/jquery-param

    // returned from OPTIONS call
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
        'sort': 'product.label'
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
        url: options.meta.resources['product'], // returned from OPTIONS call
        data: params
    }).done( function( result ) {
        console.log( result.data );
    });
    ```

This will return the results ordered by the product label. You can also tell the server to sort the result set in the reverse order by adding a minus symbol in front of the sort key:

=== "CURL"
    ```bash
    curl -X GET 'http://localhost:8000/jsonapi/product?sort=-product.label'
    ```
=== "Javascript"
    ```javascript
    const args = {
        'sort': '-product.label'
    }
    let params = {}

    if(options.meta.prefix) { // returned from OPTIONS call
        params[options.meta.prefix] = args
    } else {
        params = args
    }

    const url = options.meta.resources['product']
        + (options.meta.resources['product'].includes('?') ? '&' : '?')
        + window.param(params) // from https://github.com/knowledgecode/jquery-param

    // returned from OPTIONS call
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
        'sort': '-product.label'
    };
    var params = {};

    if(options.meta.prefix) { // returned from OPTIONS call
        params[options.meta.prefix] = args;
    } else {
        params = args
    }

    $.ajax({
        method: "GET",
        dataType: "json",
        url: options.meta.resources['product'], // returned from OPTIONS call
        data: params
    }).done( function( result ) {
        console.log( result.data );
    });
    ```

Sorting by several keys is also possible if they are separated by a comma:

=== "CURL"
    ```bash
    curl -X GET 'http://localhost:8000/jsonapi/product?sort=-product.status,product.id'
    ```
=== "Javascript"
    ```javascript
    const args = {
        'sort': '-product.status,product.id'
    }
    let params = {}

    if(options.meta.prefix) { // returned from OPTIONS call
        params[options.meta.prefix] = args
    } else {
        params = args
    }

    const url = options.meta.resources['product']
        + (options.meta.resources['product'].includes('?') ? '&' : '?')
        + window.param(params) // from https://github.com/knowledgecode/jquery-param

    // returned from OPTIONS call
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
        'sort': '-product.status,product.id'
    };
    var params = {};

    if(options.meta.prefix) { // returned from OPTIONS call
        params[options.meta.prefix] = args;
    } else {
        params = args
    }

    $.ajax({
        method: "GET",
        dataType: "json",
        url: options.meta.resources['product'], // returned from OPTIONS call
        data: params
    }).done( function( result ) {
        console.log( result.data );
    });
    ```

Here the result set is sorted by the product status (descending) and the product ID.

!!! warning
    Don't forget to [nest the parameters](index.md#nested-parameters) if a prefix is sent in the meta data!

# Retrieve slices of the result

By default, only the first 25 items are returned if nothing else is specified. To get more or less items and step through the result set, the JSON API standard uses the "page" parameter:

=== "CURL"
    ```bash
    curl -X GET 'http://localhost:8000/jsonapi/product?page[offset]=0&page[limit]=2'
    ```
=== "Javascript"
    ```javascript
    const args = {
        'page': {
            'offset': 0,
            'limit': 2
        }
    }
    let params = {}

    if(options.meta.prefix) { // returned from OPTIONS call
        params[options.meta.prefix] = args
    } else {
        params = args
    }

    const url = options.meta.resources['product']
        + (options.meta.resources['product'].includes('?') ? '&' : '?')
        + window.param(params) // from https://github.com/knowledgecode/jquery-param

    // returned from OPTIONS call
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
        'page': {
            'offset': 0,
            'limit': 2
        }
    };
    var params = {};

    if(options.meta.prefix) { // returned from OPTIONS call
        params[options.meta.prefix] = args;
    } else {
        params = args
    }

    $.ajax({
        method: "GET",
        dataType: "json",
        url: options.meta.resources['product'], // returned from OPTIONS call
        data: params
    }).done( function( result ) {
        console.log( result.data );
    });
    ```

This will get only the first 2 items. If more items are available, the first response automatically contains links for navigating through the results:

```json
"links": {
    "first": "http://localhost:8000/jsonapi/product?page%5Boffset%5D=0&page%5Blimit%5D=2",
    "prev": "http://localhost:8000/jsonapi/product?page%5Boffset%5D=0&page%5Blimit%5D=2",
    "next": "http://localhost:8000/jsonapi/product?page%5Boffset%5D=4&page%5Blimit%5D=2",
    "last": "http://localhost:8000/jsonapi/product?page%5Boffset%5D=4&page%5Blimit%5D=2",
    "self": "http://localhost:8000/jsonapi/product?page%5Boffset%5D=2&page%5Blimit%5D=2"
}
```

To get the next 2 items starting from the 3rd one use the *next* link from the above response:

=== "CURL"
    ```bash
    # URL from "links" -> "next" of the response above
    curl -X GET 'http://localhost:8000/jsonapi/product?page[offset]=2&page[limit]=2'
    ```
=== "Javascript"
    ```javascript
    // returned from previous request
    fetch(response.links.next).then(result => {
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
        url: response.links.next, // returned from previous request
        data: params
    }).done( function( result ) {
        console.log( result.data );
    });
    ```

!!! note
    Please note that the *last* link's offset ("4" in the given example) depends on the number of products available.

!!! warning
    Don't forget to [nest the parameters](index.md#nested-parameters) if a prefix is sent in the meta data!

# Return specific fields only

If you only need the values of a few fields and want to reduce the amount of data transferred over the network, you can specify the fields that should be returned without the rest of the available ones. In the JSON API standard the parameter "fields" is used for this:

=== "CURL"
    ```bash
    # product => product.id,product.label
    # product.property => product.property.type,product.property.value
    # stock => stock.stocklevel
    curl -X GET 'http://localhost:8000/jsonapi/product?fields[product]=product.id,product.label&fields[product.property]=product.property.type,product.property.value&fields[stock]=stock.stocklevel&include=stock,product.property'
    ```
=== "Javascript"
    ```javascript
    const args = {
        'fields': {
            'product': 'product.id,product.label'
            'product.property': 'product.property.type,product.property.value'
            'stock': 'stock.stocklevel'
        }
    }
    let params = {}

    if(options.meta.prefix) { // returned from OPTIONS call
        params[options.meta.prefix] = args
    } else {
        params = args
    }

    const url = options.meta.resources['product']
        + (options.meta.resources['product'].includes('?') ? '&' : '?')
        + window.param(params) // from https://github.com/knowledgecode/jquery-param

    // returned from OPTIONS call
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
        'fields': {
            'product': 'product.id,product.label'
            'product.property': 'product.property.type,product.property.value'
            'stock': 'stock.stocklevel'
        }
    };
    var params = {};

    if(options.meta.prefix) { // returned from OPTIONS call
        params[options.meta.prefix] = args;
    } else {
        params = args
    }

    $.ajax({
        method: "GET",
        dataType: "json",
        url: options.meta.resources['product'], // returned from OPTIONS call
        data: params
    }).done( function( result ) {
        console.log( result.data );
    });
    ```

The generated request will then only return the ID and label of product items.

!!! warning
    Don't forget to [nest the parameters](index.md#nested-parameters) if a prefix is sent in the meta data!

# Include related resources

## Foreign domains

To minimize the number of requests, the Aimeos JSON API can add related resources to the response. For example, you can tell the server that it should not only return the list of products but also the texts associated with these products. The JSON API uses the parameter "include" to specify the related resources:

=== "CURL"
    ```bash
    curl -X GET 'http://localhost:8000/jsonapi/product?include=product.text'
    ```
=== "Javascript"
    ```javascript
    const args = {
        'include': 'product.text'
    }
    let params = {}

    if(options.meta.prefix) { // returned from OPTIONS call
        params[options.meta.prefix] = args
    } else {
        params = args
    }

    const url = options.meta.resources['product']
        + (options.meta.resources['product'].includes('?') ? '&' : '?')
        + window.param(params) // from https://github.com/knowledgecode/jquery-param

    // returned from OPTIONS call
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
        'include': 'product.text'
    };
    var params = {};

    if(options.meta.prefix) { // returned from OPTIONS call
        params[options.meta.prefix] = args;
    } else {
        params = args
    }

    $.ajax({
        method: "GET",
        dataType: "json",
        url: options.meta.resources['product'], // returned from OPTIONS call
        data: params
    }).done( function( result ) {
        console.log( result.data );
    });
    ```

This returns the product or products as well as the texts associated with the products within the same request:

```json
{
    "data": [{
        "id": "1",
        "type": "product",
        "attributes": {
            "product.id": "1",
            "product.type": "default",
            "product.code": "demo-article",
            "product.label": "Demo article",
            "product.status": 1,
            "product.dataset": "",
            "product.datestart": null,
            "product.dateend": null,
            "product.config": [],
            "product.target": "",
            "product.ctime": "2020-07-28 08:41:18"
        },
        "relationships": {
            "text": {
                "data": [{
                    "id": "22",
                    "type": "text",
                    "attributes": {
                        "product.lists.id": "16",
                        "product.lists.domain": "text",
                        "product.lists.refid": "22",
                        "product.lists.datestart": null,
                        "product.lists.dateend": null,
                        "product.lists.config": [],
                        "product.lists.position": 3,
                        "product.lists.status": 1,
                        "product.lists.type": "default"
                    }
                },{
                    "id": "23",
                    "type": "text",
                    "attributes": {
                        "product.lists.id": "17",
                        "product.lists.domain": "text",
                        "product.lists.refid": "23",
                        "product.lists.datestart": null,
                        "product.lists.dateend": null,
                        "product.lists.config": [],
                        "product.lists.position": 4,
                        "product.lists.status": 1,
                        "product.lists.type": "default"
                    }
                },{
                    "id": "24",
                    "type": "text",
                    "attributes": {
                        "product.lists.id": "18",
                        "product.lists.domain": "text",
                        "product.lists.refid": "24",
                        "product.lists.datestart": null,
                        "product.lists.dateend": null,
                        "product.lists.config": [],
                        "product.lists.position": 5,
                        "product.lists.status": 1,
                        "product.lists.type": "default"
                    }
                }]
            }
        }
    }],
    "included": [{
        "id": "22",
        "type": "text",
        "attributes": {
            "text.id": "22",
            "text.languageid": "en",
            "text.type": "name",
            "text.label": "Demo name\/en: Demo article",
            "text.domain": "product",
            "text.content": "Demo article",
            "text.status": 1
        }
    },{
        "id": "23",
        "type": "text",
        "attributes": {
            "text.id": "23",
            "text.languageid": "en",
            "text.type": "short",
            "text.label": "Demo short\/en: This is the short description",
            "text.domain": "product",
            "text.content": "This is the short description of the demo article.",
            "text.status": 1
        }
    },{
        "id": "24",
        "type": "text",
        "attributes": {
            "text.id": "24",
            "text.languageid": "en",
            "text.type": "long",
            "text.label": "Demo long\/en: Add a detailed description",
            "text.domain": "product",
            "text.content": "Add a detailed description of the demo article that may be a little bit longer.",
            "text.status": 1
        }
    }]
}
```

You can use the "include" parameter for all domain items that are associated, via the lists, with one of these items:

* catalog (categories)
* product
* service
* attribute
* media
* price
* text

!!! note
    You can use `include=product.text` and `include=text` as parameter. The difference is that `include=product.text` will only fetch product texts while e.g. `include=attribute,text` will fetch all products, the related product texts and attributes as well as the attribute texts. To reduce the size of the response, you should prefer `product.text` over `text`. This applies to all related domain items which can be included.

## Child resources

This does also work for items from the same domain that have a parent/child relationship like product properties:

=== "CURL"
    ```bash
    curl -X GET 'http://localhost:8000/jsonapi/product?include=product.property'
    ```
=== "Javascript"
    ```javascript
    const args = {
        'include': 'product.property'
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
        'include': 'product.property'
    };
    var params = {};

    if(options.meta.prefix) { // returned from OPTIONS call
        params[options.meta.prefix] = args;
    } else {
        params = args
    }

    $.ajax({
        method: "GET",
        dataType: "json",
        url: options.meta.resources['product'], // returned from OPTIONS call
        data: params
    }).done( function( result ) {
        console.log( result.data );
    });
    ```

Then, the properties directly attached to the products will be returned:

```json
{
    "data": [{
        "id": "1",
        "type": "product",
        "attributes": {
            "product.id": "1",
            "product.type": "default",
            "product.code": "demo-article",
            "product.label": "Demo article",
            "product.status": 1,
            "product.dataset": "",
            "product.datestart": null,
            "product.dateend": null,
            "product.config": [],
            "product.target": "",
            "product.ctime": "2020-07-28 08:41:18"
        },
        "relationships": {
            "product.property": {
                "data": [{
                    "id": "1",
                    "type": "product.property"
                },{
                    "id": "2",
                    "type": "product.property"
                },{
                    "id": "3",
                    "type": "product.property"
                },{
                    "id": "4",
                    "type": "product.property"
                }]
            }
        }
    }],
    "included": [{
        "id": "1",
        "type": "product.property",
        "attributes": {
            "product.property.id": "1",
            "product.property.languageid": null,
            "product.property.value": "20.00",
            "product.property.type": "package-length"
        }
    },{
        "id": "2",
        "type": "product.property",
        "attributes": {
            "product.property.id": "2",
            "product.property.languageid": null,
            "product.property.value": "10.00",
            "product.property.type": "package-width"
        }
    },{
        "id": "3",
        "type": "product.property",
        "attributes": {
            "product.property.id": "3",
            "product.property.languageid": null,
            "product.property.value": "5.00",
            "product.property.type": "package-height"
        }
    },{
        "id": "4",
        "type": "product.property",
        "attributes": {
            "product.property.id": "4",
            "product.property.languageid": null,
            "product.property.value": "2.5",
            "product.property.type": "package-weight"
        }
    }]
}
```

!!! warning
    Don't forget to [nest the parameters](index.md#nested-parameters) if a prefix is sent in the meta data!

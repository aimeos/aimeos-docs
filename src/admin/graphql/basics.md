This article describes how to retrieve and modify data using the Aimeos GraphQL API.

!!! note
    You must be logged into the admin backend to use the GraphQL API!

# Retrieve data

GraphQL uses **query** POST requests to retrieve data from the server. There are several query methods offered by Aimeos to fetch data from different domains, e.g. for the "product" domain:

* getProduct
* findProduct
* searchProducts

Each of these methods requires different parameters:

=== "getProduct"
    ```graphql
    query {
      getProduct(id: "1") {
        id
        type
        code
        label
      }
    }
    ```
=== "findProduct"
    ```graphql
    query {
      findProduct(code: "demo-article") {
        id
        type
        code
        label
      }
    }
    ```
=== "searchProducts"
    ```graphql
    query {
      searchProducts(filter: "{}") {
        id
        type
        code
        label
      }
    }
    ```

!!! note
    The **find*()** methods are not available for all domains, only for those whose items have an unique code and whose managers implement the *find()* method!

## Example code

To retrieve a list of products using code like this:

```javascript
const body = JSON.stringify({'query':
`query {
  searchProducts(filter: "{}") {
    id
    type
    code
    label
  }
}`});

fetch($('.aimeos').data('graphql'), {
	method: 'POST',
	credentials: 'same-origin',
	headers: { // Laravel only
		'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
	},
	body: body
}).then(response => {
	return response.json();
}).then(data => {
	console.log(data);
});
```

The response is a JSON data structure with the requested data:

```json
{
  "data": {
    "searchProducts": [
      {
        "id": "1",
        "type": "default",
        "code": "demo-article",
        "label": "Demo article",
      },
      {
        "id": "2",
        "type": "default",
        "code": "demo-selection-article-1",
        "label": "Demo variant article 1",
      }
    ]
  }
}
```

Please check the articles for the different data domains for more details about the available requests and responses.

## Batched queries

You can use several queries on one request to reduce the number of requests:

```graphql
query {
  findCustomer(code: "demo@example.com") {
    id
    type
    code
    label
  }
  searchProducts(filter: "{}") {
    id
    type
    code
    label
  }
}
```

The result is a batched query with a response like this one:

```json
{
  "data": {
    "findCustomer": {
      "id": "2",
      "code": "demo@example.com",
      "label": "Test User (Test company)"
    },
    "searchProducts": [
      {
        "id": "1",
        "type": "default",
        "code": "demo-article",
        "label": "Demo article"
      },
      {
        "id": "2",
        "type": "default",
        "code": "demo-selection-article-1",
        "label": "Demo variant article 1"
      }
    ]
  }
}
```

# Modify data

Similar to query requests, GraphQL uses **mutation** POST requests to add, update and delete data at the server. The mutation methods offered by Aimeos are e.g. for the product domain:

* saveProduct
* saveProducts
* deleteProduct
* deleteProducts

Each of these methods requires different parameter types (single vs. multiple entries):

=== "saveProduct"
    ```graphql
    mutation {
      saveProduct(input: {
        code: "test"
        label: "Test product"
      }) {
        id
      }
    }
    ```
=== "saveProducts"
    ```graphql
    mutation {
      saveProducts(input: [{
        code: "test-2"
        label: "Test 2 product"
      },{
        code: "test-3"
        label: "Test 3 product"
      }]) {
        id
      }
    }
    ```
=== "deleteProduct"
    ```graphql
    mutation {
      deleteProduct(id: "1")
    }
    ```
=== "deleteProducts"
    ```graphql
    mutation {
      deleteProducts(id: ["1", "2"])
    }
    ```

## Example code

To add a new product you can use code like this:

```javascript
const body = JSON.stringify({'query':
`mutation {
  saveProduct(input: {
    code: "test"
    label: "Test product"
  }) {
    id
  }
}`});

fetch($('.aimeos').data('graphql'), {
	method: 'POST',
	credentials: 'same-origin',
	headers: { // Laravel only
		'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
	},
	body: body
}).then(response => {
	return response.json();
}).then(data => {
	console.log(data);
});
```

The response is a JSON data structure with the requested data:

```json
{
  "data": {
    "saveProduct": {
      "id": "20"
    }
  }
}
```

Please check the articles for the different data domains for more details about the available requests and responses.

## Batched mutations

You can use several mutations on one request to reduce the number of requests:

```graphql
mutation {
  saveProduct(input: {
    code: "test"
    label: "Test product"
  }) {
    id
  }
  deleteProduct(id: "1")
}
```

The result is a batched query with a response like this one:

```json
{
  "data": {
    "saveProduct": {
      "id": "134"
    },
    "deleteProduct": "1"
  }
}
```

# Filtering the result

All **search*()** methods support a *filter* parameter to retrieve only those items you need. The filter value is a JSON encoded string that contains arbitrary filter conditions with compare and combine expressions. The JSON encoded string instead of an object is necessary because the GraphQL specs doesn't allow objects with arbitrary key/value pairs due to the strict typing system of GraphQL.

Contrary to the field names in query and mutation requests, the filter keys must contain the domain using the dot notation, e.g. to filter for the product "code" field, you have to use "product.code" as filter key. Similarly, for sub-domains like product properties it's "product.property.type".

To get all product items which are selections for example, you can use this query:

=== "GraphQL"
    ```graphql
    query {
      searchProducts(filter: "{\"==\":{\"product.type\":\"select\"}}") {
        id
        type
        code
        label
      }
    }
    ```
=== "Javascript"
    ```javascript
    const filter = {
        '==': {'product.type': 'select'}
    };
    const body = JSON.stringify({'query':
    `query {
      searchProducts(filter: "` + JSON.stringify(filter).replace(/"/g, '\\"') + `") {
        id
        type
        code
        label
      }
    }`});

    fetch($('.aimeos').data('graphql'), {
        method: 'POST',
        credentials: 'same-origin',
        headers: { // Laravel only
            'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
        },
        body: body
    }).then(response => {
        return response.json();
    }).then(data => {
        console.log(data);
    });
    ```

This is known as the ["Polish"](https://en.wikipedia.org/wiki/Polish_notation) notation because the operator comes first, then the two operands (key and value). There are several operators available:

**=~**
: Strings that start with the given value

**~=**
: Strings that contain the given value

**>**
: Greater than for date, date&time, integer and float values

**>=**
: Greater than and equal for date, date&time, integer and float values

**<**
: Smaller than for date, date&time, integer and float values

**<=**
: Smaller than and equal for date, date&time, integer and float values

**==**
: Equal for boolean, date, date&time, integer, float and string values

**!=**
: Not equal for boolean, date, date&time, integer, float and string values

To combine several conditions, you can combine two or more "compare" expressions by using a "combine" expression:

=== "GraphQL"
    ```graphql
    query {
      searchProducts(filter: "{\"&&\":[{\"==\":{\"product.type\":\"select\"}},{\"=~\":{\"product.label\":\"demo\"}}]}") {
        id
        type
        code
        label
      }
    }
    ```
=== "Javascript"
    ```javascript
    const filter = {
        '&&': [
            {'==': {'product.type': 'select'}},
            {'=~': {'product.label': 'demo'}}
        ]
    };
    const body = JSON.stringify({'query':
    `query {
      searchProducts(filter: "` + JSON.stringify(filter).replace(/"/g, '\\"') + `") {
        id
        type
        code
        label
      }
    }`});

    fetch($('.aimeos').data('graphql'), {
        method: 'POST',
        credentials: 'same-origin',
        headers: { // Laravel only
            'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
        },
        body: body
    }).then(response => {
        return response.json();
    }).then(data => {
        console.log(data);
    });
    ```

That would search for all product items which are selections AND whose labels starts with "demo". The available "combine" expressions are:

**&&**
: Combines expressions using an AND operator

**||**
: Combines expressions using an OR operator

**!**
: Negates an expression

The negation is a special case because it only accepts one "compare" condition while the others require more than one condition. Nevertheless the value of the negation operator must be an array like the other "combine" operators:

=== "GraphQL"
    ```graphql
    query {
      searchProducts(filter: "{\"!\":[{\"=~\":{\"product.code\":\"demo-s\"}}]}") {
        id
        type
        code
        label
      }
    }
    ```
=== "Javascript"
    ```javascript
    const filter = {
        '!': [
            {'=~': {'product.code': 'demo-s'}}
        ]
    };
    const body = JSON.stringify({'query':
    `query {
      searchProducts(filter: "` + JSON.stringify(filter).replace(/"/g, '\\"') + `") {
        id
        type
        code
        label
      }
    }`});

    fetch($('.aimeos').data('graphql'), {
        method: 'POST',
        credentials: 'same-origin',
        headers: { // Laravel only
            'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
        },
        body: body
    }).then(response => {
        return response.json();
    }).then(data => {
        console.log(data);
    });
    ```

You can also create more complicated statements by nesting them like:

=== "GraphQL"
    ```graphql
    query {
      # filter[&&][0][!][][=~][product.label]=demo
      # &filter[&&][1][||][][==][product.datestart]=
      # &filter[&&][1][||][][>][product.datestart]=2000-01-01 00:00:00

      searchProducts(filter: "{\"&&\":[{\"!\":[{\"=~\":{\"product.code\":\"demo-s\"}}]},{\"||\": [{\"==\": {\"product.datestart\": null}},{\">\": {\"product.datestart\": \"2000-01-01 00:00:00\"}}]}]}") {
        id
        type
        code
        label
      }
    }
    ```
=== "Javascript"
    ```javascript
    const filter = {
        '&&': [
            {
                '!': [
                    {'=~': {'product.label': 'demo'}}
                ]
            },
            {
                '||': [
                    {'==': {'product.datestart': null}},
                    {'>': {'product.datestart': '2000-01-01 00:00:00'}},
                ]
            }
        ]
    };
    const body = JSON.stringify({'query':
    `query {
      searchProducts(filter: "` + JSON.stringify(filter).replace(/"/g, '\\"') + `") {
        id
        type
        code
        label
      }
    }`});

    fetch($('.aimeos').data('graphql'), {
        method: 'POST',
        credentials: 'same-origin',
        headers: { // Laravel only
            'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
        },
        body: body
    }).then(response => {
        return response.json();
    }).then(data => {
        console.log(data);
    });
    ```

It combines all three expressions by using the AND operator. In the first expression we tell the server that we want to get all items whose code doesn't start with "demo-s". The second expression in this case is an OR expression that specifies that "product.datestart" can either be a null value or the start date must be a date after the beginning of the year 2000.

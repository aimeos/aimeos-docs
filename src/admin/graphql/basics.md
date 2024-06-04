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
        items {
          id
          type
          code
          label
        }
        total
      }
    }
    ```

!!! note
    The **find*()** methods are not available for all domains, only for those whose items have an unique code and whose managers implement the *find()* method!

## Example code

To retrieve a list of products using code like this:

=== "JQAdm"
    ```javascript
    Aimeos.query(`query {
      searchProducts(filter: "{}") {
        items {
          id
          type
          code
          label
        }
        total
      }
    }`).then(data => {
      console.log(data)
    })
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `query {
      searchProducts(filter: "{}") {
        items {
          id
          type
          code
          label
        }
        total
      }
    }`});

    fetch('<GraphQL URL>', {
      method: 'POST',
      credentials: 'same-origin',
      headers: { // Laravel only
        'X-CSRF-TOKEN': '<CSRF token>'
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
    "searchProducts": {
      "items": [
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
    },
    "total": 2
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
    items {
      id
      type
      code
      label
    }
    total
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
    "searchProducts": {
      "items": [
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
      ],
      "total": 2
    }
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

=== "JQAdm"
    ```javascript
    Aimeos.query(`mutation {
      saveProduct(input: {
        code: "test"
        label: "Test product"
      }) {
        id
      }
    }`).then(data => {
      console.log(data)
    })
    ```
=== "Javascript"
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

    fetch('<GraphQL URL>', {
      method: 'POST',
      credentials: 'same-origin',
      headers: { // Laravel only
        'X-CSRF-TOKEN': '<CSRF token>'
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
      searchProducts(filter: "{\\"==\\":{\\"product.type\\":\\"select\\"}}") {
        items {
          id
          type
          code
          label
        }
        total
      }
    }
    ```
=== "JQAdm"
    ```javascript
    const filter = {
        '==': {'product.type': 'select'}
    };
    Aimeos.query(`query {
      searchProducts(filter: ` + JSON.stringify(JSON.stringify(filter)) + `) {
        items {
          id
          type
          code
          label
        }
        total
      }
    }`).then(data => {
      console.log(data)
    })
    ```
=== "Javascript"
    ```javascript
    const filter = {
        '==': {'product.type': 'select'}
    };
    const body = JSON.stringify({'query':
    `query {
      searchProducts(filter: ` + JSON.stringify(JSON.stringify(filter)) + `) {
        items {
          id
          type
          code
          label
        }
        total
      }
    }`});

    fetch('<GraphQL URL>', {
        method: 'POST',
        credentials: 'same-origin',
        headers: { // Laravel only
            'X-CSRF-TOKEN': '<CSRF token>'
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
      searchProducts(filter: "{\\"&&\\":[{\\"==\\":{\\"product.type\\":\\"select\\"}},{\\"=~\\":{\\"product.label\\":\\"demo\\"}}]}") {
        items {
          id
          type
          code
          label
        }
        total
      }
    }
    ```
=== "JQAdm"
    ```javascript
    const filter = {
        '&&': [
            {'==': {'product.type': 'select'}},
            {'=~': {'product.label': 'demo'}}
        ]
    };
    Aimeos.query(`query {
      searchProducts(filter: ` + JSON.stringify(JSON.stringify(filter)) + `) {
        items {
          id
          type
          code
          label
        }
        total
      }
    }`).then(data => {
      console.log(data)
    })
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
      searchProducts(filter: ` + JSON.stringify(JSON.stringify(filter)) + `) {
        items {
          id
          type
          code
          label
        }
        total
      }
    }`});

    fetch('<GraphQL URL>', {
        method: 'POST',
        credentials: 'same-origin',
        headers: { // Laravel only
            'X-CSRF-TOKEN': '<CSRF token>'
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
      searchProducts(filter: "{\\"!\\":[{\\"=~\\":{\\"product.code\\":\\"demo-s\\"}}]}") {
        items {
          id
          type
          code
          label
        }
        total
      }
    }
    ```
=== "JQAdm"
    ```javascript
    const filter = {
        '!': [
            {'=~': {'product.code': 'demo-s'}}
        ]
    };
    Aimeos.query(`query {
      searchProducts(filter: ` + JSON.stringify(JSON.stringify(filter)) + `) {
        items {
          id
          type
          code
          label
        }
        total
      }
    }`).then(data => {
      console.log(data)
    })
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
      searchProducts(filter: ` + JSON.stringify(JSON.stringify(filter)) + `) {
        items {
          id
          type
          code
          label
        }
        total
      }
    }`});

    fetch('<GraphQL URL>', {
        method: 'POST',
        credentials: 'same-origin',
        headers: { // Laravel only
            'X-CSRF-TOKEN': '<CSRF token>'
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
      # [&&][0][!][][=~][product.label]=demo
      # [&&][1][||][][==][product.datestart]=
      # [&&][1][||][][>][product.datestart]=2000-01-01 00:00:00

      searchProducts(filter: "{\\"&&\\":[{\\"!\\":[{\\"=~\\":{\\"product.code\\":\\"demo-s\\"}}]},{\\"||\\": [{\\"==\\": {\\"product.datestart\\": null}},{\\">\\": {\\"product.datestart\\": \\"2000-01-01 00:00:00\\"}}]}]}") {
        items {
          id
          type
          code
          label
        }
        total
      }
    }
    ```
=== "JQAdm"
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
    Aimeos.query(`query {
      searchProducts(filter: ` + JSON.stringify(JSON.stringify(filter)) + `) {
        items {
          id
          type
          code
          label
        }
        total
      }
    }`).then(data => {
      console.log(data)
    })
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
      searchProducts(filter: ` + JSON.stringify(JSON.stringify(filter)) + `) {
        items {
          id
          type
          code
          label
        }
        total
      }
    }`});

    fetch('<GraphQL URL>', {
        method: 'POST',
        credentials: 'same-origin',
        headers: { // Laravel only
            'X-CSRF-TOKEN': '<CSRF token>'
        },
        body: body
    }).then(response => {
        return response.json();
    }).then(data => {
        console.log(data);
    });
    ```

It combines all three expressions by using the AND operator. In the first expression we tell the server that we want to get all items whose code doesn't start with "demo-s". The second expression in this case is an OR expression that specifies that "product.datestart" can either be a null value or the start date must be a date after the beginning of the year 2000.

# Sorting the result set

You can use the **sort** parameter for all **search*()** query requests to pass the list of items keys to sort by, e.g.:

=== "CURL"
    ```graphql
    query {
      searchProducts(filter: "{}", sort: ["product.label"]) {
        items {
          id
          type
          code
          label
        }
        total
      }
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`query {
      searchProducts(filter: "{}", sort: ["product.label"]) {
        items {
          id
          type
          code
          label
        }
        total
      }
    }`).then(data => {
      console.log(data)
    })
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `query {
      searchProducts(filter: "{}", sort: ["product.label"]) {
        items {
          id
          type
          code
          label
        }
        total
      }
    }`});

    fetch('<GraphQL URL>', {
        method: 'POST',
        credentials: 'same-origin',
        headers: { // Laravel only
            'X-CSRF-TOKEN': '<CSRF token>'
        },
        body: body
    }).then(response => {
        return response.json();
    }).then(data => {
        console.log(data);
    });
    ```

This will return the results ordered by the product label. You can also tell the server to sort the result set in the reverse order by adding a minus symbol in front of the sort key:

=== "CURL"
    ```graphql
    query {
      searchProducts(filter: "{}", sort: ["-product.label"]) {
        items {
          id
          type
          code
          label
        }
        total
      }
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`query {
      searchProducts(filter: "{}", sort: ["-product.label"]) {
        items {
          id
          type
          code
          label
        }
        total
      }
    }`).then(data => {
      console.log(data)
    })
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `query {
      searchProducts(filter: "{}", sort: ["-product.label"]) {
        items {
          id
          type
          code
          label
        }
        total
      }
    }`});

    fetch('<GraphQL URL>', {
        method: 'POST',
        credentials: 'same-origin',
        headers: { // Laravel only
            'X-CSRF-TOKEN': '<CSRF token>'
        },
        body: body
    }).then(response => {
        return response.json();
    }).then(data => {
        console.log(data);
    });
    ```

Sorting by several keys is also possible if they are separated by a comma:

=== "CURL"
    ```graphql
    query {
      searchProducts(filter: "{}", sort: ["-product.status", "product.id"]) {
        items {
          id
          type
          code
          label
        }
        total
      }
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`query {
      searchProducts(filter: "{}", sort: ["-product.status", "product.id"]) {
        items {
          id
          type
          code
          label
        }
        total
      }
    }`).then(data => {
      console.log(data)
    })
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `query {
      searchProducts(filter: "{}", sort: ["-product.status", "product.id"]) {
        items {
          id
          type
          code
          label
        }
        total
      }
    }`});

    fetch('<GraphQL URL>', {
        method: 'POST',
        credentials: 'same-origin',
        headers: { // Laravel only
            'X-CSRF-TOKEN': '<CSRF token>'
        },
        body: body
    }).then(response => {
        return response.json();
    }).then(data => {
        console.log(data);
    });
    ```

Here the result set is sorted by the product status (descending) and the product ID.

# Retrieve slices of the result

By default, only the first 100 items are returned if nothing else is specified. To get more or less items and step through the result set, the Aimeos GraphQL API uses the **offset** and **limit** parameter:

=== "CURL"
    ```graphql
    query {
      searchProducts(filter: "{}", offset: 10, limit: 5) {
        items {
          id
          type
          code
          label
        }
        total
      }
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`query {
      searchProducts(filter: "{}", offset: 10, limit: 5) {
        items {
          id
          type
          code
          label
        }
        total
      }
    }`).then(data => {
      console.log(data)
    })
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `query {
      searchProducts(filter: "{}", offset: 10, limit: 5) {
        items {
          id
          type
          code
          label
        }
        total
      }
    }`});

    fetch('<GraphQL URL>', {
        method: 'POST',
        credentials: 'same-origin',
        headers: { // Laravel only
            'X-CSRF-TOKEN': '<CSRF token>'
        },
        body: body
    }).then(response => {
        return response.json();
    }).then(data => {
        console.log(data);
    });
    ```

This will retrieve only 5 items starting from offset 10.

# Include related resources

To minimize the number of requests, the Aimeos GraphQL API can add related resources to the response.

## Foreign domains

You can tell the server that it should not only return the list of products but also the attributes associated with these products. It's is available for these types of queries:

getX()
: e.g. *getProduct()*, *getAttribute()*, etc.

findX()
: e.g. *findProduct()*, *findAttribute()*, etc.

searchX()
: e.g. *searchProducts()*, *searchAttributes()*, etc.

The GraphQL API uses the parameter "include" to specify the related resources:

=== "GraphQL"
    ```graphql
    query {
      searchProducts(filter: "{}", include: ["product/text"]) {
        items {
          id
          type
          code
          label
          lists {
            text(listtype: "default", type: "name") {
              id
              siteid
              parentid
              refid
              domain
              type
              config
              datestart
              dateend
              status
              ctime
              mtime
              editor
              item {
                type
                domain
                label
              }
            }
          }
        }
        total
      }
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`query {
      searchProducts(filter: "{}", include: ["product/text"]) {
        items {
          id
          type
          code
          label
          lists {
            text(listtype: "default", type: "name") {
              id
              siteid
              parentid
              refid
              domain
              type
              config
              datestart
              dateend
              status
              ctime
              mtime
              editor
              item {
                type
                domain
                label
              }
            }
          }
        }
        total
      }
    }`).then(data => {
      console.log(data)
    })
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `query {
      searchProducts(filter: "{}", include: ["product/text"]) {
        items {
          id
          type
          code
          label
          lists {
            text(listtype: "default", type: "name") {
              id
              siteid
              parentid
              refid
              domain
              type
              config
              datestart
              dateend
              status
              ctime
              mtime
              editor
              item {
                type
                domain
                label
              }
            }
          }
        }
        total
      }
    }`});

    fetch('<GraphQL URL>', {
        method: 'POST',
        credentials: 'same-origin',
        headers: { // Laravel only
            'X-CSRF-TOKEN': '<CSRF token>'
        },
        body: body
    }).then(response => {
        return response.json();
    }).then(data => {
        console.log(data);
    });
    ```

This returns the product or products as well as the attributes associated with the products within the same request:

```json
{
  "data": {
    "searchProducts": {
      "items": [
        {
          "id": "118",
          "type": "select",
          "code": "demo-selection-article",
          "label": "Demo selection article",
          "lists": {
            "text": [
              {
                "id": "1442",
                "siteid": "1.",
                "parentid": 118,
                "refid": "1689",
                "domain": "text",
                "type": "default",
                "config": "{}",
                "datestart": null,
                "dateend": null,
                "status": 1,
                "ctime": "2022-12-01 11:59:05",
                "mtime": "2022-12-01 11:59:05",
                "editor": "core",
                "item": {
                  "type": "name",
                  "domain": "product",
                  "label": "Demo name/de: Demoartikel mit Auswahl"
                }
              },
              {
                "id": "1446",
                "siteid": "1.",
                "parentid": 118,
                "refid": "1693",
                "domain": "text",
                "type": "default",
                "config": "{}",
                "datestart": null,
                "dateend": null,
                "status": 1,
                "ctime": "2022-12-01 11:59:05",
                "mtime": "2022-12-01 11:59:05",
                "editor": "core",
                "item": {
                  "type": "name",
                  "domain": "product",
                  "label": "Demo name/en: Demo selection article"
                }
              }
            ]
          }
        }
      ],
      "total": 1
    }
  }
}
```

You can use the "include" parameter for all domain items that are associated, via the lists, with one of these items:

* attribute
* catalog (categories)
* customer
* media (images and files)
* price
* product
* service (delivery/payment)
* supplier
* text
* cms (only if ai-cms-grapesjs is installed)

!!! note
    You can use e.g. `["product/text"]` or `["text"]` as parameter. The difference is that `["product/text"]` will only fetch product texts while `["attribute","text"]` will fetch all products, the related product texts and attributes as well as the attribute texts. To reduce the response times, you should prefer `["product/text"]` over `["text"]`. This applies to all related domain items which can be included.

The `lists` key in the request must contain the domain name you want to retrieve (it's always e.g. `text`, not the more limiting `product/text`) and can contain two optional parameters:

**listype**
: Type of the relation itself which can be used as a sub-type, e.g. `variant` is a list type for fetching only variant attributes instead of all.

**type**
: Type of the domain item if it contains one to distinguish different types (like *name*, *short* or *long* text types)

All keys below the domain will fetch the list item properties which are:

* id
* siteid
* parentid
* refid
* domain
* type
* config
* datestart
* dateend
* status
* ctime
* mtime
* editor

The `item` key contains the fields of the domain item itself. In the example there are *type*, *domain* and *label* specified. Please have a look at the articles for the domains to see what fields are available.

## Child resources

Fetching related items does also work for items from the same domain that have a parent/child relationship like product properties:

=== "GraphQL"
    ```graphql
    query {
      searchProducts(filter: "{}", include: ["product/property"]) {
        items {
          id
          label
          property(type: "package-weight") {
              id
              siteid
              parentid
              type
              languageid
              value
              ctime
              mtime
              editor
          }
        }
        total
      }
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`query {
      searchProducts(filter: "{}", include: ["product/property"]) {
        items {
          id
          label
          property(type: "package-weight") {
              id
              siteid
              parentid
              type
              languageid
              value
              ctime
              mtime
              editor
          }
        }
        total
      }
    }`).then(data => {
      console.log(data)
    })
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `query {
    query {
      searchProducts(filter: "{}", include: ["product/property"]) {
        items {
          id
          label
          property(type: "package-weight") {
              id
              siteid
              parentid
              type
              languageid
              value
              ctime
              mtime
              editor
          }
        }
        total
      }
    }`});

    fetch('<GraphQL URL>', {
        method: 'POST',
        credentials: 'same-origin',
        headers: { // Laravel only
            'X-CSRF-TOKEN': '<CSRF token>'
        },
        body: body
    }).then(response => {
        return response.json();
    }).then(data => {
        console.log(data);
    });
    ```

Then, the properties directly attached to the products will be returned:

```json
{
  "data": {
    "searchProducts": {
      "items": [
        {
          "id": "113",
          "label": "Demo article",
          "property": [
            {
              "id": "40",
              "siteid": "1.",
              "parentid": 113,
              "type": "package-weight",
              "languageid": null,
              "value": "2.5",
              "ctime": "2022-12-01 11:59:05",
              "mtime": "2022-12-01 11:59:05",
              "editor": "core"
            }
          ]
        }
      ],
      "total": 1
    }
  }
}
```

!!! note
    The name must be always e.g. `["product/property"]` not `["property"]` as parameter!

The `property` key can contain an optional parameter:

**type**
: Type of the property item to filter for

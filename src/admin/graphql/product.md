This article contains all actions for retrieving and managing products.

!!! tip
    The product domain supports [fetching related resources](basics.md#include-related-resources).

# Get product by ID

=== "Query"
    ```graphql
    query {
      getProduct(id: "1", include: ["text", "product/property", "stock"]) {
        id
        siteid
        type
        code
        label
        url
        dataset
        datestart
        dateend
        config
        instock
        scale
        status
        target
        boost
        mtime
        ctime
        editor
        lists {
          text {
            id
            item {
              id
              content
            }
          }
        }
        property {
          id
          type
          languageid
          value
        }
        stock {
          id
          type
          stocklevel
          timeframe
          dateback
        }
      }
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`query {
      getProduct(id: "1", include: ["text", "product/property", "stock"]) {
        id
        siteid
        type
        code
        label
        url
        dataset
        datestart
        dateend
        config
        instock
        scale
        status
        target
        boost
        mtime
        ctime
        editor
        lists {
          text {
            id
            item {
              id
              content
            }
          }
        }
        property {
          id
          type
          languageid
          value
        }
        stock {
          id
          type
          stocklevel
          timeframe
          dateback
        }
      }
    }`).then(data => {
      console.log(data)
    })
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `query {
      getProduct(id: "1", include: ["text", "product/property", "stock"]) {
        id
        siteid
        type
        code
        label
        url
        dataset
        datestart
        dateend
        config
        instock
        target
        scale
        status
        boost
        mtime
        ctime
        editor
        lists {
          text {
            id
            item {
              id
              content
            }
          }
        }
        property {
          id
          type
          languageid
          value
        }
        stock {
          id
          type
          stocklevel
          timeframe
          dateback
        }
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

Response:

```json
{
  "data": {
    "getProduct": {
      "id": "113",
      "siteid": "1.",
      "type": "default",
      "code": "demo-article",
      "label": "Demo article",
      "url": "demo-article",
      "dataset": null,
      "datestart": null,
      "dateend": null,
      "config": "{}",
      "instock": null,
      "target": null,
      "scale": 1,
      "status": 1,
      "boost": 1,
      "mtime": "2023-01-13 11:25:51",
      "ctime": "2022-12-01 11:59:00",
      "editor": "aimeos@aimeos.org",
      "lists": {
        "text": [{
          "id": "1",
          "item": {
            "id": "10",
            "content": "Test content"
          }
        }]
      },
      "property": [{
        "id": "1",
        "type": "isbn",
        "languageid": null,
        "value": "12345678"
      }],
      "stock": {[
        "id": "23",
        "type": "default",
        "stocklevel": 42,
        "timeframe": "2-3d",
        "dateback": null
      ]}
    }
  }
}
```

# Find product by code

=== "Query"
    ```graphql
    query {
      findProduct(code: "demo-article", include: ["text", "product/property", "stock"]) {
        id
        siteid
        type
        code
        label
        url
        dataset
        datestart
        dateend
        config
        instock
        scale
        status
        target
        boost
        mtime
        ctime
        editor
        lists {
          text {
            id
            item {
              id
              content
            }
          }
        }
        property {
          id
          type
          languageid
          value
        }
        stock {
          id
          type
          stocklevel
          timeframe
          dateback
        }
      }
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`query {
      findProduct(code: "demo-article", include: ["text", "product/property", "stock"]) {
        id
        siteid
        type
        code
        label
        url
        dataset
        datestart
        dateend
        config
        instock
        scale
        status
        target
        boost
        mtime
        ctime
        editor
        lists {
          text {
            id
            item {
              id
              content
            }
          }
        }
        property {
          id
          type
          languageid
          value
        }
        stock {
          id
          type
          stocklevel
          timeframe
          dateback
        }
      }
    }`).then(data => {
      console.log(data)
    })
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `query {
      findProduct(code: "demo-article", include: ["text", "product/property", "stock"]) {
        id
        siteid
        type
        code
        label
        url
        dataset
        datestart
        dateend
        config
        instock
        scale
        status
        target
        boost
        mtime
        ctime
        editor
        lists {
          text {
            id
            item {
              id
              content
            }
          }
        }
        property {
          id
          type
          languageid
          value
        }
        stock {
          id
          type
          stocklevel
          timeframe
          dateback
        }
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

Response:

```json
{
  "data": {
    "findProduct": {
      "id": "1",
      "siteid": "1.",
      "type": "default",
      "code": "demo-article",
      "label": "Demo article",
      "url": "demo-article",
      "dataset": null,
      "datestart": null,
      "dateend": null,
      "config": "{}",
      "instock": null,
      "scale": 1,
      "status": 1,
      "target": null,
      "boost": 1,
      "mtime": "2023-01-13 11:25:51",
      "ctime": "2022-12-01 11:59:00",
      "editor": "aimeos@aimeos.org",
      "lists": {
        "text": [{
          "id": "1",
          "item": {
            "id": "10",
            "content": "Test content"
          }
        }]
      },
      "property": [{
        "id": "1",
        "type": "isbn",
        "languageid": null,
        "value": "12345678"
      }],
      "stock": {[
        "id": "23",
        "type": "default",
        "stocklevel": 42,
        "timeframe": "2-3d",
        "dateback": null
      ]}
    }
  }
}
```

# Search products

The filter parameter is explained in the [filter section](basics.md#filtering-the-result) of the [GraphQL basics](basics.md) article.

=== "Query"
    ```graphql
    query {
      searchProducts(filter: "{\\"=~\\": {\\"product.code\\":\\"demo-\\"}}", include: ["text", "product/property", "stock"]) {
        items {
          id
          siteid
          type
          code
          label
          url
          dataset
          datestart
          dateend
          config
          instock
          scale
          status
          target
          boost
          mtime
          ctime
          editor
          lists {
            text {
              id
              item {
                id
                content
              }
            }
          }
          property {
            id
            type
            languageid
            value
          }
          stock {
            id
            type
            stocklevel
            timeframe
            dateback
          }
        }
        total
      }
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`query {
      searchProducts(filter: "{\\"=~\\": {\\"product.code\\":\\"demo-\\"}}", include: ["text", "product/property", "stock"]) {
        items {
          id
          siteid
          type
          code
          label
          url
          dataset
          datestart
          dateend
          config
          instock
          scale
          status
          target
          boost
          mtime
          ctime
          editor
          lists {
            text {
              id
              item {
                id
                content
              }
            }
          }
          property {
            id
            type
            languageid
            value
          }
          stock {
            id
            type
            stocklevel
            timeframe
            dateback
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
    let filter = {
        "=~": {"product.code":"demo-"}
    };
    const fstr = JSON.stringify(JSON.stringify(filter));
    const body = JSON.stringify({'query':
    `query {
      searchProducts(filter: ` + fstr + `, include: ["text", "product/property", "stock"]) {
        items {
          id
          siteid
          type
          code
          label
          url
          dataset
          datestart
          dateend
          config
          instock
          scale
          status
          target
          boost
          mtime
          ctime
          editor
          lists {
            text {
              id
              item {
                id
                content
              }
            }
          }
          property {
            id
            type
            languageid
            value
          }
          stock {
            id
            type
            stocklevel
            timeframe
            dateback
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

Response:

```json
{
  "data": {
    "searchProducts": {
      "items": [
        {
          "id": "1",
          "siteid": "1.",
          "type": "default",
          "code": "demo-article",
          "label": "Demo article",
          "url": "demo-article",
          "dataset": null,
          "datestart": null,
          "dateend": null,
          "config": "{}",
          "instock": null,
          "scale": 1,
          "status": 1,
          "target": null,
          "boost": 1,
          "mtime": "2023-01-13 11:25:51",
          "ctime": "2022-12-01 11:59:00",
          "editor": "aimeos@aimeos.org",
          "lists": {
            "text": [{
              "id": "1",
              "item": {
                "id": "10",
                "content": "Test content"
              }
            }]
          },
          "property": [{
            "id": "1",
            "type": "isbn",
            "languageid": null,
            "value": "12345678"
          }],
          "stock": {[
            "id": "23",
            "type": "default",
            "stocklevel": 42,
            "timeframe": "2-3d",
            "dateback": null
          ]}
        },
        {
          "id": "2",
          "siteid": "1.",
          "type": "default",
          "code": "demo-selection-article-1",
          "label": "Demo variant article 1",
          "url": "demo-variant-article-1",
          "dataset": null,
          "datestart": null,
          "dateend": null,
          "config": "{}",
          "instock": null,
          "scale": 1,
          "status": 1,
          "target": null,
          "boost": 1,
          "mtime": "2022-12-01 11:59:05",
          "ctime": "2022-12-01 11:59:05",
          "editor": "core",
          "lists": {
            "text": []
          },
          "property": [],
          "stock": []
        }
      ],
      "total": 2
    }
  }
}
```

# Save single product

=== "Mutation"
    ```graphql
    mutation {
      saveProduct(input: {
        code: "test"
        label: "Test product"
        lists: {
          media: [{
            refid: "<ID from saveMedia or saveMedias mutation>"
          }]
          price: [{
            item: {
              currencyid: "EUR"
              value: "100.00"
              taxrates: "{\"tax\": \"19.00\"}"
            }
          }]
          text: [{
            item: {
              type: "name"
              languageid: "en"
              content: "Test content"
            }
          }]
        }
        property: [{
          type: "isbn"
          languageid: null
          value: "12345678"
        }]
        stock: [{
          type: "default"
          stocklevel: 100
        }]
      }) {
        id
      }
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`mutation {
      saveProduct(input: {
        code: "test"
        label: "Test product"
        lists: {
          media: [{
            refid: "<ID from saveMedia or saveMedias mutation>"
          }]
          price: [{
            item: {
              currencyid: "EUR"
              value: "100.00"
              taxrates: "{\"tax\": \"19.00\"}"
            }
          }]
          text: [{
            item: {
              type: "name"
              languageid: "en"
              content: "Test content"
            }
          }]
        }
        property: [{
          type: "isbn"
          languageid: null
          value: "12345678"
        }]
        stock: [{
          type: "default"
          stocklevel: 100
        }]
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
        lists: {
          media: [{
            refid: "<ID from saveMedia or saveMedias mutation>"
          }]
          price: [{
            item: {
              currencyid: "EUR"
              value: "100.00"
              taxrates: "{\"tax\": \"19.00\"}"
            }
          }]
          text: [{
            item: {
              type: "name"
              languageid: "en"
              content: "Test content"
            }
          }]
        }
        property: [{
          type: "isbn"
          languageid: null
          value: "12345678"
        }]
        stock: [{
          type: "default"
          stocklevel: 100
        }]
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

Response:

```json
{
  "data": {
    "saveProduct": {
      "id": "18"
    }
  }
}
```

# Save multiple products

=== "Mutation"
    ```graphql
    mutation {
      saveProducts(input: [{
        code: "test-2"
        label: "Test 2 product"
        lists: {
          text: [{
            item: {
              type: "name"
              languageid: "en"
              content: "Test content"
            }
          }]
        }
        property: [{
          type: "isbn"
          languageid: null
          value: "12345678"
        }]
        stock: [{
          type: "default"
          stocklevel: 100
        }]
      }
      {
        code: "test-3"
        label: "Test 3 product"
      }]) {
        id
      }
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`mutation {
      saveProducts(input: [{
        code: "test-2"
        label: "Test 2 product"
        lists: {
          text: [{
            item: {
              type: "name"
              languageid: "en"
              content: "Test content"
            }
          }]
        }
        property: [{
          type: "isbn"
          languageid: null
          value: "12345678"
        }]
        stock: [{
          type: "default"
          stocklevel: 100
        }]
      }
      {
        code: "test-3"
        label: "Test 3 product"
      }]) {
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
      saveProducts(input: [{
        code: "test-2"
        label: "Test 2 product"
        lists: {
          text: [{
            item: {
              type: "name"
              languageid: "en"
              content: "Test content"
            }
          }]
        }
        property: [{
          type: "isbn"
          languageid: null
          value: "12345678"
        }]
        stock: [{
          type: "default"
          stocklevel: 100
        }]
      }
      {
        code: "test-3"
        label: "Test 3 product"
      }]) {
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

Response:

```json
{
  "data": {
    "saveProducts": [
      {
        "id": "19"
      },
      {
        "id": "20"
      }
    ]
  }
}
```

# Delete single product

=== "Mutation"
    ```graphql
    mutation {
      deleteProduct(id: "18")
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`mutation {
      deleteProduct(id: "18")
    }`).then(data => {
      console.log(data)
    })
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deleteProduct(id: "18")
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

Response:

```json
{
  "data": {
    "deleteProduct": "18"
  }
}
```

# Delete multiple products

=== "Mutation"
    ```graphql
    mutation {
      deleteProducts(id: ["19", "20"])
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`mutation {
      deleteProducts(id: ["19", "20"])
    }`).then(data => {
      console.log(data)
    })
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deleteProducts(id: ["19", "20"])
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

Response:

```json
{
  "data": {
    "deleteProducts": [
      "19",
      "20"
    ]
  }
}
```

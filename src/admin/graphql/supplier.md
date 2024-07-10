This article contains all actions for retrieving and managing suppliers.

!!! tip
    The supplier domain supports [fetching related resources](basics.md#include-related-resources).

# Get supplier by ID

=== "Query"
    ```graphql
    query {
      getSupplier(id: "1", include: ["text"]) {
        id
        siteid
        code
        label
        position
        status
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
      }
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`query {
      getSupplier(id: "1", include: ["text"]) {
        id
        siteid
        code
        label
        position
        status
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
      }
    }`).then(data => {
      console.log(data)
    })
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `query {
      getSupplier(id: "1", include: ["text"]) {
        id
        siteid
        code
        label
        position
        status
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
    "getSupplier": {
      "id": "1",
      "siteid": "1.",
      "code": "demo-test1",
      "label": "Test supplier 1",
      "position": 0,
      "status": 1,
      "mtime": "2022-12-01 11:59:04",
      "ctime": "2022-12-01 11:59:04",
      "editor": "core",
      "lists": {
        "text": [{
          "id": "1",
          "item": {
            "id": "10",
            "content": "Test content"
          }
        }]
      }
    }
  }
}
```

# Find supplier by code

=== "Query"
    ```graphql
    query {
      findSupplier(code: "demo-test1", include: ["text"]) {
        id
        siteid
        code
        label
        position
        status
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
      }
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`query {
      findSupplier(code: "demo-test1", include: ["text"]) {
        id
        siteid
        code
        label
        position
        status
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
      }
    }`).then(data => {
      console.log(data)
    })
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `query {
      findSupplier(code: "demo-test1", include: ["text"]) {
        id
        siteid
        code
        label
        position
        status
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
    "findSupplier": {
      "id": "1",
      "siteid": "1.",
      "code": "demo-test1",
      "label": "Test supplier 1",
      "position": 0,
      "status": 1,
      "mtime": "2022-12-01 11:59:04",
      "ctime": "2022-12-01 11:59:04",
      "editor": "core",
      "lists": {
        "text": [{
          "id": "1",
          "item": {
            "id": "10",
            "content": "Test content"
          }
        }]
      }
    }
  }
}
```

# Search suppliers

The filter parameter is explained in the [filter section](basics.md#filtering-the-result) of the [GraphQL basics](basics.md) article.

=== "Query"
    ```graphql
    query {
      searchSuppliers(filter: "{\\"=~\\": {\\"supplier.code\\":\\"demo-\\"}}", include: ["text"]) {
        items {
          id
          siteid
          code
          label
          position
          status
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
        }
        total
      }
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`query {
      searchSuppliers(filter: "{\\"=~\\": {\\"supplier.code\\":\\"demo-\\"}}", include: ["text"]) {
        items {
          id
          siteid
          code
          label
          position
          status
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
        "=~": {"supplier.code":"demo-"}
    };
    const fstr = JSON.stringify(JSON.stringify(filter));
    const body = JSON.stringify({'query':
    `query {
      searchSuppliers(filter: ` + fstr + `, include: ["text"]) {
        items {
          id
          siteid
          code
          label
          position
          status
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
    "searchSuppliers": {
      "items": [
        {
          "id": "1",
          "siteid": "1.",
          "code": "demo-test1",
          "label": "Test supplier 1",
          "position": 0,
          "status": 1,
          "mtime": "2022-12-01 11:59:04",
          "ctime": "2022-12-01 11:59:04",
          "editor": "core",
          "lists": {
            "text": [{
              "id": "1",
              "item": {
                "id": "10",
                "content": "Test content"
              }
            }]
          }
        },
        {
          "id": "2",
          "siteid": "1.",
          "code": "demo-test2",
          "label": "Test supplier 2",
          "position": 0,
          "status": 1,
          "mtime": "2022-12-01 11:59:04",
          "ctime": "2022-12-01 11:59:04",
          "editor": "core",
          "lists": {
            "text": []
          }
        }
      ],
      "total": 2
    }
  }
}
```

# Save single supplier

=== "Mutation"
    ```graphql
    mutation {
      saveSupplier(input: {
        code: "test"
        label: "Test supplier",
        lists: {
          text: [{
            item: {
              content: "Test content"
            }
          }]
        }
      }) {
        id
      }
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`mutation {
      saveSupplier(input: {
        code: "test"
        label: "Test supplier",
        lists: {
          text: [{
            item: {
              content: "Test content"
            }
          }]
        }
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
      saveSupplier(input: {
        code: "test"
        label: "Test supplier",
        lists: {
          text: [{
            item: {
              content: "Test content"
            }
          }]
        }
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
    "saveSupplier": {
      "id": "3"
    }
  }
}
```

# Save multiple suppliers

=== "Mutation"
    ```graphql
    mutation {
      saveSuppliers(input: [{
        code: "test-2"
        label: "Test 2 supplier",
        lists: {
          text: [{
            item: {
              content: "Test content"
            }
          }]
        }
      },{
        code: "test-3"
        label: "Test 3 supplier"
      }]) {
        id
      }
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`mutation {
      saveSuppliers(input: [{
        code: "test-2"
        label: "Test 2 supplier",
        lists: {
          text: [{
            item: {
              content: "Test content"
            }
          }]
        }
      },{
        code: "test-3"
        label: "Test 3 supplier"
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
      saveSuppliers(input: [{
        code: "test-2"
        label: "Test 2 supplier",
        lists: {
          text: [{
            item: {
              content: "Test content"
            }
          }]
        }
      },{
        code: "test-3"
        label: "Test 3 supplier"
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
    "saveSuppliers": [
      {
        "id": "4"
      },
      {
        "id": "5"
      }
    ]
  }
}
```

# Delete single supplier

=== "Mutation"
    ```graphql
    mutation {
      deleteSupplier(id: "3")
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`mutation {
      deleteSupplier(id: "3")
    }`).then(data => {
      console.log(data)
    })
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deleteSupplier(id: "3")
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
    "deleteSupplier": "3"
  }
}
```

# Delete multiple suppliers

=== "Mutation"
    ```graphql
    mutation {
      deleteSuppliers(id: ["4", "5"])
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`mutation {
      deleteSuppliers(id: ["4", "5"])
    }`).then(data => {
      console.log(data)
    })
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deleteSuppliers(id: ["4", "5"])
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
    "deleteSuppliers": [
      "4",
      "5"
    ]
  }
}
```

This article contains all actions for retrieving and managing categories.

!!! tip
    The catalog domains supports [fetching related resources](basics.md#include-related-resources).

# Get category by ID

=== "Query"
    ```graphql
    query {
      getCatalog(id: "1", include: ["text"]) {
        id
        siteid
        parentid
        code
        label
        url
        config
        status
        target
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
      getCatalog(id: "1", include: ["text"]) {
        id
        siteid
        parentid
        code
        label
        url
        config
        status
        target
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
      getCatalog(id: "1", include: ["text"]) {
        id
        siteid
        parentid
        code
        label
        url
        config
        status
        target
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
    "getCatalog": {
      "id": "1",
      "siteid": "1.",
      "parentid": 0,
      "code": "home",
      "label": "Home",
      "url": "Home",
      "config": "{\\"css-class\\":\\"megamenu\\"}",
      "status": 1,
      "target": "",
      "mtime": "2022-06-16 10:03:47",
      "ctime": "2022-06-16 10:03:47",
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

# Get categories in path

=== "Query"
    ```graphql
    query {
      getCatalogPath(id: "4", include: ["text"]) {
        id
        label
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
      getCatalogPath(id: "4", include: ["text"]) {
        id
        label
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
      getCatalogPath(id: "4", include: ["text"]) {
        id
        label
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
    "getCatalogPath": [
      {
        "id": "1",
        "label": "Home",
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
        "label": "Best sellers",
        "lists": {
          "text": []
        }
      },
      {
        "id": "3",
        "label": "Women",
        "lists": {
          "text": []
        }
      },
      {
        "id": "4",
        "label": "Dresses",
        "lists": {
          "text": []
        }
      }
    ]
  }
}
```

# Get category tree

=== "Query"
    ```graphql
    query {
      getCatalogTree(id: "1", level: 3, include: ["text"]) {
        id
        label
        lists {
          text {
            id
            item {
              id
              content
            }
          }
        }
        children {
          id
          label
          lists {
            text {
              id
              item {
                id
                content
              }
            }
          }
          children {
            id
            label
          }
        }
      }
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`query {
      getCatalogTree(id: "1", level: 3, include: ["text"]) {
        id
        label
        lists {
          text {
            id
            item {
              id
              content
            }
          }
        }
        children {
          id
          label
          lists {
            text {
              id
              item {
                id
                content
              }
            }
          }
          children {
            id
            label
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
      getCatalogTree(id: "1", level: 3, include: ["text"]) {
        id
        label
        lists {
          text {
            id
            item {
              id
              content
            }
          }
        }
        children {
          id
          label
          lists {
            text {
              id
              item {
                id
                content
              }
            }
          }
          children {
            id
            label
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
    "getCatalogTree": {
      "id": "1",
      "label": "Home",
      "lists": {
        "text": [{
          "id": "1",
          "item": {
            "id": "10",
            "content": "Test content"
          }
        }]
      }
      "children": [
        {
          "id": "2",
          "label": "Best sellers",
          "lists": {
            "text": []
          }
          "children": [
            {
              "id": "3",
              "label": "Women"
            },
            {
              "id": "7",
              "label": "Shirts"
            },
            {
              "id": "12",
              "label": "Men"
            },
            {
              "id": "15",
              "label": "Misc"
            }
          ]
        },
        {
          "id": "16",
          "label": "New arrivals",
          "lists": {
            "text": []
          }
          "children": []
        },
        {
          "id": "17",
          "label": "Hot deals",
          "lists": {
            "text": []
          }
          "children": []
        }
      ]
    }
  }
}
```

# Find category by code

=== "Query"
    ```graphql
    query {
      findCatalog(code: "home", include: ["text"]) {
        id
        siteid
        parentid
        code
        label
        url
        config
        status
        target
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
      findCatalog(code: "home", include: ["text"]) {
        id
        siteid
        parentid
        code
        label
        url
        config
        status
        target
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
      findCatalog(code: "home", include: ["text"]) {
        id
        siteid
        parentid
        code
        label
        url
        config
        status
        target
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
    "findCatalog": {
      "id": "1",
      "siteid": "1.",
      "parentid": 0,
      "code": "home",
      "label": "Home",
      "url": "Home",
      "config": "{\\"css-class\\":\\"megamenu\\"}",
      "status": 1,
      "target": "",
      "mtime": "2022-06-16 10:03:47",
      "ctime": "2022-06-16 10:03:47",
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

# Search categories

The filter parameter is explained in the [filter section](basics.md#filtering-the-result) of the [GraphQL basics](basics.md) article.

=== "Query"
    ```graphql
    query {
      searchCatalogs(filter: "{\\"=~\\": {\\"catalog.code\\":\\"demo-\\"}}", include: ["text"]) {
        items {
          id
          siteid
          parentid
          code
          label
          url
          config
          status
          target
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
    let filter = {
        "=~": {"catalog.code":"demo-"}
    };
    const fstr = JSON.stringify(JSON.stringify(filter));
    Aimeos.query(`query {
      searchCatalogs(filter: ` + fstr + `, include: ["text"]) {
        items {
          id
          siteid
          parentid
          code
          label
          url
          config
          status
          target
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
        "=~": {"catalog.code":"demo-"}
    };
    const fstr = JSON.stringify(JSON.stringify(filter));
    const body = JSON.stringify({'query':
    `query {
      searchCatalogs(filter: ` + fstr + `, include: ["text"]) {
        items {
          id
          siteid
          parentid
          code
          label
          url
          config
          status
          target
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
    "searchCatalogs": {
      "items": [
        {
          "id": "2",
          "siteid": "1.",
          "parentid": 1,
          "code": "demo-best",
          "label": "Best sellers",
          "url": "best-sellers",
          "config": "{}",
          "status": 1,
          "target": "",
          "mtime": "2022-12-01 11:59:02",
          "ctime": "2022-12-01 11:59:02",
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
          "id": "3",
          "siteid": "1.",
          "parentid": 1,
          "code": "demo-best-women",
          "label": "Women",
          "url": "women",
          "config": "{}",
          "status": 1,
          "target": "",
          "mtime": "2022-12-01 11:59:02",
          "ctime": "2022-12-01 11:59:02",
          "editor": "core",
          "lists": {
            "text": []
          }
        },
      ],
      "total": 2
    }
  }
}
```

# Insert new category

The `insertCatalog` mutation accepts three parameters:

* input: Object with catalog item properties
* parentid: ID of the parent category (optional, default: `null` creates a new root category)
* refid: ID of the category the new item should be inserted before (optional, default: append at the end)

=== "Mutation"
    ```graphql
    mutation {
      insertCatalog(input: {
        code: "test"
        label: "Test category"
        lists: {
          text: [{
            item: {
              content: "Test content"
            }
          }]
        }
      }, parentid: "1", refid: "3") {
        id
      }
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`mutation {
      insertCatalog(input: {
        code: "test"
        label: "Test category"
        lists: {
          text: [{
            item: {
              content: "Test content"
            }
          }]
        }
      }, parentid: "1", refid: "3") {
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
      insertCatalog(input: {
        code: "test"
        label: "Test category"
        lists: {
          text: [{
            item: {
              content: "Test content"
            }
          }]
        }
      }, parentid: "1", refid: "3") {
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
    "insertCatalog": {
      "id": "15"
    }
  }
}
```

# Update existing category

=== "Mutation"
    ```graphql
    mutation {
      saveCatalog(input: {
        id: "15"
        label: "Test category label"
        lists: {
          text: [{
            item: {
              content: "Test content"
            }
          }]
        }
      }) {
        label
      }
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`mutation {
      saveCatalog(input: {
        id: "15"
        label: "Test category label"
        lists: {
          text: [{
            item: {
              content: "Test content"
            }
          }]
        }
      }) {
        label
      }
    }`).then(data => {
      console.log(data)
    })
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      saveCatalog(input: {
        id: "15"
        label: "Test category label"
        lists: {
          text: [{
            item: {
              content: "Test content"
            }
          }]
        }
      }) {
        label
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
    "saveCatalog": {
      "label": "Test category label"
    }
  }
}
```

# Save multiple existing categories

=== "Mutation"
    ```graphql
    mutation {
      saveCatalogs(input: [{
        id: "1"
        label: "Root"
      }
      {
        id: "15"
        label: "Test category label"
        lists: {
          text: [{
            item: {
              content: "Test content"
            }
          }]
        }
      }]) {
        label
      }
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`mutation {
      saveCatalogs(input: [{
        id: "1"
        label: "Root"
      }
      {
        id: "15"
        label: "Test category label"
        lists: {
          text: [{
            item: {
              content: "Test content"
            }
          }]
        }
      }]) {
        label
      }
    }`).then(data => {
      console.log(data)
    })
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      saveCatalogs(input: [{
        id: "1"
        label: "Root"
      }
      {
        id: "15"
        label: "Test category label"
        lists: {
          text: [{
            item: {
              content: "Test content"
            }
          }]
        }
      }]) {
        label
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
    "saveCatalogs": [
      {
        "label": "Root"
      },
      {
        "label": "Test category label"
      }
    ]
  }
}
```

# Move existing category

The `moveCatalog` mutation accepts four parameters:

* id: ID of the category that should be moved
* parentid: Parent category ID of the category that should be moved
* targetid: New parent category ID the category should be moved to (optional, default: `null` creates a new root category)
* refid: ID of the category the new item should be inserted before (optional, default: append at the end)

=== "Mutation"
    ```graphql
    mutation {
      moveCatalog(id: "15", parentid: "1", targetid: "2", refid: "3")
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`mutation {
      moveCatalog(id: "15", parentid: "1", targetid: "2", refid: "3")
    }`).then(data => {
      console.log(data)
    })
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      moveCatalog(id: "15", parentid: "1", targetid: "2", refid: "3")
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
    "moveCatalog": "15"
  }
}
```

# Delete single category

=== "Mutation"
    ```graphql
    mutation {
      deleteCatalog(id: "15")
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`mutation {
      deleteCatalog(id: "15")
    }`).then(data => {
      console.log(data)
    })
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deleteCatalog(id: "15")
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
    "deleteCatalog": "15"
  }
}
```

# Delete multiple categories

=== "Mutation"
    ```graphql
    mutation {
      deleteCatalogs(id: ["14", "15"])
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`mutation {
      deleteCatalogs(id: ["14", "15"])
    }`).then(data => {
      console.log(data)
    })
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deleteCatalogs(id: ["14", "15"])
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
    "deleteCatalogs": [
      "14",
      "15"
    ]
  }
}
```

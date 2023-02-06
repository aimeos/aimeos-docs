This article contains all actions for retrieving and managing categories.

# Get category by ID

=== "Query"
    ```graphql
    query {
      getCatalog(id: "1") {
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
      }
    }
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `query {
      getCatalog(id: "1") {
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
      "config": "{\"css-class\":\"megamenu\"}",
      "status": 1,
      "target": "",
      "mtime": "2022-06-16 10:03:47",
      "ctime": "2022-06-16 10:03:47",
      "editor": "core"
    }
  }
}
```

# Get categories in path

=== "Query"
    ```graphql
    query {
      getCatalogPath(id: "4", include: []) {
        id
        label
      }
    }
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `query {
      getCatalogPath(id: "4", include: []) {
        id
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

Response:

```json
{
  "data": {
    "getCatalogPath": [
      {
        "id": "1",
        "label": "Home"
      },
      {
        "id": "2",
        "label": "Best sellers"
      },
      {
        "id": "3",
        "label": "Women"
      },
      {
        "id": "4",
        "label": "Dresses"
      }
    ]
  }
}
```

# Get category tree

=== "Query"
    ```graphql
    query {
      getCatalogTree(id: "1", level: 3, include: []) {
        id
        label
        children {
          id
          label
          children {
            id
            label
          }
        }
      }
    }
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `query {
      getCatalogTree(id: "1", level: 3, include: []) {
        id
        label
        children {
          id
          label
          children {
            id
            label
          }
        }
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

Response:

```json
{
  "data": {
    "getCatalogTree": {
      "id": "1",
      "label": "Home",
      "children": [
        {
          "id": "2",
          "label": "Best sellers",
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
          "children": []
        },
        {
          "id": "17",
          "label": "Hot deals",
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
      findCatalog(code: "home") {
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
      }
    }
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `query {
      findCatalog(code: "home") {
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
      "config": "{\"css-class\":\"megamenu\"}",
      "status": 1,
      "target": "",
      "mtime": "2022-06-16 10:03:47",
      "ctime": "2022-06-16 10:03:47",
      "editor": "core"
    }
  }
}
```

# Search categories

The filter parameter is explained in the [filter section](basics.md#filtering-the-result) of the [GraphQL basics](basics.md) article.

=== "Query"
    ```graphql
    query {
      searchCatalogs(filter: "{\"=~\": {\"catalog.code\":\"demo-\"}}") {
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
      }
    }
    ```
=== "Javascript"
    ```javascript
    let filter = {
        "=~": {"catalog.code":"demo-"}
    };
    const fstr = JSON.stringify(filter).replace(/"/g, '\\"');
    const body = JSON.stringify({'query':
    `query {
      searchCatalogs(filter: "` + fstr + `") {
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

Response:

```json
{
  "data": {
    "searchCatalogs": [
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
        "editor": "core"
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
        "editor": "core"
      },
    ]
  }
}
```

# Insert new category

=== "Mutation"
    ```graphql
    mutation {
      saveCatalog(input: {
        parentid: "1"
        code: "test"
        label: "Test category"
      }) {
        id
      }
    }
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      saveCatalog(input: {
        parentid: "1"
        code: "test"
        label: "Test category"
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
      }) {
        label
      }
    }
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      saveCatalog(input: {
        id: "15"
        label: "Test category label"
      }) {
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

# Move existing category

=== "Mutation"
    ```graphql
    mutation {
      moveCatalog(id: "15", parentid: "1", targetid: "2", refid: "3")
    }
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      moveCatalog(id: "15", parentid: "1", targetid: "2", refid: "3")
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

Response:

```json
{
  "data": {
    "moveCatalog": "15"
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
      },{
        id: "15"
        label: "Test category label"
      }]) {
        label
      }
    }
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      saveCatalogs(input: [{
        id: "1"
        label: "Root"
      },{
        id: "15"
        label: "Test category label"
      }]) {
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

# Delete single category

=== "Mutation"
    ```graphql
    mutation {
      deleteCatalog(id: "15")
    }
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deleteCatalog(id: "15")
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
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deleteCatalogs(id: ["14", "15"])
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

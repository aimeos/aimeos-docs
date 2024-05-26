This article contains all actions for retrieving and managing attributes.

!!! tip
    The attribute domain supports [fetching related resources](basics.md#include-related-resources).

# Get attribute by ID

=== "Query"
    ```graphql
    query {
      getAttribute(id: "1", include: ["text"]) {
        id
        type
        siteid
        domain
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
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `query {
      getAttribute(id: "1", include: ["text"]) {
        id
        type
        siteid
        domain
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
    "getAttribute": {
      "id": "1",
      "siteid": "1.",
      "domain": "product",
      "code": "demo-black",
      "label": "Demo: Black",
      "position": 1,
      "status": 1,
      "mtime": "2022-12-01 11:59:05",
      "ctime": "2022-12-01 11:59:05",
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

# Find attribute by code

=== "Query"
    ```graphql
    query {
      findAttribute(code: "demo-black", domain: "product", type: "color", include: ["text"]) {
        id
        type
        siteid
        domain
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
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `query {
      findAttribute(code: "demo-black", domain: "product", type: "color", include: ["text"]) {
        id
        type
        siteid
        domain
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
    "findAttribute": {
      "id": "1",
      "siteid": "1.",
      "domain": "product",
      "code": "demo-black",
      "label": "Demo: Black",
      "position": 1,
      "status": 1,
      "mtime": "2022-12-01 11:59:05",
      "ctime": "2022-12-01 11:59:05",
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

# Search attributes

The filter parameter is explained in the [filter section](basics.md#filtering-the-result) of the [GraphQL basics](basics.md) article.

=== "Query"
    ```graphql
    query {
      searchAttributes(filter: "{\\"=~\\": {\\"attribute.code\\":\\"demo-\\"}}", include: ["text"]) {
        items {
          id
          type
          siteid
          domain
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
=== "Javascript"
    ```javascript
    let filter = {
        "=~": {"attribute.code":"demo-"}
    };
    const fstr = JSON.stringify(JSON.stringify(filter));
    const body = JSON.stringify({'query':
    `query {
      searchAttributes(filter: ` + fstr + `, include: ["text"]) {
        items {
          id
          type
          siteid
          domain
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
    "searchAttributes": {
      "items": [
        {
          "id": "1",
          "siteid": "1.",
          "domain": "product",
          "code": "demo-black",
          "label": "Demo: Black",
          "position": 1,
          "status": 1,
          "mtime": "2022-12-01 11:59:05",
          "ctime": "2022-12-01 11:59:05",
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
          "domain": "product",
          "code": "demo-blue",
          "label": "Demo: Blue",
          "position": 2,
          "status": 1,
          "mtime": "2022-12-01 11:59:05",
          "ctime": "2022-12-01 11:59:05",
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

# Save single attribute

=== "Mutation"
    ```graphql
    mutation {
      saveAttribute(input: {
        code: "test"
        type: "color"
        domain: "product"
        label: "Test attribute",
        lists: {
          text: {
            item: {
              content: "Test content"
            }
          }
        }
      }) {
        id
      }
    }
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      saveAttribute(input: {
        code: "test"
        type: "color"
        domain: "product"
        label: "Test attribute",
        lists: {
          text: {
            item: {
              content: "Test content"
            }
          }
        }
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
    "saveAttribute": {
      "id": "18"
    }
  }
}
```

# Save multiple attributes

=== "Mutation"
    ```graphql
    mutation {
      saveAttributes(input: [{
        code: "test-2"
        type: "color"
        domain: "product"
        label: "Test 2 attribute",
        lists: {
          text: {
            item: {
              content: "Test content"
            }
          }
        }
      },{
        code: "test-3"
        type: "color"
        domain: "product"
        label: "Test 3 attribute"
      }]) {
        id
      }
    }
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      saveAttributes(input: [{
        code: "test-2"
        type: "color"
        domain: "product"
        label: "Test 2 attribute",
        lists: {
          text: {
            item: {
              content: "Test content"
            }
          }
        }
      },{
        code: "test-3"
        type: "color"
        domain: "product"
        label: "Test 3 attribute"
      }]) {
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
    "saveAttributes": [
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

# Delete single attribute

=== "Mutation"
    ```graphql
    mutation {
      deleteAttribute(id: "18")
    }
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deleteAttribute(id: "18")
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
    "deleteAttribute": "18"
  }
}
```

# Delete multiple attributes

=== "Mutation"
    ```graphql
    mutation {
      deleteAttributes(id: ["19", "20"])
    }
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deleteAttributes(id: ["19", "20"])
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
    "deleteAttributes": [
      "19",
      "20"
    ]
  }
}
```

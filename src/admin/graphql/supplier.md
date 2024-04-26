This article contains all actions for retrieving and managing suppliers.

!!! tip
    The supplier domain supports [fetching related resources](basics.md#include-related-resources).

# Get supplier by ID

=== "Query"
    ```graphql
    query {
      getSupplier(id: "1") {
        id
        siteid
        code
        label
        position
        status
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
      getSupplier(id: "1") {
        id
        siteid
        code
        label
        position
        status
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
    "getSupplier": {
      "id": "1",
      "siteid": "1.",
      "code": "demo-test1",
      "label": "Test supplier 1",
      "position": 0,
      "status": 1,
      "mtime": "2022-12-01 11:59:04",
      "ctime": "2022-12-01 11:59:04",
      "editor": "core"
    }
  }
}
```

# Find supplier by code

=== "Query"
    ```graphql
    query {
      findSupplier(code: "demo-test1") {
        id
        siteid
        code
        label
        position
        status
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
      findSupplier(code: "demo-test1") {
        id
        siteid
        code
        label
        position
        status
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
    "findSupplier": {
      "id": "1",
      "siteid": "1.",
      "code": "demo-test1",
      "label": "Test supplier 1",
      "position": 0,
      "status": 1,
      "mtime": "2022-12-01 11:59:04",
      "ctime": "2022-12-01 11:59:04",
      "editor": "core"
    }
  }
}
```

# Search suppliers

The filter parameter is explained in the [filter section](basics.md#filtering-the-result) of the [GraphQL basics](basics.md) article.

=== "Query"
    ```graphql
    query {
      searchSuppliers(filter: "{\"=~\": {\"supplier.code\":\"demo-\"}}") {
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
        }
        total
      }
    }
    ```
=== "Javascript"
    ```javascript
    let filter = {
        "=~": {"supplier.code":"demo-"}
    };
    const fstr = JSON.stringify(JSON.stringify(filter));
    const body = JSON.stringify({'query':
    `query {
      searchSuppliers(filter: ` + fstr + `) {
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
          "editor": "core"
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
          "editor": "core"
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
        label: "Test supplier"
      }) {
        id
      }
    }
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      saveSupplier(input: {
        code: "test"
        label: "Test supplier"
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
        label: "Test 2 supplier"
      },{
        code: "test-3"
        label: "Test 3 supplier"
      }]) {
        id
      }
    }
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      saveSuppliers(input: [{
        code: "test-2"
        label: "Test 2 supplier"
      },{
        code: "test-3"
        label: "Test 3 supplier"
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
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deleteSupplier(id: "3")
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
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deleteSuppliers(id: ["4", "5"])
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
    "deleteSuppliers": [
      "4",
      "5"
    ]
  }
}
```

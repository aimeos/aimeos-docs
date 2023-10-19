This article contains all actions for retrieving and managing plugins.

# Get plugin by ID

=== "Query"
    ```graphql
    query {
      getPlugin(id: "1") {
        id
        siteid
        type
        label
        provider
        config
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
      getPlugin(id: "1") {
        id
        siteid
        type
        label
        provider
        config
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
    "getPlugin": {
      "id": "1",
      "siteid": "1.",
      "type": "catalog",
      "label": "+10% Test",
      "provider": "Percent",
      "datestart": null,
      "dateend": null,
      "config": "{\"last-plugin\":0,\"percent\":10}",
      "position": 0,
      "status": 1,
      "mtime": "2022-12-22 09:51:38",
      "ctime": "2022-06-21 13:36:28",
      "editor": "aimeos@aimeos.org"
    }
  }
}
```

# Search plugins

The filter parameter is explained in the [filter section](basics.md#filtering-the-result) of the [GraphQL basics](basics.md) article.

=== "Query"
    ```graphql
    query {
      searchPlugins(filter: "{\"~=\": {\"plugin.label\":\"Product\"}}") {
        id
        siteid
        type
        label
        provider
        config
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
    let filter = {
        "~=": {"plugin.label":"Product"}
    };
    const fstr = JSON.stringify(JSON.stringify(filter));
    const body = JSON.stringify({'query':
    `query {
      searchPlugins(filter: ` + fstr + `) {
        id
        siteid
        type
        label
        provider
        config
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
    "searchPlugins": [
      {
        "id": "1",
        "siteid": "1.",
        "type": "catalog",
        "label": "+10% Test",
        "provider": "Percent",
        "datestart": null,
        "dateend": null,
        "config": "{\"last-plugin\":0,\"percent\":10}",
        "position": 0,
        "status": 1,
        "mtime": "2022-12-22 09:51:38",
        "ctime": "2022-06-21 13:36:28",
        "editor": "aimeos@aimeos.org"
      }
    ]
  }
}
```

# Fetch plugin configuration

To retrieve the backend configuration for a plugin provider and the added decorators use:

=== "Query"
    ```graphql
    query {
      getPluginConfig(provider: "Autofill", type: "order") {
        code
        type
        label
      }
    }
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `query {
      getPluginConfig(provider: "Autofill", type: "order") {
        code
        type
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
    "getPluginConfig": [
      {
        "code":"address",
        "type":"boolean",
        "label":"Add customer address automatically"
      },{
        "code":"delivery",
        "type":"boolean",
        "label":"Add delivery option automatically"
      },{
        "code":"deliverycode",
        "type":"string",
        "label":"Add delivery by code"
      },{
        "code":"payment",
        "type":"boolean",
        "label":"Add payment option automatically"
      },{
        "code":"paymentcode",
        "type":"string",
        "label":"Add payment by code"
      },{
        "code":"useorder",
        "type":"boolean",
        "label":"Add from last order"
      },{
        "code":"orderaddress",
        "type":"boolean",
        "label":"Add address from last order"
      },{
        "code":"orderservice",
        "type":"boolean",
        "label":"Add delivery\/payment from last order"
      }
    ]
  }
}
```

# Save single plugin

=== "Mutation"
    ```graphql
    mutation {
      savePlugin(input: {
        type: "order"
        label: "Test plugin"
        provider: "Shipping"
        config: "{\"threshold\": "50.00"}"
        status: 0
      }) {
        id
      }
    }
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      savePlugin(input: {
        type: "order"
        label: "Test plugin"
        provider: "Shipping"
        config: "{\"threshold\": "50.00"}"
        status: 0
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
    "savePlugin": {
      "id": "13"
    }
  }
}
```

# Save multiple plugins

=== "Mutation"
    ```graphql
    mutation {
      savePlugins(input: [{
        type: "order"
        label: "Test plugin 2"
        provider: "Shipping"
        config: "{\"threshold\": "25.00"}"
        status: 0
      },{
        type: "order"
        label: "Test plugin 3"
        provider: "Example"
        config: "{}"
        status: 0
      }]) {
        id
      }
    }
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      savePlugins(input: [{
        type: "order"
        label: "Test plugin 2"
        provider: "Shipping"
        config: "{\"threshold\": "25.00"}"
        status: 0
      },{
        type: "order"
        label: "Test plugin 3"
        provider: "Example"
        config: "{}"
        status: 0
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
    "savePlugins": [
      {
        "id": "14"
      },
      {
        "id": "15"
      }
    ]
  }
}
```

# Delete single plugin

=== "Mutation"
    ```graphql
    mutation {
      deletePlugin(id: "13")
    }
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deletePlugin(id: "13")
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
    "deletePlugin": "13"
  }
}
```

# Delete multiple plugins

=== "Mutation"
    ```graphql
    mutation {
      deletePlugins(id: ["14", "15"])
    }
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deletePlugins(id: ["14", "15"])
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
    "deletePlugins": [
      "14",
      "15"
    ]
  }
}
```

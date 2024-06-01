This article contains all actions for retrieving and managing services.

!!! tip
    The service domain supports [fetching related resources](basics.md#include-related-resources).

# Get service by ID

=== "Query"
    ```graphql
    query {
      getService(id: "1", include: ["text"]) {
        id
        siteid
        type
        code
        label
        provider
        datestart
        dateend
        config
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
      getService(id: "1", include: ["text"]) {
        id
        siteid
        type
        code
        label
        provider
        datestart
        dateend
        config
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
    "getService": {
      "id": "1",
      "siteid": "1.",
      "type": "payment",
      "code": "paypalplus",
      "label": "PPPlus",
      "provider": "PaypalPlus",
      "datestart": null,
      "dateend": null,
      "config": "{\\"authorize\\":0,\\"clientid\\":0,\\"secret\\":0,\\"testmode\\":0}",
      "position": "0",
      "status": 1,
      "mtime": "2022-06-08 16:11:10",
      "ctime": "2022-06-08 16:11:10",
      "editor": "aimeos@aimeos.org",
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

# Find service by code

=== "Query"
    ```graphql
    query {
      findService(code: "paypalplus", include: ["text"]) {
        id
        siteid
        type
        code
        label
        provider
        datestart
        dateend
        config
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
      findService(code: "paypalplus", include: ["text"]) {
        id
        siteid
        type
        code
        label
        provider
        datestart
        dateend
        config
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
    "findService": {
      "id": "1",
      "siteid": "1.",
      "type": "payment",
      "code": "paypalplus",
      "label": "PPPlus",
      "provider": "PaypalPlus",
      "datestart": null,
      "dateend": null,
      "config": "{\\"authorize\\":0,\\"clientid\\":0,\\"secret\\":0,\\"testmode\\":0}",
      "position": "0",
      "status": 1,
      "mtime": "2022-06-08 16:11:10",
      "ctime": "2022-06-08 16:11:10",
      "editor": "aimeos@aimeos.org",
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

# Search services

The filter parameter is explained in the [filter section](basics.md#filtering-the-result) of the [GraphQL basics](basics.md) article.

=== "Query"
    ```graphql
    query {
      searchServices(filter: "{\\"=~\\": {\\"service.code\\":\\"demo-\\"}}", include: ["text"]) {
        items {
          id
          siteid
          type
          code
          label
          provider
          datestart
          dateend
          config
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
        "=~": {"service.code":"demo-"}
    };
    const fstr = JSON.stringify(JSON.stringify(filter));
    const body = JSON.stringify({'query':
    `query {
      searchServices(filter: ` + fstr + `, include: ["text"]) {
        items {
          id
          siteid
          type
          code
          label
          provider
          datestart
          dateend
          config
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
    "searchServices": {
      "items": [
        {
          "id": "1",
          "siteid": "1.",
          "type": "delivery",
          "code": "demo-pickup",
          "label": "Click & Collect",
          "provider": "Standard,Time,Supplier",
          "datestart": null,
          "dateend": null,
          "config": "{}",
          "position": 0,
          "status": 1,
          "mtime": "2022-12-01 11:59:07",
          "ctime": "2022-12-01 11:59:07",
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
          "type": "delivery",
          "code": "demo-dhl",
          "label": "DHL",
          "provider": "Standard",
          "datestart": null,
          "dateend": null,
          "config": "{}",
          "position": 1,
          "status": 1,
          "mtime": "2022-12-01 11:59:07",
          "ctime": "2022-12-01 11:59:07",
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

# Fetch service configuration

To retrieve the backend configuration for a service provider and the added decorators use:

=== "Query"
    ```graphql
    query {
      getServiceConfig(provider: "Xml,BasketValues", type: "delivery") {
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
      getServiceConfig(provider: "Xml,BasketValues", type: "delivery") {
        code
        type
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
    "getServiceConfig": [
      {
        "code":"xml.backupdir",
        "type":"string",
        "label":"Relative or absolute path of the backup directory (with date() placeholders)"
      },{
        "code":"xml.exportpath",
        "type":"string",
        "label":"Relative or absolute path and name of the XML files (with date() placeholders)"
      },{
        "code":"xml.template",
        "type":"string",
        "label":"Relative path of the template file name"
      },{
        "code":"xml.updatedir",
        "type":"string",
        "label":"Relative or absolute path and name of the order update XML files"
      },{
        "code":"basketvalues.total-value-min",
        "type":"map",
        "label":"Minimum total value of the basket"
      },{
        "code":"basketvalues.total-value-max",
        "type":"map",
        "label":"Maximum total value of the basket"
      }
    ]
  }
}
```

# Save single service

=== "Mutation"
    ```graphql
    mutation {
      saveService(input: {
        type: "delivery"
        code: "test"
        label: "Test service"
        provider: "Standard",
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
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      saveService(input: {
        type: "delivery"
        code: "test"
        label: "Test service"
        provider: "Standard",
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
    "saveService": {
      "id": "13"
    }
  }
}
```

# Save multiple services

=== "Mutation"
    ```graphql
    mutation {
      saveServices(input: [{
        type: "delivery"
        code: "test-2"
        label: "Test 2 service"
        provider: "Xml",
        lists: {
          text: [{
            item: {
              content: "Test content"
            }
          }]
        }
      },{
        type: "payment"
        code: "test-3"
        label: "Test 3 service"
        provider: "PostPay"
      }]) {
        id
      }
    }
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      saveServices(input: [{
        type: "delivery"
        code: "test-2"
        label: "Test 2 service"
        provider: "Xml",
        lists: {
          text: [{
            item: {
              content: "Test content"
            }
          }]
        }
      },{
        type: "payment"
        code: "test-3"
        label: "Test 3 service"
        provider: "PostPay"
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
    "saveServices": [
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

# Delete single service

=== "Mutation"
    ```graphql
    mutation {
      deleteService(id: "13")
    }
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deleteService(id: "13")
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
    "deleteService": "13"
  }
}
```

# Delete multiple services

=== "Mutation"
    ```graphql
    mutation {
      deleteServices(id: ["14", "15"])
    }
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deleteServices(id: ["14", "15"])
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
    "deleteServices": [
      "14",
      "15"
    ]
  }
}
```

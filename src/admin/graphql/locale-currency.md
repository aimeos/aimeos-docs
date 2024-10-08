This article contains all actions for retrieving and managing currencies.

# Get currency by ID

=== "Query"
    ```graphql
    query {
      getLocaleCurrency(id: "EUR") {
        id
        label
        status
        mtime
        ctime
        editor
      }
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`query {
      getLocaleCurrency(id: "EUR") {
        id
        label
        status
        mtime
        ctime
        editor
      }
    }`).then(data => {
      console.log(data)
    })
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `query {
      getLocaleCurrency(id: "EUR") {
        id
        label
        status
        mtime
        ctime
        editor
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
    "getLocaleCurrency": {
      "id": "EUR",
      "label": "Euro",
      "status": 1,
      "mtime": "2022-05-28 06:26:34",
      "ctime": "2022-05-28 06:26:34",
      "editor": "setup"
    }
  }
}
```

# Search currencies

The filter parameter is explained in the [filter section](basics.md#filtering-the-result) of the [GraphQL basics](basics.md) article.

=== "Query"
    ```graphql
    query {
      searchLocaleCurrencys(filter: "{\\"==\\": {\\"locale.currency.status\\":1}}") {
        items {
          id
          label
          status
          mtime
          ctime
          editor
        }
        total
      }
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`query {
      searchLocaleCurrencys(filter: "{\\"==\\": {\\"locale.currency.status\\":1}}") {
        items {
          id
          label
          status
          mtime
          ctime
          editor
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
        "==": {"locale.currency.status":1}
    };
    const fstr = JSON.stringify(JSON.stringify(filter));
    const body = JSON.stringify({'query':
    `query {
      searchLocaleCurrencys(filter: ` + fstr + `) {
        items {
          id
          label
          status
          mtime
          ctime
          editor
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
    "searchLocaleCurrencys": {
      "items": [
        {
          "id": "EUR",
          "label": "Euro",
          "status": 1,
          "mtime": "2022-05-28 06:26:34",
          "ctime": "2022-05-28 06:26:34",
          "editor": "setup"
        },
        {
          "id": "USD",
          "label": "US dollar",
          "status": 1,
          "mtime": "2022-05-28 06:26:35",
          "ctime": "2022-05-28 06:26:35",
          "editor": "setup"
        }
      ],
      "total": 2
    }
  }
}
```

# Save single currency

=== "Mutation"
    ```graphql
    mutation {
      saveLocaleCurrency(input: {
        code: "XH1"
        label: "Test currency"
      }) {
        id
      }
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`mutation {
      saveLocaleCurrency(input: {
        code: "XH1"
        label: "Test currency"
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
      saveLocaleCurrency(input: {
        code: "XH1"
        label: "Test currency"
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
    "saveLocaleCurrency": {
      "id": "XH1"
    }
  }
}
```

# Save multiple currencies

=== "Mutation"
    ```graphql
    mutation {
      saveLocaleCurrencys(input: [{
        code: "XH2"
        label: "Test currency 2"
      }
      {
        code: "XH3"
        label: "Test currency 3"
      }]) {
        id
      }
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`mutation {
      saveLocaleCurrencys(input: [{
        code: "XH2"
        label: "Test currency 2"
      }
      {
        code: "XH3"
        label: "Test currency 3"
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
      saveLocaleCurrencys(input: [{
        code: "XH2"
        label: "Test currency 2"
      }
      {
        code: "XH3"
        label: "Test currency 3"
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
    "saveLocaleCurrencys": [
      {
        "id": "XH2"
      },
      {
        "id": "XH3"
      }
    ]
  }
}
```

# Delete single currency

=== "Mutation"
    ```graphql
    mutation {
      deleteLocaleCurrency(id: "XH1")
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`mutation {
      deleteLocaleCurrency(id: "XH1")
    }`).then(data => {
      console.log(data)
    })
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deleteLocaleCurrency(id: "XH1")
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
    "deleteLocaleCurrency": "XH1"
  }
}
```

# Delete multiple currencies

=== "Mutation"
    ```graphql
    mutation {
      deleteLocaleCurrencys(id: ["XH2", "XH3"])
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`mutation {
      deleteLocaleCurrencys(id: ["XH2", "XH3"])
    }`).then(data => {
      console.log(data)
    })
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deleteLocaleCurrencys(id: ["XH2", "XH3"])
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
    "deleteLocaleCurrencys": [
      "XH2",
      "XH3"
    ]
  }
}
```

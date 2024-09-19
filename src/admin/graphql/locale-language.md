This article contains all actions for retrieving and managing languages.

# Get language by ID

=== "Query"
    ```graphql
    query {
      getLocaleLanguage(id: "de") {
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
      getLocaleLanguage(id: "de") {
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
      getLocaleLanguage(id: "de") {
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
    "getLocaleLanguage": {
      "id": "de",
      "label": "German",
      "status": 1,
      "mtime": "2022-05-28 06:26:33",
      "ctime": "2022-05-28 06:26:33",
      "editor": "setup"
    }
  }
}
```

# Search languages

The filter parameter is explained in the [filter section](basics.md#filtering-the-result) of the [GraphQL basics](basics.md) article.

=== "Query"
    ```graphql
    query {
      searchLocaleLanguages(filter: "{\\"==\\": {\\"locale.language.status\\":1}}") {
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
      searchLocaleLanguages(filter: "{\\"==\\": {\\"locale.language.status\\":1}}") {
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
        "==": {"locale.language.status":1}
    };
    const fstr = JSON.stringify(JSON.stringify(filter));
    const body = JSON.stringify({'query':
    `query {
      searchLocaleLanguages(filter: ` + fstr + `) {
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
    "searchLocaleLanguages": {
      "items" : [
        {
          "id": "de",
          "label": "German",
          "status": 1,
          "mtime": "2022-05-28 06:26:33",
          "ctime": "2022-05-28 06:26:33",
          "editor": "setup"
        },
        {
          "id": "en",
          "label": "English",
          "status": 1,
          "mtime": "2022-05-28 06:26:33",
          "ctime": "2022-05-28 06:26:33",
          "editor": "setup"
        }
      ],
      "total": 2
    }
  }
}
```

# Save single language

=== "Mutation"
    ```graphql
    mutation {
      saveLocaleLanguage(input: {
        code: "xa"
        label: "Test language"
      }) {
        id
      }
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`mutation {
      saveLocaleLanguage(input: {
        code: "xa"
        label: "Test language"
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
      saveLocaleLanguage(input: {
        code: "xa"
        label: "Test language"
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
    "saveLocaleLanguage": {
      "id": "xa"
    }
  }
}
```

# Save multiple languages

=== "Mutation"
    ```graphql
    mutation {
      saveLocaleLanguages(input: [{
        code: "xb"
        label: "Test language 2"
      }
      {
        code: "xc_US"
        label: "Test language 3"
      }]) {
        id
      }
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`mutation {
      saveLocaleLanguages(input: [{
        code: "xb"
        label: "Test language 2"
      }
      {
        code: "xc_US"
        label: "Test language 3"
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
      saveLocaleLanguages(input: [{
        code: "xb"
        label: "Test language 2"
      }
      {
        code: "xc_US"
        label: "Test language 3"
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
    "saveLocaleLanguages": [
      {
        "id": "xb"
      },
      {
        "id": "xc_US"
      }
    ]
  }
}
```

# Delete single language

=== "Mutation"
    ```graphql
    mutation {
      deleteLocaleLanguage(id: "xa")
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`mutation {
      deleteLocaleLanguage(id: "xa")
    }`).then(data => {
      console.log(data)
    })
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deleteLocaleLanguage(id: "xa")
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
    "deleteLocaleLanguage": "xa"
  }
}
```

# Delete multiple languages

=== "Mutation"
    ```graphql
    mutation {
      deleteLocaleLanguages(id: ["xb", "xc_US"])
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`mutation {
      deleteLocaleLanguages(id: ["xb", "xc_US"])
    }`).then(data => {
      console.log(data)
    })
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deleteLocaleLanguages(id: ["xb", "xc_US"])
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
    "deleteLocaleLanguages": [
      "xb",
      "xc_US"
    ]
  }
}
```

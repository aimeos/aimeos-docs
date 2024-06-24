This article contains all actions for retrieving and managing locales.

# Get locale by ID

=== "Query"
    ```graphql
    query {
      getLocale(id: "1") {
        id
        siteid
        languageid
        currencyid
        position
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
      getLocale(id: "1") {
        id
        siteid
        languageid
        currencyid
        position
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
      getLocale(id: "1") {
        id
        siteid
        languageid
        currencyid
        position
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
    "getLocale": {
      "id": "1",
      "siteid": "1.",
      "languageid": "en",
      "currencyid": "EUR",
      "position": 0,
      "status": 1,
      "mtime": "2022-06-20 15:18:08",
      "ctime": "2022-05-28 06:26:35",
      "editor": "aimeos@aimeos.org"
    }
  }
}
```

# Search locales

The filter parameter is explained in the [filter section](basics.md#filtering-the-result) of the [GraphQL basics](basics.md) article.

=== "Query"
    ```graphql
    query {
      searchLocales(filter: "{\\"==\\": {\\"locale.currencyid\\":\\"EUR\\"}}") {
        items {
          id
          siteid
          languageid
          currencyid
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
=== "JQAdm"
    ```javascript
    Aimeos.query(`query {
      searchLocales(filter: "{\\"==\\": {\\"locale.currencyid\\":\\"EUR\\"}}") {
        items {
          id
          siteid
          languageid
          currencyid
          position
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
        "==": {"locale.currencyid":"EUR"}
    };
    const fstr = JSON.stringify(JSON.stringify(filter));
    const body = JSON.stringify({'query':
    `query {
      searchLocales(filter: ` + fstr + `) {
        items {
          id
          siteid
          languageid
          currencyid
          position
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
    "searchLocales": {
      "items": [
        {
          "id": "1",
          "siteid": "1.",
          "languageid": "en",
          "currencyid": "EUR",
          "position": 0,
          "status": 1,
          "mtime": "2022-06-20 15:18:08",
          "ctime": "2022-05-28 06:26:35",
          "editor": "aimeos@aimeos.org"
        },
        {
          "id": "3",
          "siteid": "1.",
          "languageid": "de",
          "currencyid": "EUR",
          "position": 2,
          "status": 1,
          "mtime": "2022-06-20 15:15:14",
          "ctime": "2022-05-28 06:26:35",
          "editor": "aimeos@aimeos.org"
        }
      ],
      "total": 2
    }
  }
}
```

# Save single locale

=== "Mutation"
    ```graphql
    mutation {
      saveLocale(input: {
        siteid: "1."
        languageid: "fr"
        currencyid: "EUR"
        position: 2
      }) {
        id
      }
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`mutation {
      saveLocale(input: {
        siteid: "1."
        languageid: "fr"
        currencyid: "EUR"
        position: 2
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
      saveLocale(input: {
        siteid: "1."
        languageid: "fr"
        currencyid: "EUR"
        position: 2
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
    "saveLocale": {
      "id": "4"
    }
  }
}
```

# Save multiple locales

=== "Mutation"
    ```graphql
    mutation {
      saveLocales(input: [{
        siteid: "1."
        languageid: "it"
        currencyid: "EUR"
        position: 3
      },{
        siteid: "1."
        languageid: "es"
        currencyid: "EUR"
        position: 4
      }]) {
        id
      }
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`mutation {
      saveLocales(input: [{
        siteid: "1."
        languageid: "it"
        currencyid: "EUR"
        position: 3
      },{
        siteid: "1."
        languageid: "es"
        currencyid: "EUR"
        position: 4
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
      saveLocales(input: [{
        siteid: "1."
        languageid: "it"
        currencyid: "EUR"
        position: 3
      },{
        siteid: "1."
        languageid: "es"
        currencyid: "EUR"
        position: 4
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
    "saveLocales": [
      {
        "id": "5"
      },
      {
        "id": "6"
      }
    ]
  }
}
```

# Delete single locale

=== "Mutation"
    ```graphql
    mutation {
      deleteLocale(id: "3")
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`mutation {
      deleteLocale(id: "3")
    }`).then(data => {
      console.log(data)
    })
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deleteLocale(id: "3")
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
    "deleteLocale": "3"
  }
}
```

# Delete multiple locales

=== "Mutation"
    ```graphql
    mutation {
      deleteLocales(id: ["4", "5"])
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`mutation {
      deleteLocales(id: ["4", "5"])
    }`).then(data => {
      console.log(data)
    })
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deleteLocales(id: ["4", "5"])
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
    "deleteLocales": [
      "4",
      "5"
    ]
  }
}
```

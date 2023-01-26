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
}```

# Search locales

=== "Query"
    ```graphql
    query {
      searchLocales(filter: "{\"==\": {\"locale.currencyid\":\"EUR\"}}") {
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
=== "Javascript"
    ```javascript
    let filter = {
        "==": {"locale.currencyid":"EUR"}
    };
    const fstr = JSON.stringify(filter).replace(/"/g, '\\"');
    const body = JSON.stringify({'query':
    `query {
      searchLocales(filter: "` + fstr + `") {
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
    "searchLocales": [
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
    ]
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
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deleteLocale(id: "3")
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
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deleteLocales(id: ["4", "5"])
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
    "deleteLocales": [
      "4",
      "5"
    ]
  }
}
```

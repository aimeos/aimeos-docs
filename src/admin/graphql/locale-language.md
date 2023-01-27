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

=== "Query"
    ```graphql
    query {
      searchLocaleLanguages(filter: "{\"==\": {\"locale.language.status\":1}}") {
        id
        label
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
        "==": {"locale.language.status":1}
    };
    const fstr = JSON.stringify(filter).replace(/"/g, '\\"');
    const body = JSON.stringify({'query':
    `query {
      searchLocaleLanguages(filter: "` + fstr + `") {
        id
        label
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
    "searchLocaleLanguages": [
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
    ]
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
      },{
        code: "xc_US"
        label: "Test language 3"
      }]) {
        id
      }
    }
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      saveLocaleLanguages(input: [{
        code: "xb"
        label: "Test language 2"
      },{
        code: "xc_US"
        label: "Test language 3"
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
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deleteLocaleLanguage(id: "xa")
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
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deleteLocaleLanguages(id: ["xb", "xc_US"])
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
    "deleteLocaleLanguages": [
      "xb",
      "xc_US"
    ]
  }
}
```

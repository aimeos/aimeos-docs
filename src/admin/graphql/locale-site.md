This article contains all actions for retrieving and managing sites.

# Get site by ID

=== "Query"
    ```graphql
    query {
      getLocaleSite(id: "1") {
        id
        parentid
        code
        level
        label
        config
        status
        icon
        logo
        theme
        refid
        rating
        ratings
        hasChildren
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
      getLocaleSite(id: "1") {
        id
        parentid
        code
        level
        label
        config
        status
        icon
        logo
        theme
        refid
        rating
        ratings
        hasChildren
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
    "getLocaleSite": {
      "id": "1",
      "parentid": "0",
      "code": "default",
      "level": 0,
      "label": "Aimeos",
      "config": "{}",
      "status": 1,
      "icon": "logo.png",
      "logo": "{200: \"logo.svg\"}",
      "theme": "default",
      "refid": "",
      "rating": "5.0",
      "ratings": 1,
      "hasChildren": false,
      "mtime": "2022-05-28 06:26:33",
      "ctime": "2022-05-28 06:26:33",
      "editor": "setup"
    }
  }
}
```

# Search sites

The filter parameter is explained in the [filter section](basics.md#filtering-the-result) of the [GraphQL basics](basics.md) article.

=== "Query"
    ```graphql
    query {
      searchLocaleSites(filter: "{\"==\": {\"locale.site.status\":1}}") {
        id
        parentid
        code
        level
        label
        config
        status
        icon
        logo
        theme
        refid
        rating
        ratings
        hasChildren
        mtime
        ctime
        editor
      }
    }
    ```
=== "Javascript"
    ```javascript
    let filter = {
        "==": {"locale.site.status":1}
    };
    const fstr = JSON.stringify(JSON.stringify(filter));
    const body = JSON.stringify({'query':
    `query {
      searchLocaleSites(filter: ` + fstr + `) {
        id
        parentid
        code
        level
        label
        config
        status
        icon
        logo
        theme
        refid
        rating
        ratings
        hasChildren
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
    "searchLocaleSites": [
      {
        "id": "1",
        "parentid": "0",
        "code": "default",
        "level": 0,
        "label": "Aimeos",
        "config": "{}",
        "status": 1,
        "icon": "logo.png",
        "logo": "{200: \"logo.svg\"}",
        "theme": "default",
        "refid": "",
        "rating": "5.0",
        "ratings": 1,
        "hasChildren": false,
        "mtime": "2022-05-28 06:26:33",
        "ctime": "2022-05-28 06:26:33",
        "editor": "setup"
      },
      {
        "id": "1",
        "parentid": "0",
        "code": "asite",
        "level": 0,
        "label": "Another site",
        "config": "{}",
        "status": 1,
        "icon": "logo.png",
        "logo": "{200: \"logo.svg\"}",
        "theme": "default",
        "refid": "",
        "rating": "0.0",
        "ratings": 0,
        "hasChildren": false,
        "mtime": "2022-05-28 06:26:33",
        "ctime": "2022-05-28 06:26:33",
        "editor": "setup"
      }
    ]
  }
}
```

# Save single site

=== "Mutation"
    ```graphql
    mutation {
      saveLocaleSite(input: {
        id: "1"
        label: "My site"
      }) {
        id
      }
    }
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      saveLocaleSite(input: {
        id: "1"
        label: "My site"
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
    "saveLocaleSite": {
      "id": "1"
    }
  }
}
```

# Save multiple sites

=== "Mutation"
    ```graphql
    mutation {
      saveLocaleSites(input: [{
        id: "1"
        label: "My site"
      },{
        id: "2"
        label: "Your site"
      }]) {
        id
      }
    }
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      saveLocaleSites(input: [{
        id: 1
        label: "My site"
      },{
        id: 2
        label: "Your site"
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
    "saveLocaleSites": [
      {
        "id": "1"
      },
      {
        "id": "2"
      }
    ]
  }
}
```

# Delete single site

=== "Mutation"
    ```graphql
    mutation {
      deleteLocaleSite(id: "1")
    }
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deleteLocaleSite(id: "1")
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
    "deleteLocaleSite": "1"
  }
}
```

# Delete multiple sites

=== "Mutation"
    ```graphql
    mutation {
      deleteLocaleSites(id: ["1", "2"])
    }
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deleteLocaleSites(id: ["1", "2"])
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
    "deleteLocaleSites": [
      "1",
      "2"
    ]
  }
}
```

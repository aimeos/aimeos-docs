This article contains all actions for retrieving and managing texts.

# Get text by ID

=== "Query"
    ```graphql
    query {
      getText(id: "1") {
        id
        siteid
        type
        domain
        languageid
        label
        content
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
      getText(id: "1") {
        id
        siteid
        type
        domain
        languageid
        label
        content
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
    "getText": {
      "id": "1",
      "siteid": "1.",
      "type": "short",
      "domain": "catalog",
      "languageid": "en",
      "label": "Best seller short",
      "content": "<p>LARGE selection of TOP sellers<br /><strong>BEST prices guaranteed</strong></p>",
      "status": 1,
      "mtime": "2022-05-28 06:26:35",
      "ctime": "2022-05-28 06:26:35",
      "editor": "core:setup"
    }
  }
}
```

# Search texts

=== "Query"
    ```graphql
    query {
      searchTexts(filter: "{\"=~\": {\"text.label\":\"Demo\"}}") {
        id
        siteid
        type
        domain
        languageid
        label
        content
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
        "=~": {"text.label":"Demo"}
    };
    const fstr = JSON.stringify(filter).replace(/"/g, '\\"');
    const body = JSON.stringify({'query':
    `query {
      searchTexts(filter: "` + fstr + `") {
        id
        siteid
        type
        domain
        languageid
        label
        content
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
    "searchTexts": [
      {
        "id": "21",
        "siteid": "1.",
        "type": "name",
        "domain": "supplier",
        "languageid": "en",
        "label": "Demo name/en: Demo supplier",
        "content": "Demo supplier",
        "status": 1,
        "mtime": "2022-05-28 06:26:38",
        "ctime": "2022-05-28 06:26:38",
        "editor": "core:setup"
      },
      {
        "id": "22",
        "siteid": "1.",
        "type": "short",
        "domain": "supplier",
        "languageid": "en",
        "label": "Demo short/en: This is the short description",
        "content": "This is the short description of the demo supplier.",
        "status": 1,
        "mtime": "2022-05-28 06:26:38",
        "ctime": "2022-05-28 06:26:38",
        "editor": "core:setup"
      }
    ]
  }
}
```

# Save single text

=== "Mutation"
    ```graphql
    mutation {
      saveText(input: {
        type: "long"
        domain: "product"
        label: "Test text"
        languageid: "en"
        content: "This is a long product description."
      }) {
        id
      }
    }
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      saveText(input: {
        type: "long"
        domain: "product"
        label: "Test text"
        languageid: "en"
        content: "This is a long product description."
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
    "saveText": {
      "id": "120"
    }
  }
}
```

# Save multiple texts

=== "Mutation"
    ```graphql
    mutation {
      saveTexts(input: [{
        type: "short"
        domain: "catalog"
        label: "Test catalog text"
        languageid: "en"
        content: "This is a short category text."
      },{
        type: "name"
        domain: "product"
        label: "Test product name"
        languageid: "en"
        content: "This is a product name"
      }]) {
        id
      }
    }
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      saveTexts(input: [{
        type: "short"
        domain: "catalog"
        label: "Test catalog text"
        languageid: "en"
        content: "This is a short category text."
      },{
        type: "name"
        domain: "product"
        label: "Test product name"
        languageid: "en"
        content: "This is a product name"
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
    "saveTexts": [
      {
        "id": "121"
      },
      {
        "id": "122"
      }
    ]
  }
}
```

# Delete single text

=== "Mutation"
    ```graphql
    mutation {
      deleteText(id: "120")
    }
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deleteText(id: "120")
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
    "deleteText": "120"
  }
}
```

# Delete multiple texts

=== "Mutation"
    ```graphql
    mutation {
      deleteTexts(id: ["121", "122"])
    }
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deleteTexts(id: ["121", "122"])
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
    "deleteTexts": [
      "121",
      "122"
    ]
  }
}
```

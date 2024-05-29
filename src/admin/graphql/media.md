This article contains all actions for retrieving and managing media.

!!! tip
    The media domain supports [fetching related resources](basics.md#include-related-resources).

# Get media by ID

=== "Query"
    ```graphql
    query {
      getMedia(id: "1", include: ["group"]) {
        id
        siteid
        type
        label
        domain
        languageid
        mimetype
        url
        previews
        filesystem
        status
        mtime
        ctime
        editor
        lists {
          group {
            id
            item {
              id
              code
            }
          }
        }
        property {
          id
          type
          languageid
          value
        }
      }
    }
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `query {
      getMedia(id: "1", include: ["group"]) {
        id
        siteid
        type
        label
        domain
        languageid
        mimetype
        url
        previews
        filesystem
        status
        mtime
        ctime
        editor
        lists {
          group {
            id
            item {
              id
              code
            }
          }
        }
        property {
          id
          type
          languageid
          value
        }
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
    "getMedia": {
      "id": "1",
      "siteid": "1.",
      "type": "default",
      "label": "Demo: Article 1.webp",
      "domain": "product",
      "languageid": null,
      "mimetype": "image/webp",
      "url": "https://aimeos.org/media/default/product_01_A-big.webp",
      "previews": "{\\"240\\":\\"https:\\/\\/aimeos.org\\/media\\/default\\/product_01_A-low.webp\\",\\"720\\":\\"https:\\/\\/aimeos.org\\/media\\/default\\/product_01_A-med.webp\\",\\"1350\\":\\"https:\\/\\/aimeos.org\\/media\\/default\\/product_01_A-big.webp\\"}",
      "filesystem": "fs-media",
      "status": 1,
      "mtime": "2022-12-01 11:59:05",
      "ctime": "2022-12-01 11:59:05",
      "editor": "core",
      "lists": {
        "group": [{
          "id": "10",
          "item": {
            "id": "2",
            "code": "wholesale"
          }
        }]
      },
      "property": [{
        "id": "1",
        "type": "title",
        "languageid": "en",
        "value": "Demo article"
      }]
    }
  }
}
```

# Search media

The filter parameter is explained in the [filter section](basics.md#filtering-the-result) of the [GraphQL basics](basics.md) article.

=== "Query"
    ```graphql
    query {
      searchMedias(filter: "{\\"=~\\": {\\"media.code\\":\\"demo-\\"}}", include: ["group"]) {
        items {
          id
          siteid
          type
          label
          domain
          languageid
          mimetype
          url
          previews
          filesystem
          status
          mtime
          ctime
          editor
          lists {
            group {
              id
              item {
                id
                code
              }
            }
          }
          property {
            id
            type
            languageid
            value
          }
        }
        total
      }
    }
    ```
=== "Javascript"
    ```javascript
    let filter = {
        "=~": {"media.code":"demo-"}
    };
    const fstr = JSON.stringify(JSON.stringify(filter));
    const body = JSON.stringify({'query':
    `query {
      searchMedias(filter: ` + fstr + `, include: ["group"]) {
        items {
          id
          siteid
          type
          label
          domain
          languageid
          mimetype
          url
          previews
          filesystem
          status
          mtime
          ctime
          editor
          lists {
            group {
              id
              item {
                id
                code
              }
            }
          }
          property {
            id
            type
            languageid
            value
          }
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
    "searchMedias": {
      "items": [
        {
          "id": "1",
          "siteid": "1.",
          "type": "default",
          "label": "Demo: Article 1.jpg",
          "domain": "supplier",
          "languageid": null,
          "mimetype": "image/jpeg",
          "url": "https://aimeos.org/media/default/logo-1.png",
          "previews": "{\\"240\\":\\"https:\\/\\/aimeos.org\\/media\\/default\\/logo-1.png\\"}",
          "filesystem": "fs-media",
          "status": 1,
          "mtime": "2022-05-28 06:26:38",
          "ctime": "2022-05-28 06:26:38",
          "editor": "core:setup",
          "lists": {
            "group": [{
              "id": "10",
              "item": {
                "id": "2",
                "code": "wholesale"
              }
            }]
          },
          "property": [{
            "id": "1",
            "type": "title",
            "languageid": "en",
            "value": "Demo article"
          }]
        },
        {
          "id": "20",
          "siteid": "1.",
          "type": "stage",
          "label": "Demo: Best seller stage",
          "domain": "catalog",
          "languageid": "de",
          "mimetype": "image/webp",
          "url": "https://aimeos.org/media/default/main-banner-1-big.webp",
          "previews": "{\\"480\\":\\"https:\\/\\/aimeos.org\\/media\\/default\\/main-banner-1-low.webp\\",\\"960\\":\\"https:\\/\\/aimeos.org\\/media\\/default\\/main-banner-1-med.webp\\",\\"1920\\":\\"https:\\/\\/aimeos.org\\/media\\/default\\/main-banner-1-big.webp\\"}",
          "filesystem": "fs-media",
          "status": 1,
          "mtime": "2022-12-01 11:59:02",
          "ctime": "2022-12-01 11:59:02",
          "editor": "core",
          "lists": {
            "group": []
          },
          "property": []
        }
      ],
      "total": 2
    }
  }
}
```

# Save single media

=== "Mutation"
    ```graphql
    mutation {
      saveMedia(input: {
        domain: "product",
        type: "default",
        label: "Test image",
        url: "https://myshop.com/images/test.jpg",
        lists: {
          group: [{
            refid: "2"
          }]
        },
        property: [{
          type: "title",
          languageid: "en",
          value: "Demo article"
        }]
      }) {
        id
      }
    }
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      saveMedia(input: {
        domain: "product",
        type: "default",
        label: "Test image",
        url: "https://myshop.com/images/test.jpg",
        lists: {
          group: [{
            refid: "2"
          }]
        },
        property: [{
          type: "title",
          languageid: "en",
          value: "Demo article"
        }]
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
    "saveMedia": {
      "id": "21"
    }
  }
}
```

# Save multiple media

=== "Mutation"
    ```graphql
    mutation {
      saveMedias(input: [{
        domain: "product",
        type: "default",
        label: "Test 2 image",
        url: "https://myshop.com/images/test2.jpg",
        lists: {
          group: [{
            refid: "2"
          }]
        },
        property: [{
          type: "title",
          languageid: "en",
          value: "Demo article"
        }]
      },{
        domain: "catalog",
        type: "stage",
        label: "Test 3 image",
        url: "https://myshop.com/images/test3.jpg",
      }]) {
        id
      }
    }
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      saveMedias(input: [{
        domain: "product",
        type: "default",
        label: "Test 2 image",
        url: "https://myshop.com/images/test2.jpg",
        lists: {
          group: [{
            refid: "2"
          }]
        },
        property: [{
          type: "title",
          languageid: "en",
          value: "Demo article"
        }]
      },{
        domain: "catalog",
        type: "stage",
        label: "Test 3 image",
        url: "https://myshop.com/images/test3.jpg"
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
    "saveMedias": [
      {
        "id": "22"
      },
      {
        "id": "23"
      }
    ]
  }
}
```

# Delete single media

=== "Mutation"
    ```graphql
    mutation {
      deleteMedia(id: "20")
    }
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deleteMedia(id: "20")
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
    "deleteMedia": "20"
  }
}
```

# Delete multiple media

=== "Mutation"
    ```graphql
    mutation {
      deleteMedias(id: ["21", "22"])
    }
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deleteMedias(id: ["21", "22"])
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
    "deleteMedias": [
      "21",
      "22"
    ]
  }
}
```

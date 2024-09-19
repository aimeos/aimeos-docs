This article contains all actions for retrieving and managing reviews.

# Get review by ID

=== "Query"
    ```graphql
    query {
      getReview(id: "1") {
        id
        siteid
        customerid
        orderproductid
        domain
        refid
        name
        comment
        response
        rating
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
      getReview(id: "1") {
        id
        siteid
        customerid
        orderproductid
        domain
        refid
        name
        comment
        response
        rating
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
      getReview(id: "1") {
        id
        siteid
        customerid
        orderproductid
        domain
        refid
        name
        comment
        response
        rating
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
    "getReview": {
      "id": "13",
      "siteid": "1.",
      "customerid": "6",
      "orderproductid": "7",
      "domain": "product",
      "refid": "52",
      "name": "test",
      "comment": "",
      "response": "",
      "rating": 1,
      "status": -1,
      "mtime": "2022-08-22 11:42:22",
      "ctime": "2022-08-22 11:42:22",
      "editor": "aimeos@aimeos.org"
    }
  }
}
```

# Search reviews

The filter parameter is explained in the [filter section](basics.md#filtering-the-result) of the [GraphQL basics](basics.md) article.

=== "Query"
    ```graphql
    query {
      searchReviews(filter: "{\\"=~\\": {\\"review.code\\":\\"demo-\\"}}") {
        items {
          id
          siteid
          customerid
          orderproductid
          domain
          refid
          name
          comment
          response
          rating
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
      searchReviews(filter: "{\\"=~\\": {\\"review.code\\":\\"demo-\\"}}") {
        items {
          id
          siteid
          customerid
          orderproductid
          domain
          refid
          name
          comment
          response
          rating
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
        "=~": {"review.code":"demo-"}
    };
    const fstr = JSON.stringify(JSON.stringify(filter));
    const body = JSON.stringify({'query':
    `query {
      searchReviews(filter: ` + fstr + `) {
        items {
          id
          siteid
          customerid
          orderproductid
          domain
          refid
          name
          comment
          response
          rating
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
    "searchReviews": {
      "items": [
        {
          "id": "13",
          "siteid": "1.",
          "customerid": "6",
          "orderproductid": "7",
          "domain": "product",
          "refid": "52",
          "name": "test",
          "comment": "",
          "response": "",
          "rating": 1,
          "status": -1,
          "mtime": "2022-08-22 11:42:22",
          "ctime": "2022-08-22 11:42:22",
          "editor": "aimeos@aimeos.org"
        }
      ],
      "total": 1
    }
  }
}
```

# Save single review

=== "Mutation"
    ```graphql
    mutation {
      saveReview(input: {
        id: "1"
        status: 1
        response: "Thanks a lot!"
      }) {
        id
      }
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`mutation {
      saveReview(input: {
        id: "1"
        status: 1
        response: "Thanks a lot!"
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
      saveReview(input: {
        id: "1"
        status: 1
        response: "Thanks a lot!"
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
    "saveReview": {
      "id": "1"
    }
  }
}
```

# Save multiple reviews

=== "Mutation"
    ```graphql
    mutation {
      saveReviews(input: [{
        id: "1"
        status: 1
        response: "Thanks a lot too!"
      }
      {
        id: "2"
        status: 0
      }]) {
        id
      }
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`mutation {
      saveReviews(input: [{
        id: "1"
        status: 1
        response: "Thanks a lot too!"
      }
      {
        id: "2"
        status: 0
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
      saveReviews(input: [{
        id: "1"
        status: 1
        response: "Thanks a lot too!"
      }
      {
        id: "2"
        status: 0
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
    "saveReviews": [
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

# Delete single review

=== "Mutation"
    ```graphql
    mutation {
      deleteReview(id: "2")
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`mutation {
      deleteReview(id: "2")
    }`).then(data => {
      console.log(data)
    })
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deleteReview(id: "2")
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
    "deleteReview": "2"
  }
}
```

# Delete multiple reviews

=== "Mutation"
    ```graphql
    mutation {
      deleteReviews(id: ["1", "2"])
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`mutation {
      deleteReviews(id: ["1", "2"])
    }`).then(data => {
      console.log(data)
    })
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deleteReviews(id: ["1", "2"])
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
    "deleteReviews": [
      "1",
      "2"
    ]
  }
}
```

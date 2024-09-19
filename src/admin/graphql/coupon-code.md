This article contains all actions for retrieving and managing coupon codes.

# Get coupon by ID

=== "Query"
    ```graphql
    query {
      getCouponCode(id: "1") {
        id
        siteid
        parentid
        code
        count
        dateend
        datestart
        ref
        mtime
        ctime
        editor
      }
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`query {
      getCouponCode(id: "1") {
        id
        siteid
        parentid
        code
        count
        dateend
        datestart
        ref
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
      getCouponCode(id: "1") {
        id
        siteid
        parentid
        code
        count
        dateend
        datestart
        ref
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
    "getCouponCode": {
      "id": "32",
      "siteid": "1.",
      "parentid": 38,
      "code": "fixed",
      "count": "1000",
      "dateend": null,
      "datestart": null,
      "ref": "",
      "mtime": "2022-12-01 11:59:03",
      "ctime": "2022-12-01 11:59:03",
      "editor": "core"
    }
  }
}
```

# Search coupon codes

The filter parameter is explained in the [filter section](basics.md#filtering-the-result) of the [GraphQL basics](basics.md) article.

=== "Query"
    ```graphql
    query {
      searchCouponCodes(filter: "{\\"==\\": {\\"coupon.code.count\\":1000}}") {
        items {
          id
          siteid
          parentid
          code
          count
          dateend
          datestart
          ref
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
    let filter = {
        "==": {"coupon.code.count":1000}
    };
    const fstr = JSON.stringify(JSON.stringify(filter));
    Aimeos.query(`query {
      searchCouponCodes(filter: ` + fstr + `) {
        items {
          id
          siteid
          parentid
          code
          count
          dateend
          datestart
          ref
          mtime
          ctime
          editor
        }
        total
    }`).then(data => {
      console.log(data)
    })
    ```
=== "Javascript"
    ```javascript
    let filter = {
        "==": {"coupon.code.count":1000}
    };
    const fstr = JSON.stringify(JSON.stringify(filter));
    const body = JSON.stringify({'query':
    `query {
      searchCouponCodes(filter: ` + fstr + `) {
        items {
          id
          siteid
          parentid
          code
          count
          dateend
          datestart
          ref
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
    "searchCouponCodes": {
      "items": [
        {
          "id": "32",
          "siteid": "1.",
          "parentid": 38,
          "code": "fixed",
          "count": "1000",
          "dateend": null,
          "datestart": null,
          "ref": "",
          "mtime": "2022-12-01 11:59:03",
          "ctime": "2022-12-01 11:59:03",
          "editor": "core"
        },
        {
          "id": "33",
          "siteid": "1.",
          "parentid": 39,
          "code": "percent",
          "count": "1000",
          "dateend": null,
          "datestart": null,
          "ref": "",
          "mtime": "2022-12-01 11:59:03",
          "ctime": "2022-12-01 11:59:03",
          "editor": "core"
        }
      ],
      "total": 2
    }
  }
}
```

# Save single coupon

=== "Mutation"
    ```graphql
    mutation {
      saveCouponCode(input: {
        parentid: 1
        code: "TEST"
        count: 1
      }) {
        id
      }
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`mutation {
      saveCouponCode(input: {
        parentid: 1
        code: "TEST"
        count: 1
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
      saveCouponCode(input: {
        parentid: 1
        code: "TEST"
        count: 1
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
    "saveCouponCode": {
      "id": "3"
    }
  }
}
```

# Save multiple coupon codes

=== "Mutation"
    ```graphql
    mutation {
      saveCouponCodes(input: [{
        parentid: 2
        code: "TEST2"
        count: 10
      }
      {
        parentid: 12
        code: "TEST3"
        count: null
      }]) {
        id
      }
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`mutation {
      saveCouponCodes(input: [{
        parentid: 2
        code: "TEST2"
        count: 10
      }
      {
        parentid: 12
        code: "TEST3"
        count: null
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
      saveCouponCodes(input: [{
        parentid: 2
        code: "TEST2"
        count: 10
      }
      {
        parentid: 12
        code: "TEST3"
        count: null
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
    "saveCouponCodes": [
      {
        "id": "4"
      },
      {
        "id": "5"
      }
    ]
  }
}
```

# Delete single coupon

=== "Mutation"
    ```graphql
    mutation {
      deleteCouponCode(id: "3")
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`mutation {
      deleteCouponCode(id: "3")
    }`).then(data => {
      console.log(data)
    })
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deleteCouponCode(id: "3")
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
    "deleteCouponCode": "3"
  }
}
```

# Delete multiple coupon codes

=== "Mutation"
    ```graphql
    mutation {
      deleteCouponCodes(id: ["4", "5"])
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`mutation {
      deleteCouponCodes(id: ["4", "5"])
    }`).then(data => {
      console.log(data)
    })
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deleteCouponCodes(id: ["4", "5"])
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
    "deleteCouponCodes": [
      "4",
      "5"
    ]
  }
}
```

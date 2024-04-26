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
      searchCouponCodes(filter: "{\"==\": {\"coupon.code.count\":1000}}") {
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
      },{
        parentid: 12
        code: "TEST3"
        count: null
      }]) {
        id
      }
    }
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      saveCouponCodes(input: [{
        parentid: 2
        code: "TEST2"
        count: 10
      },{
        parentid: 12
        code: "TEST3"
        count: null
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
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deleteCouponCode(id: "3")
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
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deleteCouponCodes(id: ["4", "5"])
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
    "deleteCouponCodes": [
      "4",
      "5"
    ]
  }
}
```

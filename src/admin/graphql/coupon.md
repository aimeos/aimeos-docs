This article contains all actions for retrieving and managing coupons.

# Get coupon by ID

=== "Query"
    ```graphql
    query {
      getCoupon(id: "1") {
        id
        siteid
        label
        provider
        config
        datestart
        dateend
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
      getCoupon(id: "1") {
        id
        siteid
        label
        provider
        config
        datestart
        dateend
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
    "getCoupon": {
      "id": "1",
      "siteid": "1.",
      "label": "demo-voucher",
      "provider": "Voucher",
      "config": "{\"voucher.productcode\":\"demo-rebate\"}",
      "datestart": null,
      "dateend": null,
      "status": 1,
      "mtime": "2022-12-01 11:59:03",
      "ctime": "2022-12-01 11:59:03",
      "editor": "core"
    }
  }
}
```

# Search coupons

The filter parameter is explained in the [filter section](basics.md#filtering-the-result) of the [GraphQL basics](basics.md) article.

=== "Query"
    ```graphql
    query {
      searchCoupons(filter: "{\"~=\": {\"coupon.label\":\"demo\"}}") {
        id
        siteid
        label
        provider
        config
        datestart
        dateend
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
        "~=": {"coupon.label":"demo"}
    };
    const fstr = JSON.stringify(filter).replace(/"/g, '\\"');
    const body = JSON.stringify({'query':
    `query {
      searchCoupons(filter: "` + fstr + `") {
        id
        siteid
        label
        provider
        config
        datestart
        dateend
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
    "searchCoupons": [
      {
        "id": "1",
        "siteid": "1.",
        "label": "demo-voucher",
        "provider": "Voucher",
        "config": "{\"voucher.productcode\":\"demo-rebate\"}",
        "datestart": null,
        "dateend": null,
        "status": 1,
        "mtime": "2022-12-01 11:59:03",
        "ctime": "2022-12-01 11:59:03",
        "editor": "core"
      },
      {
        "id": "2",
        "siteid": "1.",
        "label": "demo-percent",
        "provider": "PercentRebate",
        "config": "{\"percentrebate.productcode\":\"demo-rebate\",\"percentrebate.rebate\":\"10\"}",
        "datestart": null,
        "dateend": null,
        "status": 1,
        "mtime": "2022-12-01 11:59:03",
        "ctime": "2022-12-01 11:59:03",
        "editor": "core"
      }
    ]
  }
}
```

# Save single coupon

=== "Mutation"
    ```graphql
    mutation {
      saveCoupon(input: {
        label: "Test coupon"
        provider: "PercentRebate"
        config: "{\"percentrebate.productcode\":\"demo-rebate\",\"percentrebate.rebate\":\"25\"}",
      }) {
        id
      }
    }
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      saveCoupon(input: {
        label: "Test coupon"
        provider: "PercentRebate"
        config: "{\"percentrebate.productcode\":\"demo-rebate\",\"percentrebate.rebate\":\"25\"}",
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
    "saveCoupon": {
      "id": "4"
    }
  }
}
```

# Save multiple coupons

=== "Mutation"
    ```graphql
    mutation {
      saveCoupons(input: [{
        label: "Test coupon 2"
        provider: "PercentRebate"
        config: "{\"percentrebate.productcode\":\"demo-rebate\",\"percentrebate.rebate\":\"7.5\"}",
      },{
        label: "Test coupon 3"
        provider: "FixedRebate,BasketValues"
        config: "{\"fixedrebate.productcode\":\"demo-rebate\",\"fixedrebate.rebate\":{\"EUR\":"10.00"},\"basket.total-value-min\":{\"EUR\":100}}",,
      }]) {
        id
      }
    }
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      saveCoupons(input: [{
        label: "Test coupon 2"
        provider: "PercentRebate"
        config: "{\"percentrebate.productcode\":\"demo-rebate\",\"percentrebate.rebate\":\"7.5\"}",
      },{
        label: "Test coupon 3"
        provider: "FixedRebate,BasketValues"
        config: "{\"fixedrebate.productcode\":\"demo-rebate\",\"fixedrebate.rebate\":{\"EUR\":"10.00"},\"basket.total-value-min\":{\"EUR\":100}}",
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
    "saveCoupons": [
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

# Delete single coupon

=== "Mutation"
    ```graphql
    mutation {
      deleteCoupon(id: "4")
    }
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deleteCoupon(id: "4")
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
    "deleteCoupon": "4"
  }
}
```

# Delete multiple coupons

=== "Mutation"
    ```graphql
    mutation {
      deleteCoupons(id: ["5", "6"])
    }
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deleteCoupons(id: ["5", "6"])
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
    "deleteCoupons": [
      "5",
      "6"
    ]
  }
}
```

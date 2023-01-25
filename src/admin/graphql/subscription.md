This article contains all actions for retrieving and managing subscriptions.

# Get subscription by ID

=== "Query"
    ```graphql
    query {
      getSubscription(id: "1") {
        id
        siteid
        orderid
        ordprodid
        productid
        datenext
        dateend
        interval
        reason
        period
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
      getSubscription(id: "1") {
        id
        siteid
        orderid
        ordprodid
        productid
        datenext
        dateend
        interval
        reason
        period
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
    "getSubscription": {
      "id": "1",
      "siteid": "1.",
      "orderid": 1,
      "ordprodid": 1,
      "productid": "1",
      "datenext": "2022-06-12",
      "dateend": "2022-06-13",
      "interval": "P1M",
      "reason": -1,
      "period": 1,
      "status": 0,
      "mtime": "2022-06-15 08:27:50",
      "ctime": "2022-06-13 08:37:19",
      "editor": "aimeos@aimeos.org"
    }
  }
}
```

# Search subscriptions

=== "Query"
    ```graphql
    query {
      searchSubscriptions(filter: "{\"==\": {\"subscription.period\":1}}") {
        id
        siteid
        orderid
        ordprodid
        productid
        datenext
        dateend
        interval
        reason
        period
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
        "==": {"subscription.period":1}
    };
    const fstr = JSON.stringify(filter).replace(/"/g, '\\"');
    const body = JSON.stringify({'query':
    `query {
      searchSubscriptions(filter: "` + fstr + `") {
        id
        siteid
        orderid
        ordprodid
        productid
        datenext
        dateend
        interval
        reason
        period
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
    "searchSubscriptions": [
      {
        "id": "1",
        "siteid": "1.",
        "orderid": 1,
        "ordprodid": 1,
        "productid": "1",
        "datenext": "2022-06-12",
        "dateend": "2022-06-13",
        "interval": "P1M",
        "reason": -1,
        "period": 1,
        "status": 0,
        "mtime": "2022-06-15 08:27:50",
        "ctime": "2022-06-13 08:37:19",
        "editor": "aimeos@aimeos.org"
      },
      {
        "id": "2",
        "siteid": "1.",
        "orderid": 2,
        "ordprodid": 3,
        "productid": "2",
        "datenext": null,
        "dateend": null,
        "interval": "P0Y1M0W0D",
        "reason": null,
        "period": 1,
        "status": 1,
        "mtime": "2022-08-03 11:58:34",
        "ctime": "2022-08-03 11:58:34",
        "editor": "aimeos@aimeos.org"
      }
    ]
  }
}
```

# Save single subscription

=== "Mutation"
    ```graphql
    mutation {
      saveSubscription(input: {
        orderid: 1
        ordprodid: 1
        productid: "1"
        interval: "P1Y"
      }) {
        id
      }
    }
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      saveSubscription(input: {
        orderid: 1
        ordprodid: 1
        productid: "1"
        interval: "P1Y"
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
    "saveSubscription": {
      "id": "3"
    }
  }
}
```

# Save multiple subscriptions

=== "Mutation"
    ```graphql
    mutation {
      saveSubscriptions(input: [{
        orderid: 2
        ordprodid: 3
        productid: "2"
        interval: "P30D"
      },{
        orderid: 3
        ordprodid: 5
        productid: "3"
        interval: "P1M"
      }]) {
        id
      }
    }
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      saveSubscriptions(input: [{
        orderid: 2
        ordprodid: 3
        productid: "2"
        interval: "P30D"
      },{
        orderid: 3
        ordprodid: 5
        productid: "3"
        interval: "P1M"
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
    "saveSubscriptions": [
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

# Delete single subscription

=== "Mutation"
    ```graphql
    mutation {
      deleteSubscription(id: "3")
    }
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deleteSubscription(id: "3")
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
    "deleteSubscription": "3"
  }
}
```

# Delete multiple subscriptions

=== "Mutation"
    ```graphql
    mutation {
      deleteSubscriptions(id: ["4", "5"])
    }
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deleteSubscriptions(id: ["4", "5"])
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
    "deleteSubscriptions": [
      "4",
      "5"
    ]
  }
}
```

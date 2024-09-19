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
=== "JQAdm"
    ```javascript
    Aimeos.query(`query {
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
    }`).then(data => {
      console.log(data)
    })
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

The filter parameter is explained in the [filter section](basics.md#filtering-the-result) of the [GraphQL basics](basics.md) article.

=== "Query"
    ```graphql
    query {
      searchSubscriptions(filter: "{\\"==\\": {\\"subscription.period\\":1}}") {
        items {
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
        total
      }
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`query {
      searchSubscriptions(filter: "{\\"==\\": {\\"subscription.period\\":1}}") {
        items {
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
        total
      }
    }`).then(data => {
      console.log(data)
    })
    ```
=== "Javascript"
    ```javascript
    let filter = {
        "==": {"subscription.period":1}
    };
    const fstr = JSON.stringify(JSON.stringify(filter));
    const body = JSON.stringify({'query':
    `query {
      searchSubscriptions(filter: ` + fstr + `) {
        items {
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
    "searchSubscriptions": {
      "items": [
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
      ],
      "total": 2
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
=== "JQAdm"
    ```javascript
    Aimeos.query(`mutation {
      saveSubscription(input: {
        orderid: 1
        ordprodid: 1
        productid: "1"
        interval: "P1Y"
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
      saveSubscription(input: {
        orderid: 1
        ordprodid: 1
        productid: "1"
        interval: "P1Y"
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
      }
      {
        orderid: 3
        ordprodid: 5
        productid: "3"
        interval: "P1M"
      }]) {
        id
      }
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`mutation {
      saveSubscriptions(input: [{
        orderid: 2
        ordprodid: 3
        productid: "2"
        interval: "P30D"
      }
      {
        orderid: 3
        ordprodid: 5
        productid: "3"
        interval: "P1M"
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
      saveSubscriptions(input: [{
        orderid: 2
        ordprodid: 3
        productid: "2"
        interval: "P30D"
      }
      {
        orderid: 3
        ordprodid: 5
        productid: "3"
        interval: "P1M"
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
=== "JQAdm"
    ```javascript
    Aimeos.query(`mutation {
      deleteSubscription(id: "3")
    }`).then(data => {
      console.log(data)
    })
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deleteSubscription(id: "3")
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
=== "JQAdm"
    ```javascript
    Aimeos.query(`mutation {
      deleteSubscriptions(id: ["4", "5"])
    }`).then(data => {
      console.log(data)
    })
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deleteSubscriptions(id: ["4", "5"])
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
    "deleteSubscriptions": [
      "4",
      "5"
    ]
  }
}
```

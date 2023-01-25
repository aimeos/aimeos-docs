This article contains all actions for retrieving and managing orders.

# Get order by ID

=== "Query"
    ```graphql
    query {
      getOrder(id: "1") {
        id
        siteid
        baseid
        invoiceno
        relatedid
        channel
        datepayment
        datedelivery
        statusdelivery
        statuspayment
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
      getOrder(id: "1") {
        id
        siteid
        baseid
        invoiceno
        relatedid
        channel
        datepayment
        datedelivery
        statusdelivery
        statuspayment
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
    "getOrder": {
      "id": "1",
      "siteid": "1.",
      "baseid": 1,
      "invoiceno": "",
      "relatedid": "123",
      "channel": "web",
      "datepayment": "2022-06-12 00:00:00",
      "datedelivery": "2022-06-13 00:00:00",
      "statusdelivery": 0,
      "statuspayment": 1,
      "mtime": "2022-06-13 09:03:50",
      "ctime": "2022-06-01 08:55:25",
      "editor": "aimeos@aimeos.org"
    }
  }
}
```

# Search orders

=== "Query"
    ```graphql
    query {
      searchOrders(filter: "{\"==\": {\"order.channel\":\"web\"}}") {
        id
        siteid
        baseid
        invoiceno
        relatedid
        channel
        datepayment
        datedelivery
        statusdelivery
        statuspayment
        mtime
        ctime
        editor
      }
    }
    ```
=== "Javascript"
    ```javascript
    let filter = {
        "==": {"order.channel":"web"}
    };
    const fstr = JSON.stringify(filter).replace(/"/g, '\\"');
    const body = JSON.stringify({'query':
    `query {
      searchOrders(filter: "` + fstr + `") {
        id
        siteid
        baseid
        invoiceno
        relatedid
        channel
        datepayment
        datedelivery
        statusdelivery
        statuspayment
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
    "searchOrders": [
{
  "data": {
    "searchOrders": [
      {
        "id": "2",
        "siteid": "1.",
        "baseid": 2,
        "invoiceno": "INV-1002",
        "relatedid": "",
        "channel": "web",
        "datepayment": null,
        "datedelivery": null,
        "statusdelivery": -1,
        "statuspayment": -1,
        "mtime": "2022-12-05 15:21:21",
        "ctime": "2022-12-05 15:21:21",
        "editor": "aimeos@aimeos.org"
      },
      {
        "id": "3",
        "siteid": "1.",
        "baseid": 3,
        "invoiceno": "INV-1003",
        "relatedid": "",
        "channel": "web",
        "datepayment": "2022-12-05 18:25:28",
        "datedelivery": null,
        "statusdelivery": -1,
        "statuspayment": 5,
        "mtime": "2022-12-05 18:25:28",
        "ctime": "2022-12-05 18:25:28",
        "editor": "aimeos@aimeos.org"
      }
    ]
  }
}
```

# Save single order

=== "Mutation"
    ```graphql
    mutation {
      saveOrder(input: {
        baseid: 4
        channel: "web"
        statuspayment: 6
      }) {
        id
      }
    }
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      saveOrder(input: {
        baseid: 4
        channel: "web"
        statuspayment: 6
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
    "saveOrder": {
      "id": "4"
    }
  }
}
```

# Save multiple orders

=== "Mutation"
    ```graphql
    mutation {
      saveOrders(input: [{
        baseid: 5
        channel: "web"
        statuspayment: -1
      },{
        baseid: 6
        channel: "web"
        statuspayment: 5
      }]) {
        id
      }
    }
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      saveOrders(input: [{
        baseid: 5
        channel: "web"
        statuspayment: -1
      },{
        baseid: 6
        channel: "web"
        statuspayment: 5
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
    "saveOrders": [
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

# Delete single order

=== "Mutation"
    ```graphql
    mutation {
      deleteOrder(id: "4")
    }
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deleteOrder(id: "4")
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
    "deleteOrder": "4"
  }
}
```

# Delete multiple orders

=== "Mutation"
    ```graphql
    mutation {
      deleteOrders(id: ["5", "6"])
    }
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deleteOrders(id: ["5", "6"])
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
    "deleteOrders": [
      "5",
      "6"
    ]
  }
}
```

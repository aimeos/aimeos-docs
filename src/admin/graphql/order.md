This article contains all actions for retrieving and managing orders.

# Get order by ID

=== "Query"
    ```graphql
    query {
      getOrder(id: "1") {
        id
        siteid
        sitecode
        channel
        invoiceno
        relatedid
        languageid
        currencyid
        price
        costs
        rebate
        taxflag
        taxvalue
        datepayment
        datedelivery
        statusdelivery
        statuspayment
        customerid
        customerref
        comment
        mtime
        ctime
        editor
      }
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`query {
      getOrder(id: "1") {
        id
        siteid
        sitecode
        channel
        invoiceno
        relatedid
        languageid
        currencyid
        price
        costs
        rebate
        taxflag
        taxvalue
        datepayment
        datedelivery
        statusdelivery
        statuspayment
        customerid
        customerref
        comment
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
      getOrder(id: "1") {
        id
        siteid
        sitecode
        channel
        invoiceno
        relatedid
        languageid
        currencyid
        price
        costs
        rebate
        taxflag
        taxvalue
        datepayment
        datedelivery
        statusdelivery
        statuspayment
        customerid
        customerref
        comment
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
    "getOrder": {
      "id": "1",
      "siteid": "1.",
      "sitecode": "default",
      "channel": "web",
      "invoiceno": "INV-123",
      "relatedid": "123",
      "languageid": "de",
      "currencyid": "EUR",
      "price": "100.00",
      "costs": "5.00",
      "rebate": "5.00",
      "taxflag": false,
      "taxvalue": "10.00",
      "datepayment": "2022-06-12 00:00:00",
      "datedelivery": "2022-06-13 00:00:00",
      "statusdelivery": 0,
      "statuspayment": 1,
      "customerid": "456",
      "customerref": "REF-987",
      "comment": "Test comment",
      "mtime": "2022-06-13 09:03:50",
      "ctime": "2022-06-01 08:55:25",
      "editor": "aimeos@aimeos.org"
    }
  }
}
```

# Search orders

The filter parameter is explained in the [filter section](basics.md#filtering-the-result) of the [GraphQL basics](basics.md) article.

=== "Query"
    ```graphql
    query {
      searchOrders(filter: "{\\"==\\": {\\"order.channel\\":\\"web\\"}}") {
        items {
          id
          siteid
          sitecode
          channel
          invoiceno
          relatedid
          languageid
          currencyid
          price
          costs
          rebate
          taxflag
          taxvalue
          datepayment
          datedelivery
          statusdelivery
          statuspayment
          customerid
          customerref
          comment
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
      searchOrders(filter: "{\\"==\\": {\\"order.channel\\":\\"web\\"}}") {
        items {
          id
          siteid
          sitecode
          channel
          invoiceno
          relatedid
          languageid
          currencyid
          price
          costs
          rebate
          taxflag
          taxvalue
          datepayment
          datedelivery
          statusdelivery
          statuspayment
          customerid
          customerref
          comment
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
        "==": {"order.channel":"web"}
    };
    const fstr = JSON.stringify(JSON.stringify(filter));
    const body = JSON.stringify({'query':
    `query {
      searchOrders(filter: ` + fstr + `) {
        items {
          id
          siteid
          sitecode
          channel
          invoiceno
          relatedid
          languageid
          currencyid
          price
          costs
          rebate
          taxflag
          taxvalue
          datepayment
          datedelivery
          statusdelivery
          statuspayment
          customerid
          customerref
          comment
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
    "searchOrders": {
      "items": [
        {
          "id": "1",
          "siteid": "1.",
          "sitecode": "default",
          "channel": "web",
          "invoiceno": "INV-123",
          "relatedid": "123",
          "languageid": "de",
          "currencyid": "EUR",
          "price": "100.00",
          "costs": "5.00",
          "rebate": "5.00",
          "taxflag": false,
          "taxvalue": "10.00",
          "datepayment": "2022-06-12 00:00:00",
          "datedelivery": "2022-06-13 00:00:00",
          "statusdelivery": 0,
          "statuspayment": 1,
          "customerid": "456",
          "customerref": "REF-987",
          "comment": "Test comment",
          "mtime": "2022-06-13 09:03:50",
          "ctime": "2022-06-01 08:55:25",
          "editor": "aimeos@aimeos.org"
        },
        {
          "id": "3",
          "siteid": "1.",
          "sitecode": "default",
          "channel": "web",
          "invoiceno": "",
          "relatedid": "",
          "languageid": "de",
          "currencyid": "EUR",
          "price": "50.00",
          "costs": "0.00",
          "rebate": "0.00",
          "taxflag": false,
          "taxvalue": "5.00",
          "datepayment": "2022-06-15 00:00:00",
          "datedelivery": "2022-06-17 00:00:00",
          "statusdelivery": 0,
          "statuspayment": 1,
          "customerid": "345",
          "customerref": "",
          "comment": "Test",
          "mtime": "2022-06-13 09:03:50",
          "ctime": "2022-06-01 08:55:25",
          "editor": "aimeos@aimeos.org"
        }
      ],
      "total": 2
    }
  }
}
```

# Save single order

=== "Mutation"
    ```graphql
    mutation {
      saveOrder(input: {
        channel: "web"
        statuspayment: 6
      }) {
        id
      }
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`mutation {
      saveOrder(input: {
        channel: "web"
        statuspayment: 6
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
      saveOrder(input: {
        channel: "web"
        statuspayment: 6
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
        channel: "web"
        statuspayment: -1
      },{
        channel: "web"
        statuspayment: 5
      }]) {
        id
      }
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`mutation {
      saveOrders(input: [{
        channel: "web"
        statuspayment: -1
      },{
        channel: "web"
        statuspayment: 5
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
      saveOrders(input: [{
        channel: "web"
        statuspayment: -1
      },{
        channel: "web"
        statuspayment: 5
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
=== "JQAdm"
    ```javascript
    Aimeos.query(`mutation {
      deleteOrder(id: "4")
    }`).then(data => {
      console.log(data)
    })
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deleteOrder(id: "4")
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
=== "JQAdm"
    ```javascript
    Aimeos.query(`mutation {
      deleteOrders(id: ["5", "6"])
    }`).then(data => {
      console.log(data)
    })
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deleteOrders(id: ["5", "6"])
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
    "deleteOrders": [
      "5",
      "6"
    ]
  }
}
```

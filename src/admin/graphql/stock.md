This article contains all actions for retrieving and managing stocks.

# Get stock by ID

=== "Query"
    ```graphql
    query {
      getStock(id: "1") {
        id
        siteid
        type
        productid
        stocklevel
        timeframe
        dateback
        mtime
        ctime
        editor
      }
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`query {
      getStock(id: "1") {
        id
        siteid
        type
        productid
        stocklevel
        timeframe
        dateback
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
      getStock(id: "1") {
        id
        siteid
        type
        productid
        stocklevel
        timeframe
        dateback
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
    "getStock": {
      "id": "1",
      "siteid": "1.",
      "type": "default",
      "productid": "114",
      "stocklevel": 5,
      "timeframe": "",
      "dateback": null,
      "mtime": "2022-12-01 11:59:05",
      "ctime": "2022-12-01 11:59:05",
      "editor": "core"
    }
  }
}
```

# Search stocks

The filter parameter is explained in the [filter section](basics.md#filtering-the-result) of the [GraphQL basics](basics.md) article.

=== "Query"
    ```graphql
    query {
      searchStocks(filter: "{\\"~=\\": {\\"stock.type\\":\\"default\\"}}") {
        items {
          id
          siteid
          type
          productid
          stocklevel
          timeframe
          dateback
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
      searchStocks(filter: "{\\"~=\\": {\\"stock.type\\":\\"default\\"}}") {
        items {
          id
          siteid
          type
          productid
          stocklevel
          timeframe
          dateback
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
        "~=": {"stock.type":"default"}
    };
    const fstr = JSON.stringify(JSON.stringify(filter));
    const body = JSON.stringify({'query':
    `query {
      searchStocks(filter: ` + fstr + `) {
        items {
          id
          siteid
          type
          productid
          stocklevel
          timeframe
          dateback
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
    "searchStocks": {
      "items": [
        {
          "id": "1",
          "siteid": "1.",
          "type": "default",
          "productid": "114",
          "stocklevel": 5,
          "timeframe": "",
          "dateback": null,
          "mtime": "2022-12-01 11:59:05",
          "ctime": "2022-12-01 11:59:05",
          "editor": "core"
        },
        {
          "id": "12",
          "siteid": "1.",
          "type": "default",
          "productid": "115",
          "stocklevel": 0,
          "timeframe": "",
          "dateback": "2015-01-01 12:00:00",
          "mtime": "2022-12-01 11:59:05",
          "ctime": "2022-12-01 11:59:05",
          "editor": "core"
        }
      ],
      "total": 2
    }
  }
}
```

# Save single stock

=== "Mutation"
    ```graphql
    mutation {
      saveStock(input: {
        type: "warehouse-de"
        productid: "1"
        stocklevel: 100
      }) {
        id
      }
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`mutation {
      saveStock(input: {
        type: "warehouse-de"
        productid: "1"
        stocklevel: 100
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
      saveStock(input: {
        type: "warehouse-de"
        productid: "1"
        stocklevel: 100
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
    "saveStock": {
      "id": "18"
    }
  }
}
```

# Save multiple stocks

=== "Mutation"
    ```graphql
    mutation {
      saveStocks(input: [{
        type: "warehouse-fr"
        productid: "1"
        stocklevel: 50
      }
      {
        type: "warehouse-it"
        productid: "1"
        stocklevel: 500
      }]) {
        id
      }
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`mutation {
      saveStocks(input: [{
        type: "warehouse-fr"
        productid: "1"
        stocklevel: 50
      }
      {
        type: "warehouse-it"
        productid: "1"
        stocklevel: 500
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
      saveStocks(input: [{
        type: "warehouse-fr"
        productid: "1"
        stocklevel: 50
      }
      {
        type: "warehouse-it"
        productid: "1"
        stocklevel: 500
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
    "saveStocks": [
      {
        "id": "19"
      },
      {
        "id": "20"
      }
    ]
  }
}
```

# Delete single stock

=== "Mutation"
    ```graphql
    mutation {
      deleteStock(id: "18")
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`mutation {
      deleteStock(id: "18")
    }`).then(data => {
      console.log(data)
    })
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deleteStock(id: "18")
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
    "deleteStock": "18"
  }
}
```

# Delete multiple stocks

=== "Mutation"
    ```graphql
    mutation {
      deleteStocks(id: ["19", "20"])
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`mutation {
      deleteStocks(id: ["19", "20"])
    }`).then(data => {
      console.log(data)
    })
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deleteStocks(id: ["19", "20"])
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
    "deleteStocks": [
      "19",
      "20"
    ]
  }
}
```

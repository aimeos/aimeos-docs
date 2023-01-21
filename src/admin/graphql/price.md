This article contains all actions for retrieving and managing prices.

# Get price by ID

=== "Query"
    ```graphql
    query {
      getPrice(id: "1") {
        id
        siteid
        type
        domain
        label
        currencyid
        quantity
        value
        costs
        rebate
        taxrates
        taxflag
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
      getPrice(id: "1") {
        id
        siteid
        type
        domain
        label
        currencyid
        quantity
        value
        costs
        rebate
        taxrates
        taxflag
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
    "getPrice": {
      "id": "1",
      "siteid": "1.",
      "type": "default",
      "domain": "attribute",
      "label": "Demo: Large print",
      "currencyid": "EUR",
      "quantity": 1,
      "value": "15.00",
      "costs": "0.00",
      "rebate": "0.00",
      "taxrates": "{\"tax\":\"20.00\"}",
      "taxflag": true,
      "status": 1,
      "mtime": "2022-05-28 06:26:38",
      "ctime": "2022-05-28 06:26:38",
      "editor": "core:setup"
    }
  }
}
```

# Search prices

=== "Query"
    ```graphql
    query {
      searchPrices(filter: "{\"=~\": {\"price.label\":\"Demo\"}}") {
        id
        siteid
        type
        domain
        label
        currencyid
        quantity
        value
        costs
        rebate
        taxrates
        taxflag
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
        "=~": {"price.code":"demo-"}
    };
    const fstr = JSON.stringify(filter).replace(/"/g, '\\"');
    const body = JSON.stringify({'query':
    `query {
      searchPrices(filter: "` + fstr + `") {
        id
        siteid
        type
        domain
        label
        currencyid
        quantity
        value
        costs
        rebate
        taxrates
        taxflag
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
    "searchPrices": [
      {
        "id": "3",
        "siteid": "1.",
        "type": "default",
        "domain": "attribute",
        "label": "Demo: Large print",
        "currencyid": "EUR",
        "quantity": 1,
        "value": "15.00",
        "costs": "0.00",
        "rebate": "0.00",
        "taxrates": "{\"tax\":\"20.00\"}",
        "taxflag": true,
        "status": 1,
        "mtime": "2022-05-28 06:26:38",
        "ctime": "2022-05-28 06:26:38",
        "editor": "core:setup"
      },
      {
        "id": "4",
        "siteid": "1.",
        "type": "default",
        "domain": "attribute",
        "label": "Demo: Large print",
        "currencyid": "USD",
        "quantity": 1,
        "value": "20.00",
        "costs": "0.00",
        "rebate": "0.00",
        "taxrates": "{\"tax\":\"10.00\"}",
        "taxflag": true,
        "status": 1,
        "mtime": "2022-05-28 06:26:38",
        "ctime": "2022-05-28 06:26:38",
        "editor": "core:setup"
      }
    ]
  }
}
```

# Save single price

=== "Mutation"
    ```graphql
    mutation {
      savePrice(input: {
        domain: "product"
        label: "Test price"
        currencyid: "EUR"
        value: "100.00"
      }) {
        id
      }
    }
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      savePrice(input: {
        domain: "product"
        label: "Test price"
        currencyid: "EUR"
        value: "100.00"
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
    "savePrice": {
      "id": "30"
    }
  }
}
```

# Save multiple prices

=== "Mutation"
    ```graphql
    mutation {
      savePrices(input: [{
        domain: "product"
        label: "Test 2 price"
        currencyid: "EUR"
        value: "200.00"
      },{
        domain: "product"
        label: "Test 3 price"
        currencyid: "USD"
        value: "220.00"
      }]) {
        id
      }
    }
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      savePrices(input: [{
        domain: "product"
        label: "Test 2 price"
        currencyid: "EUR"
        value: "200.00"
      },{
        domain: "product"
        label: "Test 3 price"
        currencyid: "USD"
        value: "220.00"
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
    "savePrices": [
      {
        "id": "31"
      },
      {
        "id": "32"
      }
    ]
  }
}
```

# Delete single price

=== "Mutation"
    ```graphql
    mutation {
      deletePrice(id: "30")
    }
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deletePrice(id: "30")
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
    "deletePrice": "30"
  }
}
```

# Delete multiple prices

=== "Mutation"
    ```graphql
    mutation {
      deletePrices(id: ["31", "32"])
    }
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deletePrices(id: ["31", "32"])
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
    "deletePrices": [
      "31",
      "32"
    ]
  }
}
```

This article contains all actions for retrieving and managing prices.

!!! tip
    The price domain supports [fetching related resources](basics.md#include-related-resources).

# Get price by ID

=== "Query"
    ```graphql
    query {
      getPrice(id: "1", include: ["group"]) {
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
        lists {
          group {
            id
            item {
              id
              code
            }
          }
        }
        property {
          id
          type
          languageid
          value
        }
      }
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`query {
      getPrice(id: "1", include: ["group"]) {
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
        lists {
          group {
            id
            item {
              id
              code
            }
          }
        }
        property {
          id
          type
          languageid
          value
        }
      }
    }`).then(data => {
      console.log(data)
    })
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `query {
      getPrice(id: "1", include: ["group"]) {
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
        lists {
          group {
            id
            item {
              id
              code
            }
          }
        }
        property {
          id
          type
          languageid
          value
        }
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
      "taxrates": "{\\"tax\\":\\"20.00\\"}",
      "taxflag": true,
      "status": 1,
      "mtime": "2022-05-28 06:26:38",
      "ctime": "2022-05-28 06:26:38",
      "editor": "core:setup",
      "lists": {
        "group": [{
          "id": "10",
          "item": {
            "id": "2",
            "code": "wholesale"
          }
        }]
      },
      "property": [{
        "id": "1",
        "type": "country",
        "languageid": null,
        "value": "DE"
      }]
    }
  }
}
```

# Search prices

The filter parameter is explained in the [filter section](basics.md#filtering-the-result) of the [GraphQL basics](basics.md) article.

=== "Query"
    ```graphql
    query {
      searchPrices(filter: "{\\"=~\\": {\\"price.label\\":\\"Demo\\"}}", include: ["group"]) {
        items {
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
          lists {
            group {
              id
              item {
                id
                code
              }
            }
          }
          property {
            id
            type
            languageid
            value
          }
        }
        total
      }
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`query {
      searchPrices(filter: "{\\"=~\\": {\\"price.label\\":\\"Demo\\"}}", include: ["group"]) {
        items {
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
          lists {
            group {
              id
              item {
                id
                code
              }
            }
          }
          property {
            id
            type
            languageid
            value
          }
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
        "=~": {"price.label":"Demo"}
    };
    const fstr = JSON.stringify(JSON.stringify(filter));
    const body = JSON.stringify({'query':
    `query {
      searchPrices(filter: ` + fstr + `, include: ["group"]) {
        items {
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
          lists {
            group {
              id
              item {
                id
                code
              }
            }
          }
          property {
            id
            type
            languageid
            value
          }
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
    "searchPrices": {
      "items": [
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
          "taxrates": "{\\"tax\\":\\"20.00\\"}",
          "taxflag": true,
          "status": 1,
          "mtime": "2022-05-28 06:26:38",
          "ctime": "2022-05-28 06:26:38",
          "editor": "core:setup",
          "lists": {
            "group": [{
              "id": "10",
              "item": {
                "id": "2",
                "code": "wholesale"
              }
            }]
          },
          "property": [{
            "id": "1",
            "type": "country",
            "languageid": null,
            "value": "DE"
          }]
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
          "taxrates": "{\\"tax\\":\\"10.00\\"}",
          "taxflag": true,
          "status": 1,
          "mtime": "2022-05-28 06:26:38",
          "ctime": "2022-05-28 06:26:38",
          "editor": "core:setup",
          "lists": {
            "group": []
          },
          "property": [{
          }]
        }
      ],
      "total": 2
    }
  }
}
```

# Save single price

=== "Mutation"
    ```graphql
    mutation {
      savePrice(input: {
        domain: "product",
        label: "Test price",
        currencyid: "EUR",
        value: "100.00",
        lists: {
          group: {
            refid: "2"
          }
        },
        property: [{
          type: "country",
          languageid: null,
          value: "DE"
        }]
      }) {
        id
      }
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`mutation {
      savePrice(input: {
        domain: "product",
        label: "Test price",
        currencyid: "EUR",
        value: "100.00",
        lists: {
          group: {
            refid: "2"
          }
        },
        property: [{
          type: "country",
          languageid: null,
          value: "DE"
        }]
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
      savePrice(input: {
        domain: "product",
        label: "Test price",
        currencyid: "EUR",
        value: "100.00",
        lists: {
          group: {
            refid: "2"
          }
        },
        property: [{
          type: "country",
          languageid: null,
          value: "DE"
        }]
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
        domain: "product",
        label: "Test 2 price",
        currencyid: "EUR",
        value: "200.00",
        lists: {
          group: [{
            refid: "2"
          }]
        },
        property: [{
          type: "country",
          languageid: null,
          value: "DE"
        }]
      },{
        domain: "product",
        label: "Test 3 price",
        currencyid: "USD",
        value: "220.00"
      }]) {
        id
      }
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`mutation {
      savePrices(input: [{
        domain: "product",
        label: "Test 2 price",
        currencyid: "EUR",
        value: "200.00",
        lists: {
          group: [{
            refid: "2"
          }]
        },
        property: [{
          type: "country",
          languageid: null,
          value: "DE"
        }]
      },{
        domain: "product",
        label: "Test 3 price",
        currencyid: "USD",
        value: "220.00"
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
      savePrices(input: [{
        domain: "product",
        label: "Test 2 price",
        currencyid: "EUR",
        value: "200.00",
        lists: {
          group: [{
            refid: "2"
          }]
        },
        property: [{
          type: "country",
          languageid: null,
          value: "DE"
        }]
      },{
        domain: "product",
        label: "Test 3 price",
        currencyid: "USD",
        value: "220.00"
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
=== "JQAdm"
    ```javascript
    Aimeos.query(`mutation {
      deletePrice(id: "30")
    }`).then(data => {
      console.log(data)
    })
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deletePrice(id: "30")
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
=== "JQAdm"
    ```javascript
    Aimeos.query(`mutation {
      deletePrices(id: ["31", "32"])
    }`).then(data => {
      console.log(data)
    })
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deletePrices(id: ["31", "32"])
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
    "deletePrices": [
      "31",
      "32"
    ]
  }
}
```

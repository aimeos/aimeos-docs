This article contains all actions for retrieving and managing customers.

!!! tip
    The customer domain supports [fetching related resources](basics.md#include-related-resources).

# Get customer by ID

=== "Query"
    ```graphql
    query {
      getCustomer(id: "1", ["product", "customer/property"]) {
        id
        siteid
        code
        label
        salutation
        company
        vatid
        title
        firstname
        lastname
        address1
        address2
        address3
        postal
        city
        state
        languageid
        countryid
        telephone
        email
        telefax
        website
        longitude
        status
        latitude
        birthday
        status
        dateverified
        password
        mtime
        ctime
        editor
        lists {
          product {
            id {
              item {
                id
                label
              }
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
      getCustomer(id: "1", ["product", "customer/property"]) {
        id
        siteid
        code
        label
        salutation
        company
        vatid
        title
        firstname
        lastname
        address1
        address2
        address3
        postal
        city
        state
        languageid
        countryid
        telephone
        email
        telefax
        website
        longitude
        status
        latitude
        birthday
        status
        dateverified
        password
        mtime
        ctime
        editor
        lists {
          product {
            id {
              item {
                id
                label
              }
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
      getCustomer(id: "1", ["product", "customer/property"]) {
        id
        siteid
        code
        label
        salutation
        company
        vatid
        title
        firstname
        lastname
        address1
        address2
        address3
        postal
        city
        state
        languageid
        countryid
        telephone
        email
        telefax
        website
        longitude
        status
        latitude
        birthday
        status
        dateverified
        password
        mtime
        ctime
        editor
        lists {
          product {
            id {
              item {
                id
                label
              }
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
    "getCustomer": {
      "id": "1",
      "siteid": "1.",
      "code": "demo@example.com",
      "label": "Test user",
      "salutation": "mr",
      "company": "Test company",
      "vatid": "DE999999999",
      "title": null,
      "firstname": "Test",
      "lastname": "User",
      "address1": "Test street",
      "address2": "1",
      "address3": null,
      "postal": "10000",
      "city": "Test city",
      "state": "CA",
      "languageid": "en",
      "countryid": "US",
      "telephone": null,
      "email": "demo@example.com",
      "telefax": null,
      "website": null,
      "longitude": null,
      "status": 1,
      "latitude": null,
      "birthday": "2000-01-01",
      "dateverified": null,
      "password": "$2y$10$cdjdim/ITpPnf8H06i5wMOvlo6l3Slsz6E39sX6gZSpOIfIBD6W66",
      "mtime": "2022-12-01 11:59:04",
      "ctime": "2022-12-01 11:59:04",
      "editor": "core",
      "lists": {
        "product": [{
          "id": "10",
          "item": {
            "id": "1",
            "label": "Test article"
          }
        }]
      },
      "property": [{
        "id": "1",
        "type": "test",
        "languageid": null,
        "value": "Test property"
      }]
    }
  }
}
```

# Find customer by code

=== "Query"
    ```graphql
    query {
      findCustomer(code: "test@example.com", ["product", "customer/property"]) {
        id
        siteid
        code
        label
        salutation
        company
        vatid
        title
        firstname
        lastname
        address1
        address2
        address3
        postal
        city
        state
        languageid
        countryid
        telephone
        email
        telefax
        website
        longitude
        status
        latitude
        birthday
        status
        dateverified
        password
        mtime
        ctime
        editor
        lists {
          product {
            id {
              item {
                id
                label
              }
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
      findCustomer(code: "test@example.com", ["product", "customer/property"]) {
        id
        siteid
        code
        label
        salutation
        company
        vatid
        title
        firstname
        lastname
        address1
        address2
        address3
        postal
        city
        state
        languageid
        countryid
        telephone
        email
        telefax
        website
        longitude
        status
        latitude
        birthday
        status
        dateverified
        password
        mtime
        ctime
        editor
        lists {
          product {
            id {
              item {
                id
                label
              }
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
      findCustomer(code: "test@example.com", ["product", "customer/property"]) {
        id
        siteid
        code
        label
        salutation
        company
        vatid
        title
        firstname
        lastname
        address1
        address2
        address3
        postal
        city
        state
        languageid
        countryid
        telephone
        email
        telefax
        website
        longitude
        status
        latitude
        birthday
        status
        dateverified
        password
        mtime
        ctime
        editor
        lists {
          product {
            id {
              item {
                id
                label
              }
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
    "findCustomer": {
      "id": "1",
      "siteid": "1.",
      "code": "demo@example.com",
      "label": "Test user",
      "salutation": "mr",
      "company": "Test company",
      "vatid": "DE999999999",
      "title": null,
      "firstname": "Test",
      "lastname": "User",
      "address1": "Test street",
      "address2": "1",
      "address3": null,
      "postal": "10000",
      "city": "Test city",
      "state": "CA",
      "languageid": "en",
      "countryid": "US",
      "telephone": null,
      "email": "demo@example.com",
      "telefax": null,
      "website": null,
      "longitude": null,
      "status": 1,
      "latitude": null,
      "birthday": "2000-01-01",
      "dateverified": null,
      "password": "$2y$10$cdjdim/ITpPnf8H06i5wMOvlo6l3Slsz6E39sX6gZSpOIfIBD6W66",
      "mtime": "2022-12-01 11:59:04",
      "ctime": "2022-12-01 11:59:04",
      "editor": "core",
      "lists": {
        "product": [{
          "id": "10",
          "item": {
            "id": "1",
            "label": "Test article"
          }
        }]
      },
      "property": [{
        "id": "1",
        "type": "test",
        "languageid": null,
        "value": "Test property"
      }]
    }
  }
}
```

# Search customers

The filter parameter is explained in the [filter section](basics.md#filtering-the-result) of the [GraphQL basics](basics.md) article.

=== "Query"
    ```graphql
    query {
      searchCustomers(filter: "{\\"=~\\": {\\"customer.code\\":\\"demo-\\"}}", ["product", "customer/property"]) {
        items {
          id
          siteid
          code
          label
          salutation
          company
          vatid
          title
          firstname
          lastname
          address1
          address2
          address3
          postal
          city
          state
          languageid
          countryid
          telephone
          email
          telefax
          website
          longitude
          status
          latitude
          birthday
          status
          dateverified
          password
          mtime
          ctime
          editor
          lists {
            product {
              id {
                item {
                  id
                  label
                }
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
      searchCustomers(filter: "{\\"=~\\": {\\"customer.code\\":\\"demo-\\"}}", ["product", "customer/property"]) {
        items {
          id
          siteid
          code
          label
          salutation
          company
          vatid
          title
          firstname
          lastname
          address1
          address2
          address3
          postal
          city
          state
          languageid
          countryid
          telephone
          email
          telefax
          website
          longitude
          status
          latitude
          birthday
          status
          dateverified
          password
          mtime
          ctime
          editor
          lists {
            product {
              id {
                item {
                  id
                  label
                }
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
        "=~": {"customer.code":"demo-"}
    };
    const fstr = JSON.stringify(JSON.stringify(filter));
    const body = JSON.stringify({'query':
    `query {
      searchCustomers(filter: ` + fstr + `, ["product", "customer/property"]) {
        items {
          id
          siteid
          code
          label
          salutation
          company
          vatid
          title
          firstname
          lastname
          address1
          address2
          address3
          postal
          city
          state
          languageid
          countryid
          telephone
          email
          telefax
          website
          longitude
          status
          latitude
          birthday
          status
          dateverified
          password
          mtime
          ctime
          editor
          lists {
            product {
              id {
                item {
                  id
                  label
                }
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
    "searchCustomers": {
      "items": [
        {
          "id": "1",
          "siteid": "1.",
          "code": "demo@example.com",
          "label": "Test user",
          "salutation": "mr",
          "company": "Test company",
          "vatid": "DE999999999",
          "title": null,
          "firstname": "Test",
          "lastname": "User",
          "address1": "Test street",
          "address2": "1",
          "address3": null,
          "postal": "10000",
          "city": "Test city",
          "state": "CA",
          "languageid": "en",
          "countryid": "US",
          "telephone": null,
          "email": "demo@example.com",
          "telefax": null,
          "website": null,
          "longitude": null,
          "status": 1,
          "latitude": null,
          "birthday": "2000-01-01",
          "dateverified": null,
          "password": "$2y$10$cdjdim/ITpPnf8H06i5wMOvlo6l3Slsz6E39sX6gZSpOIfIBD6W66",
          "mtime": "2022-12-01 11:59:04",
          "ctime": "2022-12-01 11:59:04",
          "editor": "core",
          "lists": {
            "product": [{
              "id": "10",
              "item": {
                "id": "1",
                "label": "Test article"
              }
            }]
          },
          "property": [{
            "id": "1",
            "type": "test",
            "languageid": null,
            "value": "Test property"
          }]
        }
      ],
      "total": 1
    }
  }
}
```

# Save single customer

=== "Mutation"
    ```graphql
    mutation {
      saveCustomer(input: {
        code: "test-2@example.com"
        label: "Test 2 customer"
        city: "Test city"
        languageid: "en"
        lists: {
          product: [{
            type: "suggest"
            refid: "2"
          }]
        },
        property: [{
          type: "test"
          languageid: null
          value: "Test property"
        }]
      }) {
        id
      }
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`mutation {
      saveCustomer(input: {
        code: "test-3@example.com"
        label: "Test customer"
        city: "Test city"
        languageid: "en"
        lists: {
          product: [{
            type: "suggest"
            refid: "2"
          }]
        },
        property: [{
          type: "test"
          languageid: null
          value: "Test property"
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
      saveCustomer(input: {
        code: "test-3@example.com"
        label: "Test customer"
        city: "Test city"
        languageid: "en"
        lists: {
          product: [{
            type: "suggest"
            refid: "2"
          }]
        },
        property: [{
          type: "test"
          languageid: null
          value: "Test property"
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
    "saveCustomer": {
      "id": "3"
    }
  }
}
```

# Save multiple customers

=== "Mutation"
    ```graphql
    mutation {
      saveCustomers(input: [{
        code: "test-3@example.com"
        label: "Test 3 customer"
        city: "Test city"
        languageid: "en"
        lists: {
          product: [{
            type: "suggest"
            refid: "2"
          }]
        }
        property: [{
          type: "test"
          languageid: null
          value: "Test property"
        }]
      },{
        code: "test-4@example.com"
        label: "Test 4 customer"
        city: "Test city"
        languageid: "en"
      }]) {
        id
      }
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`mutation {
      saveCustomers(input: [{
        code: "test-3@example.com"
        label: "Test 3 customer"
        city: "Test city"
        languageid: "en"
        lists: {
          product: [{
            type: "suggest"
            refid: "2"
          }]
        }
        property: [{
          type: "test"
          languageid: null
          value: "Test property"
        }]
      },{
        code: "test-4@example.com"
        label: "Test 4 customer"
        city: "Test city"
        languageid: "en"
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
      saveCustomers(input: [{
        code: "test-3@example.com"
        label: "Test 3 customer"
        city: "Test city"
        languageid: "en"
        lists: {
          product: [{
            type: "suggest"
            refid: "2"
          }]
        }
        property: [{
          type: "test"
          languageid: null
          value: "Test property"
        }]
      },{
        code: "test-4@example.com"
        label: "Test 4 customer"
        city: "Test city"
        languageid: "en"
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
    "saveCustomers": [
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

# Delete single customer

=== "Mutation"
    ```graphql
    mutation {
      deleteCustomer(id: "3")
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`mutation {
      deleteCustomer(id: "3")
    }`).then(data => {
      console.log(data)
    })
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deleteCustomer(id: "3")
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
    "deleteCustomer": "3"
  }
}
```

# Delete multiple customers

=== "Mutation"
    ```graphql
    mutation {
      deleteCustomers(id: ["4", "5"])
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`mutation {
      deleteCustomers(id: ["4", "5"])
    }`).then(data => {
      console.log(data)
    })
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deleteCustomers(id: ["4", "5"])
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
    "deleteCustomers": [
      "4",
      "5"
    ]
  }
}
```

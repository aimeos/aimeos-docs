This article contains all actions for retrieving and managing types.
There are queries and mutations for different data domains available.

# Get type by ID

Available queries:

* getAttributeType
* getAttributeListType
* getAttributePropertyType
* getCatalogListType
* getCustomerListType
* getCustomerPropertyType
* getMediaType
* getMediaListType
* getMediaPropertyType
* getPluginType
* getPriceType
* getPriceListType
* getPricePropertyType
* getProductType
* getProductListType
* getProductPropertyType
* getRuleType
* getServiceType
* getServiceListType
* getStockType
* getSupplierListType
* getTextType
* getTextListType

=== "Query"
    ```graphql
    query {
      getProductType(id: "1") {
        id
        siteid
        domain
        code
        label
        position
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
      getProductType(id: "1") {
        id
        siteid
        domain
        code
        label
        position
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
      getProductType(id: "1") {
        id
        siteid
        domain
        code
        label
        position
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
    "getProductType": {
      "id": "1",
      "siteid": "1.",
      "domain": "product",
      "code": "default",
      "label": "Article",
      "position": 0,
      "status": 1,
      "mtime": "2022-05-28 06:26:37",
      "ctime": "2022-05-28 06:26:37",
      "editor": "core:setup"
    }
  }
}
```

# Find type by code

Available queries:

* findAttributeType
* findAttributeListType
* findAttributePropertyType
* findCatalogListType
* findCustomerListType
* findCustomerPropertyType
* findMediaType
* findMediaListType
* findMediaPropertyType
* findPluginType
* findPriceType
* findPriceListType
* findPricePropertyType
* findProductType
* findProductListType
* findProductPropertyType
* findRuleType
* findServiceType
* findServiceListType
* findStockType
* findSupplierListType
* findTextType
* findTextListType

=== "Query"
    ```graphql
    query {
      findProductType(code: "default", domain: "product") {
        id
        siteid
        domain
        code
        label
        position
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
      findProductType(code: "default", domain: "product") {
        id
        siteid
        domain
        code
        label
        position
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
      findProductType(code: "default", domain: "product") {
        id
        siteid
        domain
        code
        label
        position
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
    "findProductType": {
      "id": "1",
      "siteid": "1.",
      "domain": "product",
      "code": "default",
      "label": "Article",
      "position": 0,
      "status": 1,
      "mtime": "2022-05-28 06:26:37",
      "ctime": "2022-05-28 06:26:37",
      "editor": "core:setup"
    }
  }
}
```

# Search types

Available queries:

* searchAttributeTypes
* searchAttributeListTypes
* searchAttributePropertyTypes
* searchCatalogListTypes
* searchCustomerListTypes
* searchCustomerPropertyTypes
* searchMediaTypes
* searchMediaListTypes
* searchMediaPropertyTypes
* searchPluginTypes
* searchPriceTypes
* searchPriceListTypes
* searchPricePropertyTypes
* searchProductTypes
* searchProductListTypes
* searchProductPropertyTypes
* searchRuleTypes
* searchServiceTypes
* searchServiceListTypes
* searchStockTypes
* searchSupplierListTypes
* searchTextTypes
* searchTextListTypes

The filter parameter is explained in the [filter section](basics.md#filtering-the-result) of the [GraphQL basics](basics.md) article.

=== "Query"
    ```graphql
    query {
      searchProductTypes(filter: "{\\"==\\": {\\"product.type.domain\\":\\"product\\"}}") {
        items {
          id
          siteid
          domain
          code
          label
          position
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
      searchProductTypes(filter: "{\\"==\\": {\\"product.type.domain\\":\\"product\\"}}") {
        items {
          id
          siteid
          domain
          code
          label
          position
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
        "==": {"product.type.domain":"product"}
    };
    const fstr = JSON.stringify(JSON.stringify(filter));
    const body = JSON.stringify({'query':
    `query {
      searchProductTypes(filter: ` + fstr + `) {
        items {
          id
          siteid
          domain
          code
          label
          position
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
    "searchProductTypes": {
      "items": [
        {
          "id": "1",
          "siteid": "1.",
          "domain": "product",
          "code": "default",
          "label": "Article",
          "position": 0,
          "status": 1,
          "mtime": "2022-05-28 06:26:37",
          "ctime": "2022-05-28 06:26:37",
          "editor": "core:setup"
        },
        {
          "id": "2",
          "siteid": "1.",
          "domain": "product",
          "code": "bundle",
          "label": "Bundle",
          "position": 0,
          "status": 1,
          "mtime": "2022-05-28 06:26:37",
          "ctime": "2022-05-28 06:26:37",
          "editor": "core:setup"
        }
      ],
    }
    "total": 2
  }
}
```

# Save single type

Available mutations:

* saveAttributeType
* saveAttributeListType
* saveAttributePropertyType
* saveCatalogListType
* saveCustomerListType
* saveCustomerPropertyType
* saveMediaType
* saveMediaListType
* saveMediaPropertyType
* savePluginType
* savePriceType
* savePriceListType
* savePricePropertyType
* saveProductType
* saveProductListType
* saveProductPropertyType
* saveRuleType
* saveServiceType
* saveServiceListType
* saveStockType
* saveSupplierListType
* saveTextType
* saveTextListType

=== "Mutation"
    ```graphql
    mutation {
      saveProductType(input: {
        code: "test"
        domain: "product"
        label: "Test type"
      }) {
        id
      }
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`query {
      saveProductType(input: {
        code: "test"
        domain: "product"
        label: "Test type"
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
      saveProductType(input: {
        code: "test"
        domain: "product"
        label: "Test type"
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
    "saveProductType": {
      "id": "7"
    }
  }
}
```

# Save multiple types

Available mutations:

* saveAttributeTypes
* saveAttributeListTypes
* saveAttributePropertyTypes
* saveCatalogListTypes
* saveCustomerListTypes
* saveCustomerPropertyTypes
* saveMediaTypes
* saveMediaListTypes
* saveMediaPropertyTypes
* savePluginTypes
* savePriceTypes
* savePriceListTypes
* savePricePropertyTypes
* saveProductTypes
* saveProductListTypes
* saveProductPropertyTypes
* saveRuleTypes
* saveServiceTypes
* saveServiceListTypes
* saveStockTypes
* saveSupplierListTypes
* saveTextTypes
* saveTextListTypes

=== "Mutation"
    ```graphql
    mutation {
      saveProductTypes(input: [{
        code: "test"
        domain: "product"
        label: "Test type 2"
      },{
        code: "test"
        domain: "product"
        label: "Test type 3"
      }]) {
        id
      }
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`query {
      saveProductTypes(input: [{
        code: "test"
        domain: "product"
        label: "Test type 2"
      },{
        code: "test"
        domain: "product"
        label: "Test type 3"
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
      saveProductTypes(input: [{
        code: "test"
        domain: "product"
        label: "Test type 2"
      },{
        code: "test"
        domain: "product"
        label: "Test type 3"
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
    "saveProductTypes": [
      {
        "id": "8"
      },
      {
        "id": "9"
      }
    ]
  }
}
```

# Delete single type

Available mutations:

* deleteAttributeType
* deleteAttributeListType
* deleteAttributePropertyType
* deleteCatalogListType
* deleteCustomerListType
* deleteCustomerPropertyType
* deleteMediaType
* deleteMediaListType
* deleteMediaPropertyType
* deletePluginType
* deletePriceType
* deletePriceListType
* deletePricePropertyType
* deleteProductType
* deleteProductListType
* deleteProductPropertyType
* deleteRuleType
* deleteServiceType
* deleteServiceListType
* deleteStockType
* deleteSupplierListType
* deleteTextType
* deleteTextListType

=== "Mutation"
    ```graphql
    mutation {
      deleteProductType(id: "7")
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`query {
      deleteProductType(id: "7")
    }`).then(data => {
      console.log(data)
    })
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deleteProductType(id: "7")
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
    "deleteProductType": "7"
  }
}
```

# Delete multiple types

Available mutations:

* deleteAttributeTypes
* deleteAttributeListTypes
* deleteAttributePropertyTypes
* deleteCatalogListTypes
* deleteCustomerListTypes
* deleteCustomerPropertyTypes
* deleteMediaTypes
* deleteMediaListTypes
* deleteMediaPropertyTypes
* deletePluginTypes
* deletePriceTypes
* deletePriceListTypes
* deletePricePropertyTypes
* deleteProductTypes
* deleteProductListTypes
* deleteProductPropertyTypes
* deleteRuleTypes
* deleteServiceTypes
* deleteServiceListTypes
* deleteStockTypes
* deleteSupplierListTypes
* deleteTextTypes
* deleteTextListTypes

=== "Mutation"
    ```graphql
    mutation {
      deleteProductTypes(id: ["8", "9"])
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`query {
      deleteProductTypes(id: ["8", "9"])
    }`).then(data => {
      console.log(data)
    })
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deleteProductTypes(id: ["8", "9"])
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
    "deleteProductTypes": [
      "8",
      "9"
    ]
  }
}
```

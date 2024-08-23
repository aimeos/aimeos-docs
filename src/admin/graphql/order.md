This article contains all actions for retrieving and managing orders.

!!! note
    It's not possible to delete orders via the GraphQL API for accounting reasons. You should set the payment status of the order you want to delete to `0` instead.

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
        address {
          id
          siteid
          type
          parentid
          addressid
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
          status
          longitude
          latitude
          birthday
          position
          mtime
          ctime
          editor
        }
        coupon {
          code
        }
        product {
          id
          siteid
          parentid
          orderproductid
          orderaddressid
          type
          stocktype
          prodcode
          productid
          parentproductid
          vendor
          scale
          quantity
          qtyopen
          currencyid
          price
          costs
          rebate
          taxrates
          taxvalue
          taxflag
          name
          description
          mediaurl
          timeframe
          position
          notes
          statuspayment
          statusdelivery
          target
          flags
          mtime
          ctime
          editor
          attribute {
            id
            siteid
            parentid
            attributeid
            type
            code
            name
            value
            price
            quantity
            mtime
            ctime
            editor
          }
          product {
            id
            siteid
            parentid
            orderproductid
            orderaddressid
            type
            stocktype
            prodcode
            productid
            parentproductid
            vendor
            scale
            quantity
            qtyopen
            currencyid
            price
            costs
            rebate
            taxrates
            taxvalue
            taxflag
            name
            description
            mediaurl
            timeframe
            position
            notes
            statuspayment
            statusdelivery
            target
            flags
            mtime
            ctime
            editor
            attribute {
              id
              siteid
              parentid
              attributeid
              type
              code
              name
              value
              price
              quantity
              mtime
              ctime
              editor
            }
          }
        }
        service {
          id
          siteid
          serviceid
          type
          code
          name
          currencyid
          price
          costs
          rebate
          taxrates
          taxvalue
          taxflag
          position
          mediaurl
          attribute {
            id
            siteid
            parentid
            attributeid
            type
            code
            name
            value
            price
            quantity
            mtime
            ctime
            editor
          }
          transaction {
            id
            siteid
            parentid
            config
            status
            currencyid
            type
            price
            costs
            rebate
            taxvalue
            taxflag
            mtime
            ctime
            editor
          }
        }
        status {
            id
            siteid
            parentid
            type
            value
            mtime
            ctime
            editor
        }
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
        address {
          id
          siteid
          type
          parentid
          addressid
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
          status
          longitude
          latitude
          birthday
          position
          mtime
          ctime
          editor
        }
        coupon {
          code
        }
        product {
          id
          siteid
          parentid
          orderproductid
          orderaddressid
          type
          stocktype
          prodcode
          productid
          parentproductid
          vendor
          scale
          quantity
          qtyopen
          currencyid
          price
          costs
          rebate
          taxrates
          taxvalue
          taxflag
          name
          description
          mediaurl
          timeframe
          position
          notes
          statuspayment
          statusdelivery
          target
          flags
          mtime
          ctime
          editor
          attribute {
            id
            siteid
            parentid
            attributeid
            type
            code
            name
            value
            price
            quantity
            mtime
            ctime
            editor
          }
          product {
            id
            siteid
            parentid
            orderproductid
            orderaddressid
            type
            stocktype
            prodcode
            productid
            parentproductid
            vendor
            scale
            quantity
            qtyopen
            currencyid
            price
            costs
            rebate
            taxrates
            taxvalue
            taxflag
            name
            description
            mediaurl
            timeframe
            position
            notes
            statuspayment
            statusdelivery
            target
            flags
            mtime
            ctime
            editor
            attribute {
              id
              siteid
              parentid
              attributeid
              type
              code
              name
              value
              price
              quantity
              mtime
              ctime
              editor
            }
          }
        }
        service {
          id
          siteid
          serviceid
          type
          code
          name
          currencyid
          price
          costs
          rebate
          taxrates
          taxvalue
          taxflag
          position
          mediaurl
          attribute {
            id
            siteid
            parentid
            attributeid
            type
            code
            name
            value
            price
            quantity
            mtime
            ctime
            editor
          }
          transaction {
            id
            siteid
            parentid
            config
            status
            currencyid
            type
            price
            costs
            rebate
            taxvalue
            taxflag
            mtime
            ctime
            editor
          }
        }
        status {
            id
            siteid
            parentid
            type
            value
            mtime
            ctime
            editor
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
        address {
          id
          siteid
          type
          parentid
          addressid
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
          status
          longitude
          latitude
          birthday
          position
          mtime
          ctime
          editor
        }
        coupon {
          code
        }
        product {
          id
          siteid
          parentid
          orderproductid
          orderaddressid
          type
          stocktype
          prodcode
          productid
          parentproductid
          vendor
          scale
          quantity
          qtyopen
          currencyid
          price
          costs
          rebate
          taxrates
          taxvalue
          taxflag
          name
          description
          mediaurl
          timeframe
          position
          notes
          statuspayment
          statusdelivery
          target
          flags
          mtime
          ctime
          editor
          attribute {
            id
            siteid
            parentid
            attributeid
            type
            code
            name
            value
            price
            quantity
            mtime
            ctime
            editor
          }
          product {
            id
            siteid
            parentid
            orderproductid
            orderaddressid
            type
            stocktype
            prodcode
            productid
            parentproductid
            vendor
            scale
            quantity
            qtyopen
            currencyid
            price
            costs
            rebate
            taxrates
            taxvalue
            taxflag
            name
            description
            mediaurl
            timeframe
            position
            notes
            statuspayment
            statusdelivery
            target
            flags
            mtime
            ctime
            editor
            attribute {
              id
              siteid
              parentid
              attributeid
              type
              code
              name
              value
              price
              quantity
              mtime
              ctime
              editor
            }
          }
        }
        service {
          id
          siteid
          serviceid
          type
          code
          name
          currencyid
          price
          costs
          rebate
          taxrates
          taxvalue
          taxflag
          position
          mediaurl
          mtime
          ctime
          editor
          attribute {
            id
            siteid
            parentid
            attributeid
            type
            code
            name
            value
            price
            quantity
            mtime
            ctime
            editor
          }
          transaction {
            id
            siteid
            parentid
            config
            status
            currencyid
            type
            price
            costs
            rebate
            taxvalue
            taxflag
            mtime
            ctime
            editor
          }
        }
        status {
            id
            siteid
            parentid
            type
            value
            mtime
            ctime
            editor
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
      "editor": "aimeos@aimeos.org",
      "address": [{
        "id": "2",
        "siteid": "1.",
        "type": "payment",
        "parentid": "1",
        "addressid": "1",
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
        "position": 0,
        "mtime": "2022-06-01 08:55:25",
        "ctime": "2022-06-01 08:55:25",
        "editor": "aimeos@aimeos.org"
      }],
      "coupon": [{
        "code": "discount-10",
      }],
      "product": [{
        "id": "4",
        "siteid": "1.",
        "parentid": "1",
        "orderaddressid": "",
        "type": "default",
        "stocktype": "default",
        "prodcode": "demo-bundle",
        "productid": "1",
        "parentproductid": "",
        "vendor": "Aimeos",
        "scale": "1.0",
        "quantity": 1,
        "qtyopen": 1,
        "currencyid": "EUR",
        "price": "100.00",
        "costs": "5.00",
        "rebate": "0.00",
        "taxrates": "{\"tax\":\"20.00\"}",
        "taxvalue": "17.5000",
        "taxflag": 1,
        "name": "Dress bundle",
        "description": "",
        "mediaurl": "https://aimeos.org/media/default/product_01_A-low.webp",
        "timeframe": "",
        "position": 1,
        "notes": "",
        "statuspayment": -1,
        "statusdelivery": -1,
        "target": "",
        "flags": 0,
        "mtime": "2022-06-01 08:55:25",
        "ctime": "2022-06-01 08:55:25",
        "editor": "aimeos@aimeos.org",
        "attribute" [{
          "id": "2",
          "siteid": "1.",
          "parentid": "4",
          "attributeid": "42",
          "type": "custom",
          "code": "text",
          "name": "Custom text",
          "value": "Me, myself and I",
          "price": "0.00",
          "quantity": 1,
          "mtime": "2022-06-01 08:55:25",
          "ctime": "2022-06-01 08:55:25",
          "editor": "aimeos@aimeos.org",
        }],
        "product": [{
          "id": "5",
          "siteid": "1.",
          "parentid": "1",
          "orderproductid": "4",
          "orderaddressid": "",
          "type": "default",
          "stocktype": "default",
          "prodcode": "demo-article",
          "productid": "1",
          "parentproductid": "",
          "vendor": "Aimeos",
          "scale": "1.0",
          "quantity": 1,
          "qtyopen": 1,
          "currencyid": "EUR",
          "price": "100.00",
          "costs": "5.00",
          "rebate": "0.00",
          "taxrates": "{\"tax\":\"20.00\"}",
          "taxvalue": "17.5000",
          "taxflag": 1,
          "name": "Dark grey dress",
          "description": "",
          "mediaurl": "https://aimeos.org/media/default/product_01_A-low.webp",
          "timeframe": "",
          "position": 1,
          "notes": "",
          "statuspayment": -1,
          "statusdelivery": -1,
          "target": "",
          "flags": 0,
          "mtime": "2022-06-01 08:55:25",
          "ctime": "2022-06-01 08:55:25",
          "editor": "aimeos@aimeos.org",
          "attribute" []
        }],
      }],
      "service": [{
        "id": "3",
        "siteid": "1.",
        "parentid": "1",
        "orderserviceid": "1",
        "type": "delivery",
        "code": "demo-pickup",
        "name": "Click & Collect",
        "currencyid": "EUR",
        "price": "0.00",
        "costs": "0.00",
        "rebate": "0.00",
        "taxrates": "{\"tax\":\"0.00\"}",
        "taxvalue": "0.0000",
        "taxflag": 1,
        "position": 0,
        "mediaurl": "",
        "mtime": "2022-06-01 08:55:25",
        "ctime": "2022-06-01 08:55:25",
        "editor": "aimeos@aimeos.org",
        "attribute" []
      }, {
        "id": "4",
        "siteid": "1.",
        "parentid": "1",
        "orderserviceid": "6",
        "type": "payment",
        "code": "demo-sepa",
        "name": "Direct debit",
        "currencyid": "EUR",
        "price": "0.00",
        "costs": "0.00",
        "rebate": "0.00",
        "taxrates": "{\"tax\":\"0.00\"}",
        "taxvalue": "0.0000",
        "taxflag": 1,
        "position": 0,
        "mediaurl": "",
        "mtime": "2022-06-01 08:55:25",
        "ctime": "2022-06-01 08:55:25",
        "editor": "aimeos@aimeos.org",
        "attribute" [{
          "id": "8",
          "siteid": "1.",
          "parentid": "4",
          "attributeid": "",
          "type": "hidden",
          "code": "txid",
          "name": "Transaction ID",
          "value": "abcd1234",
          "price": "0.00",
          "quantity": 1,
          "mtime": "2022-06-01 08:55:30",
          "ctime": "2022-06-01 08:55:30",
          "editor": "aimeos@aimeos.org",
        }]
      }],
      "status": [{
        "id": "3",
        "siteid": "1.",
        "parentid": "1",
        "type": "email-payment",
        "value": "5",
        "mtime": "2022-06-01 08:55:30",
        "ctime": "2022-06-01 08:55:30",
        "editor": "aimeos@aimeos.org",
      }]
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
          address {
            company
          }
          coupon {
            code
          }
          product {
            id
            prodcode
            product {
              id
              prodcode
            }
          }
          service {
            code
          }
          status {
            type
          }
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
          address {
            company
          }
          coupon {
            code
          }
          product {
            id
            prodcode
            product {
              id
              prodcode
            }
          }
          service {
            code
          }
          status {
            type
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
          address {
            company
          }
          coupon {
            code
          }
          product {
            id
            prodcode
            product {
              id
              prodcode
            }
          }
          service {
            code
          }
          status {
            type
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
          "editor": "aimeos@aimeos.org",
          "address": [{
            "company": "Test company"
          }],
          "coupon": [{
            "code": "fixed"
          }],
          "product": [{
            "id": "4",
            "prodcode": "demo-selection",
            "product": [{
              "id": "5",
              "prodcode": "demo-article"
            }],
          }],
          "service": [{
            "code": "demo-pickup"
          }, {
            "code": "demo-sepa"
          }],
          "status": [{
            "type": "email-payment"
          }, {
            "type": "email-payment"
          }]
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
          "editor": "aimeos@aimeos.org",
          "address": [{
            "company": "Example company"
          }],
          "coupon": [],
          "product": [{
            "id": "5",
            "prodcode": "demo-article-2"
          }],
          "service": [{
            "code": "demo-dhl"
          }, {
            "code": "demo-invoice"
          }],
          "status": [{
            "type": "email-payment"
          }, {
            "type": "email-payment"
          }]
        }
      ],
      "total": 2
    }
  }
}
```

# Save single order

!!! note
    You can only update basic order data and update or add order addresses, products, services, product attributes, servive attributes/transactions or statuses (not coupons) but not remove existing entries!

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

!!! note
    You can only update basic order data and update or add order addresses, products, services, product attributes, servive attributes/transactions or statuses (not coupons) but not remove existing entries!

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

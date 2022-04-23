Products can be added and removed from the basket as well as some attributes of each product entry in the basket changed. For the start, you need to [fetch one or more products](basics.md) using the product resource from the [OPTIONS response](index.md).

Each listed product will contain the link how it could be added to the basket:

```json
{
    "data": [{
        "id": "1",
        "type": "product",
        "links": {
            "self": {
                "href": "http://localhost:8000/jsonapi/product?id=1",
                "allow": ["GET"]
            },
            "basket\/product": {
                "href": "http://localhost:8000/jsonapi/basket?id=default&related=product",
                "allow": ["POST"]
            }
        },
    }]
}
```

The URL to add the product to the basket is in `data['links']['basket/product']['href']`

!!! warning
    Don't take these URLs for granted! They change depending on the route configuration and the application.

# Add products

When adding a product to the basket, you can specify some more attributes than just the product ID which are all optional:

quantity
: Amount of products that will be added to the basket

stocktype
: Warehouse or local store where the product is available

vendor
: Name of the vendor, e.g. the site name or the supplier name

siteid
: ID of the site whose vendor will ship the bought product (in multi-site environments)

variant
: List of product attribute IDs that uniquely determine the article of a selection product

config
: Additional options the customer can buy for this product

custom
: Map of attribute ID and custom value pairs for data entered by the customer (e.g. text)

To add a simple product to the basket may look like this:

=== "CURL"
    ```bash
    curl -b cookies.txt -c cookies.txt \
    -X POST 'http://localhost:8000/jsonapi/basket?id=default&related=product&_token=...' \
    -H 'Content-Type: application/json' \
    -d '{"data": [{
        "attributes": {
            "product.id": "1",
            "quantity": 1,
            "stocktype": "default"
        }
    }]}'
    ```
=== "jQuery"
    ```javascript
    var data = {'data': [{
        'attributes': {
            'product.id': '1', // from product response
            'quantity': 1, // optional
            'stocktype': 'default', // warehouse code (optional)
        }
    }]};

    var url = response['data'][0]['links']['basket/product']['href']; // from product response

    if(response['meta']['csrf']) { // add CSRF token if available and therefore required
        var csrf = {};
        csrf[response['meta']['csrf']['name']] = response['meta']['csrf']['value'];
        url += (url.indexOf('?') === -1 ? '?' : '&') + $.param(csrf);
    }

    $.ajax({
        url: url,
        method: "POST",
        dataType: "json",
        data: JSON.stringify(data)
    }).done( function( result ) {
        console.log( result );
    });
    ```

Then the response will contain an additional "relationships" entry in the basket data that points to the order product entry in the "included" section:

```json
{
    "meta": {
        "total": 1,
        "prefix": null,
        "content-baseurl": "/"
    },
    "links": {
        "self": {
            "href": "http://localhost:8000/jsonapi/basket?id=defaul",
            "allow": ["DELETE","GET","PATCH", "POST"]
        }
    },
    "data": {
        "id": "default",
        "type": "basket",
        "links": {
            "self": {
                "href": "http://localhost:8000/jsonapi/basket?id=default",
                "allow": ["DELETE", "GET", "PATCH", "POST"]
            }
        },
        "attributes": {
            "order.base.id": null,
            "order.base.customerid": "",
            "order.base.sitecode": "",
            "order.base.languageid": "en",
            "order.base.currencyid": "EUR",
            "order.base.price": "100.00",
            "order.base.costs": "5.00",
            "order.base.rebate": "0.00",
            "order.base.status": 0,
            "order.base.comment": ""
        },
        "relationships": {
            "basket\/product": {
                "data": [{
                    "type": "basket\/product",
                    "id": 0
                }]
            }
        }
    },
    "included": [{
        "id": 0,
        "type": "basket\/product",
        "attributes": {
            "order.base.product.id": null,
            "order.base.product.type": "default",
            "order.base.product.stocktype": "default",
            "order.base.product.vendor": "",
            "order.base.product.productid": "7",
            "order.base.product.prodcode": "demo-article",
            "order.base.product.name": "Demo article",
            "order.base.product.mediaurl": "http:\/\/demo.aimeos.org\/media\/1.jpg",
            "order.base.product.position": null,
            "order.base.product.price": "100.00",
            "order.base.product.costs": "5.00",
            "order.base.product.rebate": "0.00",
            "order.base.product.taxrate": "20.00",
            "order.base.product.quantity": 1,
            "order.base.product.status": -1,
            "order.base.product.flags": 0
        },
        "links": {
            "self": {
                "href": "http://localhost:8000/jsonapi/basket?id=default&related=product&relatedid=0",
                "allow": ["DELETE", "PATCH"]
            }
        }
    }]
}
```

## Selection products

For selection products you have to pass the ID of the selection product and one ID for each variant attribute type assigned to the article, so the concrete article can be identified. If you have a shirt as selection product which includes two colors, your product structure would look like this one:

Shirt product (product.type: select)

* Blue shirt article (product.type: default)
    * variant attribute type: color
    * variant attribute code: blue
* Beige shirt article (product.type: default)
    * variant attribute type: color
    * variant attribute code: beige

There's some documentation available on how to [create selection products](../../manual/products.md#selections).

You will get the selection product including its variant attributes if you add *&include=product,attribute* to the product URL:

```json
{
    "data": {
        "id": "4",
        "type": "product",
        "attributes": {
            "product.id": "4"
        },
        "relationships": {
            "attribute": {
                "data": [{
                    "id": "2",
                    "type": "product",
                    "attributes": {
                        "product.lists.id": "1",
                        "product.lists.domain": "product",
                        "product.lists.refid": "2",
                        "product.lists.datestart": null,
                        "product.lists.dateend": null,
                        "product.lists.config": [],
                        "product.lists.position": 0,
                        "product.lists.status": 1,
                        "product.lists.type": "default"
                    }
                },{
                    "id": "3",
                    "type": "product",
                    "attributes": {
                        "product.lists.id": "2",
                        "product.lists.domain": "product",
                        "product.lists.refid": "3",
                        "product.lists.datestart": null,
                        "product.lists.dateend": null,
                        "product.lists.config": [],
                        "product.lists.position": 1,
                        "product.lists.status": 1,
                        "product.lists.type": "default"
                    }
                }]
            }
        }
    },
    "included": [{
        "id": "2",
        "type": "product",
        "attributes": {
            "product.id": "2"
        },
        "relationships": {
            "attribute": {
                "data": [{
                    "id": "2",
                    "type": "attribute",
                    "attributes": {
                        "product.lists.id": "1",
                        "product.lists.domain": "attribute",
                        "product.lists.refid": "2",
                        "product.lists.datestart": null,
                        "product.lists.dateend": null,
                        "product.lists.config": [],
                        "product.lists.position": 0,
                        "product.lists.status": 1,
                        "product.lists.type": "variant"
                    }
                }]
            }
        }
    },{
        "id": "3",
        "type": "product",
        "attributes": {
            "product.id": "3"
        },
        "relationships": {
            "attribute": {
                "data": [{
                    "id": "5",
                    "type": "attribute",
                    "attributes": {
                        "product.lists.id": "2",
                        "product.lists.domain": "attribute",
                        "product.lists.refid": "5",
                        "product.lists.datestart": null,
                        "product.lists.dateend": null,
                        "product.lists.config": [],
                        "product.lists.position": 1,
                        "product.lists.status": 1,
                        "product.lists.type": "variant"
                    }
                }]
            }
        }
    },{
        "id": "1",
        "type": "attribute",
        "attributes": {
            "attribute.id": "1",
            "attribute.domain": "product",
            "attribute.type": "color",
            "attribute.code": "demo-blue",
            "attribute.label": "Demo: Blue",
            "attribute.status": 1,
            "attribute.position": 0
        },
    }, {
        "id": "5",
        "type": "attribute",
        "attributes": {
            "attribute.id": "5",
            "attribute.domain": "product",
            "attribute.type": "color",
            "attribute.code": "demo-beige",
            "attribute.label": "Demo: Beige",
            "attribute.status": 1,
            "attribute.position": 1
        },
    }]
}
```

The included article products (*product.lists.domain*: **product** and *product.lists.type*: **default**) reference the variant attribute (*product.lists.domain*: **attribute** and *product.lists.type*: **variant**) for each article.

Here, the attributes with the IDs "1" and "5" are the variant attributes because the *product.lists.type* in

```relationships['attribute']['data'][*]['attributes']['product.lists.type']```

is **variant** in the included articles. Pass the ID of the variant attribute the user has chosen in the request to the server:

=== "CURL"
    ```bash
    curl -b cookies.txt -c cookies.txt \
    -X POST 'http://localhost:8000/jsonapi/basket?id=default&related=product&_token=...' \
    -H 'Content-Type: application/json' \
    -d '{"data": [{
        "attributes": {
            "product.id": "4",
            "variant": ["5"]
        }
    }]}'
    ```
=== "jQuery"
    ```javascript
    var data = {"data": [{
        "attributes": {
            "product.id": '4', // from product response
            "variant": ['5'], // one variant attribute ID for each variant dimension
        }
    }]};

    var url = response['data'][0]['links']['basket/product']['href']; // from product response

    if(response['meta']['csrf']) { // add CSRF token if available and therefore required
        var csrf = {};
        csrf[response['meta']['csrf']['name']] = response['meta']['csrf']['value'];
        url += (url.indexOf('?') === -1 ? '?' : '&') + $.param(csrf);
    }

    $.ajax({
        url: url,
        method: "POST",
        dataType: "json",
        data: JSON.stringify(data)
    }).done( function( result ) {
        console.log( result );
    });
    ```

!!! tip
    The response for selection products tends to get big if all articles, texts, images and attributes are included. You can limit the returned fields using the [fields parameter](basics.md#return-specific-fields-only). This works for the relationship fields, too, if you use e.g. *&fields[product/lists]=product.lists.type* to return the type of the product resp. attribute relationship only.

## Configurable options

You also get the config attribute IDs from the product response if you've used *&include=attribute* and if there are configurable attribute options available:

```json
{
    "data": {
        "id": "1",
        "type": "product",
        "attributes": {
            "product.id": "1"
        },
        "relationships": {
            "attribute": {
                "data": [{
                    "id": "2",
                    "type": "attribute",
                    "attributes": {
                        "product.lists.id": "3",
                        "product.lists.domain": "attribute",
                        "product.lists.refid": "2",
                        "product.lists.datestart": null,
                        "product.lists.dateend": null,
                        "product.lists.config": [],
                        "product.lists.position": 0,
                        "product.lists.status": 1,
                        "product.lists.type": "config"
                    }
                },{
                    "id": "6",
                    "type": "attribute",
                    "attributes": {
                        "product.lists.id": "4",
                        "product.lists.domain": "attribute",
                        "product.lists.refid": "6",
                        "product.lists.datestart": null,
                        "product.lists.dateend": null,
                        "product.lists.config": [],
                        "product.lists.position": 1,
                        "product.lists.status": 1,
                        "product.lists.type": "config"
                    }
                }]
            }
        }
    },
    "included": [{
        "id": "2",
        "type": "attribute",
        "attributes": {
            "attribute.id": "2",
            "attribute.domain": "product",
            "attribute.type": "print",
            "attribute.code": "demo-print-small",
            "attribute.label": "Demo: Small print",
            "attribute.status": 1,
            "attribute.position": 0
        },
    }, {
        "id": "6",
        "type": "attribute",
        "attributes": {
            "attribute.id": "6",
            "attribute.domain": "product",
            "attribute.type": "print",
            "attribute.code": "demo-print-large",
            "attribute.label": "Demo: Large print",
            "attribute.status": 1,
            "attribute.position": 1
        },
    }]
}
```

The response contains two configurable attributes with the IDs "2" and "6" because the *product.lists.type* in

```data['relationships']['attribute']['data'][*]['attributes']['product.lists.type']```

is **config**. Now add all of those configurable attribute IDs and their quantities (`"<id>"': <qty>` pairs) the user selected to the request. The example below adds the "large print" option with a quantity of "2" to the basket product:

=== "CURL"
    ```bash
    curl -b cookies.txt -c cookies.txt \
    -X POST 'http://localhost:8000/jsonapi/basket?id=default&related=product&_token=...' \
    -H 'Content-Type: application/json' \
    -d '{"data": [{
        "attributes": {
            "product.id": "1",
            "config": {
                "6": 2
            }
        }
    }]}'
    ```
=== "jQuery"
    ```javascript
    var data = {'data': [{
        'attributes': {
            'product.id': '1', // from product response
            'config': {
                '6': 2 // config attribute IDs/quantity pairs
            },
        }
    }]};

    var url = response['data'][0]['links']['basket/product']['href']; // from product response

    if(response['meta']['csrf']) { // add CSRF token if available and therefore required
        var csrf = {};
        csrf[response['meta']['csrf']['name']] = response['meta']['csrf']['value'];
        url += (url.indexOf('?') === -1 ? '?' : '&') + $.param(csrf);
    }

    $.ajax({
        url: url,
        method: "POST",
        dataType: "json",
        data: JSON.stringify(data)
    }).done( function( result ) {
        console.log( result );
    });
    ```

## Custom options

Custom attributes are a way to add values like a date, a text or even a custom price to an ordered product. They are included in the product response if you've added *&include=attribute* and if there are custom attribute options available:

```json
{
    "data": {
        "id": "1",
        "type": "product",
        "attributes": {
            "product.id": "6"
        },
        "relationships": {
            "attribute": {
                "data": [{
                    "id": "3",
                    "type": "attribute",
                    "attributes": {
                        "product.lists.id": "5",
                        "product.lists.domain": "attribute",
                        "product.lists.refid": "3",
                        "product.lists.datestart": null,
                        "product.lists.dateend": null,
                        "product.lists.config": [],
                        "product.lists.position": 0,
                        "product.lists.status": 1,
                        "product.lists.type": "custom"
                    }
                },{
                    "id": "4",
                    "type": "attribute",
                    "attributes": {
                        "product.lists.id": "6",
                        "product.lists.domain": "attribute",
                        "product.lists.refid": "4",
                        "product.lists.datestart": null,
                        "product.lists.dateend": null,
                        "product.lists.config": [],
                        "product.lists.position": 0,
                        "product.lists.status": 1,
                        "product.lists.type": "custom"
                    }
                },{
                    "id": "7",
                    "type": "attribute",
                    "attributes": {
                        "product.lists.id": "8",
                        "product.lists.domain": "attribute",
                        "product.lists.refid": "7",
                        "product.lists.datestart": null,
                        "product.lists.dateend": null,
                        "product.lists.config": [],
                        "product.lists.position": 0,
                        "product.lists.status": 1,
                        "product.lists.type": "custom"
                    }
                }]
            }
        }
    },
    "included": [{
        "id": "3",
        "type": "attribute",
        "attributes": {
            "attribute.id": "3",
            "attribute.domain": "product",
            "attribute.type": "date",
            "attribute.code": "custom",
            "attribute.label": "Custom date",
            "attribute.status": 1,
            "attribute.position": 0
        },
    }, {
        "id": "4",
        "type": "attribute",
        "attributes": {
            "attribute.id": "4",
            "attribute.domain": "product",
            "attribute.type": "price",
            "attribute.code": "custom",
            "attribute.label": "Custom price",
            "attribute.status": 1,
            "attribute.position": 0
        },
    }, {
        "id": "7",
        "type": "attribute",
        "attributes": {
            "attribute.id": "7",
            "attribute.domain": "product",
            "attribute.type": "text",
            "attribute.code": "custom",
            "attribute.label": "Custom text",
            "attribute.status": 1,
            "attribute.position": 0
        },
    }]
}
```

Now we have three possible custom attributes with the IDs "3", "4" and "7" because the *product.lists.type* in

```data['relationships']['attribute']['data'][*]['attributes']['product.lists.type']```

is **custom**. To add all of those configurable attribute IDs and their values (`"<id>": "<value>"` pairs) the user entered use a request like this passing the IDs and values of the **custom** attributes as key/value pairs:

=== "CURL"
    ```bash
    curl -b cookies.txt -c cookies.txt \
    -X POST 'http://localhost:8000/jsonapi/basket?id=default&related=product&_token=...' \
    -H 'Content-Type: application/json' \
    -d '{"data": [{
        "attributes": {
            "product.id": "6",
            "custom": {
                "3": "2020-01-01",
                "4": "100.00",
                "7": "Happy birthday"
            }
        }
    }]}'
    ```
=== "jQuery"
    ```javascript
    var data = {'data': [{
        'attributes': {
            'product.id': '6', // from product response
            'custom': { // custom attribute ID/value pairs
                '3': '2020-01-01',
                '4': '100.00',
                '7': 'Happy birthday'
            }
        }
    }]};

    var url = response['data'][0]['links']['basket/product']['href']; // from product response

    if(response['meta']['csrf']) { // add CSRF token if available and therefore required
        var csrf = {};
        csrf[response['meta']['csrf']['name']] = response['meta']['csrf']['value'];
        url += (url.indexOf('?') === -1 ? '?' : '&') + $.param(csrf);
    }

    $.ajax({
        url: url,
        method: "POST",
        dataType: "json",
        data: JSON.stringify(data)
    }).done( function( result ) {
        console.log( result );
    });
    ```

# Edit products

To edit already added products in the basket, you can send a PATCH request to the URL listed in the links section of the ordered product. Based on a response URL like this:

```
http://localhost:8000/jsonapi/basket?id=default&related=product&relatedid=0
```

you can change the quantity of the product in the basket:

quantity
: Amount of products that should be bought

Editing products in the basket should be similar to this:

=== "CURL"
    ```bash
    curl -b cookies.txt -c cookies.txt \
    -X PATCH 'http://localhost:8000/jsonapi/basket?id=default&related=product&relatedid=0&_token=...' \
    -H 'Content-Type: application/json' \
    -d '{"data": {
        "attributes": {
            "quantity": "2"
        }
    }}'
    ```
=== "jQuery"
    ```javascript
    var params = {'data': {
        'attributes': {
            'quantity': 2
        }
    }};

    // basket product URL returned from basket response
    var url = response['included'][0]['links']['self']['href'],

    if(response['meta']['csrf']) { // add CSRF token if available and therefore required
        var csrf = {};
        csrf[response['meta']['csrf']['name']] = response['meta']['csrf']['value'];
        url += (url.indexOf('?') === -1 ? '?' : '&') + $.param(csrf);
    }

    $.ajax({
        url: url,
        method: "PATCH",
        dataType: "json",
        data: JSON.stringify(params)
    }).done( function( result ) {
        console.log( result );
    });
    ```

The PATCH requests will change primarily the product data in the basket. Depending on the activated basket plugins, they can also lead to additional or fewer entries in the response:

```json
{
    "meta": {
        "total": 1,
        "prefix": "null",
        "content-baseurl": "/"
    },
    "links": {
        "self": {
            "href": "http://localhost:8000/jsonapi/basket?id=default&related=product/",
            "allow": ["DELETE","GET","PATCH"]
        }
    },
    "data": {
        "id": "default",
        "type": "basket",
        "links": {
            "self": {
                "href": "http://localhost:8000/jsonapi/basket?id=default",
                "allow": ["DELETE", "GET", "PATCH", "POST"]
            }
        },
        "attributes": {
            "order.base.id": null,
            "order.base.customerid": "",
            "order.base.sitecode": "",
            "order.base.languageid": "en",
            "order.base.currencyid": "EUR",
            "order.base.price": "200.00",
            "order.base.costs": "10.00",
            "order.base.rebate": "0.00",
            "order.base.status": 0,
            "order.base.comment": ""
        },
        "relationships": {
            "basket\/product": {
                "data": [{
                    "type": "basket\/product",
                    "id": 0
                }]
            }
        }
    },
    "included": [{
        "id": 0,
        "type": "basket\/product",
        "attributes": {
            "order.base.product.id": null,
            "order.base.product.type": "default",
            "order.base.product.stocktype": "default",
            "order.base.product.vendor": "",
            "order.base.product.productid": "7",
            "order.base.product.prodcode": "demo-article",
            "order.base.product.name": "Demo article",
            "order.base.product.mediaurl": "http:\/\/demo.aimeos.org\/media\/1.jpg",
            "order.base.product.position": null,
            "order.base.product.price": "100.00",
            "order.base.product.costs": "5.00",
            "order.base.product.rebate": "0.00",
            "order.base.product.taxrate": "20.00",
            "order.base.product.quantity": 2,
            "order.base.product.status": -1,
            "order.base.product.flags": 0
        },
        "links": {
            "self": {
                "href": "http://localhost:8000/jsonapi/basket?id=default&related=product&relatedid=0",
                "allow": ["DELETE", "PATCH"]
            }
        }
    }]
}
```

In this example the response only contains the updated product and basket details.

# Delete products

Removing product entries from the basket is done by using a DELETE request to the URL of the ordered product. In our current example the URL is:

```
http://localhost:8000/jsonapi/basket?id=default&related=product&relatedid=0
```

The code for the DELETE request itself is fairly simple:

=== "CURL"
    ```bash
    curl -b cookies.txt -c cookies.txt \
    -X DELETE 'http://localhost:8000/jsonapi/basket?id=default&related=product&relatedid=0&_token=...'
    ```
=== "jQuery"
    ```javascript
    // basket product URL returned from basket response
    var url = response['included'][0]['links']['self']['href'];

    if(response['meta']['csrf']) { // add CSRF token if available and therefore required
        var csrf = {};
        csrf[response['meta']['csrf']['name']] = response['meta']['csrf']['value'];
        url += (url.indexOf('?') === -1 ? '?' : '&') + $.param(csrf);
    }

    $.ajax({
        url: url,
        method: "DELETE",
        dataType: "json"
    }).done( function( result ) {
        console.log( result );
    });
    ```


Afterwards the product in the basket identified by the URL is removed from the basket. Depending on the activated basket plugins, more changes might have happened.

Before you can retrieve the available services (delivery and payment options), you must get the resource endpoint via the OPTIONS request. Depending on the used routes it might be something like this:

```bash
curl -X OPTIONS 'http://localhost:8000/jsonapi'
```

The response will contain the required endpoints you have to use:

```json
{
    "meta": {
        "prefix": null,
        "resources": {
            "site": "http://localhost:8000/jsonapi/service"
        }
    }
}
```

# Fetch services

Now you can retrieve site via the "service" resource you've just received from the OPTIONS response. The response of the "service" endpoint contains the list of the available services, e.g.:

=== "CURL"
    ```bash
    curl -X GET 'http://localhost:8000/jsonapi/service'
    ```
=== "Javascript"
    ```javascript
    // returned from OPTIONS call
    fetch(options.meta.resources['service']).then(result => {
        if(!result.ok) {
            throw new Error(`Response error: ${response.status}`)
        }
        return result.json()
    }).then(result => {
        console.log(result.data)
    })
    ```
=== "jQuery"
    ```javascript
    $.ajax({
        method: "GET",
        dataType: "json",
        url: options.meta.resources['service'], // returned from OPTIONS call
    }).done( function( result ) {
        console.log( result );
    });
    ```

This response contains all available services for the current site:

```json
{
    "meta": {
        "total": 1,
        "prefix": null,
        "content-baseurl": "http://localhost:8000/",
		"content-baseurls": {
			"fs-media": "http://localhost:8000/aimeos",
			"fs-mimeicon": "http://localhost:8000/vendor/shop/mimeicons",
			"fs-theme": "http://localhost:8000/vendor/shop/themes"
		},
        "csrf": {
            "name": "_token",
            "value": "..."
        }
    },
    "links": {
        "self": "http://localhost:8000/jsonapi/service"
    },
    "data": [
        {
            "id":"21",
            "type":"service",
            "links":{
                "self":{
                    "href":"http://localhost:8000/jsonapi/service?id=21",
                    "allow":["GET"]
                },
                "basket.service":{
                    "href":"http://localhost:8000/jsonapi/basket?id=default&related=service&relatedid=delivery",
                    "allow":["POST"],
                    "meta":{
                        "time.hourminute":{
                            "code":"time.hourminute",
                            "type":"time",
                            "label":"Delivery time",
                            "public":true,
                            "default":"10:25",
                            "required":true,
                            "value":null
                        },
                        "supplier.code":{
                            "code":"supplier.code",
                            "type":"list",
                            "label":"Pick-up address",
                            "public":true,
                            "default":{
                                "demo-ballroom":"Ballroom\nTest company\nTest road 10\n20000 Test town\nNY United States\ndemo2@example.com",
                                "demo-cstory":"C-Story\nTest company\nTest street 1\n10000 Test city\nNY United States\ndemo1@example.com",
                                "demo-hr":"H&R\nTest company\nTest street 1\n10000 Test city\nNY United States\ndemo1@example.com",
                                "demo-sb":"Sergio Blunic\nTest company\nTest street 1\n10000 Test city\nNY United States\ndemo1@example.com"
                            },
                            "required":true,
                            "value":null
                        }
                    }
                }
            },
            "attributes":{
                "service.id":"21",
                "service.type":"delivery",
                "service.code":"demo-pickup",
                "service.label":"Click & Collect",
                "service.provider":"Standard,Time,Supplier",
                "service.position":0,
                "service.datestart":null,
                "service.dateend":null,
                "service.status":1,
                "price":{
                    "price.id":"168",
                    "price.type":"default",
                    "price.currencyid":"USD",
                    "price.domain":"service",
                    "price.quantity":1,
                    "price.value":"0.00",
                    "price.costs":"0.00",
                    "price.rebate":"0.00",
                    "price.taxvalue":"0.0000",
                    "price.taxrates":{
                        "tax":"0.00"
                    },
                    "price.taxrate":"0.00",
                    "price.taxflag":true,
                    "price.status":1,
                    "price.label":"Demo: Click&Collect"
                }
            },
            "relationships":{
                "media":{
                    "data":[
                        {
                            "id":"125",
                            "type":"media",
                            "attributes":{
                                "service.lists.id":"149",
                                "service.lists.domain":"media",
                                "service.lists.refid":"125",
                                "service.lists.datestart":null,
                                "service.lists.dateend":null,
                                "service.lists.config":[],
                                "service.lists.position":0,
                                "service.lists.status":1,
                                "service.lists.type":"default"
                            }
                        }
                    ]
                },
                "price":{
                    "data":[
                        {
                            "id":"168",
                            "type":"price",
                            "attributes":{
                                "service.lists.id":"151",
                                "service.lists.domain":"price",
                                "service.lists.refid":"168",
                                "service.lists.datestart":null,
                                "service.lists.dateend":null,
                                "service.lists.config":[],
                                "service.lists.position":1,
                                "service.lists.status":1,
                                "service.lists.type":"default"
                            }
                        }
                    ]
                },
                "text":{
                    "data":[
                        {
                            "id":"584",
                            "type":"text",
                            "attributes":{
                                "service.lists.id":"154",
                                "service.lists.domain":"text",
                                "service.lists.refid":"584",
                                "service.lists.datestart":null,
                                "service.lists.dateend":null,
                                "service.lists.config":[],
                                "service.lists.position":2,
                                "service.lists.status":1,
                                "service.lists.type":"default"
                            }
                        },
                        {
                            "id":"585",
                            "type":"text",
                            "attributes":{
                                "service.lists.id":"155",
                                "service.lists.domain":"text",
                                "service.lists.refid":"585",
                                "service.lists.datestart":null,
                                "service.lists.dateend":null,
                                "service.lists.config":[],
                                "service.lists.position":3,
                                "service.lists.status":1,
                                "service.lists.type":"default"
                            }
                        }
                    ]
                }
            }
        },
        {
            "id":"26",
            "type":"service",
            "links":{
                "self":{
                    "href":"http://localhost:8000/jsonapi/service?id=26",
                    "allow":["GET"]
                },
                "basket.service":{
                    "href":"http://localhost:8000/jsonapi/basket?id=default&related=service&relatedid=payment",
                    "allow":["POST"],
                    "meta":[]
                }
            },
            "attributes":{
                "service.id":"26",
                "service.type":"payment",
                "service.code":"demo-invoice",
                "service.label":"Invoice",
                "service.provider":"PostPay",
                "service.position":0,
                "service.datestart":null,
                "service.dateend":null,
                "service.status":1,
                "price":{
                    "price.id":"178",
                    "price.type":"default",
                    "price.currencyid":"USD",
                    "price.domain":"service",
                    "price.quantity":1,
                    "price.value":"0.00",
                    "price.costs":"0.00",
                    "price.rebate":"0.00",
                    "price.taxvalue":"0.0000",
                    "price.taxrates":{
                        "tax":"10.00"
                    },
                    "price.taxrate":"10.00",
                    "price.taxflag":true,
                    "price.status":1,
                    "price.label":"Demo: Invoice"
                }
            },
            "relationships":{
                "price":{
                    "data":[
                        {
                            "id":"178",
                            "type":"price",
                            "attributes":{
                                "service.lists.id":"186",
                                "service.lists.domain":"price",
                                "service.lists.refid":"178",
                                "service.lists.datestart":null,
                                "service.lists.dateend":null,
                                "service.lists.config":[],
                                "service.lists.position":1,
                                "service.lists.status":1,
                                "service.lists.type":"default"
                            }
                        }
                    ]
                },
                "text":{
                    "data":[
                        {
                            "id":"605",
                            "type":"text",
                            "attributes":{
                                "service.lists.id":"190",
                                "service.lists.domain":"text",
                                "service.lists.refid":"605",
                                "service.lists.datestart":null,
                                "service.lists.dateend":null,
                                "service.lists.config":[],
                                "service.lists.position":3,
                                "service.lists.status":1,
                                "service.lists.type":"default"
                            }
                        },
                        {
                            "id":"606",
                            "type":"text",
                            "attributes":{
                                "service.lists.id":"191",
                                "service.lists.domain":"text",
                                "service.lists.refid":"606",
                                "service.lists.datestart":null,
                                "service.lists.dateend":null,
                                "service.lists.config":[],
                                "service.lists.position":4,
                                "service.lists.status":1,
                                "service.lists.type":"default"
                            }
                        }
                    ]
                }
            }
        }
    ],
    "included": [
        {
            "id":"125",
            "type":"media",
            "attributes":{
                "media.id":"125",
                "media.filesystem":"fs-media",
                "media.domain":"service",
                "media.label":"Demo: pickup.png",
                "media.languageid":null,
                "media.mimetype":"image/png",
                "media.type":"icon",
                "media.preview":"https://aimeos.org/media/service/pickup.png",
                "media.previews":{
                    "1":"https://aimeos.org/media/service/pickup.png"
                },
                "media.url":"https://aimeos.org/media/service/pickup.png",
                "media.status":1
            }
        },
        {
            "id":"168",
            "type":"price",
            "attributes":{
                "price.id":"168",
                "price.type":"default",
                "price.currencyid":"USD",
                "price.domain":"service",
                "price.quantity":1,
                "price.value":"0.00",
                "price.costs":"0.00",
                "price.rebate":"0.00",
                "price.taxvalue":"0.0000",
                "price.taxrates":{
                    "tax":"0.00"
                },
                "price.taxrate":"0.00",
                "price.taxflag":true,
                "price.status":1,
                "price.label":"Demo: Click&Collect"
            }
        },
        {
            "id":"178",
            "type":"price",
            "attributes":{
                "price.id":"178",
                "price.type":"default",
                "price.currencyid":"USD",
                "price.domain":"service",
                "price.quantity":1,
                "price.value":"0.00",
                "price.costs":"0.00",
                "price.rebate":"0.00",
                "price.taxvalue":"0.0000",
                "price.taxrates":{
                    "tax":"10.00"
                },
                "price.taxrate":"10.00",
                "price.taxflag":true,
                "price.status":1,
                "price.label":"Demo: Invoice"
            }
        },
        {
            "id":"584",
            "type":"text",
            "attributes":{
                "text.id":"584",
                "text.languageid":"en",
                "text.type":"short",
                "text.label":"Demo short/en: Local pick-up",
                "text.domain":"service",
                "text.content":"Local pick-up",
                "text.status":1
            }
        },
        {
            "id":"585",
            "type":"text",
            "attributes":{
                "text.id":"585",
                "text.languageid":"en",
                "text.type":"long",
                "text.label":"Demo long/en: Local pick-up",
                "text.domain":"service",
                "text.content":"Pick-up at one of our local stores",
                "text.status":1
            }
        },
        {
            "id":"605",
            "type":"text",
            "attributes":{
                "text.id":"605",
                "text.languageid":"en",
                "text.type":"short",
                "text.label":"Demo short/en: Pay by invoice",
                "text.domain":"service",
                "text.content":"Pay by invoice within 14 days",
                "text.status":1
            }
        },
        {
            "id":"606",
            "type":"text",
            "attributes":{
                "text.id":"606",
                "text.languageid":"en",
                "text.type":"long",
                "text.label":"Demo long/en: Please transfer the money",
                "text.domain":"service",
                "text.content":"Please transfer the money within 14 days to BIC: XXX, IBAN: YYY",
                "text.status":1
            }
        }
    ]
}
```

# Filter services

You can filter services by their type using the *cs_type* parameter to fetch delivery OR payment options only:

=== "CURL"
    ```bash
    curl -X GET 'http://localhost:8000/jsonapi/service?filter[cs_type]=delivery'
    ```
=== "Javascript"
    ```javascript
    const args = {
        'filter': {
            'cs_type': 'delivery'
        }
    }
    let params = {}

    if(options.meta.prefix) { // returned from OPTIONS call
        params[options.meta.prefix] = args
    } else {
        params = args
    }

    // returned from OPTIONS call
    const url = options.meta.resources['service']
        + (options.meta.resources['service'].includes('?') ? '&' : '?')
        + window.param(params) // from https://github.com/knowledgecode/jquery-param

    fetch(url).then(result => {
        if(!result.ok) {
            throw new Error(`Response error: ${response.status}`)
        }
        return result.json()
    }).then(result => {
        console.log(result.data)
    })
    ```
=== "jQuery"
    ```javascript
    var args = {
        'filter': {
            'cs_type': 'delivery'
        }
    };
    var params = {};

    if(options.meta.prefix) { // returned from OPTIONS call
        params[options.meta.prefix] = args;
    } else {
        params = args;
    }

    $.ajax({
        method: 'GET',
        dataType: 'json',
        url: options.meta.resources['service'], // returned from OPTIONS call
        data: params
    }).done( function( result ) {
        console.log( result );
    });
    ```

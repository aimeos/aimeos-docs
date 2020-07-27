Before you can retrieve the product items, you have to get to know the product resource endpoint via the OPTIONS request. Depending on the used routes it might be something like:

```bash
curl -X OPTIONS http://localhost:8000/jsonapi
```

```json
{
    "meta": {
        "prefix": "ai",
        "resources": {
            "attribute": "http://localhost:8000/jsonapi/attribute",
            "catalog": "http://localhost:8000/jsonapi/catalog",
            "product": "http://localhost:8000/jsonapi/product",
            "stock": "http://localhost:8000/jsonapi/stock",
            ...
        }
    }
}
```

Have a look at [retrieving an OPTIONS request](index.md#retrieve-meta-data) for more details.

# Fetch products

Now you can retrieve product data directly via the "product" resource you get from the OPTIONS response. As the full, unsorted list of products isn't very helpful for users, you should offer the possibilities to search for products, list them by categories and filter them by their attributes in a faceted search.

Independent of how you filter products, you will always get back a JSON object like this if you use:

```bash
curl -X GET http://localhost:8000/jsonapi/product?include=attribute,media,price,product,product/property,text
curl -X GET http://localhost:8000/jsonapi/product?ai[include]=attribute,media,price,product,product/property,text
```

```json
{
    "meta": {
        "total": 3
    },
    "links": {
        "self": "http:\/\/localhost:8000\/jsonapi\/product?include=attribute%2Cmedia%2Cprice%2Cproduct%2Cproduct%2Fproperty%2Ctext&page%5Boffset%5D=0"
    },
    "data": [{
        "id": "13",
        "type": "product",
        "links": {
            "self": {
                "href": "http:\/\/localhost:8000\/jsonapi\/product\/13",
                "allow": ["GET"]
            },
            "basket\/product": {
                "href": "http:\/\/localhost:8000\/jsonapi\/basket\/default\/product",
                "allow": ["POST"]
            }
        },
        "attributes": {
            "product.id": "13",
            "product.typename": "Article",
            "product.type": "default",
            "product.code": "demo-article",
            "product.label": "Demo article",
            "product.status": 1,
            "product.datestart": null,
            "product.dateend": null,
            "product.config": []
        },
        "relationships": {
            "product\/property": {
                "data": [
                    {"id": "12", "type": "product\/property"}
                ]
            },
            "attribute": {
                "data": [{
                    "id": "25", "type": "attribute",
                    "attributes": {"product.lists.type": "default", ...}
                }]
            },
            "media": {
                "data": [{
                    "id": "55", "type": "media",
                    "attributes": {"product.lists.type": "default", .... }
                }]
            },
            "price": {
                "data": [{
                    "id": "93", "type": "price",
                    "attributes": {"product.lists.type": "default", ...}
                }]
            },
            "text": {
                "data": [{
                    "id": "228", "type": "text",
                    "attributes": {"product.lists.type": "default", ...}
                }]
            }
        }
    }],
    "included": [{
        "id": "12",
        "type": "product\/property",
        "attributes": {
            "product.property.id": "12",
            "product.property.typename": "Package length",
            "product.property.languageid": null,
            "product.property.value": "20.00",
            "product.property.type": "package-length"
        }
    }, {
        "id": "25",
        "type": "attribute",
        "attributes": {
            "attribute.id": "25",
            "attribute.domain": "product",
            "attribute.code": "demo-black",
            "attribute.status": 1,
            "attribute.type": "color",
            "attribute.typename": "Color",
            "attribute.position": 1,
            "attribute.label": "Demo: Black"
        }
    }, {
        "id": "55",
        "type": "media",
        "attributes": {
            "media.id": "55",
            "media.domain": "product",
            "media.label": "Demo: Article 1.jpg",
            "media.languageid": null,
            "media.mimetype": "image\/jpeg",
            "media.type": "default",
            "media.typename": "Standard",
            "media.preview": "http:\/\/demo.aimeos.org\/media\/1.jpg",
            "media.url": "http:\/\/demo.aimeos.org\/media\/1-big.jpg",
            "media.status": 1
        }
    }, {
        "id": "93",
        "type": "price",
        "attributes": {
            "price.id": "93",
            "price.type": "default",
            "price.typename": "Standard",
            "price.currencyid": "EUR",
            "price.domain": "product",
            "price.quantity": 1,
            "price.value": "100.00",
            "price.costs": "5.00",
            "price.rebate": "20.00",
            "price.taxvalue": "21.0000",
            "price.taxrate": "20.00",
            "price.taxflag": false,
            "price.status": 1,
            "price.label": "Demo: Article from 1"
        }
    }, {
        "id": "228",
        "type": "text",
        "attributes": {
            "text.id": "228",
            "text.languageid": "en",
            "text.typename": "Short description",
            "text.type": "short",
            "text.label": "Demo short\/en: This is the short description",
            "text.domain": "product",
            "text.content": "This is the short description of the demo article.",
            "text.status": 1
        }
    }]
}
```

# Sort product lists

Additional to the generic filter possibilities, the product lists can be easily sorted by these keys:

* "relevance" (asc) or "-relevance" (desc)
* "name" (asc) or "-name" (desc)
* "price" (asc) or "-price" (desc)
* "ctime" (asc) or "-ctime" (desc)

=== "CURL"
	```bash
	curl -X GET http://localhost:8000/jsonapi/product?sort=...
	curl -X GET http://localhost:8000/jsonapi/product?ai[sort]=...
	```
=== "jQuery"
	```javascript
	var params = {sort: '...'};

	if(options.meta.prefix) { // returned from OPTIONS call
		params[options.meta.prefix] = params;
	}

	$.ajax({
		method: "GET",
		dataType: "json",
		url: options.meta.resources['product'], // returned from OPTIONS call
		data: params
	}).done( function( result ) {
		console.log( result );
	});
	```

Sorting by "relevance" is the default if no sort parameter is passed to the server.

# Search products by text

If you offer users a search field for products, you have to add the entered text as query parameter to the URL of the product resource you got from the OPTIONS response:

=== "CURL"
	```bash
	curl -X GET http://localhost:8000/jsonapi/product?filter[f_search]=...
	curl -X GET http://localhost:8000/jsonapi/product?ai[filter][f_search]=...
	```
=== "jQuery"
	```javascript
	var params = {filter: {f_search: '...'}};

	if(options.meta.prefix) { // returned from OPTIONS call
		params[options.meta.prefix] = params;
	}

	$.ajax({
		method: "GET",
		dataType: "json",
		url: options.meta.resources['product'], // returned from OPTIONS call
		data: params
	}).done( function( result ) {
		console.log( result );
	});
	```

# Filter products by price

To enable users to filter products by price, you need to use the *index.price:value* filter and it requires the three letter currency code as parameter in round brackets and quotation marks ("). To return only products with a price of less than 99.50 Euro, you need:

=== "CURL"
	```bash
	curl -X GET http://localhost:8000/jsonapi/product?filter[<][index.price:value("EUR")]=99.50
	curl -X GET http://localhost:8000/jsonapi/product?ai[filter][<][index.price:value("EUR")]=99.50
	```
=== "jQuery"
	```javascript
	var params = {filter: {'<': {'index.price:value("EUR")': 99.50}}};

	if(options.meta.prefix) { // returned from OPTIONS call
		params[options.meta.prefix] = params;
	}

	$.ajax({
		method: "GET",
		dataType: "json",
		url: options.meta.resources['product'], // returned from OPTIONS call
		data: params
	}).done( function( result ) {
		console.log( result );
	});
	```

Usually, you want to filter for a price range, so you need to pass an upper and a lower value:

=== "CURL"
	```bash
	# filter[&&][][>][index.price:value("EUR")]=50
	# &filter[&&][][<][index.price:value("EUR")]=100
	curl -X GET http://localhost:8000/jsonapi/product?filter[%26%26][][%3E][index.price:value("EUR")]=50&filter[%26%26][][%3C][index.price:value("EUR")]=100
	curl -X GET http://localhost:8000/jsonapi/product?ai[filter][%26%26][][%3E][index.price:value("EUR")]=50&ai[filter][%26%26][][%3C][index.price:value("EUR")]=100
	```
=== "jQuery"
	```javascript
	var params = {filter: {'&&': [
		{'>': {'index.price:value("EUR")': 50}},
		{'<': {'index.price:value("EUR")': 100}}
	]}};

	if(options.meta.prefix) { // returned from OPTIONS call
		params[options.meta.prefix] = params;
	}

	$.ajax({
		method: "GET",
		dataType: "json",
		url: options.meta.resources['product'], // returned from OPTIONS call
		data: params
	}).done( function( result ) {
		console.log( result );
	});
	```

# Retrieve categories

To display the category tree, you have to use the "catalog" resource returned by the OPTIONS method:

=== "CURL"
	```bash
	curl -X GET http://localhost:8000/jsonapi/catalog?include=catalog,media,text
	curl -X GET http://localhost:8000/jsonapi/catalog?ai[include]=catalog,media,text
	```
=== "jQuery"
	```javascript
	var params = {include: 'catalog,media,text'};

	if(options.meta.prefix) { // returned from OPTIONS call
		params[options.meta.prefix] = params;
	}

	$.ajax({
		method: "GET",
		dataType: "json",
		url: options.meta.resources['catalog'], // returned from OPTIONS call
		data: params
	}).done( function( result ) {
		console.log( result );
	});
	```

This will return the root catalog node and its direct children as well as the texts and images:

```json
{
    ...,
    "data": {
        "id": "201",
        "type": "catalog",
        "links": {
            "self": {"href": "http:\/\/localhost:8000\/jsonapi\/catalog\/201", "allow": ["GET"]},
            "product": {"href": "http:\/\/localhost:8000\/jsonapi\/product?filter%5Bf_catid%5D=201", "allow": ["GET"]}
        },
        "attributes": {
            "catalog.id": "201",
            "catalog.code": "root",
            "catalog.label": "Root",
            "catalog.status": 1,
            "catalog.config": {"css-class": "home"},
            "catalog.hasChildren": true
        },
        "relationships": {
            "catalog": {
                "data": [{
                    "id": "203", "type": "catalog",
                    "attributes": {"catalog.list.type": "default"}
                }]
            }
        }
    },
    "included": [{
        "id": "203",
        "type": "catalog",
        "links": {
            "self": {"href": "http:\/\/localhost:8000\/jsonapi\/catalog\/203", "allow": ["GET"]}
        },
        "attributes": {
            "catalog.id": "203",
            ...
        }
        "relationships": {
            "media": {
                "data": [
                    {
                        "id": "360",
                        "type": "media",
                        "attributes": {
                            "catalog.lists.type": "icon",
                            ...
                        }
                    }
                ]
            }
        }
    },
    {
        "id": "360",
        "type": "media",
        "attributes": {
            "media.id": "360",
            "media.preview": "example4.jpg",
            "media.url": "path\/to\/folder\/example4.jpg",
            ...
        }
    }
]}
```

You can repeat this with the catalog children returned in the "included" section to get their children. In **links[self]** of the children, the right URL for retrieving them is available.

# Get products by category

To get the products for a category, use the *f_catid* filter parameter:

=== "CURL"
	```bash
	curl -X GET http://localhost:8000/jsonapi/product?filter[f_catid]=...
	curl -X GET http://localhost:8000/jsonapi/product?ai[filter][f_catid]=...
	```
=== "jQuery"
	```javascript
	var params = {filter: {f_catid: ...}};

	if(options.meta.prefix) { // returned from OPTIONS call
		params[options.meta.prefix] = params;
	}

	$.ajax({
		method: "GET",
		dataType: "json",
		url: options.meta.resources['product'], // returned from OPTIONS call
		data: params
	}).done( function( result ) {
		console.log( result );
	});
	```

By default, the found products all use "default" as category list type. You can change the list type searched for by adding the *f_listtype* parameter to e.g. **promotion** to get promotional products:

=== "CURL"
	```bash
	curl -X GET http://localhost:8000/jsonapi/product?filter[f_catid]=...&filter[f_listtype]=promotion
	curl -X GET http://localhost:8000/jsonapi/product?ai[filter][f_catid]=...&ai[filter][f_listtype]=promotion
	```
=== "jQuery"
	```javascript
	var params = {filter: {f_catid: ...}};

	if(options.meta.prefix) { // returned from OPTIONS call
		params[options.meta.prefix] = params;
	}

	$.ajax({
		method: "GET",
		dataType: "json",
		url: options.meta.resources['product'], // returned from OPTIONS call
		data: params
	}).done( function( result ) {
		console.log( result );
	});
	```

# Attributes for faceted search

The product attributes for building the faceted search can be retrieved using the "attribute" resource returned by the OPTIONS method:

=== "CURL"
	```bash
	curl -X GET http://localhost:8000/jsonapi/attribute?include=media,text
	curl -X GET http://localhost:8000/jsonapi/attribute?ai[include]=media,text
	```
=== "jQuery"
	```javascript
	var params = {include: 'media,text'};

	if(options.meta.prefix) { // returned from OPTIONS call
		params[options.meta.prefix] = params;
	}

	$.ajax({
		method: "GET",
		dataType: "json",
		url: options.meta.resources['attribute'], // returned from OPTIONS call
		data: params
	}).done( function( result ) {
		console.log( result );
	});
	```

This will return the first slice of attribute items as well as the texts and images:

```json
{
    ...,
    "data": [{
        "id": "32",
        "type": "attribute",
        "links": {
            "self": {
                "href": "http:\/\/localhost:8000\/jsonapi\/attribute\/32",
                "allow": ["GET"]
            }
        },
        "attributes": {
            "attribute.id": "32",
            "attribute.domain": "product",
            "attribute.code": "demo-beige",
            "attribute.status": 1,
            "attribute.type": "color",
            "attribute.typename": "Color",
            "attribute.position": 0,
            "attribute.label": "Demo: Beige"
        },
        "relationships": {
            "media": {
                "data": [{
                    "id": "60", "type": "media"
                    "attributes": {"attribute.list.type": "default"}
                }]
            },
            "text": {
                "data": [{
                    "id": "241", "type": "text"
                    "attributes": {"attribute.list.type": "default"}
                }]
            }
        }
    }],
    "included": [{
        "id": "60",
        "type": "media",
        "attributes": {
            "media.id": "60",
            "media.domain": "attribute",
            "media.label": "Demo: beige.gif",
            "media.languageid": null,
            "media.mimetype": "image\/gif",
            "media.type": "default",
            "media.typename": "Standard",
            "media.preview": "relative/path/to/preview.jpg",
            "media.url": "relative/path/to/original.jpg",
            "media.status": 1
        }
    }, {
        "id": "241",
        "type": "text",
        "attributes": {
            "text.id": "241",
            "text.languageid": "en",
            "text.typename": "Name",
            "text.type": "name",
            "text.label": "Demo name\/en: Beige",
            "text.domain": "attribute",
            "text.content": "Beige",
            "text.status": 1
        }
    }]
}
```

Group the attributes by their "attribute.code" and sort them by "attribute.position" to make it easy for users to find the product attributes.

# Get products by attributes

If the user selects one or more of the attributes, you can get the corresponding products by adding a *f_attrid* to the product URL:

=== "CURL"
	```bash
	curl -X GET http://localhost:8000/jsonapi/product?f_attrid[]=...&f_attrid[]=...
	curl -X GET http://localhost:8000/jsonapi/product?ai[f_attrid][]=...&ai[f_attrid][]=...
	```
=== "jQuery"
	```javascript
	var params = {f_attrid: [...]};

	if(options.meta.prefix) { // returned from OPTIONS call
		params[options.meta.prefix] = params;
	}

	$.ajax({
		method: "GET",
		dataType: "json",
		url: options.meta.resources['product'], // returned from OPTIONS call
		data: params
	}).done( function( result ) {
		console.log( result );
	});
	```

Instead of *f_attrid* which combines all attributes by an **AND** condition, you can also use *f_optid* which uses an **OR** condition:

=== "CURL"
	```bash
	curl -X GET http://localhost:8000/jsonapi/product?f_optid[]=...&f_optid[]=...
	curl -X GET http://localhost:8000/jsonapi/product?ai[f_optid][]=...&ai[f_optid][]=...
	```
=== "jQuery"
	```javascript
	var params = {f_optid: [...]};

	if(options.meta.prefix) { // returned from OPTIONS call
		params[options.meta.prefix] = params;
	}

	$.ajax({
		method: "GET",
		dataType: "json",
		url: options.meta.resources['product'], // returned from OPTIONS call
		data: params
	}).done( function( result ) {
		console.log( result );
	});
	```

Or you can use *f_oneid* with pairs of attribute types and list of attribute IDs to filter for product that contains **at least one** of the attributes per type:

=== "CURL"
	```bash
	curl -X GET http://localhost:8000/jsonapi/product?f_oneid[color][]=...&f_oneid[length][]=...
	curl -X GET http://localhost:8000/jsonapi/product?ai[f_oneid][color][]=...&ai[f_oneid][length][]=...
	```
=== "jQuery"
	```javascript
	var params = {f_oneid: {
		color: [...],
		size: [...]
	}};

	if(options.meta.prefix) { // returned from OPTIONS call
		params[options.meta.prefix] = params;
	}

	$.ajax({
		method: "GET",
		dataType: "json",
		url: options.meta.resources['product'], // returned from OPTIONS call
		data: params
	}).done( function( result ) {
		console.log( result );
	});
	```

# Count matching products

For a real faceted search, you need the number of matching products per attribute and category.

## Attribute count

You can get the attribute counts by using the **aggregate** key and the corresponding *index.attribute.id* search key:

=== "CURL"
	```bash
	curl -X GET http://localhost:8000/jsonapi/product?aggregate=index.attribute.id
	curl -X GET http://localhost:8000/jsonapi/product?ai[aggregate]=index.attribute.id
	```
=== "jQuery"
	```javascript
	var params = {aggregate: 'index.attribute.id'};

	if(options.meta.prefix) { // returned from OPTIONS call
		params[options.meta.prefix] = params;
	}

	$.ajax({
		method: "GET",
		dataType: "json",
		url: options.meta.resources['product'], // returned from OPTIONS call
		data: params
	}).done( function( result ) {
		console.log( result );
	});
	```

This will return a list of "id" and "attributes" pairs where the value of "id" is the attribute ID and "attributes" is the number of products that contains that attribute:

```javascript
{
    "meta": {
        "total": 12
    },
    "data": [
        {"id":25, "type":"index.attribute.id", "attributes":"2"},
        {"id":26,"type":"index.attribute.id","attributes":"2"},
        {"id":29,"type":"index.attribute.id","attributes":"1"}
    ]
}
```

## Categories count

In the same way you can get the product counts for the categories by using the **aggregate** key and the corresponding *index.catalog.id* search key:

=== "CURL"
	```bash
	curl -X GET http://localhost:8000/jsonapi/product?aggregate=index.catalog.id
	curl -X GET http://localhost:8000/jsonapi/product?ai[aggregate]=index.catalog.id
	```
=== "jQuery"
	```javascript
	var params = {aggregate: 'index.catalog.id'};

	if(options.meta.prefix) { // returned from OPTIONS call
		params[options.meta.prefix] = params;
	}

	$.ajax({
		method: "GET",
		dataType: "json",
		url: options.meta.resources['product'], // returned from OPTIONS call
		data: params
	}).done( function( result ) {
		console.log( result );
	});
	```

This will return a list of "id" and "attributes" pairs where the value of "id" is the category ID and "attributes" is the number of products that are associated to the category:

```javascript
{
    "meta": {
        "total": 1
    },
    "data": [
        {"id":1,"type":"index.catalog.id","attributes":"3"}
    ]
}
```

# Stock levels for products

To retrieve the stock levels you need the value of the "product.code" attribute:

=== "CURL"
	```bash
	curl -X GET http://localhost:8000/jsonapi/stock?filter=[s_prodcode][]=ABCD
	curl -X GET http://localhost:8000/jsonapi/stock?ai[filter][s_prodcode][]=ABCD
	```
=== "jQuery"
	```javascript
	var params = {filter: {s_prodcode: ['ABCD']}};

	if(options.meta.prefix) { // returned from OPTIONS call
		params[options.meta.prefix] = params;
	}

	$.ajax({
		method: "GET",
		dataType: "json",
		url: options.meta.resources['stock'], // returned from OPTIONS call
		data: params
	}).done( function( result ) {
		console.log( result );
	});
	```

It returns the list of stock items for the given product codes:

```json
{
    "data": [{
        "id": "12",
        "type": "stock",
        "links": {
            "self": {
                "href": "http:\/\/localhost:8000\/jsonapi\/stock\/12",
                "allow": ["GET"]
            }
        },
        "attributes": {
            "stock.id": "12",
            "stock.productcode": "demo-article",
            "stock.stocklevel": null,
            "stock.dateback": null,
            "stock.typename": "Standard",
            "stock.type": "default"
        }
    }
]}
```

If the shop has different warehouses or local stores where customers can pick up their ordered products, you can use the *s_stocktype* parameter to fetch stock levels for different locations than the "default" one:


=== "CURL"
	```bash
	curl -X GET http://localhost:8000/jsonapi/stock?filter=[s_prodcode][]=ABCD&s_stocktype=...
	curl -X GET http://localhost:8000/jsonapi/stock?ai[filter][s_prodcode][]=ABCD&ai[s_stocktype]=...
	```
=== "jQuery"
	```javascript
	var params = {filter: {s_prodcode: ['ABCD']}};

	if(options.meta.prefix) { // returned from OPTIONS call
		params[options.meta.prefix] = params;
	}

	$.ajax({
		method: "GET",
		dataType: "json",
		url: options.meta.resources['stock'], // returned from OPTIONS call
		data: params
	}).done( function( result ) {
		console.log( result );
	});
	```

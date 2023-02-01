This article describes how to retrieve and modify data using the Aimeos GraphQL API.

!!! note
    You must be logged into the admin backend to use the GraphQL API!

# Retrieve data

GraphQL uses **query** POST requests to retrieve data from the server. There are several query methods offered by Aimeos to fetch data from different domains, e.g. for the "product" domain:

* getProduct
* findProduct
* searchProducts

Each of these methods requires different parameters:

=== "getProduct"
    ```graphql
    query {
      getProduct(id: "1") {
        id
        type
        code
        label
      }
    }
    ```
=== "findProduct"
    ```graphql
    query {
      findProduct(code: "demo-article") {
        id
        type
        code
        label
      }
    }
    ```
=== "searchProducts"
    ```graphql
    query {
      searchProducts(filter: "{}") {
        id
        type
        code
        label
      }
    }
    ```

!!! note
    The **find*()** methods are not available for all domains, only for those whose items have an unique code and whose managers implement the *find()* method!

## Example code

To retrieve a list of products using code like this:

```javascript
const body = JSON.stringify({'query':
`query {
  searchProducts(filter: "{}") {
    id
    type
    code
    label
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

The response is a JSON data structure with the requested data:

```json
{
  "data": {
    "searchProducts": [
      {
        "id": "1",
        "type": "default",
        "code": "demo-article",
        "label": "Demo article",
      },
      {
        "id": "2",
        "type": "default",
        "code": "demo-selection-article-1",
        "label": "Demo variant article 1",
      }
    ]
  }
}
```

## Batched queries

You can use several queries on one request to reduce the number of requests:

```graphql
query {
  findCustomer(code: "demo@example.com") {
    id
    type
    code
    label
  }
  searchProducts(filter: "{}") {
    id
    type
    code
    label
  }
}
```

The result is a batched query with a response like this one:

```json
{
  "data": {
    "findCustomer": {
      "id": "2",
      "code": "demo@example.com",
      "label": "Test User (Test company)"
    },
    "searchProducts": [
      {
        "id": "1",
        "type": "default",
        "code": "demo-article",
        "label": "Demo article"
      },
      {
        "id": "2",
        "type": "default",
        "code": "demo-selection-article-1",
        "label": "Demo variant article 1"
      }
    ]
  }
}
```

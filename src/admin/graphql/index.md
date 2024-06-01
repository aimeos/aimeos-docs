Since 2022.10, Aimeos contains a GraphQL API for administration. It allows full access to all shop data and is especially useful to manage the content.

There's no common entry point to access the GraphQL API. This depends on the host application and you have to retrieve the GraphQL URL from the admin HTML pages. The URL of the GraphQL API is stored in the `data` attribute of the HTML node with class àimeos`:

```html
<div class="aimeos" data-graphql="https://yourdomain.com/admin/default/graphql">
```

You can retrieve the URL easily using:

```javascript
'<GraphQL URL>'
```

!!! note
    Because you can retrieve and modify all shop content, the GraphQL API is protected and requires an administrative users to be logged in before they can use the API. What actions the GraphQL API allows depends on the permissions the user has (superuser, admin or editor). You can adapt the permissions by configuring the `admin/graphql/resource/` sections. Take a look at the [default permissions](https://github.com/aimeos/ai-admin-graphql/blob/master/config/admin/graphql/resource.php) for reference.

To authenticate, you have to send the cookies with each request and (for Laravel only) the `X-CSRF-TOKEN` as header:

```javascript
const body = JSON.stringify({'query':
`query {
  searchProducts(filter: "{}") {
    items {
      id
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
    if(!response.ok) {
        throw new Error(response.statusText)
    }
	return response.json();
}).then(result => {
    if(result.errors) {
        throw result.errors
    }
    return result
}).catch(err => {
    console.error(err)
});
```

When you've managed to authenticate and got the base URL, you can start working with the Aimeos GraphQL API.

!!! tip
    If you think there something missing in the API or you have suggestions how to improve it and make it even easier, feel free to drop us a note on [GitHub](https://github.com/aimeos/ai-admin-graphql) or in the [Aimeos forum](https://aimeos.org/help/help-f15/).

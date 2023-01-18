Since 2022.10, Aimeos contains a GraphQL API for administration. It allows full access to all shop data and is especially useful to manage the content.

There's no common entry point to access the GraphQL API. This depends on the host application and you have to retrieve the GraphQL URL from the admin HTML pages. The URL of the GraphQL API is stored in the `data` attribute of the HTML node with class àimeos`:

```html
<div class="aimeos" data-graphql="https://yourdomain.com/admin/default/graphql">
```

You can retrieve the URL easily using:

```javascript
$('.aimeos').data('graphql')
```

!!! note
    Because you have access to all shop content, the GraphQL API is protected and the administrative users must be logged in before they can use the API.

To authenticate, you have to send the cookies with each request and (for Laravel only) the `X-CSRF-TOKEN`:

```javascript
const body = JSON.stringify({'query':
`query {
  searchProducts(filter: "{}") {
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

When you've managed to authenticate and got the base URL, you can start working with the Aimeos GraphQL API.

!!! tip
    If you think there something missing in the API or you have suggestions how to improve it and make it even easier, feel free to drop us a note on [GitHub](https://github.com/aimeos/ai-admin-graphql) or in the [Aimeos forum](https://aimeos.org/help/help-f15/).

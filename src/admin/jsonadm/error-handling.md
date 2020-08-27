Errors can an will occur sooner or later. The [JSON API](https://jsonapi.org/) standard like every REST protocol uses the HTTP status codes to signal error conditions. Used HTTP status codes are:

* 2xx : Successful operation
    * 200 : Operation was performed successfully
    * 201 : Resource has been created
* 4xx : Bad request
    * 401 : Authentication required
    * 403 : Operation is forbidden/unsupported
    * 404 : The resource wasn't found
* 5xx : Internal server error
    * 500 : A non-recoverable error occured
    * 501 : Operation not implemented

Also, the JSON API standard specifies an "errors" section in the JSON response that can contain error hints for one or more operations:

```json
{
    "errors": [{
		"title": "No product with ID 1 available",
		"detail": "<stack trace where the error occured>"
    }]
}
```

Each error item contains a "title" attribute that contains the error message for the user and the "detail" attribute including the stack trace for developers. Returning the stack trace has no security implications because the REST client is authenticated and needs administrator or editor privileges to use the JSON API. For usability reasons, you should show the error details only on request.

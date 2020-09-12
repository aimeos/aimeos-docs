Since 2016.01, Aimeos contains a JSON API modeled after the guidelines of <https://jsonapi.org/>. It allows full access to all shop data and is especially useful to manage the content.

There's no common entry point to access the JSON API. This depends on the host application and you have to retrieve the initial base URL from a configuration setting. Also, the resource URLs are different depending on the environment but you can get the available ones by querying the meta data from the base URL (via the HTTP OPTIONS method).

!!! note
    Because you have access to all shop content, the JSON API is protected and the administrative users must be logged in before they can use the API.

When you've managed to authenticate your client and got the base URL from the configuration settings, you can start working with the Aimeos JSON API:

* [Retrieve metadata](metadata.md)
* [Search and filter](search-filter.md)
* [Manage resources](manage-resources.md)
* [Manage trees](manage-trees.md)
* [Error handling](error-handling.md)

!!! tip
    If you think there something missing in the API or you have suggestions how to improve it and make it even easier, feel free to drop us a note on [GitHub](https://github.com/aimeos/ai-admin-jsonadm) or in the [Aimeos forum](https://aimeos.org/help/help-f15/).

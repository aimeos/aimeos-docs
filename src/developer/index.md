Aimeos uses an advanced architecture that makes it incredible flexible and is also highly optimized for performance and the ability to scale. Thus, it may be different from other software you've used up to now so it's important to understand how things work in Aimeos.

## Architecture

First of all, you should have a look at the different layers within Aimeos and what is their purpose. Also, the dependency injection container (context) is important because you need it almost every time. Both are explained here:

* [Aimeos architecture](architecture.md)
* [Dependency injection container](../infrastructure/context.md)

## Customization

Aimeos is totally customizable without the need to touch any Aimeos code and you should never (!) modify any files in the Aimeos core or the official extesnions! Instead, create your own Aimeos extension for your project where you can store your own classes, templates and configuration. The structure of extensions and how to generate them is described here:

* [Aimeos extensions](extensions.md)

## Fetch and store data

The "MShop" layer using the data access / data transfer object design pattern and consists of managers and items for different data domains (from domain driven design) to interact with the storage like a relational or NoSQL database. They hide the differences between different implementations and offer a single interface for all storage services. Thus, managers allow you to store products in a document oriented storage like ElasticSearch instead of a relational database without any change in your code. How to use managers and items is described here:

* [Managing items](../models/managing-items.md)
* [Query builder](../models/search-filter.md)

## Extend managers

Sometimes, you need to store e.g. additional product data and the first idea might be to extend the product table for that. As said, Aimeos is incredible flexible and allows you to store arbitrary data in property items or attributes. Property items belong to one (product) item only while attributes can be shared between several (product) items. Thus, using properties and attributes, extending the data structures isn't necessary in most cases:

* [Manage related items](../models/managing-items.md#manage-related-items)

One valid case where you need to extend the data structure (i.e. table or document) is if you need fast filtering and sorting of the (product) items for those values. In that case, you should read:

* [Schema migrations](../infrastructure/schema-migrations.md)
* [Extend managers](../models/extend-managers.md)

# Favorite

Customers are able to mark products as their favorites. References to these products are stored in the account of the customer and are listed by the "account favorite" component. Customers can view their list of favorite products and also remove items from the list.

![Account favorite](Aimeos-account-favorite.png)

## Structure

In the ["account favorite" component](../../config/client-html/account-favorite.md#name), the products are listed similarly to the standard product list. This list is also paged if customers save a lot of products on their favorite list. Shop owners can configure the [number of products](../../config/client-html/account-favorite.md#size) that are shown per page and the [domain items](../../config/client-html/account-favorite.md#domains) which are fetched from the database (text, media, attributes, etc.).

## Templates

You can adapt the templates for the favorite component by overwriting the templates in your own extension or configuring alternative template names:

* [account favorite body](../../config/client-html/account-favorite.md#template-body)
* [account favorite header](../../config/client-html/account-favorite.md#template-header)

If you want to change the HTML structure of one of the templates, please have a look at the original versions to ensure that you don't loose essential functionality.

# History

In the "account history" component, customers can see their placed orders including the order details and the latest delivery and payment status.

![Aimeos account history](Aimeos-account-history.png)

## Structure

In the ["account history" component](../../config/client-html/account-history.md#name), the order item including the complete order base content (basket) is available for each entry. For the order details, the [common summary partials](https://github.com/aimeos/ai-client-html/tree/master/templates/client/html/common/summary) are reused, which contains the address, service and detail sections so the same information as in the checkout summary page is available.

## Templates

You can adapt the templates for the subparts by overwriting the templates in your own extension or configuring alternative template names:

* [account history body](../../config/client-html/account-history.md#template-body)
* [account history header](../../config/client-html/account-history.md#template-header)

If you want to change the HTML structure of one of the templates, please have a look at the original versions to ensure that you don't loose essential functionality.

# Profile

The profile component offers customers the ability to change their account details including billing and delivery addresses.

![Aimeos-account-profile](Aimeos-account-profile.png)

## Structure

The ["account profile" component](../../config/client-html/account-profile.md#name) contains a section for editing the customers' billing address as well as the delivery addresses if one or more is available. Delivery address can be also added there to the customer account.

## Templates

You can adapt the templates for the "account profile" component by overwriting the templates in your own extension or configuring alternative template names:

* [account profile body](../../config/client-html/account-profile.md#template-body)
* [account profile header](../../config/client-html/account-profile.md#template-header)

If you change the HTML structure of the templates, please have a look at the original versions to ensure that you don't loose essential functionality, e.g. the dynamic JS features.

# Review

The review component allows customers to rate and review products they have bought before and only for those products to prevent fake reviews. New reviews are stored with status "in review" and are only visible in the frontend after changing their status to "enabled" (can be configured).

![Aimeos-account-review](Aimeos-account-review.png)

## Structure

The ["account review" component](../../config/client-html/account-review.md#name) shows all bought products of the customer which haven't been reviewed yet by a rating (and optionally a comment).

## Templates

You can adapt the templates for the "account review" component by overwriting the templates in your own extension or configuring alternative template names:

* [account review body](../../config/client-html/account-review.md#template-body)
* [account review header](../../config/client-html/account-review.md#template-header)

If you change the HTML structure of the templates, please have a look at the original versions to ensure that you don't loose essential functionality.

## Configuration

There are additional confiugration settings available to control the "account review" component:

[client/html/account/review/size](../../config/client-html/account-review.md#size)
: Max. number of products shown for review

[client/html/account/review/days-after](../../config/client-html/account-review.md#days-after)
: Number of days before a bought product can be reviewed

[controller/frontend/review/status](../../config/controller-frontend/review.md#status)
: Status of the review after the customer review has been stored

# Subscription

In the "account subscription" component, customers can see their placed orders including the order details and the latest delivery and payment status.

![Aimeos account subscription](Aimeos-account-subscription.png)

## Structure

In the ["account subscription" component](../../config/client-html/account-subscription.md#name), the order item including the complete order base content (basket) is available for each entry. For the order details, the [common summary partials](https://github.com/aimeos/ai-client-html/tree/master/templates/client/html/common/summary) are reused, which contains the address, service and detail sections so the same information as in the checkout summary page is available.

## Templates

You can adapt the templates for the subparts by overwriting the templates in your own extension or configuring alternative template names:

* [account subscription body](../../config/client-html/account-subscription.md#template-body)
* [account subscription header](../../config/client-html/account-subscription.md#template-header)

If you want to change the HTML structure of one of the templates, please have a look at the original versions to ensure that you don't loose essential functionality.

# Watch

Visitors who create an account can watch products and will be notified if those products are back in stock or if their price decreases - depending on what the customers have chosen. They are also able to remove watched products from this list again.

![Aimeos-account-watch](Aimeos-account-watch.png)

## Structure

In the ["account watch" component](../../config/client-html/account-watch.md#name), the products are listed similarly to the standard product list. This list is also paged if customers save a lot of products on their watch list. Shop owners can configure the [number for products](../../config/client-html/account-watch.md#size) that are shown per page and the [domain items](../../config/client-html/account-watch.md#domains) which are fetched from the database (text, media, attributes, etc.). Additionally, shop owners can limit the number of products customer can watch in parallel with the [maxitems](../../config/client-html/account-watch.md#maxitems) option.

## Templates

You can adapt the templates for the "account watch" component by overwriting the templates in your own extension or configuring alternative template names:

* [account watch body](../../config/client-html/account-watch.md#template-body)
* [account watch header](../../config/client-html/account-watch.md#template-header)

If you want to change the HTML structure of one of the templates, please have a look at the original versions to ensure that you don't loose essential functionality.

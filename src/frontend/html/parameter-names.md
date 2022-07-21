For building routes in any application it's good to know which parameter names are used and if a parameter can only appear in combination with another one.

# Catalog filter and list

f_catid
: Category ID

f_name
: Category name, only when "f_catid" is available

f_sort
: Sorting within the product list with values "code", "-code", "name", "-name", "price", "-price" and "relevance". Even if it's normally a product list parameter, it's required for the filter as well

f_search
: Entered text for searching products

f_supid
: List of supplier IDs the user has filtered for. They are of the form "f_supid[]=<id>"

f_attrid
: List of attribute IDs the user has filtered for. They are of the form "f_attrid[]=<id>"

f_optid
: List of attribute IDs combined by an OR-condition. They are of the form "f_optid[]=<id>"

f_oneid
: List of attribute IDs combined by an OR-condition within the given type. They are of the form "f_oneid[<type>][]=<id>"

# Catalog list

l_page
: Page number for moving back and forth in product lists

l_size
: Number of products per page

l_type
: Layout type shown for the list, maps to "items-body-<l_type>.php" templates

# Product details

d_name (mandatory if no product ID available)
: Product name

d_prodid (mandatory if no product name available)
: Product ID, used if available

d_pos
: Product position within the current product list. It's required for the previous/next links in the product detail pages and it's only used in combination with "d_prodid"

# Basket

b_action
: Performed action, can be "add", "delete", "edit" or "coupon-delete"

b_prodid
: ID of the product to add to the basket

b_attrvarid
: Selected variant attributes to determine the article. The key must be the attribute type of the passed attribute ID.

b_attrconfid
: Associative list of IDs and quantities for the selected configurable attributes. The configurable attriubutes must contain the *qty* (*b_attrconfid[qty]*) and *id* (*b_attrconfid[id]*) keys fields and below the quantity resp. ID with the same key so Aimeos knows they belong to together, e.g. *b_attrconfid[qty][0]* and *b_attrconfid[id][0]*.

b_attrcustid
: Associative list of IDs and values for the custom attributes

b_stocktype
: Stock type (warehouse code) the product should be sent from

b_position
: Position of the product within the basket. This is required for "delete" and "edit" actions

b_quantity
: New number of products for the basket entry referenced by "b_position"

b_coupon
: Coupon code that is entered or should be removed

b_prod
: Multi-dimensional array of indexes and product  for adding multiple products at once

The value of the ''b_prod'' parameter is structured like this:

```php
b_prod[0][prodid]: 15
b_prod[0][quantity]: 1
b_prod[0][attrvarid][color]: 39
b_prod[0][attrvarid][length]: 41
b_prod[0][attrconfid][qty][]: 2
b_prod[0][attrconfid][id][]: 18
b_prod[0][attrcustid][36]: sometext
b_prod[0][stocktype]: default
b_prod[1][prodid]: 23
b_prod[1] ...
```

# Checkout

c_step
: Current step of the checkout process. If none is given the content of the first step that requires attention is displayed or the configured step (summary by default)

# Favorite products

fav_action
: Performed action, can be "add" or "delete"

fav_id
: Product ID of the favorite product

fav_page
: Page number if the user has more favorite products than the maximum number of displayed products in the favorite list

# Pinned products

pin_action
: Performed action, can be "add" or "delete"

pin_id
: Product ID of the pinned product

# Watched products

wat_action
: Performed action, can be "add", "delete" or "edit"

wat_id
: Product ID of the watched product

wat_page
: Page number if the user has more watched products than the maximum number of displayed products in the watch list

# Product downloads

dl_id
: ID of the order product attribute storing the reference to the bought file

# Locale selector

site
: Site code referencing the shop instance

locale
: Language ID for switching between available languages

currency
: Currency ID for switching between available currencies

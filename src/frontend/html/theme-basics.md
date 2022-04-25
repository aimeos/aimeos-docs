Themes are an easy way to adapt an existing design or to create a new one for an Aimeos online shop. A theme only consists of CSS and Javascript to style and animate the structural HTML. In combination with the possibility to rearrange the sub-parts of the front-end, it's a powerful way to completely redesign a shop without touching the HTML code.

The default themes are located in the [themes/client/html](https://github.com/aimeos/ai-client-html/tree/master/themes/client/html) directory of the *aimeos/ai-client-html* extension. Each theme has its own directory containing the CSS and Javascript files as well as its images. The shared Javascript files are located in the base directory, which are used by all themes.

# Structure

A theme must consist at least of these files and directories:

aimeos.css
: Common CSS styles which makes the theme unique. You may also include styles that are necessary for JS library that is used.

aimeos.js
: Additional Javascript code for animations or to modify the existing JS code.

assets/ (optional)
: Directory for all images, fonts and other media items that are used by the theme. They must be referenced relative to the aimeos.css file like "url(assets/aimeos.png)".

email.css
: Contains the CSS styles that are used by the HTML e-mails.

The CSS/JS for each component must be stored in an own file which is loaded by the browser only if the component is used at the page the customer is viewing. The files for the components are named like the components in lower case, i.e.:

```
catalog-detail.css
catalog-detail.js
```

for the catalog detail component. Please have a look into the [default theme directory](https://github.com/aimeos/ai-client-html/tree/master/themes/client/html) to see which files are available there.

# Cascading Style Sheets

CSS is a very powerful style sheet language to describe the presentation for the existing HTML structure. It is possible to create a totally different layout by using individual styles for the same HTML elements.

!!! tip
    If you want to create a new theme it is best to start with a CSS file of an existing theme. Their CSS definitions already contain a great amount of brain-power which makes them compatible with different browsers and for different devices like smartphones or tablets.

## CSS classes and selectors

Styling the HTML for a theme is pretty straight forward as each component and almost all of its child elements have CSS class attributes associated to them. The root node of each component also contains a CSS class named "aimeos". Thus, you are able to identify and style all components that belong to the web shop at once, e.g. applying a font definition to the "aimeos" CSS class.

```html
<section class="aimeos account-history">...</section>
<section class="aimeos catalog-filter">...</section>
<section class="aimeos catalog-detail">...</section>
<section class="aimeos basket-standard">...</section>
<section class="aimeos checkout-standard">...</section>
```

Furthermore, each component can be uniquely identified by its CSS class. The catalog detail component has the class "catalog-detail" for example. The names of the CSS classes for all other components follow the same naming scheme which is

```html
<component type (catalog)>-<component name (detail)>
```

Since some components are built from several subparts (e.g. the "catalog-detail" view consists of the main template and a service section), each subpart has its own CSS class (e.g. "catalog-detail-service"). Additionally, subparts of subparts have their own CSS class too if they exist. This allows you as a theme designer to uniquely identify each subpart and apply a specific styling.

!!! tip
    When defining new styles for a theme, always start with the CSS class of the subpart you want to style and then the class that is associated to the relevant HTML node, e.g.
    ```css
    .catalog-detail-basic .name {
        font-size: 125%
    }
    ```
     This uniquely identifies the node and keeps the CSS path short so the browser isn't required to check for intermediate CSS classes that aren't necessary.

For partials used several times at different locations, the same CSS classes apply to all locations. Examples for those classes are:

* product
* media-list and media-item
* price-list and price-item

!!! warning
    Don't use simple CSS classes like "product", "name" or similar for styling without a class identifying the component or the "aimeos" CSS class. This will cause side effects to the HTML the components are embedded into!

## Responsive web design

Today, we have very different device sizes starting from small smartphones with 320px width to huge TVs that span 3960px in width and countless device widths in between. The art of web design is to create pages that look great on all of these devices.

!!! tip
    Frameworks like [https://getbootstrap.com/ Twitter bootstrap] provide fluid grid systems that help developers create web sites optimized for different device sizes.

The first rule of responsive web design is: **Avoid fixed measure units like px!**
They are only useful for defining a maximum or minimum device width for media queries. If you pay no attention to this advice, your theme will scale miserably! If you define a margin of 50px to both sides of a div container it will eat up most of the space on a smartphone and won't be noticed on a 4k TV. Instead, use

* "%" for relative widths and font sizes
* "rem" for fixed widths
* "rem" for heights

Dump all thoughts about pixel perfect layouts immediately to the trash bin! Layouts must be fluid and adapt to the content, not the other way round.

# Javacript

The Javascript code of a theme should only be used to improve site usability (by doing client side checks), to display necessary content, and to create animations. It should NOT be essential to use the shop! This usually results in poor usability for your site's visitors who do not use a mouse.

The Aimeos JS theme files contains some objects that are named just like the HTML clients that are available as components:

* Aimeos
* AimeosAccountHistory
* AimeosAccountFavorite
* AimeosAccountProfile
* AimeosAccountReview
* AimeosAccountSubscription
* AimeosAccountWatch
* AimeosBasket
* AimeosBasketBulk
* AimeosBasketMini
* AimeosBasketRelated
* AimeosBasketStandard
* AimeosCatalog
* AimeosCatalogDetail
* AimeosCatalogList
* AimeosCatalogFilter
* AimeosCatalogStage
* AimeosCatalogSession
* AimeosCheckoutConfirm
* AimeosCheckoutStandard
* AimeosLocaleSelect
* AimeosPage

These Javascript objects are globally available and their methods are responsible for executing the implemented actions if the required HTML DOM nodes are available. You can extend or overwrite each method to perform additional action, another action, or no action at all. The article about [adapting existing themes](adapt-themes.md#Javascript) has more information and examples of how to do this in detail.

!!! note
    To initialize the objects and set up the available methods, the **init()** method of each object is called after the DOM is ready.

## Aimeos

This JS object contains the common methods used by more than one component.

createContainer(content)
: Creates a floating container over the page displaying the given content node

createOverlay()
: Adds an overlay on top of the current page

createSpinner()
: Adds a waiting animation in the center of the current page

removeOverlay()
: Removes an existing overlay from the current page

removeSpinner()
: Removes an existing spinner animation from the current page

loadImages()
: Lazy load product image in list views

onCloseContainer()
: Sets up the ways to close the container by the user

init()
: Initializes the setup methods

## AimeosAccountFavorite

Customers can save products and they will be listed in their personal accounts.

onRemoveProduct()
: Deletes a favorite item without page reload

init()
: Initializes the account favorite actions

## AimeosAccountHistory

The account history is a feature for the personal account of each customer displaying their orders.

onToggleDetail()
: Shows or hides the order details

init()
: Initializes the account history actions

## AimeosAccountProfile

onAddress()
: Reset and close the new address form

onAddressNew()
: Adds a new delivery address form

onCheckMandatory()
: Checks address form for missing or wrong values

## AimeosAccountSubscription

onToggleDetail()
: Shows or hides the subscription details

## AimeosAccountWatch

Each customer has a personal watch list of products. If a product is added to the watch list, customers will be notified if the price of the product decreases or the product is back in stock again.

onRemoveProduct()
: Deletes a watched item without page reload

onSaveProduct()
: Saves a modifed watched item without page reload

init()
: Initializes the account watch actions

## AimeosBasket

onBack()
: Goes back to underlying page when back or close button of the basket is clicked

updateBasket(data)
: Updates the basket without page reload

init()
: Initializes the common basket actions

## AimeosBasketBulk

bulkcomplete()
: Autocomplete for products based on entered text

autocomplete(node)
: Sets up autocompletion for the given node

add()
: Adds a new line to the bulk order form

onDelete()
: Deletes lines if clicked on the delete icon

get(attr, included)
: Returns the data for the current item

getRef(map, rel, domain, listtype, type)
: Returns the attributes for the passed domain, type and listtype

setup()
: Sets up autocompletion for bulk order form

update(row)
: Updates the price of the given row element

init()
: Initializes the basket bulk actions

## AimeosBasketMini

The small basket is responsible to display the number of products in the basket and their total price.

update()
: Updates the basket mini content using the JSON API

updateBasket()
: Updates the basket mini content

onDelete()
: Delete a product without page reload

onHideBasket()
: Hides the small basket

onShowBasket()
: Displays the small basket

init()
: Initializes the basket mini actions

## AimeosBasketStandard

This is the standard basket component displaying all details of the products as well as the delivery and payment costs of the chosen service items and any redeemed coupon codes.

onChange()
: Updates quantity and deletes products without page reload

onSubmit()
: Updates basket without page reload

onQuantity()
: Hides the update button and show only on quantity change

init()
: Initializes the basket standard actions

## AimeosCatalog

Contains common function uses in more than one catalog component.

isValidVariant(node)
: Checks if all variant attributes of a variant article have been selected

onSelectDependencies()
: Evaluates the product variant dependencies

onSelectVariant()
: Displays the associated stock level, price items and attributes for the selected product variant

onCheckVariant()
: Checks if all required variant attributes are selected

onImageVariant()
: Shows the images associated to the variant attributes

onFavoriteAction()
: Adds a product to the favorite list without page reload

onWatchAction()
: Adds a product to the watch list without page reload

toggleVariantData(item, prodId)
: Shows the variant data for the given product ID and hides the rest

init()
: Initializes the common catalog actions

## AimeosCatalogDetail

The catalog detail component shows all information that is available for a product.

addReviews(response, container)
: Adds the reviews to the passed container

fetchReviews(container)
: Fetches reviews for the product

updateReview(entry, template)
: Renders the reviews in the page

onOpenLightbox
: Opens the lightbox with big images

onSelectThumbnail()
: Initializes the slider for the thumbnail gallery (small images)

onTogglePrice()
: Initializes the slide in/out for block prices

onToggleServices()
: Initializes the slide in/out for delivery/payment services

onShowReviews()
: Initializes loading reviews

onMoreReviews()
: Initializes loading more reviews

onSortReviews()
: Initializes sorting reviews

onExpandReviews()
: Initializes expanding reviews

onAddBasket()
: Adds products to the basket without page reload

init()
: Initializes the catalog detail actions

## AimeosCatalogFilter

For displaying categories, the full text search box and the faceted search, the catalog filter component is required.

onMenuHover():
: Show mega menu

onHideCategories()
: Hide category offscreen menu

onShowCategories()
: Show category offscreen menu

onLoadSearch()
: Autocompleter for quick search

onResetSearch()
: Registers events for the catalog filter search input reset

onCheckForm()
: Sets up the form checks

onToggleAttribute()
: Toggles the attribute filters if hover isn't available

onToggleAttributes()
: Toggles the attribute filters if hover isn't available

onShowAttributes()
: Shows the attribute filter if products are available for

onSubmitAttribute()
: Submits the form when clicking on filter attribute names or counts

onSyncPrice()
: Syncs the price input field and slider

onTogglePrice()
: Toggles the price filters if hover isn't available

onToggleSearch()
: Toggles the search filters if hover isn't available

onToggleSupplier()
: Toggles the supplier filters if hover isn't available

onSubmitSupplier()
: Submits the form when clicking on filter supplier names or counts

init()
: Initialize the catalog filter actions

## AimeosCatalogList

All product lists are managed by the catalog list component.

showBasket(form)
: Shows the basket after submitting the form

setPinned()
: Marks products as pinned

onAddBasket()
: Add to basket

onScroll()
: Enables infinite scroll if available

onPin()
: Add products to pinned list

init()
: Initializes the catalog list actions

## AimeosCatalogSession

The catalog session is user content related like for the last seen products.

onToggleSeen()
: Toggles the Last Seen filters if hover isn't available

onTogglePinned()
: Toggles pinned items

onRemovePinned()
: Delete a product without page reload

init()
: Initializes the catalog session actions

## AimeosCheckoutStandard

The checkout process is represented by the checkout standard component. It's one of the multi-step components that display different content based on the given parameters.

setupAddressForms()
: Shows only selected address forms

setupCountryState()
: Shows states only from selected countries

setupServiceForms()
: Shows only form fields of selected service option

setupMandatoryCheck()
: Checks for mandatory fields in all forms

setupPaymentRedirect()
: Redirect to payment provider / confirm page when order has been created successfully

init()
: Initializes the checkout standard section

## AimeosLocaleSelect

To allow users to switch the used language and/or currency, the locale selector component provides a list of available languages and/or currencies. Both depend on the site of the shop and the combinations added by the shop owner.

setupMenuToggle()
: Keeps menu open on click resp. closes on second click

init()
: Initializes the locale selector actions

## AimeosPage

This sections contains methods that are available at all pages.

onLinkTop()
: Link to top

onMenuScroll()
: Menu transition

onHideOffscreen()
: Close offscreen on overlay click

setupOffscreen()
: Initializes offscreen menus

init()
: Initializes the page actions

## New components

If you decide to implement a new component like an additional one for the catalog views, you should also provide a new Javascript object in your aimeos.js theme file. As long as you don't need any methods to interact with the HTML DOM, only an empty init() method is  required:

```javascript
/**
 * <type> <component> client actions
 */
Aimeos<type><component> = {

    /**
     * Initializes the <type> <component> actions
     */
    init: function() {
    }
}
```

Please replace the placeholders for <type> and <component> with the appropriate names, like "Catalog" (type) and "Mycomponent" (component) depending on the names you've used for the HTML client class so you get e.g.:

```javascript
AimeosCatalogMycomponent = {}
```

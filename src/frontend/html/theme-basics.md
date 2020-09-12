Themes are an easy way to adapt an existing design or to create a new one for an Aimeos online shop. A theme only consists of CSS and Javascript to style and animate the structural HTML. In combination with the possibility to rearrange the sub-parts of the front-end, it's a powerful way to completely redesign a shop without touching the HTML code.

The default themes are located in the [client/html/themes](https://github.com/aimeos/ai-client-html/tree/master/client/html/themes) directory of the *aimeos/ai-client-html* extension. Each theme has its own directory containing the CSS and Javascript files as well as its images. The shared Javascript files are located in the base directory, which are used by all themes.

# Structure

A theme must consist of these files and directories:

email.css
: Contains the CSS styles that are used by the HTML e-mails.

aimeos.css
: All CSS styles which makes the theme unique. You may also include styles that are necessary for any jQuery plug-in that is used.

aimeos.js
: Additional Javascript code for animations or to modify the existing JS code.

media/ (optional)
: Directory for all images, fonts and other media items that are used by the theme. They must be referenced relative to the aimeos.css file like "url(images/aimeos.png)".

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

It's guaranteed that these jQuery libraries are available and included before the aimeos.js file:

* jQuery
* jQuery-migrate
* jQuery-UI (customized)

The jQuery-UI package contains the following features:

* core
* widget
* mouse
* position
* autocomplete
* menu

!!! tip
    If you need additional jQuery-UI plug-ins for your theme, you can add them to the aimeos.js file of your theme. As they can be very big, you should be careful what you want to use in your theme. Otherwise, customers will be disappointed with the page load time.

The Aimeos shared library files contains some objects that are named just like the HTML clients that are available as components:

* Aimeos
* AimeosAccountHistory
* AimeosAccountFavorite
* AimeosAccountProfile
* AimeosAccountSubscription
* AimeosAccountWatch
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

setupContainerClose()
: Sets up the ways to close the container by the user

init()
: Initializes the setup methods

## AimeosAccountFavorite

Customers can save products and they will be listed in their personal accounts.

setupProductRemoval()
: Deletes a favorite item without page reload

init()
: Initializes the account favorite actions

## AimeosAccountHistory

The account history is a feature for the personal account of each customer displaying their orders.

setupOrderShow()
: Shows order details without page reload

setupOrderClose()
: Closes the order details without page reload

init()
: Initializes the account history actions

## AimeosAccountProfile

setupAddress()
: Reset and close the new address form

setupAddressNew()
: Adds a new delivery address form

setupMandatoryCheck()
: Checks address form for missing or wrong values

## AimeosAccountSubscription

setupDetailShow()
: Shows subscription details without page reload

setupDetailClose()
: Closes the order details without page reload

## AimeosAccountWatch

Each customer has a personal watch list of products. If a product is added to the watch list, customers will be notified if the price of the product decreases or the product is back in stock again.

setupProductRemoval()
: Deletes a watched item without page reload

setupProductSave()
: Saves a modifed watched item without page reload

init()
: Initializes the account watch actions

## AimeosBasketBulk

bulkcomplete()
: Autocomplete for products based on entered text

autocomplete(node)
: Sets up autocompletion for the given node

add()
: Adds a new line to the bulk order form

delete()
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

setupBasketDelete()
: Delete a product without page reload

setupBasketToggle()
: Displays or hides the small basket

init()
: Initializes the basket mini actions

## AimeosBasketRelated

The related basket component can be used to display e.g. products related to the basket content.

init()
: Initializes the basket related actions

## AimeosBasketStandard

This is the standard basket component displaying all details of the products as well as the delivery and payment costs of the chosen service items and any redeemed coupon codes.

updateBasket(data)
: Updates the basket using the given HTML code without page reload

setupBasketBack()
: Goes back to underlying page when back or close button of the basket is clicked

setupUpdateHide()
: Hides the update button and show only on quantity change

setupUpdateSubmit()
: Updates basket without page reload

setupUpdateChange()
: Updates quantity and deletes products without page reload

init()
: Initializes the basket standard actions

## AimeosCatalog

Contains common function uses in more than one catalog component.

setupSelectionDependencies()
: Evaluates the product variant dependencies

setupSelectionContent()
: Displays the associated stock level, price items and attributes for the selected product variant

setupVariantCheck()
: Checks if all required variant attributes are selected

setupVariantImages()
: Shows the images associated to the variant attributes

setupBasketAdd()
: Adds products to the basket without page reload

setupFavoriteAction()
: Adds a product to the favorite list without page reload

setupWatchAction()
: Adds a product to the watch list without page reload

init()
: Initializes the common catalog actions

## AimeosCatalogDetail

The catalog detail component shows all information that is available for a product.

setupThumbnailSlider()
: Initializes the slider for the thumbnail gallery (small images)

setupImageSwap()
: Displays the big image and highlight thumbnail after it was selected

setupImageLightbox()
: Opens the lightbox with big images

setupBlockPriceSlider()
: Initializes the slide in/out for block prices

setupServiceSlider()
: Initializes the slide in/out for delivery/payment services

setupAdditionalContentSlider()
: Initializes the slide in/out for additional content

init()
: Initializes the catalog detail actions

## AimeosCatalogFilter

For displaying categories, the full text search box and the faceted search, the catalog filter component is required.

setupSearchAutocompletion()
: Autocompleter for quick search

setupFormChecks()
: Sets up the form checks

setupListFadeout()
: Sets up the fade out of the catalog list

setupCategoryToggle()
: Toggles the categories if hover isn't available

setupAttributeToggle()
: Toggles the attribute filters if hover isn't available

setupAttributeListsToggle()
: Toggles the attribute filters if hover isn't available

setupAttributeListsEmtpy()
: Hides the attribute filter if no products are available for

setupAttributeItemSubmit()
: Submits the form when clicking on filter attribute names or counts

setupSupplierToggle()
: Toggles the supplier filters if hover isn't available

setupSupplierItemSubmit()
: Submits the form when clicking on filter supplier names or counts

setupSearchTextReset()
: Registers events for the catalog filter search input reset

init()
: Initialize the catalog filter actions

## AimeosCatalogList

All product lists are managed by the catalog list component.

setupImageSwitch
: Switches product images on hover

setupInfiniteScroll
: Enables infinite scroll if available

init()
: Initializes the catalog list actions

## AimeosCatalogSession

The catalog session is user content related like for the last seen products.

init()
: Initializes the catalog session actions

## AimeosCatalogStage

The catalog stage component is usually placed on top of the catalog list and detail views. It can display per-category images and the breadcrumb navigation.

init()
: Initializes the catalog stage actions

## AimeosCheckoutStandard

The checkout process is represented by the checkout standard component. It's one of the multi-step components that display different content based on the given parameters.

setupAddressForms()
: Shows only selected address forms

setupSalutationCompany()
: Shows company and VAT ID fields if salutation is "company", otherwise hide the fields

setupCountryState()
: Shows states only from selected countries

setupBirthdayPicker()
: Shows date picker for birthday field

setupServiceForms()
: Shows only form fields of selected service option

setupMandatoryCheck()
: Checks for mandatory fields in all forms

setupPaymentRedirect()
: Redirect to payment provider / confirm page when order has been created successfully

init()
: Initializes the checkout standard section

## AimeosCheckoutConfirm

The last step of each successful order is the "thank you" page.

init()
: Initializes the checkout confirm section

## AimeosLocaleSelect

To allow users to switch the used language and/or currency, the locale selector component provides a list of available languages and/or currencies. Both depend on the site of the shop and the combinations added by the shop owner.

setupMenuToggle()
: Keeps menu open on click resp. closes on second click

init()
: Initializes the locale selector actions

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

Please replace the placeholders for <type> and <component> with the appropriate names, like "Catalog" (type) and "Mysubpart" (component) depending on the names you've used for the HTML client class so you get e.g.:

```javascript
AimeosCatalogMysubpart = {}
```

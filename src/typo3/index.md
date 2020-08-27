The Aimeos TYPO3 extension integrates the Aimeos e-commerce PHP library within any TYPO3 installation. The most obvious advantage of this extension is the direct, seamless and easy integration of Aimeos in an existing TYPO3 website like a company internet presence. But there is more: The Aimeos frontend can be adapted to the corporate design using usual TYPO3 techniques.

If you like Aimeos: [Give a star](https://github.com/aimeos/aimeos-typo3)

The extension provides several plug-ins for certain functionalities (product filter, article listings, detail view, basket, checkout, etc.) which can be placed anywhere on any TYPO3 page. Furthermore the Aimeos administration interface is accessible via the TYPO3 back end, with no need of extra user accounts.

1. [Install Aimeos](setup.md)
1. [Read the manual](../manual/index.md)
1. [Create an extension](../developer/extensions.md)
1. [Customize Aimeos](customize.md)
1. [Adapt the frontend](#html-frontend)
1. [Extend Aimeos](extend.md)
1. [Import data](#import-data)
1. [Optimize Aimeos](optimize.md)

# HTML Frontend

* [Overwrite existing templates](../frontend/html/overwrite-templates.md)
* [Template syntax and view helper](../infrastructure/view-helpers.md)
* [Use Fluid templates](customize.md#fluid-templates)

* [Create new subparts for existing components](../frontend/html/create-subparts.md)
* [Implement new shop components](../frontend/html/implement-components.md)
* [Extend existing components](../frontend/html/extend-components.md)

## Catalog

* [Configure catalog behavior and templates](../frontend/html/catalog-components.md)

## Basket

* [Configure basket behavior and templates](../frontend/html/basket-components.md)
* [Implement basket plug-ins](../providers/basket-plugins.md)

## Checkout

* [Configure checkout behavior and templates](../frontend/html/checkout-components.md)
* [Configure countries, regions and states](customize.md#countries-regions-and-states)
* [Change delivery and payment options](../manual/services.md)
* [Create own delivery and payment service providers](../providers/service/index.md)

## Account

* [Configure profile behavior and templates](../frontend/html/account-components.md)

## E-Mails

* [Configure payment behavior and templates](../frontend/html/email-components.md#payment)
* [Configure delivery behavior and templates](../frontend/html/email-components.md#delivery)
* [Configure product notification behavior and templates](../frontend/html/email-components.md#product-watch)

# Import data

* [Import products from CSV](../cronjobs/product-csv-import.md)
* [Import categories from CSV](../cronjobs/catalog-csv-import.md)
* [Implement recurring tasks](../cronjobs/create-job-controller.md)

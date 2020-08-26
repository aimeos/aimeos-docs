# Selector

The "locale select" component allows visitors to switch between the configured language/currency combinations. It generates menus for the available languages visitors can choose from and for the dependent currencies that are available.

## Structure

![Aimeos-locale-select](Aimeos-locale-select.png)

In the [locale select component implementation](../../config/client-html/locale-select.md#name_2), two sections are available that can be controlled via the [select subpart configuration](../../config/client-html/locale-select.md#subparts): The [language client](../../config/client-html/locale-select.md#name_1) for the language menu and the [currency client](../../config/client-html/locale-select.md#name) for the currency menu. Each of these sections can contain further subparts and they can be configured by the [language subpart](../../config/client-html/locale-select.md#standardsubparts_1) and [currency subpart](../../config/client-html/locale-select.md#standardsubparts) settings.

It's possible to pass options to the URL generator when the URLs for the menus are created:

* [Language URL settings, e.g. for absolute URLs](../../config/client-html/locale-select.md#urlconfig_1)
* [Currency URL settings, e.g. for absolute URLs](../../config/client-html/locale-select.md#urlconfig)

The target, controller and action will stay the same after the page reload when visitors click on the links for changing the language or currency.

## Templates

You can adapt the templates for the locale select component and their subparts by overwriting the templates in you own extension or configuring alternative template names:

* [template body for the select component](../../config/client-html/locale-select.md#template-body)
* [template header for the select component](../../config/client-html/locale-select.md#template-header)
* [template body for the language menu](../../config/client-html/locale-select.md#standardtemplate-body_1)
* [template body for the currency menu](../../config/client-html/locale-select.md#standardtemplate-body)

If you want to change the HTML structure of one of the templates, please have a look at the original versions to ensure that you don't loose essential functionality.
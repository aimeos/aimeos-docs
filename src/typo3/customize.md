# Change configuration

There are a lot of configuration options available and documented in the *Configuration* section.

## Frontend

To add or overwrite configuration options in TYPO3, you can use TypoScript added to the setup section of a page TypoScript template to set the values. The keys in the configuration documentation are always in the form:

```
client/html/catalog/filter/default/button = 1
```

To use such a key, replace the slashes (/) by dots (.) and prepend it with "plugin.tx_aimeos.settings.":

```typoscript
plugin.tx_aimeos.settings.client.html.catalog.filter.default.button = 1
```

If the configuration key accepts an array of values, then you can add them like this:

```typoscript
plugin.tx_aimeos.settings.client.html.catalog.filter.default.subparts {
  0 = search
  1 = tree
  2 = attribute
}
```

## Per Plugin

Several plugins provide the possibility to add plug-in specific TypoScript configuration in the "Plugin" tab of the plug-ins placed on a page. Use the configuration keys from the documentation as in the example below:

```typoscript
client.html.catalog.filter.default.button = 1
```

Slashes (/) are replaced by a dot (.) and nothing is prepended. The same works with arrays of values as well. Please have a look at the [frontend section](#frontend) above for an example.

## PageTS

TYPO3 needs a special handling for configuration options that should affect what the plugins will show in their own options view when you edit a plugin placed on a page in the backend. This is called the Page TypoScript or PageTS. Aimeos only has one setting that affects the shown plugin options and this is the selection of the site if you have several ones:

```typoscript
tx_aimeos.mshop.locale.site = myshop
```

If you have several shops in your TYPO3 installation, this setting will e.g. change categories shown in the plugin options view of the catalog filter plugin. In order to change this setting, you have to edit the page and go to the "Resources" tab. There's a text area where you can add the line above.

## Admin backend

Like the frontend, the shop administration interface can be configured as well. It's implemented as TYPO3 backend module which means that the prefix for the TypoScript configuration must be "module.tx_aimeos.settings." for all settings that should be handed over to the admin interface, e.g.

```typoscript
module.tx_aimeos.settings.mshop.locale.site = myshop
```

It doesn't make sense to assign all frontend settings also to the backend module. This would only slow down loading the administration interface. There are only a few settings that you may want to share between frontend and backend for the same page, namely the "mshop.locale.site" setting.

## Scheduler

All scheduler tasks allow adding specific TypoScript configuration for the jobs that should be executed. This is especially useful for setting or overwriting configuration values for e-mails that should be sent to customers. Use the configuration keys from the documentation as in the example below:

```typoscript
client.html.common.content.baseurl = https://yourdomain/uploads/tx_aimeos
```

The same works with arrays of values as well:

```typoscript
client.html {
    common.content.baseurl = https://yourdomain/uploads/tx_aimeos
}
controller.jobs.order.email.payment.default.status {
    0 = 5
    1 = 6
}
```
# Overwrite translations

There is the possibility to overwrite translations from the core or other Aimeos extensions via TypoScript. This is very comfortable if you only want to replace certain existing translations by your own one. For each translation, you need the ISO language code, the translation domain, the original string and the new translation, e.g.

```typoscript
plugin.tx_aimeos.settings.i18n.<ISO language code>.<number> {
  domain = <translation domain>
  string = <original English singular from source code>
  trans = <new translation>
}
```

!!! warning
    This should be used only to replace a few translations. If you would like to translate Aimeos to a new language, please use the [Transifex website](https://www.transifex.com/aimeos/public/) instead. It will be available in the next Aimeos release automatically. Also, if you need to overwrite more than a few translations, you should read the article about [adding translations](../developer/translations.md).

## Required information

ISO language code
: To specify the language for the translation, the [two letter ISO language codes (639-1)](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) are necessary. It's also possible to add the [two letter ISO country codes](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) to refer to country specific language variants like "en_GB" for British English. You can use all languages that are mapped via TypoScript from the TYPO3 language IDs. Please make sure the language code is always in lower case while the the optional country code is always in upper case.

number
: This is a continuous number to distinguish between the different translations added to the TypoScript configuration. If you are using a number twice, the later translation definition will overwrite the former one.

domain
: The translation domain where the original string is from. The Aimeos core has six translation domains: "mshop" (core lib with managers), "controller/frontend" (basic business logic for the frontend), "client" (frontend HTML parts), "controller/jobs" (asynchronous cronjob tasks) and "admin" (administration interface). To find out the domain a string is from, you have to look at the .pot files in the Aimeos core for the string.

string
: It's the original singular string from the source code or the .pot file. The string must be exactly the same (character case, white spaces, etc.) as in the English source code / .pot file! You can not use an already translated string as source.

trans
: New translation for the original string. This can be also an array, if one or more plural forms are necessary.

## Singular translations

A simple singular translation to English:

```typoscript
plugin.tx_aimeos.settings.i18n.en.0 {
  domain = client
  string = address
  trans = Addresses
}
```

A simple singular translation to US English:

```typoscript
plugin.tx_aimeos.settings.i18n.en_US.0 {
  domain = client
  string = basket
  trans = Shopping cart
}
```

Several singular translations to English:

```typoscript
plugin.tx_aimeos.settings.i18n.en {
  0 {
    domain = client
    string = basket
    trans = Basket
  }
  1 {
    domain = client
    string = address
    trans = Address
  }
}
```

Plural translation to English:

```typoscript
plugin.tx_aimeos.settings.i18n.en.0 {
  domain = client
  string = address
  trans {
    0 = Address
    1 = Addresses
  }
}
```

## Plural translations

A translations including one or more plural forms can be defined, if the original string in the source code also supports plurals. In this case the source code looks like

```
translation method>( '<domain>', '<singular>, '<plural>', <count> );
```

and the translation methods for plurals can be `translate()` or `dn()`. To overwrite a plural translation, the simplest form is:

```typoscript
plugin.tx_aimeos.settings.i18n.<ISO language code>.<number> {
  domain = <translation domain>
  string = <original singular>
  trans {
    0 = <singular translation>
    <index> = <plural translation>
}
```

The index "0" is always the singular translation. Most languages only have one plural form, so it must be defined by using the index "1". But some languages use several plural forms depending on the count given in the last parameter of the translation method. In this case, the index depends on the language and the value of <count>. To find out the right index for the language, you have to have a look into the [`getPluralIndex()` method](https://github.com/aimeos/aimeos-core/blob/master/lib/mwlib/src/MW/Translation/Base.php) that maps *count* to the index for the language you want to translate. An example for Czech would be:

```typoscript
plugin.tx_aimeos.settings.i18n.cz.0 {
  domain = client
  string = hour
  trans {
    # one hour
    0 = dlouhá hodina
    # two to four hours
    1 = dlouhé hodiny
    # more than four hours
    2 = dlouhých hodin
  }
}
```

## Special characters

Sometimes, the source string, that should be translated, contains special characters like new lines (\n) or backslashes (\). This is no problem, if you place them in a .po file of your project specific extension (same location as the original .po file) and transform its content using the Unix Gettext command, e.g.:

```bash
msgfmt -c -o de de.po
```

Using them in TypoScript is more difficult, because TypoScript doesn't allow new lines in values. Therefore, you have to use "\n" (a backslash and the character "n") as replacement:

```typoscript
plugin.tx_aimeos.settings.i18n.de.0 {
  domain = client
  string = The payment was canceled.\nDo you wish to retry your order?
  trans = Die Zahlung wurde abgebrochen.\nMöchten Sie Ihre Bestellung wiederholen?
```

If the source translation contains a backslash, it must be preserved in TypoScript:

```typoscript
plugin.tx_aimeos.settings.i18n.de.0 {
  domain = client
  string = You\'ve chosen to pay in advance
  trans = Sie haben Vorauskasse gewählt
```

# Fluid templates

All Aimeos templates are written in PHP using a template engine and view helpers that are easy to understand. It works in all integrations in the same way, is extremely fast and doesn't require you as developer to learn a new syntax.

Alternatively, you can use the TYPO3 Fluid template engine for Aimeos templates overwritten for your project. Thus, all your templates will be in the same template language.

!!! tip
    The Aimeos templates contains nested objects and their methods sometimes needs arguments. To be able to call these methods within Fluid templates, you need to install the [VHS view helper extension](https://typo3.org/extensions/repository/view/vhs) and use the `v:call()` view helper for this.

To replace an Aimeos PHP template by our own Fluid template, the Fluid template needs to be stored at the same location as you would store the PHP template, i.e. the `./client/html/templates/` folder of your project-specific Aimeos extension. You should also keep the directory structure underneath and must save the file as `<template-name>.html`, e.g.

```
./client/html/templates/catalog/detail/body-default.html
```

The file extension `.html` is important to be recognized as template that should be processed by the Fluid engine.

The Fluid view helpers available by default can't give you access to all data you need. Therefore, the Aimeos package contains some view helpers to retrieve data from Aimeos specific sources like configuration settings or translations. You have to include this view helpers by adding this to the Fluid template before using them:

```
{namespace ai=Aimeos\Aimeos\ViewHelper}
```

## Configurations

```
{ai:config(key: 'key/to/config', default: '' )}

<ai:config key="key/to/config" default="" />
```

The `ai:config` view helper retrieves the Aimeos setting for the given key, e.g. *client/html/catalog/lists/basket-add*. If no value is found for the key, the given default value (optional) is returned instead.

## Translations

```
{ai:translate(singular: 'string for singular', plural: 'string for plural', number: 1, arguments: {0: 10, 1: 'value'}, domain: 'client', escape: true)}

<ai:translate singular="string for singular" plural="string for plural" number="1" arguments="{0: 10, 1: 'value'}" domain="client" escape="true" />
```

The `ai:translate` view helper retrieves the translated value from the Aimeos Gettext files. It's similar to the `f:translate` view helper and useful for translating singular and plural phrases, e.g.

```
{ai:translate(singular: '%1$d apple', plural: '%1$d apples', number: 10, arguments: {0: 10})}
```

When the third parameter is "1", the function would return "1 apple" and for values greater than 1 it returns e.g. "10 apples". The method takes care about the different plural rules for all languages.

If the fourth argument (`arguments`) contains values, they will be used to replace the placeholders in the translated string. Internally, the [vsprintf()](https://php.net/manual/en/function.vsprintf.php) method takes care about that.

The *domain* argument is the same as used in the Aimeos `$this->translate()` view helper. In the frontend it's either "client" or "client/code" while for templates in the administration interface it's "admin".

If you don't want the output to be escaped (i.e. HTML tags returned as source), you should set the *escape* argument to *false*.

!!! note
    All arguments besides "singular" are optional.

## Blocks

The Aimeos template engine has a "block" view helper to save a rendered template so it can be inserted in another template. This is very similar to the `f:section` tags of the Fluid engine and you should replace the block view helper statements with the appropriate Fluid section tags, e.g.

```php
 <?php $this->block()->start( 'cataog/detail/actions' ); ?>
     <div class="actions">
         ...
     </div>
 <?php $this->block()->stop(); ?>
 <?php echo $this->block()->get( 'catalog/detail/actions' ); ?>
```

by this Fluid template:

```html
 <f:section name="catalog/detail/actions">
     <div class="actions">
         ...
     </div>
 </f:section>
 <f:render section="catalog/detail/actions" arguments="{...}"/>
```

# Multiple shops

Aimeos is multi-site capable and allows storing several shops in one database. In order to tell TYPO3 which shop should be used in what page tree, you have to add a TypoScript configuration for each shop page tree. This is not necessary for the page tree that should contain the first shop (site: "default").

## Create new site

In the Aimeos configuration settings within the extension manager, you can enter a site code for which a new site will be created. If it already exists, it will get updated with the required entries for the used extension version.

![Aimeos extension settings](Aimeos-settings.png)

* Admin Tools::Settings:
    1. Search for "aimeos"
    1. Enter a new site code in the corresponding input field
    1. Save and return
* Admin Tools::Extensions:
    1. Click on the update icon of the Aimeos extension

You will see a list of checks that have been done and at the end the types of data that has been added to the new site.

!!! warning
    If you update Aimeos from a previous version, you need to run the update script for all sites you've created! Otherwise, required records may be missing and existing data isn't migrated.

!!! tip
    Don't forget to create the appropriate "locale" entries for your new site in the administration interface!

## Page TS config

Some plugins display e.g. the category tree of the shop/site to be able to select one of those categories. To display the available options from the required shop/site, please insert an additional line into the PageTS field of the page:

![PageTS for multiple sites](Aimeos-pagets.png)

* Web::Page
    1. Select second page tree
    1. Edit page
    1. Tab *Resources*, section *TypoScript Configuration*

```typoscript
tx_aimeos.mshop.locale.site = <code of site>
```

Click on the icon for *Save and close document* at the top to store the change. Repeat these steps for each page tree where an other shop site other than the "default" site should be used. Clear all TYPO3 caches when you are done.

## TypoScript config

To tell the front-end that it should use another shop/site by default instead of the standard one ("default"), add a line of TypoScript to the setup config:

![Aimeos setup TS configuration](Aimeos-setupts.png)

* Web::Template
    1. Select second page tree
    1. Choose *Info/Modify* in the drop-down at the top
    1. Click on *Setup* in the box below

```typoscript
plugin.tx_aimeos.settings.mshop.locale.site = <code of site>
```

Click on the icon for *Save and close document* at the top to store the change. Repeat these steps for each page tree where an other shop site other than the "default" site should be used. Clear all TYPO3 caches when you are done.

## Site parameter

Users can switch between multiple shops if the `loc-site` parameter is included in the URL. You can configure the name of the parameter (`loc-site` by default) to a different name in the TypoScript setup section:

```typoscript
plugin.tx_aimeos.settings.typo3.param.name.site = <name of the site parameter>
```

For example, if you use the parameter "C" for the countries and that matches the site code too, then you have to add this configuration to your TypoScript setup:

```typoscript
plugin.tx_aimeos.settings.typo3.param.name.site = C
```

# Basket in navigation

Most e-commerce sites show a small basket at the top right corner of each page. The Aimeos TYPO3 extension provides a plug-in for a small basket too, containing only the number of products and the total value. You can either add this basket plug-in by

* placing the plug-in inside a column of a backend page layout
* assigning the plug-in output to a TypoScript object used in your Fluid layout

!!! tip
    Using a Typoscript object for the basket doesn't require a column in the backend page layout which easier understandable by editors as long as they shouldn't be able to place the basket plug-in themselves.

## TypoScript object

The following TypoScript code must be placed in a **TypoScript setup template**. The best place would be a .ts file in your `./fileadmin/` directory that is included in the setup section of your site. For example, create a `./fileadmin/setup.ts` file with the following content:

```typoscript
lib.navigation.basket = COA
lib.navigation.basket.10 = USER
lib.navigation.basket.10 {
    # userFunc = tx_extbase_core_bootstrap->run
    userFunc = TYPO3\CMS\Extbase\Core\Bootstrap->run
    vendorName = Aimeos
    extensionName = Aimeos
    pluginName = basket-small
    controller = Basket
    action = small
    settings =< plugin.tx_aimeos.settings
}
```

Afterwards, you have to add an include statement in the *Web::Template -> Setup* section of your root page:

```typoscript
<INCLUDE_TYPOSCRIPT: source="FILE:fileadmin/setup.ts">

plugin.tx_aimeos.settings.client.html.basket.standard.url.target = <page ID of your basket page>
plugin.tx_aimeos.settings.client.jsonapi.url.target = <page ID of your JSON API page>
```

You can find more about TypoScript includes in the [documentation of TYPO3](https://docs.typo3.org/m/typo3/reference-coreapi/master/en-us/ApiOverview/TypoScriptSyntax/Syntax/Includes.html). **Don't forget to replace the placeholders** with page ID of your basket page (without the angle brackets!). Otherwise, the small basket won't link to your basket page. Afterwards, the output of the plug-in is available as cObject in your Fluid templates:

```xml
<f:cObject typoscriptObjectPath="lib.navigation.basket" />
```

## Show in navigation

The TYPO3 [bootstrap_package](https://typo3.org/extensions/repository/view/bootstrap_package) makes it very easy to create a site using of a responsive web layout. To add the small basket to the navigation bar, you have to modify the navigation partial. Instead of changing the file in the bootstrap_package directly, you should create your own extension and add your version of this file there:

* Create a new extension using the [extension builder](https://typo3.org/extensions/repository/view/extension_builder)
* Copy the `./Resources/Private/Partials/Page/` directory to your extension using the same directory structure
* Adapt the navigation partial in `./Resources/Private/Partials/Page/Navigation/Main.html`
* Add the Fluid condition as the first child element inside the `<div class="container">` element:

```xml
<div class="container">
    <f:if condition="{f:cObject(typoscriptObjectPath:'lib.navigation.basket')}">
        <f:cObject typoscriptObjectPath="lib.navigation.basket" />
    </f:if>
    ...
</div>
```

Afterwards, add this TypoScript configuration in *Web::Template -> Constants* telling the *bootstrap_package* to look for the partials inside your extension:

```typoscript
page.fluidtemplate.partialRootPath = EXT:<your extension name>/Resources/Private/Partials/Page/
```

Now the small basket should be displayed in the navigation bar on top of your site and you can start styling the HTML.

# Countries, regions and states

## Countries

If you want to ship your products to several countries or you need to know from which countries your customers are, you have to enable the country selection in the address page of the checkout process.

By default, the country list is hidden for the billing and delivery address in the checkout process. To make show them and make them mandatory you need to add "order.base.address.countryid" to the list of values defined in

* [client/html/checkout/standard/address/billing/mandatory](../config/client-html/checkout-standard/#billingmandatory)
* [client/html/checkout/standard/address/delivery/mandatory](../config/client-html/checkout-standard/#deliverymandatory)

In TYPO3 this is configured for billing and delivery addresses via TypoScript:

```typoscript
plugin.tx_aimeos.settings.client.html.checkout.standard.address {
    billing.mandatory {
        0 = order.base.address.salutation
        1 = order.base.address.firstname
        2 = order.base.address.lastname
        3 = order.base.address.address1
        4 = order.base.address.postal
        5 = order.base.address.city
        6 = order.base.address.languageid
        7 = order.base.address.email
        8 = order.base.address.countryid
    }
    delivery.mandatory < .billing.mandatory
}
```

If no selection should be enforced, you can use instead

* [client/html/checkout/standard/address/billing/optional](../config/client-html/checkout-standard/#billingoptional)
* [client/html/checkout/standard/address/delivery/optional](../config/client-html/checkout-standard/#deliveryoptional)

In TYPO3 the country for billing and delivery addresses are optional with this TypoScript configuration:

```typoscript
plugin.tx_aimeos.settings.client.html.checkout.standard.address {
    billing.optional {
        0 = order.base.address.salutation
        1 = order.base.address.firstname
        2 = order.base.address.lastname
        3 = order.base.address.address1
        4 = order.base.address.postal
        5 = order.base.address.city
        6 = order.base.address.languageid
        7 = order.base.address.email
        8 = order.base.address.countryid
    }
    delivery.optional < .billing.optional
}
```

The list of countries is defined by the values added to the configuration key [client/html/checkout/standard/address/countries](../config/client-html/checkout-standard/#countries). The TypoScript below will add all countries worldwide to the select boxes for the billing and delivery address:

```typoscript
plugin.tx_aimeos.settings.client.html.checkout.standard.address.countries {
     0 = AD
     # Andorra
     1 = AE
     # United Arab Emirates
     2 = AF
     # Afghanistan
     3 = AG
     # Antigua and Barbuda
     4 = AI
     # Anguilla
     5 = AL
     # Albania
     6 = AM
     # Armenia
     7 = AO
     # Angola
     8 = AQ
     # Antarctica
     9 = AR
     # Argentina
     10 = AS
     # American Samoa
     11 = AT
     # Austria
     12 = AU
     # Australia
     13 = AW
     # Aruba
     14 = AX
     # Åland Islands
     15 = AZ
     # Azerbaijan
     16 = BA
     # Bosnia and Herzegovina
     17 = BB
     # Barbados
     18 = BD
     # Bangladesh
     19 = BE
     # Belgium
     20 = BF
     # Burkina Faso
     21 = BG
     # Bulgaria
     22 = BH
     # Bahrain
     23 = BI
     # Burundi
     24 = BJ
     # Benin
     25 = BL
     # Saint Barthélemy
     26 = BM
     # Bermuda
     27 = BN
     # Brunei Darussalam
     28 = BO
     # Bolivia, Plurinational State of
     29 = BQ
     # Bonaire, Sint Eustatius and Saba
     30 = BR
     # Brazil
     31 = BS
     # Bahamas
     32 = BT
     # Bhutan
     33 = BV
     # Bouvet Island
     34 = BW
     # Botswana
     35 = BY
     # Belarus
     36 = BZ
     # Belize
     37 = CA
     # Canada
     38 = CC
     # Cocos (Keeling) Islands
     39 = CD
     # Congo, the Democratic Republic of the
     40 = CF
     # Central African Republic
     41 = CG
     # Congo
     42 = CH
     # Switzerland
     43 = CI
     # Côte d'Ivoire
     44 = CK
     # Cook Islands
     45 = CL
     # Chile
     46 = CM
     # Cameroon
     47 = CN
     # China
     48 = CO
     # Colombia
     49 = CR
     # Costa Rica
     50 = CU
     # Cuba
     51 = CV
     # Cape Verde
     52 = CW
     # Curaçao
     53 = CX
     # Christmas Island
     54 = CY
     # Cyprus
     55 = CZ
     # Czech Republic
     56 = DE
     # Germany
     57 = DJ
     # Djibouti
     58 = DK
     # Denmark
     59 = DM
     # Dominica
     60 = DO
     # Dominican Republic
     61 = DZ
     # Algeria
     62 = EC
     # Ecuador
     63 = EE
     # Estonia
     64 = EG
     # Egypt
     65 = EH
     # Western Sahara
     66 = ER
     # Eritrea
     67 = ES
     # Spain
     68 = ET
     # Ethiopia
     69 = FI
     # Finland
     70 = FJ
     # Fiji
     71 = FK
     # Falkland Islands (Malvinas)
     72 = FM
     # Micronesia, Federated States of
     73 = FO
     # Faroe Islands
     74 = FR
     # France
     75 = GA
     # Gabon
     76 = GB
     # United Kingdom
     77 = GD
     # Grenada
     78 = GE
     # Georgia
     79 = GF
     # French Guiana
     80 = GG
     # Guernsey
     81 = GH
     # Ghana
     82 = GI
     # Gibraltar
     83 = GL
     # Greenland
     84 = GM
     # Gambia
     85 = GN
     # Guinea
     86 = GP
     # Guadeloupe
     87 = GQ
     # Equatorial Guinea
     88 = GR
     # Greece
     89 = GS
     # South Georgia and the South Sandwich Islands
     90 = GT
     # Guatemala
     91 = GU
     # Guam
     92 = GW
     # Guinea-Bissau
     93 = GY
     # Guyana
     94 = HK
     # Hong Kong
     95 = HM
     # Heard Island and McDonald Islands
     96 = HN
     # Honduras
     97 = HR
     # Croatia
     98 = HT
     # Haiti
     99 = HU
     # Hungary
     100 = ID
     # Indonesia
     101 = IE
     # Ireland
     102 = IL
     # Israel
     103 = IM
     # Isle of Man
     104 = IN
     # India
     105 = IO
     # British Indian Ocean Territory
     106 = IQ
     # Iraq
     107 = IR
     # Iran, Islamic Republic of
     108 = IS
     # Iceland
     109 = IT
     # Italy
     110 = JE
     # Jersey
     111 = JM
     # Jamaica
     112 = JO
     # Jordan
     113 = JP
     # Japan
     114 = KE
     # Kenya
     115 = KG
     # Kyrgyzstan
     116 = KH
     # Cambodia
     117 = KI
     # Kiribati
     118 = KM
     # Comoros
     119 = KN
     # Saint Kitts and Nevis
     120 = KP
     # Korea, Democratic People's Republic of
     121 = KR
     # Korea, Republic of
     122 = KW
     # Kuwait
     123 = KY
     # Cayman Islands
     124 = KZ
     # Kazakhstan
     125 = LA
     # Lao People's Democratic Republic
     126 = LB
     # Lebanon
     127 = LC
     # Saint Lucia
     128 = LI
     # Liechtenstein
     129 = LK
     # Sri Lanka
     130 = LR
     # Liberia
     131 = LS
     # Lesotho
     132 = LT
     # Lithuania
     133 = LU
     # Luxembourg
     134 = LV
     # Latvia
     135 = LY
     # Libya
     136 = MA
     # Morocco
     137 = MC
     # Monaco
     138 = MD
     # Moldova, Republic of
     139 = ME
     # Montenegro
     140 = MF
     # Saint Martin (French part)
     141 = MG
     # Madagascar
     142 = MH
     # Marshall Islands
     143 = MK
     # Macedonia
     144 = ML
     # Mali
     145 = MM
     # Myanmar
     146 = MN
     # Mongolia
     147 = MO
     # Macao
     148 = MP
     # Northern Mariana Islands
     149 = MQ
     # Martinique
     150 = MR
     # Mauritania
     151 = MS
     # Montserrat
     152 = MT
     # Malta
     153 = MU
     # Mauritius
     154 = MV
     # Maldives
     155 = MW
     # Malawi
     156 = MX
     # Mexico
     157 = MY
     # Malaysia
     158 = MZ
     # Mozambique
     159 = NA
     # Namibia
     160 = NC
     # New Caledonia
     161 = NE
     # Niger
     162 = NF
     # Norfolk Island
     163 = NG
     # Nigeria
     164 = NI
     # Nicaragua
     165 = NL
     # Netherlands
     166 = NO
     # Norway
     167 = NP
     # Nepal
     168 = NR
     # Nauru
     169 = NU
     # Niue
     170 = NZ
     # New Zealand
     171 = OM
     # Oman
     172 = PA
     # Panama
     173 = PE
     # Peru
     174 = PF
     # French Polynesia
     175 = PG
     # Papua New Guinea
     176 = PH
     # Philippines
     177 = PK
     # Pakistan
     178 = PL
     # Poland
     179 = PM
     # Saint Pierre and Miquelon
     180 = PN
     # Pitcairn
     181 = PR
     # Puerto Rico
     182 = PS
     # Palestine, State of
     183 = PT
     # Portugal
     184 = PW
     # Palau
     185 = PY
     # Paraguay
     186 = QA
     # Qatar
     187 = RE
     # Réunion
     188 = RO
     # Romania
     189 = RS
     # Serbia
     190 = RU
     # Russian Federation
     191 = RW
     # Rwanda
     192 = SA
     # Saudi Arabia
     193 = SB
     # Solomon Islands
     194 = SC
     # Seychelles
     195 = SD
     # Sudan
     196 = SE
     # Sweden
     197 = SG
     # Singapore
     198 = SH
     # Saint Helena, Ascension and Tristan da Cunha
     199 = SI
     # Slovenia
     200 = SJ
     # Svalbard and Jan Mayen
     201 = SK
     # Slovakia
     202 = SL
     # Sierra Leone
     203 = SM
     # San Marino
     204 = SN
     # Senegal
     205 = SO
     # Somalia
     206 = SR
     # Suriname
     207 = SS
     # South Sudan
     208 = ST
     # Sao Tome and Principe
     209 = SV
     # El Salvador
     210 = SX
     # Sint Maarten (Dutch part)
     211 = SY
     # Syrian Arab Republic
     212 = SZ
     # Swaziland
     213 = TC
     # Turks and Caicos Islands
     214 = TD
     # Chad
     215 = TF
     # French Southern Territories
     216 = TG
     # Togo
     217 = TH
     # Thailand
     218 = TJ
     # Tajikistan
     219 = TK
     # Tokelau
     220 = TL
     # Timor-Leste
     221 = TM
     # Turkmenistan
     222 = TN
     # Tunisia
     223 = TO
     # Tonga
     224 = TR
     # Turkey
     225 = TT
     # Trinidad and Tobago
     226 = TV
     # Tuvalu
     227 = TW
     # Taiwan
     228 = TZ
     # Tanzania, United Republic of
     229 = UA
     # Ukraine
     230 = UG
     # Uganda
     231 = UM
     # United States Minor Outlying Islands
     232 = US
     # United States
     233 = UY
     # Uruguay
     234 = UZ
     # Uzbekistan
     235 = VA
     # Vatican City State (Holy See)
     236 = VC
     # Saint Vincent and the Grenadines
     237 = VE
     # Venezuela, Bolivarian Republic of
     238 = VG
     # Virgin Islands, British
     239 = VI
     # Virgin Islands, U.S.
     240 = VN
     # Viet Nam
     241 = VU
     # Vanuatu
     242 = WF
     # Wallis and Futuna
     243 = WS
     # Samoa
     244 = YE
     # Yemen
     245 = YT
     # Mayotte
     246 = ZA
     # South Africa
     247 = ZM
     # Zambia
     248 = ZW
     # Zimbabwe
 }
```

## States and Regions

For each country you can freely define a list of states or regions that can be used afterwards to calculate the final price for each delivery option. To define states or regions via TypoScript use something like this:

```typoscript
plugin.tx_aimeos.settings.client.html.checkout.standard.address.states {
    US {
        CA = California
        NY = New York
       ...
    }
    EU {
        W = Western Europe
        C = Central Europe
        ...
    }
}
```

The key you have chosen for the state or region will be stored in the order address of the customer and can then be used during the rest of the checkout process. More details can be found in [client/html/checkout/standard/address/states](../config/client-html/checkout-standard/#states).

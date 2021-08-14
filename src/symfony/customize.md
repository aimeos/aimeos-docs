# Change configuration

The core library contains a lot of configuration options documented in the "Configuration" section that can be changed in the `./config/packages/aimeos_shop.php` file and they are displayed in the documentation like this:

```
client/html/catalog/filter/button = 1
```

Symfony uses normal PHP arrays for configuration. As a rule of thumb, replace each part separated by a slash (/) by `'...':`:

```yaml
aimeos_shop:
    client:
        html:
            catalog:
                filter:
                    button: 1
```

## Value lists

The same works with arrays of values as well:

```yaml
aimeos_shop:
    client:
        html:
            catalog:
                filter:
                    subparts: ['search', 'tree', 'attribute']
```

## Quoting

All keys and values must be enclosed in single quotes (') if they contain white spaces or special characters:

```php
test: 'my test value'
```

## Area specifc

Sometimes it's necessary to apply configuration settings only to the frontend, the admin backend or the CLI commands. Aimeos currently supports three areas:

* command
* backend
* frontend

The `./config/packages/aimeos_shop.php` configuration file can contain sections with settings only for these areas. Inside these sections, you can add all configuration options available, e.g.

```yaml
aimeos_shop:
    command:
        madmin:
            log:
                manager:
                    loglevel: 7
    backend:
        madmin:
            log:
                manager:
                    loglevel: 5
    frontend:
        madmin:
            log:
                manager:
                    loglevel: 4
```

# Overwrite translations

There is the possibility to overwrite translations from the core or other Aimeos extensions via the `./config/packages/aimeos_shop.php` file. This is very comfortable if you only want to replace certain existing translations by your own one. For each translation, you need the ISO language code, the translation domain, the original string and the new translation, e.g.

```yaml
aimeos_shop:
    i18n:
        '<ISO language code>':
                '<translation domain>':
                    '<original English singular from source code>': ['<new translation>']
```

!!! warning
    This should be used only to replace a few translations. If you would like to translate Aimeos to a new language, please use the [Transifex website](https://www.transifex.com/aimeos/public/) instead. It will be available in the next Aimeos release automatically. Also, if you need to overwrite more than a few translations, you should read the article about [adding translations](../developer/translations.md).

## Required information

ISO language code
: To specify the language for the translation, the [two letter ISO language codes (639-1)](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) are necessary. It's also possible to add the [two letter ISO country codes](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) to refer to country specific language variants like "en_GB" for British English. Please make sure the language code is always in lower case while the the optional country code is always in upper case.

translation domain
: The translation domain where the original string is from. The Aimeos core has six translation domains: `mshop` (core lib with managers), `controller/frontend` (basic business logic for the frontend), `client` (frontend clients), `controller/jobs` (asynchronous cronjob tasks) and `admin` (administration interface). To find out the domain a string is from, you have to look at the .pot files in the Aimeos core for the string.

original singular
: It's the original singular string from the source code or the .pot file. The string must be exactly the same (character case, white spaces, etc.) as in the source code / .pot file. You can not use already translated strings as source.

new translation
: New translation for the original string. This must be an array to support one or more plural forms.

!!! warning
    The original string is **case sensitive** so it makes a difference if you use "Basket" or "basket"! Always use the same string as used in the template or source code.

## Singular translations

A simple singular translation to English:

```yaml
aimeos_shop:
    i18n:
        en:
            client:
                'address': ['Addresses']
```

A simple singular translation to US English:

```yaml
aimeos_shop:
    i18n:
        en_US:
            client:
                'Basket': ['Cart']
```

Several singular translations to English:

```yaml
aimeos_shop:
    i18n:
        en_US:
            client:
                'address': ['Address']
                'Basket': ['Cart']
```

Plural translation to English:

```yaml
aimeos_shop:
    i18n:
        en:
            client:
                'address': ['Address','Addresses']
```

## Plural translations

A translations including one or more plural forms can be defined if the original string in the source code also supports plurals. In this case the source code looks like

```php
$i18n->dn( 'client', '%1$d hour', '%1$d hours', 1 );
$this->translate( 'client', '%1$d hour', '%1$d hours', 1 );
```

and the translation methods for plurals can be *translate()* or *dn()*. To overwrite a plural translation, the simplest form is:

```yaml
aimeos_shop:
    i18n:
        de:
            client:
                    '%1$d hour': ['%1$d Stunde','%1$d Stunden']
```

The index "0" is always the singular translation and most languages only have one plural form, so it must be defined by using the index "1" (PHP arrays always start with index "0" automatically).

But some languages use several plural forms depending on the count given in the last parameter of the translation method. In this case, the index depends on the language and the count value passed as fourth parameter of *dn()* or *translate()*.

To find out the right index for the language, you have to have a look into the [ *getPluralIndex()* method](https://github.com/aimeos/aimeos-core/blob/master/lib/mwlib/src/MW/Translation/Base.php) that maps the count value to the index for the language you want to translate. An example for Czech would be:

```yaml
aimeos_shop:
    i18n:
        de:
            client:
                hour:
                    - 'dlouhá hodina'
                    - 'dlouhé hodiny'
                    - 'dlouhých hodin'
```

All Aimeos templates are written in PHP using a template engine and view helpers that are easy to understand. It works in all integrations in the same way, is extremely fast and doesn't require you as developer to learn a new syntax.

You can alternatively use the Twig template engine for Aimeos templates overwritten for your project. Thus, all your templates will be in the same template language.

# Twig templates

To replace an Aimeos PHP template by our own Twig template, the Twig template needs to be stored at the same location as you would store the PHP template, i.e. the **./client/html/templates/** folder of your project-specific Aimeos extension. You should also keep the directory structure underneath and must save the file as **<template-name>.html.twig**, e.g.

```
./client/html/templates/catalog/detail/body-standard.html.twig
```

The file extension **.html.twig** is important to be recognized as template that should be processed by the Twig engine.

The Symfony functions available in the Twig templates can't give you access to all data you need. Therefore, the Aimeos package contains some functions to retrieve data from Aimeos specific sources like configuration settings or translations.

## Configurations

```php
aiconfig( $key, $default = null )
```

The **aiconfig()** function retrieves the Aimeos setting for the given key, e.g. "client/html/catalog/lists/basket-add". If no value is found for the key, the given default value is returned instead.

## Translations

```php
aitrans( $singular, $params = [], $domain = 'client', $locale = null )

aitransplural( $singular, $plural, $number, $params = [], $domain = 'client', $locale = null )
```

The **aitrans()** function retrieves the translated value from the Aimeos Gettext files. It's similar to Symfonys `trans()` function and useful for translating singular phrases only. The **aitransplural()** function must be used to translate strings where numbers are involved, e.g.

```php
aitransplural( '%1$d apple', '%1$d apples', 10, [10] );
```

When the third parameter is "1", the function would return "1 apple" and for values greater than 1 it returns e.g. "10 apples". The method takes care about the different plural rules for all languages.

If the fourth argument (**params**) contains values, they will be used to replace the placeholders in the translated string. Internally, the [vsprintf()](https://php.net/manual/en/function.vsprintf.php) method takes care about that.

The **domain** argument is the same as used in the Aimeos `$this->translate()` view helper. In the frontend it's either "client" or "client/code" while for templates in the administration interface it's "admin".

To retrieve translations for a different language than the current one, you can pass over the ISO language code for that language in the fifth parameter (**locale**). Depending on the languages available, you can also use country specific language codes, e.g. "en_US".

## Blocks

The Aimeos template engine has a "block" view helper to save a rendered template so it can be inserted in another template. This is very similar to the `{% block %}` and `{% endblock %}` tags of Symfonys Twig engine and you should replace the block view helper statements with the appropriate Twig block directives, e.g.

```php
<?php $this->block()->start( 'cataog/detail/actions' ); ?>
    <div class="actions">
        ...
    </div>
<?php $this->block()->stop(); ?>
<?php echo $this->block()->get( 'catalog/detail/actions' ); ?>
```
by this Twig template:

```twig
{% block cataog_detail_actions %}
    <div class="actions">
        ...
    </div>
{% endblock %}
{{ block('cataog_detail_actions') }}
```

!!! warning
    Twig doesn't allow slashes ("/") in block names. Thus, you have to **replace each slash with an underscore** when using the block/endblock directives. In Aimeos templates, these blocks will be available with slashes as separator again.

# Add locale selector

For shops offering multiple languages, currencies or both, Aimeos contains a locale selector component that renders menus of the configured language/currency combinations, so visitors are able to choose their preferred language and/or currency. By default, both will be part of the URL afterwards.

How to add locales for language/currency combinations is described in the [user manual](../manual/locales.md).

## Configuration

To make the locale selector available in the templates, you need to add the component name to the page configuration. Add these settings for the "page" configuration in your `./config/packages/aimeos_shop.yaml` file:

```yaml
aimeos_shop:
    page:
        account-index: ['locale/select', ...]
        basket-index: ['locale/select', ...]
        catalog-detail: ['locale/select', ...]
        catalog-list: ['locale/select', ...]
```

They add the "locale/select" component to the account, basket, catalog detail and catalog list templates where they can be rendered afterwards.

## Routes

Language and currency ID chosen by the visitor are part of the URL by default, so they are explicit and can be cached (contrary to information based on session data). To make this work, you need to redefine all routes besides the "adm" (admin) routes with a prefix in your `./config/routing.yaml`:

```yaml
aimeos_shop_account:
    path: /{locale}/myaccount
    defaults: { _controller: AimeosShopBundle:Account:index, locale: 'en' }

# ...
```

## Adapt selector

The locale selector is a normal component with subparts, that can be adapted like any other component. If you e.g. only need a language or currency menu, you can remove the subpart you don't need via the [client/html/locale/select/subparts](../config/client-html/locale-select.md#subparts) configuration.

Adapting the layout of the locale selector is possible via CSS.

# Multiple shops

Aimeos is multi-site capable and allows storing several shops in one database.

## Create new site

Creating a new site is very easy. You only need to execute this command in the base directory of your Symfony application:

```bash
php ./bin/console aimeos:setup <site code> [<template site>]
```

The value for `<site code>` can be either a new site code for creating a new site or an existing site code for updating a site. The `<template site>` code is optional and tells the setup command which site template to use as reference when creating a new site (currently "default", "unittest" and "unitperf" are available as templates). If no value for `<template site>` is given, "default" is used.

!!! note
    If you update Aimeos from a previous version, you need to run the `aimeos:setup` command for all sites you've created! Otherwise, required records may be missing and existing data isn't migrated.

!!! warning
    Don't forget to create the appropriate "locale" entries for your new site in the administration interface!

## Adapt the routing

In order to tell your Symfony application which shop should be used, you have to use routes that include at least the "site" parameter. This is not necessary for the first shop (site: `default`).

The Aimeos shop bundle contains a routing definition that can be extended for several shops. Simply use the "{site}" placeholder to your prefix setting and add the routes for the administration interface:

```yaml
aimeos_shop:
    resource: "@AimeosShopBundle/Resources/config/routing.yml"
    prefix:   /{site}/
    defaults: { site: 'default' }

aimeos_shop_admin:
    path: /admin
    defaults: { _controller: AimeosShopBundle:Admin:index }

aimeos_shop_admin_check:
    path: /admin_check
```

The difference is the value for the "prefix" parameter ("/{site}/" instead of just "/"). Then, the path of all routes additionally start with ```/{site}/``` which contains the shop site code. The routes for the administration interface are necessary to leave them not prefixed. More details about the "prefix" setting including the possibility to add language and currency placeholders can be found in the [section about custom routes](#custom-routes).

!!! note
    It's good to set a default value for the site parameter if you have multiple sites! This prevents wrong links if no site value is available at the current page.

# Countries, regions and states

## Countries

If you want to ship your products to several countries or you need to know from which countries your customers are, you have to enable the country selection in the address page of the checkout process.

By default, the country list is hidden for the billing and delivery address in the checkout process. To make show them and make them mandatory you need to add "order.base.address.countryid" to the list of values defined in

* [client/html/checkout/address/billing/mandatory](../config/client-html/checkout-standard.md#billingmandatory)
* [client/html/checkout/address/delivery/mandatory](../config/client-html/checkout-standard.md#deliverymandatory)

In the Aimeos package this is configured for billing and delivery addresses in the `config/shop.php` configuration file:

```yaml
aimeos_shop:
    client:
        html:
            checkout:
                standard:
                    address:
                        billing:
                            mandatory:
                                'order.base.address.salutation'
                                'order.base.address.firstname'
                                'order.base.address.lastname'
                                'order.base.address.address1'
                                'order.base.address.postal'
                                'order.base.address.city'
                                'order.base.address.languageid'
                                'order.base.address.email'
                                'order.base.address.countryid'
                        delivery:
                            mandatory:
                                'order.base.address.salutation'
                                'order.base.address.firstname'
                                'order.base.address.lastname'
                                'order.base.address.address1'
                                'order.base.address.postal'
                                'order.base.address.city'
                                'order.base.address.languageid'
                                'order.base.address.email'
                                'order.base.address.countryid'
```

If no selection should be enforced, you can use instead

* [client/html/checkout/address/billing/optional](../config/client-html/checkout-standard.md#billingoptional)
* [client/html/checkout/address/delivery/optional](../config/client-html/checkout-standard.md#deliveryoptional)


To make the country for billing and delivery addresses optional, use this configuration:


```yaml
aimeos_shop:
    client:
        html:
            checkout:
                standard:
                    address:
                        billing:
                            optional:
                                'order.base.address.countryid'
                        delivery:
                            optional:
                                'order.base.address.countryid'
```

The list of countries is defined by the values added to the configuration key [client/html/checkout/address/countries](../config/client-html/checkout-standard.md#countries). The configuration below will add all countries worldwide to the select boxes for the billing and delivery address:

```yaml
aimeos_shop:
    client:
        html:
            checkout:
                standard:
                    address:
                        countries:
                            - AD # Andorra
                            - AE # United Arab Emirates
                            - AF # Afghanistan
                            - AG # Antigua and Barbuda
                            - AI # Anguilla
                            - AL # Albania
                            - AM # Armenia
                            - AO # Angola
                            - AQ # Antarctica
                            - AR # Argentina
                            - AS # American Samoa
                            - AT # Austria
                            - AU # Australia
                            - AW # Aruba
                            - AX # Åland Islands
                            - AZ # Azerbaijan
                            - BA # Bosnia and Herzegovina
                            - BB # Barbados
                            - BD # Bangladesh
                            - BE # Belgium
                            - BF # Burkina Faso
                            - BG # Bulgaria
                            - BH # Bahrain
                            - BI # Burundi
                            - BJ # Benin
                            - BL # Saint Barthélemy
                            - BM # Bermuda
                            - BN # Brunei Darussalam
                            - BO # Bolivia, Plurinational State of
                            - BQ # Bonaire, Sint Eustatius and Saba
                            - BR # Brazil
                            - BS # Bahamas
                            - BT # Bhutan
                            - BV # Bouvet Island
                            - BW # Botswana
                            - BY # Belarus
                            - BZ # Belize
                            - CA # Canada
                            - CC # Cocos (Keeling) Islands
                            - CD # Congo, the Democratic Republic of the
                            - CF # Central African Republic
                            - CG # Congo
                            - CH # Switzerland
                            - CI # Côte d'Ivoire
                            - CK # Cook Islands
                            - CL # Chile
                            - CM # Cameroon
                            - CN # China
                            - CO # Colombia
                            - CR # Costa Rica
                            - CU # Cuba
                            - CV # Cape Verde
                            - CW # Curaçao
                            - CX # Christmas Island
                            - CY # Cyprus
                            - CZ # Czech Republic
                            - DE # Germany
                            - DJ # Djibouti
                            - DK # Denmark
                            - DM # Dominica
                            - DO # Dominican Republic
                            - DZ # Algeria
                            - EC # Ecuador
                            - EE # Estonia
                            - EG # Egypt
                            - EH # Western Sahara
                            - ER # Eritrea
                            - ES # Spain
                            - ET # Ethiopia
                            - FI # Finland
                            - FJ # Fiji
                            - FK # Falkland Islands (Malvinas)
                            - FM # Micronesia, Federated States of
                            - FO # Faroe Islands
                            - FR # France
                            - GA # Gabon
                            - GB # United Kingdom
                            - GD # Grenada
                            - GE # Georgia
                            - GF # French Guiana
                            - GG # Guernsey
                            - GH # Ghana
                            - GI # Gibraltar
                            - GL # Greenland
                            - GM # Gambia
                            - GN # Guinea
                            - GP # Guadeloupe
                            - GQ # Equatorial Guinea
                            - GR # Greece
                            - GS # South Georgia and the South Sandwich Islands
                            - GT # Guatemala
                            - GU # Guam
                            - GW # Guinea-Bissau
                            - GY # Guyana
                            - HK # Hong Kong
                            - HM # Heard Island and McDonald Islands
                            - HN # Honduras
                            - HR # Croatia
                            - HT # Haiti
                            - HU # Hungary
                            - ID # Indonesia
                            - IE # Ireland
                            - IL # Israel
                            - IM # Isle of Man
                            - IN # India
                            - IO # British Indian Ocean Territory
                            - IQ # Iraq
                            - IR # Iran, Islamic Republic of
                            - IS # Iceland
                            - IT # Italy
                            - JE # Jersey
                            - JM # Jamaica
                            - JO # Jordan
                            - JP # Japan
                            - KE # Kenya
                            - KG # Kyrgyzstan
                            - KH # Cambodia
                            - KI # Kiribati
                            - KM # Comoros
                            - KN # Saint Kitts and Nevis
                            - KP # Korea, Democratic People's Republic of
                            - KR # Korea, Republic of
                            - KW # Kuwait
                            - KY # Cayman Islands
                            - KZ # Kazakhstan
                            - LA # Lao People's Democratic Republic
                            - LB # Lebanon
                            - LC # Saint Lucia
                            - LI # Liechtenstein
                            - LK # Sri Lanka
                            - LR # Liberia
                            - LS # Lesotho
                            - LT # Lithuania
                            - LU # Luxembourg
                            - LV # Latvia
                            - LY # Libya
                            - MA # Morocco
                            - MC # Monaco
                            - MD # Moldova, Republic of
                            - ME # Montenegro
                            - MF # Saint Martin (French part)
                            - MG # Madagascar
                            - MH # Marshall Islands
                            - MK # Macedonia
                            - ML # Mali
                            - MM # Myanmar
                            - MN # Mongolia
                            - MO # Macao
                            - MP # Northern Mariana Islands
                            - MQ # Martinique
                            - MR # Mauritania
                            - MS # Montserrat
                            - MT # Malta
                            - MU # Mauritius
                            - MV # Maldives
                            - MW # Malawi
                            - MX # Mexico
                            - MY # Malaysia
                            - MZ # Mozambique
                            - NA # Namibia
                            - NC # New Caledonia
                            - NE # Niger
                            - NF # Norfolk Island
                            - NG # Nigeria
                            - NI # Nicaragua
                            - NL # Netherlands
                            - NO # Norway
                            - NP # Nepal
                            - NR # Nauru
                            - NU # Niue
                            - NZ # New Zealand
                            - OM # Oman
                            - PA # Panama
                            - PE # Peru
                            - PF # French Polynesia
                            - PG # Papua New Guinea
                            - PH # Philippines
                            - PK # Pakistan
                            - PL # Poland
                            - PM # Saint Pierre and Miquelon
                            - PN # Pitcairn
                            - PR # Puerto Rico
                            - PS # Palestine, State of
                            - PT # Portugal
                            - PW # Palau
                            - PY # Paraguay
                            - QA # Qatar
                            - RE # Réunion
                            - RO # Romania
                            - RS # Serbia
                            - RU # Russian Federation
                            - RW # Rwanda
                            - SA # Saudi Arabia
                            - SB # Solomon Islands
                            - SC # Seychelles
                            - SD # Sudan
                            - SE # Sweden
                            - SG # Singapore
                            - SH # Saint Helena, Ascension and Tristan da Cunha
                            - SI # Slovenia
                            - SJ # Svalbard and Jan Mayen
                            - SK # Slovakia
                            - SL # Sierra Leone
                            - SM # San Marino
                            - SN # Senegal
                            - SO # Somalia
                            - SR # Suriname
                            - SS # South Sudan
                            - ST # Sao Tome and Principe
                            - SV # El Salvador
                            - SX # Sint Maarten (Dutch part)
                            - SY # Syrian Arab Republic
                            - SZ # Swaziland
                            - TC # Turks and Caicos Islands
                            - TD # Chad
                            - TF # French Southern Territories
                            - TG # Togo
                            - TH # Thailand
                            - TJ # Tajikistan
                            - TK # Tokelau
                            - TL # Timor-Leste
                            - TM # Turkmenistan
                            - TN # Tunisia
                            - TO # Tonga
                            - TR # Turkey
                            - TT # Trinidad and Tobago
                            - TV # Tuvalu
                            - TW # Taiwan
                            - TZ # Tanzania, United Republic of
                            - UA # Ukraine
                            - UG # Uganda
                            - UM # United States Minor Outlying Islands
                            - US # United States
                            - UY # Uruguay
                            - UZ # Uzbekistan
                            - VA # Vatican City State (Holy See)
                            - VC # Saint Vincent and the Grenadines
                            - VE # Venezuela, Bolivarian Republic of
                            - VG # Virgin Islands, British
                            - VI # Virgin Islands, U.S.
                            - VN # Viet Nam
                            - VU # Vanuatu
                            - WF # Wallis and Futuna
                            - WS # Samoa
                            - YE # Yemen
                            - YT # Mayotte
                            - ZA # South Africa
                            - ZM # Zambia
                            - ZW # Zimbabwe
```

## States and Regions

For each country you can freely define a list of states or regions that can be used afterwards to calculate the final price for each delivery option.

To define states or regions via the configuration use something like this:

```yaml
aimeos_shop:
    client:
        html:
            checkout:
                standard:
                    address:
                        states:
                            US:
                                CA: 'California'
                                NY: 'New York'
                                # ...
                            EU:
                                W: 'Western Europe'
                                C: 'Central Europe'
                                # ...
```

The key you have chosen for the state or region will be stored in the order address of the customer and can then be used during the rest of the checkout process. More details can be found in the documentation of the configuration option:

* [client/html/checkout/address/states](../config/client-html/checkout-standard.md#states)

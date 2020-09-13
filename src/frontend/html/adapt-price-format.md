To display prices in the frontend, translations are used to get them into the right format. This offers a great flexibility, not only for how values and currencies are displayed but it's also used for generating the strings for different price types like those for subscriptions.

!!! tip
    For a better understanding of the examples, please have a look into the documentation for changing translations. There are articles for [Laravel](../../start/laravel/overwrite-translations), [Symfony](../../start/symfony/overwrite-translations) and [TYPO3](../../start/typo3/overwrite-translations) available.

Each price must have a type to distinguish between different prices for one product, e.g. a subscription price per month or per year. The price of type "default" is used in the basket, the checkout process and the order but in the catalog, you are able to display different price types depending on your products.

!!! tip
    Use CSS to show or hide price types in the catalog views. The price type code is used as CSS class for each price item container.

You can show only a specific price type or several price types at once, e.g. the default price and the price per month for a subscription product. The default price contains the value and the currency and may be formatted like this:

```php
"i18n" => [
    "en" => [
        "client/code" => [
            "price:default" => ["%1$s %2$s"]
        ],
    ],
],
```

The format is determined by the translation which contains the placeholders. To swap the value and currency symbol for example, you only need to change the order of the placeholders, e.g. "%2$s %1$s". All translations by price type are located in the "client/code" domain and the translation key consists of "price:" and the code of the price type.

!!! note
    You need to add a translation for every new price type you create. Otherwise, the "price:&lt;code&gt;" string will be displayed in the frontend instead of the price.

Imagine you need to display additional text next to your new price type, e.g. that the price is per month or per kilogram. After you've created a new price type and assigned prices with that type to your product, you need to add an appropriate translation to display the price as you like:

```php
"i18n" => [
    "en" => [
        "client/code" => [
            "price:month" => ["%1$s %2$s / month"]
            "price:kilo" => ["%1$s %2$s / kg"]
        ],
    ],
],
```

This will create a translation for the price types "month" and "kilo" to strings like "99 € / month" or "1.99 € / kg". If your shop offers additional languages that visitors can view the web site in, you need to add translations for those languages as well. Simply copy the code and exchange the two letter ISO language code ("en") by that language code your website offers too.

Since 2020.10, there's a simple way to create new themes, install and configure them. Please read the article about [theme basics](theme-basics.md) first to understand how a theme is structured. Then, the steps are:

* [Create an extension](#create-theme-extension)
* [Use custom templates](#custom-templates)
* [Use custom theme](#custom-themes)

# Create extension

To create a portable theme, you should generate an extension for your theme first using the [Aimeos extension generator](https://aimeos.org/extensions). Choose **Aimeos YYYY.x extension** suitable for your installed Aimeos version.

Installation must be done via composer as this ensures that everything works out of the box for everyone automatically. This requires that you distribute your theme package via one of the [repository types supported by composer](https://getcomposer.org/doc/05-repositories.md). Then, you or your users just need to execute:

```
composer req aimeos-themes/<mytheme>
```

For local installations only, you can add your theme package into the `./packages/` directory of your Laravel application.

* Create the directory for your theme by executing e.g. `mkdir -p packages/mytheme`
* Unzip the downloaded .zip theme package into that directory
* The name entered during extension generation must be the same as the directory name

Furthermore, you have to add a *repositories* section to the `composer.json` of your Laravel application which must contain these lines:

```json
    "repositories": [{
        "type": "composer",
        "url": "https://packages.aimeos.org/aimeoscom"
    }, {
        "type": "path",
        "url": "packages/*"
    }],
```

Finally, install your theme using:

```
composer req aimeos-extensions/<mytheme>
```

# Custom templates

Most often, you don't need to change the structure of the HTML templates because you can rearrange the layout using CSS to a large degree. If your layout requires a different HTML structure, you can [overwrite the HTML client templates](overwrite-templates.md) from the *ai-client-html* extension.

The base layout of your application offers the general structure including HTML head and body tags but for Laravel and Symfony, there are additional layouts for each page. This doesn't apply to TYPO3 because as full-featured CMS, you can choose from different layout structures for each page and add or move the compenents to the slot where you need them.

# Custom themes

For a custom theme, you need to create the required CSS and JS files in `./themes/client/html/<themename>/` of your extension:

* app.css (CSS framework code)
* app.rtl.css (CSS framework code for RTL languages)
* app.js (JS framework code)
* aimeos.css
* aimeos.js
* account-favorite.css
* account-favorite.js
* account-history.css
* account-history.js
* account-profile.css
* account-profile.js
* account-review.css
* account-review.js
* account-subscription.css
* account-subscription.js
* account-watch.css
* account-watch.js
* basket-bulk.css
* basket-bulk.js
* basket-mini.css
* basket-mini.js
* basket-related.css
* basket-related.js
* basket-standard.css
* basket-standard.js
* catalog-detail.css
* catalog-detail.js
* catalog-filter.css
* catalog-filter.js
* catalog-home.css
* catalog-home.js
* catalog-lists.css
* catalog-lists.js
* catalog-product.css
* catalog-product.js
* catalog-session.css
* catalog-session.js
* catalog-stage.css
* catalog-stage.js
* checkout-confirm.css
* checkout-confirm.js
* checkout-standard.css
* checkout-standard.js
* email.css
* locale-select.css
* locale-select.js
* slider.css
* slider.js
* summary.css
* supplier-detail.css
* supplier-detail.js

For the start, you can copy the existing ["default" Aimeos theme](https://github.com/aimeos/ai-client-html/tree/master/themes/client/html/default) directory and the included CSS, Javascript and image files and adapt them according to your needs, e.g.

```bash
cp -r ./themes/client/html/default/ ./themes/client/html/mytheme/
```

## Deployment

How to deploy your files depends on your host application:

TYPO3
: Adapt the TypoScript constants offered by the Aimeos extension in the "Template" panel of the navigation bar

Laravel
: Run `composer up`

For Laravel, to avoid having to use `composer update` or `composer up` when changing the CSS and JS (development environment) files in the theme extension, a symbolic link can be made with the following command:

```bash
ln -s ./packages/<extname>/themes/client/html/<extname> ./public/vendor/shop/themes/<extname>
```

With this, the changes you make to your package will be published automatically. Also, you can use "hot reload" of changed files with Laravel Mix and Browser Sync:

```bash
npm install laravel-mix --save-dev
npm install -g browser-sync
```

In your webpack.mix.js, you need to add these directories:

```javascript
mix.browserSync({
    injectChanges: true,
    proxy: 'example.com',
    hostname: 'example.com',
    port: 3000,
    ignored: /node_modules/,
    files: [
        'config/shop.php',
        'public/**/*.css',
        'resources/**/*',
        'lang/*.json',
        'packages/**/*.{php,css,js}'
    ]
});
```

## Custom CSS styles

You have to adapt the CSS filesin your theme directory in `./themes/client/html/<themename>/`. These files must contain all styles for the HTML frontend and the sent e-mails (*email.css*).

The simplest way is to copy the files from the default ["default" Aimeos theme](https://github.com/aimeos/ai-client-html/tree/master/themes/client/html/default) and adapt them to your needs. Remove the styles you don't need to keep the file small and add the new styles for your theme.

The CSS class names used in the templates are semantic, so you can add CSS styles for the shop components only. To learn more about semantic naming, please read the article about [theme basics](theme-basics.md#cascading-style-sheets).

You can also add icons you need for your theme to the `./themes/client/html/<themename>/assets/` directory and reference them in the CSS using:

```css
url(assets/icon.png)
```

## Custom Javascript

By default, there are seveeral JS files included in the theme directory and they contain the JS code for all dynamic features, which are described in the [theme basics article](theme-basics.md#javacript).

Since 2020.10, there's a simple way to create new themes, install and configure them. Please read the article about [theme basics](theme-basics.md) first to understand how a theme is structured. Then, the steps are:

* [Create an extension](#create-theme-extension)
* [Use custom templates](#custom-templates)
* [Use custom theme](#custom-themes)

# Create extension

To create a portable theme, you should generate an extension for your theme first using the [Aimeos extension generator](https://aimeos.org/extensions). Choose **Aimeos YYYY.x extension** suitable for your installed Aimeos version.

Installation must be done via composer as this ensures that everything works out of the box for everyone automatically. This requires that you distribute your theme package via one of the [repository types supported by composer](https://getcomposer.org/doc/05-repositories.md). Then, you or your users just need to execute:

```
composer req aimeos-extensions/<mytheme>
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

For a custom theme, you need to create the required CSS and JS files in `./client/html/themes/<themename>/` of your extension:

* aimeos.css
* email.css
* aimeos.js
* aimeos-detail.js

For the start, you can copy the existing ["default" Aimeos theme](https://github.com/aimeos/ai-client-html/tree/master/client/html/themes/default) directory and the included CSS, Javascript and image files and adapt them according to your needs, e.g.

```bash
cp -r ./client/html/themes/default/ ./client/html/themes/mytheme/
```

How to deploy your files depends on your host application:

Laravel and Symfony
: Run `composer up`

TYPO3
: Adapt the TypoScript constants offered by the Aimeos extension in the "Template" panel of the navigation bar

For Laravel and Symfony, you have to adapt the `client/html/common/template/baseurl` setting to point to your new theme. The value must be the absolute directory to your theme and it's required to fetch the styling for the e-mail templates.

## Custom CSS styles

You have to adapt the two CSS files named

* aimeos.css
* email.css

to your theme directory in `./client/html/themes/<themename>/`. These files must contain all styles for the HTML frontend (*aimeos.css*) and the sent e-mails (*email.css*).

The simplest way is to copy the files from the default ["default" Aimeos theme](https://github.com/aimeos/ai-client-html/tree/master/client/html/themes/default) and adapt them to your needs. Remove the styles you don't need to keep the file small and add the new styles for your theme.

The CSS class names used in the templates are semantic, so you can add CSS styles for the shop components only. To learn more about semantic naming, please read the article about [theme basics](theme-basics.md#cascading-style-sheets).

You can also add icons you need for your theme to the `./client/html/themes/<themename>/assets/` directory and reference them in the CSS using:

```css
url(assets/icon.png)
```

## Custom Javascript

By default, there are two standard JS files included in the theme directories: *aimeos.js* and *aimeos-detail.js* (catalog detail page only). Both are offered by the Aimeos ai-client-html extension and are located in `./vendor/aimeos/ai-client-html/client/html/themes/default` of your installation. They contain the JS code for all dynamic features, which is described in the [theme basics article](theme-basics.md#javacript).

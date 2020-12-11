Since 2020.10, there's a simple way to create new themes, install and configure them. Please read the article about [theme basics](theme-basics.md) first to understand how a theme is structured. Then, the steps are:

* [Create an extension](#create-theme-extension)
* [Use custom templates](#custom-templates)
* [Use custom theme](#custom-themes)

# Create extension

To create a portable theme, you should generate an extension for your theme first using the [Aimeos extension generator](https://aimeos.org/extensions). Copy it to the `./ext/` directory of your application where also the other Aimeos extensions are located. You should also put that extension under version control, e.g. by adding it to a Git repository.

# Custom templates

Most often, you don't need to change the structure of the HTML templates because you can rearrange the layout using CSS to a large degree. If your layout requires a different HTML structure, you can [overwrite the HTML client templates](overwrite-templates.md) from the ai-client-html extension.

The base layout of your application offers the general structure including HTML head and body tags but for Laravel and Symfony, there are additional layouts for each page. This doesn't apply to TYPO3 because as full-featured CMS, you can choose from different layout structures for each page and add or move the compenents to the slot where you need them.

## Laravel templates

For Laravel, the Aimeos package includes structural templates for each page which extend from the base layout to build e.g. a catalog list, a basket or checkout page. These [structural Blade template files](https://github.com/aimeos/aimeos-laravel/tree/master/src/views) are located in the `./src/views/` directory of the Aimeos extension.

The `base.blade.php` template file is used by most templates and references the CSS and JS files of the theme. The `./catalog/list.blade.php` template uses the base template via `@extends('shop::base')` and adds the output of the configured components to the sections defined in the `resources/views/app.blade.php` layout template.

If you want change the structure and use a two column layout for your list page, you must copy the `./catalog/list.blade.php` file to the `./resources/views/vendor/shop/catalog/` directory and change the `aimeos_nav` and `aimeos_body` sections like in this example:

```blade
@section('aimeos_nav')
@stop

@section('aimeos_body')
	<div class="row">
		<div class="col-md-3">
			<?= $aibody['catalog/filter'] ?>
		</div>
		<div class="col-md-9">
			<?= $aibody['catalog/lists'] ?>
		</div>
	</div>
@stop
```

Afterwards, the categories, price, supplier and attribute filter will be shown on the left in the search result page.

!!! note
    For the pages displaying a category, you have to adapt the `./catalog/tree.blade.php` file too.

# Custom themes

For a custom theme, you need to create the required CSS and JS files in `./client/html/themes/<themename>/` of your extension:

* aimeos.css
* email.css
* aimeos.js

For the start, you can copy the existing ["elegance" Aimeos theme](https://github.com/aimeos/ai-client-html/tree/master/client/html/themes/elegance) directory and the included files, e.g.

```bash
cp -r ./client/html/themes/elegance/ ./client/html/themes/mytheme/
```

Chage the theme files according to your needs. Then, use `composer update` to copy your theme files to the `./public/` directory so the files will be available. Change the `client/html/common/baseurl` configuration afterwards to point to your new theme.

For Laravel, open the `./config/shop.php` file and search for the `baseurl` key:

```php
	'client' => [
		'html' => [
			'common' => [
				'template' => [
					'baseurl' => 'packages/aimeos/shop/themes/elegance',
				],
			],
		],
	],
```

Uncomment the line with `baseurl` and replace `elegance` by your new theme name.

## Custom CSS styles

You have to adapt the two CSS files named

* aimeos.css
* email.css

to your theme directory in `./client/html/themes/<themename>/`. These files must contain all styles for the HTML frontend (*aimeos.css*) and the sent e-mails (*email.css*).

The simplest way is to copy the files from the default ["elegance" Aimeos theme](https://github.com/aimeos/ai-client-html/tree/master/client/html/themes/elegance) and adapt them to your needs. Remove the styles you don't need to keep the file small and add the new styles for your theme.

The CSS class names used in the templates are semantic, so you can add CSS styles for the shop components only. To learn more about semantic naming, please read the article about [theme basics](theme-basics.md#cascading-style-sheets).

You can also add icons you need for your theme to the `./client/html/themes/<themename>/media/` directory and reference them in the CSS using:

```css
url(media/icon.png)
```

## Custom Javascript

By default, there are two standard JS files included outside of the theme directories: *aimeos.js* and *aimeos-detail.js* (catalog detail page only). Both are offered by the Aimeos ai-client-html extension and are located in `./ext/ai-client-html/client/html/themes/` of your installation. They contain the JS code for all dynamic features, which is described in the [theme basics article](theme-basics.md#javacript).

Additionally, you must add a file named

* aimeos.js

in the `./client/html/themes/<themename>/` of your extension. This file should contain your own Javascript code or JS libraries for certain features you want to use.

!!! note
    If you don't need more JS code, the *aimeos.js* file can be empty but it must exist to avoid 404 errors.

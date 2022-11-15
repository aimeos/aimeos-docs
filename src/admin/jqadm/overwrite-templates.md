Often, it's necessary to replace the templates of a panel or subpart with a different one, e.g. if you need want to remove input fields or add own HTML code. In these cases, you can overwrite an existing template by creating a new file with the same name and within the same directory structure as the original file in your own extension.

!!! tip
    Use the [Aimeos extension builder](https://aimeos.org/extensions) to create an extension for your shop site. The generated extension skeletons contains all necessary directories and configuration to be used out of the box.

# Templates

The template views itself consist of HTML with [alternative PHP syntax](https://php.net/manual/en/control-structures.alternative-syntax.php). It's also possible to use the native template engine of your framework or application, i.e. Blade for Laravel, Twig for Symfony and Fluid for TYPO3. Please have a look at the "Get started" section to find out more.

All standard templates are stored in the [templates/admin/jqadm/](https://github.com/aimeos/ai-admin-jqadm/tree/master/templates/admin/jqadm) directory of the ai-admin-jqadm extension. There are sub-directories for each panel, e.g. the "product" sub-directory contains all templates related to the product panel and it's sub-panels:

```
<panel>/item[-<subpart>[-<sub-subpart>]]-<variant>.php
```

The naming schema matches the hierarchy of the panels and their subparts, which is also reflected by the corresponding classes in the `src/` directory. Examples for this naming are:

```
product/list.php
product/item.php
product/item-text.php
product/item-characteristics-property.php
```

Own extensions that contain template files in the `templates/admin/jqadm/` directory which are named the same as the existing ones are used first. If no template files are found in own extensions, then the default ones from the ai-admin-jqadm extension are used.

# Data access

You have access to all data that has been assigned by the JQAdm client which renders the view, as well as all data that has been assigned by the parent JQAdm clients, e.g.

```
Admin/JQAdm/Product/Standard
Admin/JQAdm/Product/Text/Standard
Admin/JQAdm/Product/Characteristics/Property/Standard
```

The JQAdm clients use these templates and assign:

* Admin/JQAdm/Product/Standard
    * template: product/item.php
    * assigns: itemData, etc.
* Admin/JQAdm/Product/Text/Standard
    * template: product/item-text.php
    * assigns: textData, etc.
* Admin/JQAdm/Product/Characteristics/Property/Standard
    * template: product/item-characteristics-property.php
    * assigns: propertyData, propertyTypes, etc.

In the template of the *Admin/JQAdm/Product/Characteristics/Property/Standard* JQAdm client, you have now access to *propertyData*, *propertyTypes* assigned by the own JQAdm class and *itemData* from the product JQAdm class. Take a look at the JQAdm classes to find out, which data they assign.

To access the data in the view, you can use:

```php
$this->get( 'propertyTypes', [] ) // second parameter is the default value if not available
$this->propertyTypes // throws an exception if not available
isset( $this->propertyTypes ) // tests if the parameter is available
```

# View helpers

For the list of available view helpers, how they work and what their parameters are, please have a look at the [view helper article](../../infrastructure/view.md).

Additionally, the JQAdm adds a few view helpers that are only available in JQAdm templates.

## Datetime

Returns the formatted date and time suitable for input fields of type *datetime-local*.

```php
<?= $this->datetime( '2000-01-01 00:00:00' ) ?>
```

The input must be an ISO date format in "YYYY-MM-DD HH:mm:ss" format.

## Site

This view helper offers easy access to site information.

To return the name of the current site use:
```php
<?= $this->site()->label() ?>
```

To return the label if the site ID matches:
```php
<?= $this->site()->match( $siteid ) ?>
```

Returns the string "readonly" suitable for input or select fields if the site ID doesn't match the current one:
```php
<?= $this->site()->readonly( $siteid ) ?>
```

Returns the current site ID:
```php
<?= $this->site()->siteid() ?>
```

Extensions are an easy way to add new features, change existing ones or manage configurations specific for your Aimeos shop project without touching the core code. Thus, you are still able to update to later versions while keeping your own code separate.

!!! tip
    Create a new extension for your project by using the [Aimeos extension builder](https://aimeos.org/extensions/). It generates a .zip package for download which contains the ready to use extension. Furthermore, it's able to create installable packages for content management systems with the Aimeos extensions pre-configured.

# Location

Your new extension should be installed via composer and they will be added to the `./vendor/` directory by composer. CMS applications like TYPO3 require the Aimeos extension to be part of an application specific extension. The [Aimeos extension builder](https://aimeos.org/extensions) can create both at the same time, packaged together in one .zip file. The Aimeos extension is then placed in the appropriate sub-directory like `./Resources/Private/Extensions/` for TYPO3.

!!! tip
    Create only one extension for your project and add all code that modifies and extends Aimeos to that project specific extension. The main advantage to this approach is that you will only have one place to look. It will also keep the response times low because less directories have to be looked at for templates, configuration settings, and translations.

For local only composer installations, you can add your theme package into the `./packages/` directory of your Laravel application.

* Create the directory for your theme by executing e.g. `mkdir -p packages/myextension`
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
composer req aimeos-extensions/<myextension>
```

You can use your extension immediately to overwrite existing template with your own version. If you want to add classes to your extension adding new features, make sure they will be found by composer. It may be necessary to run:

```bash
composer dump-autoload
```

to update the composer autoloader.

# Structure

An Aimeos extension reflects the directory structure of the core and contains these main directories:

* `config` (configuration for extension)
* `i18n` (gettext translation files)
* `setup` (setup tasks creating and updating the database tables)
* `src` (PHP classes of the extension)
* `templates` (templates file generating the output)
* `themes` (default themes and shared JS files)
* `tests` (unit tests for the PHP classes)
* `phing.xml` (automated development task)

## Aimeos core

The code for the data access managers use:

* `config/` (default configuration for the managers)
* `i18n/` (gettext translation files)
* `setup/` (setup tasks creating and updating the database tables)
* `src/` (PHP manager, item and provider classes)
* `templates/` (templates generating output)
* `tests/` (unit tests for the classes)

Tutorials:

* [Database setup](../infrastructure/databases.md)
* [Database migrations](../infrastructure/schema-migrations.md)
* [Using managers and items](../models/managing-items.md)
* [Implement payment/delivery providers](../providers/service/index.md)
* [Implement basket plugins](../providers/basket-plugins.md)

## admin/jqadm


The administration interface based on Bootstrap and VueJS including the classes plus templates generating the output. Also a default theme is included. Used directories are:

* `config/admin.php` (configuration for extension)
* `i18n/` (gettext translation files)
* `src/` (PHP client classes of the extension)
* `templates/admin/jqadm/` (html templates)
* `themes/admin/jqadm/` (default themes and shared JS files)
* `tests/` (unit tests for the client classes)


## admin/jsonadm

The used directories for the admin JSON REST API are:

* `config/admin.php` (configuration for extension)
* `i18n/` (gettext translation files)
* `src/` (PHP admin classes of the extension)
* `templates/admin/jsonadm/` (html templates)
* `tests/` (unit tests for the admin classes)

Tutorials:

* [Work with the admin JSON REST API](../admin/jsonadm/index.md)

## client/html

The HTML front-end and the classes plus templates generating the HTML output. Also the default themes are included there and this directories are used:

* `config/client.php` (configuration for extension)
* `src/` (PHP client classes of the extension)
* `templates/client/html/` (html templates)
* `themes/client/html/` (default themes and shared JS files)
* `tests/` (unit tests for the client classes)

Tutorials:

* [Implement new components](../frontend/html/implement-components.md)
* [Extend existing components](../frontend/html/extend-components.md)
* [Adapt account components](../frontend/html/account-components.md)
* [Adapt basket components](../frontend/html/basket-components.md)
* [Adapt catalog components](../frontend/html/catalog-components.md)
* [Adapt checkout components](../frontend/html/checkout-components.md)
* [Adapt email components](../frontend/html/email-components.md)
* [Adapt locale components](../frontend/html/locale-components.md)
* [Used parameter names](../frontend/html/parameter-names.md)

Theme tutorials:

* [Theme basics](../frontend/html/theme-basics.md)
* [How to adapt themes](../frontend/html/adapt-themes.md)

## client/jsonapi

The JSON REST API for the front-end and the classes plus templates generating the JSON output:

* `config/client.php` (configuration for extension)
* `i18n/` (gettext translation files)
* `src/` (PHP client classes of the extension)
* `templates/client/jsonapi/` (html templates)
* `tests/` (unit tests for the client classes)

Tutorials:

* [How to use the JSON REST API](../frontend/jsonapi/index.md)

## controller/frontend

The front-end clients use these classes to perform standard actions like retrieving product lists, adding a product to the basket, or doing the necessary actions for a checkout. The directories used are:

* `config/controller.php` (configuration for extension)
* `i18n/` (gettext translation files)
* `src/` (PHP front-end controller classes)
* `tests/` (unit tests for the front-end controller classes)

## controller/jobs

A shop has to run several tasks in an asynchronous manner, like sending e-mails or payed orders to the ERP system. Each class in this part of the directory tree performs one task and the directories used are:

* `config/controller.php` (configuration for extension)
* `i18n/` (gettext translation files)
* `src/` (PHP job controller classes)
* `templates/controller/jobs/` (html templates)
* `tests/` (unit tests for the job controller classes)
* `build.xml` (automated development task)

Tutorials:

* [Implement a job controller](../cronjobs/create-job-controller.md)

# Manifest

The **manifest.php** is one of the most important files in an extension. It describes the extension and where are the directories that should be included, used for configuration, translation and setting up the database. It also contains a custom section which contains the configuration for specific parts of the shop.

The basic structure looks like:

```php
<?php
return [
    'name' => '<vendor key>-<extension name>',
    'depends' => [
        // ...
    ],
    'config' => [
        // ...
    ],
    'include' => [
        // ...
    ],
    'i18n' => [
        // ...
    ],
    'setup' => [
        // ...
    ],
    'custom' => [
        // ...
    ],
];
```

## depends

When you overwrite templates or configuration settings in your own extension, the Aimeos bootstrap process have to make sure that the file are loaded in the correct order. For templates, this means to look into the custom extensions first, configuration files from custom extensions must be added last so they can overwrite the configuration from the core and other Aimeos extensions.

By depending on the core and the Aimeos extensions, you can be sure that you are able to overwrite both, templates and configuration settings. The default dependencies are:

```php
'depends' => [
    'aimeos-core',
    'ai-admin-jqadm',
    'ai-admin-jsonadm',
    'ai-client-html',
    'ai-client-jsonapi',
    'ai-controller-jobs',
    'ai-controller-frontend',
],
```

## config

Aimeos is very flexible by using a lot of configuration, especially by avoiding to hard-code any SQL statements. These configuration is provided in .php files in the "config" directory of the custom library part and may look like:

```php
'config' => [
    'config',
],
```

## include

The list of directories that contains the source code and which should be used by the autoloader to search for the PHP class files. If your extension provides classes for managers, controllers and clients, it will usually look like:


```php
'include' => [
    'src',
],
```

## i18n

Strings that are displayed in the front-end or in the adminstration interface should be available in the native language of the customer or the editor.

Aimeos uses the well known and mature **gettext** infrastructure to extract these strings and makes them available as .po files which can be easily translated using standard tools. After translation to a new language these files are compiled into a binary representation for fast lookups while generating the output.

The "i18n" section of the manifest file lists the directories that contains .po files like this:

```php
'i18n' => [
    'admin' => 'i18n',
    'client' => 'i18n',
    'client/code' => 'i18n',
    'controller/common' => 'i18n',
    'controller/frontend' => 'i18n',
    'controller/jobs' => 'i18n',
    'mshop' => 'i18n',
],
```

## setup

Setup tasks are a great way to create and update your database structure. They are part of your extension and take care of creating your tables and updating them as changes occur. Setup tasks are usually only located in the lib/custom/setup directory:

```php
'i18n' => [
    'setup',
],
```

## templates

The "templates" section of the manifest.php is reserved for directory configurations that are specific for the different parts of the library. The directory must be the array key and the value must be the list of subdirectories or files that are required for the specific purpose. A full example would be:

```php
'templates' => [
    'admin/jqadm/templates' => [
        'templates/admin/jqadm',
    ],
    'admin/jsonadm/templates' => [
        'templates/admin/jsonadm',
    ],
    'client/jsonapi/templates' => [
        'templates/client/jsonapi',
    ],
    'client/html/templates' => [
        'templates/client/html',
    ],
    'controller/jobs/templates' => [
        'templates/controller/jobs',
    ],
],
```

admin/jqadm/templates
: Specifies the directories that contains the HTML template files for the JQAdm interface, either new ones for newly implemented sub-parts or files with the same name of existing ones which will be used instead of the original files.

admin/jsonadm/templates
: List of directories that contains the template files for the JSON admin clients, either new ones or files with the same name of existing ones which will be used instead of the original ones.

client/html/templates
: Specifies the directories that contains the HTML template files for the HTML clients, either new ones for newly implemented sub-parts or files with the same name of existing ones which will be used instead of the original files.

client/jsonapi/templates
: List of directories that contains the template files for the front-end JSON REST API clients, either new ones or files with the same name of existing ones which will be used instead of the original ones.

controller/jobs/templates
: List of directories that contains the template files for the job controllers, either new ones or files with the same name of existing ones which will be used instead of the original ones.

## custom


```php
'custom' => [
    'admin/jqadm' => [
        'manifest.jsb2',
    ],
    'controller/jobs' => [
        'src',
    ],
],
```

admin/jqadm
: Manifest file for including CSS and JS files

controller/jobs
: Describes the source directory which should be used to generate a list of asynchronous tasks presented to the shop administrator.

# phing.xml

[Phing](https://phing.info) is a great tool for automating tasks and in Aimeos it's used to e.g. set up the database, execute the unit tests or handle the extraction and compilation of the translations.

For an Aimeos extension it's not absolutely necessary but can help a lot during development. Therefore, the XML configuration files for phing are always included in the packages generated by the Aimeos extension builder. The phing.xml file in the base directory of your extension should contain at least this targets:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project name="<extension name> extension" default="test">
  <target name="test" description="Executes all tests"></target>
  <target name="coverage" description="Generates the code coverage report"></target>
  <target name="check" description="Executes all tests"></target>
  <target name="clean" description="Cleans up temporary files"></target>
  <target name="i18n" description="Creates all translation files"></target>
  <target name="build" description="Builds package for deployment"></target>
</project>
```

For a detailed example which also contains the executed tasks, please have a look at the extensions generated by the Aimeos extension builder.

# Extension tests

The easiest way is using [Phing](https://phing.info) for executing the unit tests of extensions. You also need [composer](https://getcomposer.org/) and set up a database that will contain the unit test data. Then follow these steps:


* Checkout the Aimeos core somewhere on your disk (`git clone https://github.com/aimeos/aimeos-core`)
* Configure your database connection in `./config/resources.php` available in the cloned directory
* Copy your extension to the `./ext/` directory created during cloning the repository
* Execute `composer update` to install the dependent packages and development tools
* Run `vendor/bin/phing setup` to populate the database with unit test data from the cloned directory
* Execute `vendor/bin/phing -Ddir=ext/<extname> testext` to run the tests also from the cloned directory

That are the same steps as done by the integration tests of every extension running on the Travis-ci platform. You can have a look at the [.travis.yml example](https://github.com/aimeos/ai-controller-frontend/blob/master/.travis.yml#L17-L25) from the ai-controller-frontend extension.

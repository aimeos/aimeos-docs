Extensions are an easy way to add new features, change existing ones or manage configurations specific for your Aimeos shop project without touching the core code. Thus, you are still able to update to later versions while keeping your own code separate.

!!! tip
    Create a new extension for your project by using the [Aimeos extension builder](https://aimeos.org/extensions/). It generates a .zip package for download which contains the ready to use extension. Furthermore, it's able to create installable packages for content management systems with the Aimeos extensions pre-configured.

# Location

Your new extension has to be placed in the Aimeos extension directory. This directory is usually named `./ext/` if you are working with either the Laravel or Symfony.

CMS applications like TYPO3 require the Aimeos extension to be part of an application specific extension. The [Aimeos extension builder](https://aimeos.org/extensions) can create both at the same time, packaged together in one .zip file. The Aimeos extension is then placed in the appropriate sub-directory like `./Resources/Private/Extensions/` for TYPO3.

!!! tip
    Create only one extension for your project and add all code that modifies and extends Aimeos to that project specific extension. The main advantage to this approach is that you will only have one place to look. It will also keep the response times low because less directories have to be looked at for templates, configuration settings, and translations.

The extension files and directories have to be placed in a sub-directory of the Aimeos extension directory ( e.g. `./ext/myextname/`).  This applies to the generated .zip file too, which must be unpacked in your newly created sub-directory.

You can use your extension immediately to overwrite existing template with your own version. If you want to add classes to your extension adding new features, make sure they will be found by composer. If you add your Aimeos extension to an own repository and add that repository to your composer.json file, you are on the save side because composer automatically configures its class loader correctly.

If you only copy your new Aimeos extension to the `./ext/` directory, your classes won't be found by composer. To make them known to composer, you need to add the directories to the composer.json autoload section:

```php
    "autoload": {
        "classmap": [
            "ext/<yourext>/lib/custom/src",
            "ext/<yourext>/controller/common/src",
            "ext/<yourext>/controller/frontend/src",
            "ext/<yourext>/controller/jobs/src",
            "ext/<yourext>/client/html/src",
            "ext/<yourext>/client/jsonapi/src",
            "ext/<yourext>/admin/html/src",
            "ext/<yourext>/admin/jsonadm/src"
        ]
    },
```

Afterwards, you have to run

```bash
composer dump-autoload
```

to update the composer class map file for the autoloader.

!!! warning
    In case you forget to add the directories of your Aimeos extension to the composer.json of your application, you will get **class not found** errors!

# Structure

An Aimeos extension reflects the directory structure of the core and contains these main directories:

* admin/jqadm
* admin/jsonadm
* client/html
* client/jsonapi
* controller/common
* controller/frontend
* controller/jobs
* lib/custom

## admin

There's a shared directory between all admin interfaces for translations:

* `i18n/` (gettext translation files)

## admin/jqadm


The administration interface based on Bootstrap and JQuery including the classes plus templates generating the output. Also a default theme is included and it contains:

* `src/` (PHP client classes of the extension)
* `templates/` (html templates)
* `tests/` (unit tests for the client classes)
* `themes/` (default themes and shared JS files)
* `build.xml` (automated development task)

There's a shared directory between all admin interfaces for translations:

* `i18n/` (gettext translation files)

## admin/jsonadm

The directory for the admin JSON REST API contains:

* `src/` (PHP admin classes of the extension)
* `templates/` (html templates)
* `tests/` (unit tests for the admin classes)
* `i18n/` (gettext translation files)
* `build.xml` (automated development task)

Tutorials:

* [Work with the admin JSON REST API](../admin/jsonadm/index.md)

## client

There's a shared directory between all clients for translations:

* `i18n/` (gettext translation files)

## client/html

The HTML front-end and the classes plus templates generating the HTML output. Also the default themes are included there and the directory contains:

* `src/` (PHP client classes of the extension)
* `templates/` (html templates)
* `tests/` (unit tests for the client classes)
* `themes/` (default themes and shared JS files)
* `build.xml` (automated development task)

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

* `src/` (PHP client classes of the extension)
* `templates/` (html templates)
* `tests/` (unit tests for the client classes)
* `build.xml` (automated development task)

Tutorials:

* [How to use the JSON REST API](../frontend/jsonapi/index.md)

## controller/common

Code shared by more than one controller is located in the "common" directory. This includes mainly the media and order processing code as well as the CSV import processors and caches:

* `config/` (default configuration for the controllers)
* `src/` (PHP controller classes)
* `tests/` (unit tests for the controller classes)
* `build.xml` (automated development task)

## controller/frontend

The front-end clients use these classes to perform standard actions like retrieving product lists, adding a product to the basket, or doing the necessary actions for a checkout. The directory layout includes:

* `i18n/` (gettext translation files)
* `src/` (PHP front-end controller classes)
* `tests/` (unit tests for the front-end controller classes)
* `build.xml` (automated development task)

## controller/jobs

A shop has to run several tasks in an asynchronous manner, like sending e-mails or payed orders to the ERP system. Each class in this part of the directory tree performs one task and they are located in:

* `i18n/` (gettext translation files)
* `src/` (PHP job controller classes)
* `tests/` (unit tests for the job controller classes)
* `build.xml` (automated development task)

Tutorials:

* [Implement a job controller](../cronjobs/create-job-controller.md)

## lib/custom

For the low level layer of the core including the adapters and data access manager layer (`./lib/mwlib/` and `./lib/mshoplib/` in the core], the `./lib/custom/` directory is used and it contains:

* `config/` (default configuration for the managers)
* `i18n/` (gettext translation files)
* `setup/` (setup tasks creating and updating the database tables)
* `src/` (PHP manager, item and provider classes)
* `tests/` (unit tests for the classes)
* `build.xml` (automated development task)

Tutorials:

* [Database setup](../infrastructure/databases.md)
* [Database migrations](../infrastructure/schema-migrations.md)
* [Using managers and items](../infrastructure/managing-items.md)
* [Implement payment/delivery providers](../providers/service/index.md)
* [Implement basket plugins](../providers/basket-plugins.md)

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
    'lib/custom/config',
],
```

## include

The list of directories that contains the source code and which should be used by the autoloader to search for the PHP class files. If your extension provides classes for managers, controllers and clients, it will usually look like:


```php
'include' => [
    'lib/custom/src',
    'client/html/src',
    'controller/frontend/src',
    'controller/extjs/src',
    'controller/jobs/src',
    'admin/jqadm/src',
],
```

## i18n

Strings that are displayed in the front-end or in the adminstration interface should be available in the native language of the customer or the editor.

Aimeos uses the well known and mature **gettext** infrastructure to extract these strings and makes them available as .po files which can be easily translated using standard tools. After translation to a new language these files are compiled into a binary representation for fast lookups while generating the output.

The "i18n" section of the manifest file lists the directories that contains .po files like this:

```php
'i18n' => [
    'admin' => 'admin/i18n',
    'client' => 'client/i18n',
    'custom' => 'lib/custom/i18n',
    'controller/frontend' => 'controller/frontend/i18n',
    'controller/extjs' => 'controller/extjs/i18n',
    'controller/jobs' => 'controller/jobs/i18n',
],
```

## setup

Setup tasks are a great way to create and update your database structure. They are part of your extension and take care of creating your tables and updating them as changes occur. Setup tasks are usually only located in the lib/custom/setup directory:

```php
'i18n' => [
    'lib/custom/setup',
],
```

## custom

The "custom" section of the manifest.php is reserved for directory configurations that are specific for the different parts of the library. The directory for the library part must the key and the value is always a list of subdirectories or files that are required for specific the purpose. A full example would be:

```php
'custom' => [
    'admin/jqadm/templates' => [
        'admin/jqadm/templates',
    ],
    'admin/jsonadm/templates' => [
        'admin/jsonadm/templates',
    ],
    'client/html/templates' => [
        'client/html/templates',
    ],
    'client/jsonapi/templates' => [
        'client/jsonapi/templates',
    ],
    'controller/jobs' => [
        'controller/jobs/src',
    ],
    'controller/jobs/templates' => [
        'controller/jobs/templates',
        'client/html/templates',
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

controller/jobs
: Describes the source directory which should be used to generate a list of asynchronous tasks presented to the shop administrator.

controller/jobs/templates
: List of directories that contains the template files for the job controllers, either new ones or files with the same name of existing ones which will be used instead of the original ones.

# phing.xml

[Phing](https://phing.info) is a great tool for automating tasks and in Aimeos it's used to e.g. set up the database, execute the unit tests or handle the extraction and compilation of the translations.

For an Aimeos extension it's not absolutely necessary but can help a lot during development. Therefore, the XML configuration files for phing are always included in the packages generated by the Aimeos extension builder. The phing.xml file in the base directory of your extension should contain at least this targets:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project name="<extension name> extension" default="test">
  <target name="test" description="Executes all tests"></target>
  <target name="testperf" description="Executes all performance tests"></target>
  <target name="coverage" description="Generates the code coverage report"></target>
  <target name="check" description="Executes all tests"></target>
  <target name="clean" description="Cleans up temporary files"></target>
  <target name="i18n" description="Creates all translation files"></target>
  <target name="build" description="Builds package for deployment"></target>
  <target name="release" description="Creates new release" depends="build"></target>
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

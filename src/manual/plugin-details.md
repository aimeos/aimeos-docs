![Detail view for plug-ins](Admin-backend-plugin-detail.png)

There are some select and input fields in the left section of the detail view that are all required. Their purpose is:

Status (required)
: Controls the global availability of the configured plugin. There are several status values available but the plugin will only be used if the status is "enabled".

Type (required)
: The plugin type, which can be only "Order" for basket plugins at the moment.

Provider (required)
: This is the last part of the plugin provider class name, e.g. "Shipping" for the "\Aimeos\MShop\Plugin\Provider\Order\Shipping". The name of the provider is **case sensitive**, so "shipping" is not the same as "Shipping"! Each plugin provider can be enhanced by one or more decorators that must be added to the provider name and separated by a comma. To configure the "Shipping" plugin provider in combination with e.g. a decorator called "Example", enter "Shipping,Example" into the input field of the provider. For a list of plugins and decorators that are part of the Aimeos core, please have a look at the [plugin overview](plugins.md).

Label (required)
: An internal label which helps you to identify the plugin and can be used for searching in the administration interface.

Created (read-only)
: Date and time when the entry was added. This value is set automatically.

Last modified (read-only)
: Last date and time when the entry was edited. This value is set automatically.

Editor (read-only)
: Last user who added or modified the entry. This value is set automatically.


# Plugin configuration

The right side of the plugin detail view contains a key/value configuration panel where the necessary configuration values of the plugin and the decorators must be added. The left column in the configuration panel is for the configuration key, the right column for the value and at least the left column of each line must be filled with a valid key. You can add lines by clicking on the "Add" button in the menu bar and delete selected lines with the "Delete" button. The order of the lines doesn't matter.

Each plugin and decorator needs its own configuration. The available settings are automatically added as soon as you select a provider (and decorator). Settings can be of different types like strings, yes/no values or lists of values and for each setting the type defined in the provider class will be shown. You can also add more custom options if requried and these will show text fields where you can enter arbitrary values. Documentation for the built-in ones is available at the [plugin overview](plugins.md) page.

# CKEditor

Aimeos offers a rich text HTML editor in the text panels for adding HTML formatting to short and long descriptions and currently, the *CKEditor v4 Standard All Edition* is used. This version comes with all standard plugins activated and all *official* plugins included, but deactivated. The standard configuration hides some buttons (e.g. "superscript", "subscript"), something to be aware of, when it comes to configuration.

!!! note
    CKEditor configuraton works since v2020.7.10-dev.

## Customize

Your own Aimeos extensions includes a *./admin/jqadm/themes/custom.js* script which allows you to configure CKEditor. Initially this file is empty but you can add Javascript to overwrite the default HTML editor settings like this:

```javascript
Aimeos.editorcfg = [
  [ 'Undo', 'Redo' ],
  [ 'Link', 'Unlink', 'Anchor' ],
  [ 'Bold', 'Italic', 'Underline', 'Strike' ],
  [ 'NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote' ],
  [ 'SpecialChar' ],
  [ 'Source', '-', 'RemoveFormat' ]
]
```

This configuration will replace the existing Aimeos configuration and will be applied to all available text area fields in all text panels.

### Activate plugins

In order to make buttons like the text align options (JustifyLeft, JustifyCenter, JustifyRight, JustifyBlock) visible, you have to add a plugin to the *editorExtraPlugins* option, in this case the *justify* plugin:

```javascript
Aimeos.editorExtraPlugins = 'divarea,justify'
```

Now the text align options will be visible.

!!! note
    The default configuration contains `divarea` to render the CKEditor in a `div` tag instead of an `iframe`. We recommend to keep that plugin to avoid problems!

## Allow HTML tags

By default, CKEditor's [allowed content rules](https://ckeditor.com/docs/ckeditor4/latest/guide/dev_allowed_content_rules.html) are used with the addition of those tags listed in the `Aimeos.editortags` configuration, which are assigned to CKEditor's *extraAllowedContent* setting. The Aimeos standard configuration is:

```javascript
Aimeos.editortags = 'div(*);span(*);p(*);';
```

The `Aimeos.editortags` option enables you to configure more tags which are allowed in the source view, replace them by your own list or remove them completely. The format of the setting must be the tag name, followed by the list of CSS classes in round brackets or "\*" for all classes. Each tags/class combination must contain a semicolon at the end. Don't use spaces anywhere in the string!

## Show more buttons

If you wish to activate certain buttons, e.g. for super- and/or subscript, or add e.g. text align options, extend your configuration like this:
  
```javascript
Aimeos.editorcfg = [
  [ 'Undo', 'Redo', 'Anchor' ],
  [ 'Link', 'Unlink' ],
  [ 'JustifyLeft', 'JustifyCenter', 'JustifyRight' ],
  [ 'Bold', 'Italic', 'Underline', 'Strike', 'Superscript', 'Subscript' ],
  [ 'NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote' ],
  [ 'SpecialChar' ],
  [ 'Source', '-', 'RemoveFormat' ]
]
```

This would only be the first step, though, since neither the text align nor the super-/subscript buttons would be available/visible yet. This is due to the fact that the *CKEditor v4 Standard Edition* disables additional plugins by default as well as removes some buttons.

### Remove buttons

The buttons for "Underline", "Superscript" and "Subscript" are not visible, because the *CKEDITOR v4 Standard Edition* removes them by default. You can change the list of buttons using the `Aimeos.editorRemoveButtons` setting. The default configuration in Aimeos is:

```javascript
Aimeos.editorRemoveButtons = 'Underline,Subscript,Superscript';
```

The button names must be separated by comma. To show all buttons, set the configuration option to an empty string:

```javascript
Aimeos.editorRemoveButtons = '';
```

There's a complete [list of CKEditor button names](https://ckeditor.com/old/forums/CKEditor/Complete-list-of-toolbar-items#comment-123266) available for reference.

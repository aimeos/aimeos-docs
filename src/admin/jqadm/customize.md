# Text Editor (CKEditor v4 Standard Edition)

Aimeos currently implements the *CKEditor v4 Standard All Edition* via [jsdelivr](https://www.jsdelivr.com/) which hosts the npm version (https://www.npmjs.com/package/ckeditor4). This version comes with all standard plugins activated and all *official* plugins included, but deactivated. The standard configuration is ruled by CKEditor's  [Allowed Content Rules](https://ckeditor.com/docs/ckeditor4/latest/guide/dev_allowed_content_rules.html) which, by default, hides some buttons (e.g. "superscript", "subscript"), something to be aware of, when it comes to configuration.

## Configure CKEditor in *custom.js*

Your aimeos extensions includes a *custom.js* script which allows you to configure CKEditor. 

!!! note
    If you decide to rename this file, make sure to also change the file reference in the *manifest.jsb2* file one folder level above!

Initially this file is empty. To configure the editor, override the `Aimeos.editorcfg` object like this:

```javascript
// Override the toolbar options
Aimeos.editorcfg = [
  [ 'Undo', 'Redo' ],
  [ 'Link', 'Unlink', 'Anchor' ],
  [ 'Bold', 'Italic', 'Underline', 'Strike' ],
  [ 'NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote' ],
  [ 'SpecialChar' ],
  [ 'Source', '-', 'RemoveFormat' ]
]
```

This configuration will be merged in the global Aimeos configuration and, since it is currently not possible to create an individual configuration for a specific text field, applied to all available text fields of all domains.

If you wish to add buttons like super- and/or subscript or activate text align options, you have to extend your configuration like this:
  
```javascript
// Override the toolbar options
Aimeos.editorcfg = [
  [ 'Undo', 'Redo' ],
  [ 'Link', 'Unlink', 'Anchor' ],
  [ 'JustifyLeft', 'JustifyCenter', 'JustifyRight' ],
  [ 'Bold', 'Italic', 'Underline', 'Strike', 'Superscript', 'Subscript' ],
  [ 'NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote' ],
  [ 'SpecialChar' ],
  [ 'Source', '-', 'RemoveFormat' ]
]
```

but this would only be the first step, since the text editor's buttons would not be available yet. This is due to the fact that the *CKEditor v4 Standard Edition* disables additional plugins.

## Activate plugins

In order to make the text align options visible, you need to add the *justify* plugin to the *extraPlugins* option:

```javascript
Aimeos.extraPlugins = ',justify'
```

!!! warning
    Please make sure to put a comma first! Otherwise the *Aimeos* standard configuration will break!

Now the text align options will be visible.

## Manage removed buttons

However, "Superscript" and "Subscript" are still not visible, because the *CKEDITOR v4 Standard Edition* removes these (and other) buttons. In order to make these buttons visible again, you need to configure the *removeButtons* option:

```javascript
Aimeos.removeButtons = ''
```

## Add external CSS

Adding styles via an external CSS file is currently not implemented by *Aimeos*.
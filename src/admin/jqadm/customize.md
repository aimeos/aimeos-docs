# Text Editor (CKEditor v4 Standard Edition)

Aimeos currently implements the *CKEditor v4 Standard All Edition* via [jsdelivr](https://www.jsdelivr.com/) which hosts the npm version (https://www.npmjs.com/package/ckeditor4). This version comes with all standard plugins activated and all *official* plugins included, but deactivated. The standard configuration is ruled by CKEditor's  [Allowed Content Rules](https://ckeditor.com/docs/ckeditor4/latest/guide/dev_allowed_content_rules.html) which, by default, hides some buttons (e.g. "superscript", "subscript"), something to be aware of, when it comes to configuration.

!!! note
    CKEditor configuraton works since v2020.7.10-dev.

## Configure CKEditor via *custom.js*

Your aimeos extensions includes a *custom.js* script which allows you to configure CKEditor. 

!!! note
    If you decide to rename this file, make sure to also change the file reference in the *manifest.jsb2* file one folder level above!

Initially this file is empty. If you want to customize CKEditor's *toolbar*, you can configure `Aimeos.editorcfg` like this:

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

This configuration will be merged into the global *Aimeos* configuration and applied to all available text fields of all domains. (Individual configurations for specific text fields is currently not available.)

## Manage visibility of buttons

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

This would only be the first step, though, since neither the text align nor the super-/subscript buttons would be available/visible yet. This is due to the fact that the *CKEditor v4 Standard Edition* disables additional plugins by default as well as removes some buttons. (If you wish to activate other plugins or buttons like the ones mentioned here, please research the CKEditor website to find out, which plugins are offered by the *CKEditor v4 Standard Edition (from npm)* and which buttons are hidden by default.)

### Activate plugins

In order to make buttons like the text align options (JustifyLeft, JustifyCenter, JustifyRight, JustifyBlock) visible, you have to add a plugin to the *editorExtraPlugins* option, in this case the *justify* plugin:

```javascript
Aimeos.editorExtraPlugins = 'divarea,justify'
```

Now the text align options will be visible.

!!! note
    Please note that the default configuration is `Aimeos.editorExtraPlugins = 'divarea'`. `divarea` is a CKEditor plugin that renders the CKEditor in a div tag instead of an iframe. We recommend to not remove it!

### Manage removed buttons

Buttons like "Superscript" and "Subscript" are not visible, because the *CKEDITOR v4 Standard Edition* removes them (and others) by default. In order to make these buttons visible again, you need to configure the *editorRemoveButtons* option:

```javascript
Aimeos.editorRemoveButtons = ''
```

!!! note
    Please note that the default configuration is `Aimeos.editorRemoveButtons = 'Underline,Subscript,Superscript'`.

## Manage allowed tags

The `Aimeos.editortags` options allows you to add or remove tags. It is used to configure CKEditor's *extraAllowedContent* option.

!!! note
    The default configuration is `Aimeos.editortags = 'div(*);span(*);p(*);'`.

## Add external CSS

The option to add styles via an external CSS file is currently not implemented.
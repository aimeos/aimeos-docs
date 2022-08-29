# Custom CSS/JS

If you [generate an Aimeos extension](https://aimeos.org/extensions) for your project, you can add own CSS and JS code in these files included in the generated extension:

```
./themes/admin/jqadm/custom.css
./themes/admin/jqadm/custom.js
```

They will be loaded automatically and appended to the Aimeos core files so you can overwrite any Aimeos CSS or JS code.

You can also add more CSS/JS files if you have lots of code and want to keep them in separate files. Then, you have to register your files in the *manifest.jsb2* file stored in:

```
./manifest.jsb2
```

This file contains a *pkgs* section for the CSS and the JS files:

```
{
	"pkgs": [{
		"name": "yourext CSS",
		"file": "yourext.css",
		"fileIncludes": [{
			"text": "additonal-styles.css",
			"path": "themes/"
		}]
	}, {
		"name": "yourext JS",
		"file": "yourext.js",
		"fileIncludes": [{
			"text": "additional-javascript.js",
			"path": "js/"
		}]
	}],
}
```

The *fileIncludes* sections contain the list of files that will be included in each request. It's a list of Javascript objects with *text* and *path* keys.

!!! caution
    The *text* value must be the file name **without path** while the *path* value must contain the path relative to the *manifest.jsb2* file including a **trailing slash** ("/").

# CKEditor

Aimeos offers a rich text HTML editor in the text panels for adding HTML formatting to short and long descriptions and currently, the *CKEditor v5* is used. This version comes with allmost all plugins included but not all icons are available in the menu. You can adapt the toolbar configuration to add or remove those features.

## Customize

Your own Aimeos extensions includes a *./themes/admin/jqadm/custom.js* script which allows you to configure CKEditor. Initially this file is empty but you can add Javascript to overwrite the default HTML editor settings like this:

```javascript
Aimeos.ckeditor.toolbar = [
  'link', '|',
  'bold', 'italic', '|',
  'undo', 'redo', '|',
  'specialCharacters', 'removeFormat', '|',
  'bulletedList', 'numberedList', '|',
  'blockQuote', '|',
  'insertTable', 'mediaEmbed', '|',
  'sourceEditing'
]
```

This configuration will replace the existing Aimeos configuration and will be applied to all available text area fields in all text panels.

## Add plugins

In order to add buttons for e.g. text options (underline, strikethrough), you have to add the plugins to the *toolbar* setting, in this case the *justify* plugin:

```javascript
Aimeos.ckeditor.toolbar = [
  'link', '|',
  'bold', 'italic', 'underline', 'strikethrough '|',
  'undo', 'redo', '|',
  'specialCharacters', 'removeFormat', '|',
  'bulletedList', 'numberedList', '|',
  'blockQuote', '|',
  'insertTable', 'mediaEmbed', '|',
  'sourceEditing'
]
```

## Allow HTML tags

By default, CKEditor's [General HTML Support plugin](https://ckeditor.com/docs/ckeditor5/latest/features/general-html-support.html) is included. The Aimeos standard configuration is:

```javascript
Aimeos.ckeditor.htmlSupport = {
  allow: [{
    name: /div|p|span/,
    attributes: false,
    classes: true,
    styles: false,
  }],
  disallow: []
};
```

The *allow* option enables features like additional HTML tags ("name" option), attributes, classes and styles while the *disallow* option can remove them. By default, *div* and *span* tags as well as class names are allowed in addition.

!!! warning
    Attributes, classes and styles doesn't work on all HTML tags and they will be removed if the tags are managed by another plugin which doesn't preserve that data!
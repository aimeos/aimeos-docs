
# page

Relative path to the template for the base page template

```
admin/jqadm/template/page = page
```

* Default: `page`
* Type: string - Relative path to the partial creating the HTML code
* Since: 2016.04

The template file contains the HTML code and processing instructions
to generate the result shown in the administration interface. The
configuration string is the path to the template file relative
to the templates directory (usually in templates/admin/jqadm).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "default" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "default"
should be replaced by the name of the new class.

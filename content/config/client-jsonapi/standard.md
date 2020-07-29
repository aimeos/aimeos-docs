
# template-error

Relative path to the default JSON API template

```
client/jsonapi/standard/template-error = error-standard
```

* Default: error-standard
* Type: string - Relative path to the template creating the body for the JSON API response
* Since: 2017.02

The template file contains the code and processing instructions
to generate the result shown in the JSON API body. The
configuration string is the path to the template file relative
to the templates directory (usually in client/jsonapi/templates).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "standard" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "standard"
should be replaced by the name of the new class.

See also:

* client/jsonapi/standard/template-delete
* client/jsonapi/standard/template-patch
* client/jsonapi/standard/template-post
* client/jsonapi/standard/template-get
* client/jsonapi/standard/template-options

# template-get

Relative path to the default JSON API template for unknown GET request

```
client/jsonapi/standard/template-get = get-standard
```

* Default: get-standard
* Type: string - Relative path to the template creating the body for the JSON API GET response
* Since: 2017.05

The template file contains the code and processing instructions
to generate the result shown in the JSON API body. The
configuration string is the path to the template file relative
to the templates directory (usually in client/jsonapi/templates).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "standard" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "standard"
should be replaced by the name of the new class.

See also:

* client/jsonapi/standard/template-options

# template-options

Relative path to the JSON API template for OPTIONS requests

```
client/jsonapi/standard/template-options = options-standard
```

* Default: options-standard
* Type: string - Relative path to the template creating the body for the OPTIONS method of the JSON API
* Since: 2017.02

The template file contains the code and processing instructions
to generate the result shown in the JSON API body. The
configuration string is the path to the template file relative
to the templates directory (usually in client/jsonapi/templates).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "standard" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "standard"
should be replaced by the name of the new class.

See also:

* client/jsonapi/standard/template-get
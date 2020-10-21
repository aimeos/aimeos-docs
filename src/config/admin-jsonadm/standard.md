
# template-aggregate

Relative path to the JSON API template for GET aggregate requests

```
admin/jsonadm/standard/template-aggregate = aggregate-standard
```

* Default: aggregate-standard
* Type: string - Relative path to the template creating the body for the GET aggregate request of the JSON API
* Since: 2016.07

The template file contains the code and processing instructions
to generate the result shown in the JSON API body. The
configuration string is the path to the template file relative
to the templates directory (usually in admin/jsonadm/templates).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "standard" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "standard"
should be replaced by the name of the new class.

See also:

* admin/jsonadm/standard/template-delete
* admin/jsonadm/standard/template-get
* admin/jsonadm/standard/template-patch
* admin/jsonadm/standard/template-post
* admin/jsonadm/standard/template-put
* admin/jsonadm/standard/template-options

# template-delete

Relative path to the JSON API template for DELETE requests

```
admin/jsonadm/standard/template-delete = delete-standard
```

* Default: delete-standard
* Type: string - Relative path to the template creating the body for the DELETE method of the JSON API
* Since: 2020.10
* Since: 2015.12

The template file contains the code and processing instructions
to generate the result shown in the JSON API body. The
configuration string is the path to the template file relative
to the templates directory (usually in admin/jsonadm/templates).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "standard" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "standard"
should be replaced by the name of the new class.

See also:

* admin/jsonadm/standard/template-aggregate
* admin/jsonadm/standard/template-get
* admin/jsonadm/standard/template-patch
* admin/jsonadm/standard/template-post
* admin/jsonadm/standard/template-put
* admin/jsonadm/standard/template-options
* admin/jsonadm/standard/template-aggregate
* admin/jsonadm/standard/template-get
* admin/jsonadm/standard/template-patch
* admin/jsonadm/standard/template-post
* admin/jsonadm/standard/template-put
* admin/jsonadm/standard/template-options

# template-get

Relative path to the JSON API template for GET requests

```
admin/jsonadm/standard/template-get = get-standard
```

* Default: get-standard
* Type: string - Relative path to the template creating the body for the GET method of the JSON API
* Since: 2015.12

The template file contains the code and processing instructions
to generate the result shown in the JSON API body. The
configuration string is the path to the template file relative
to the templates directory (usually in admin/jsonadm/templates).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "standard" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "standard"
should be replaced by the name of the new class.

See also:

* admin/jsonadm/standard/template-aggregate
* admin/jsonadm/standard/template-delete
* admin/jsonadm/standard/template-patch
* admin/jsonadm/standard/template-post
* admin/jsonadm/standard/template-put
* admin/jsonadm/standard/template-options

# template-options

Relative path to the JSON API template for OPTIONS requests

```
admin/jsonadm/standard/template-options = options-standard
```

* Default: options-standard
* Type: string - Relative path to the template creating the body for the OPTIONS method of the JSON API
* Since: 2015.12

The template file contains the code and processing instructions
to generate the result shown in the JSON API body. The
configuration string is the path to the template file relative
to the templates directory (usually in admin/jsonadm/templates).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "standard" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "standard"
should be replaced by the name of the new class.

See also:

* admin/jsonadm/standard/template-aggregate
* admin/jsonadm/standard/template-delete
* admin/jsonadm/standard/template-patch
* admin/jsonadm/standard/template-post
* admin/jsonadm/standard/template-get
* admin/jsonadm/standard/template-put

# template-patch

Relative path to the JSON API template for PATCH requests

```
admin/jsonadm/standard/template-patch = patch-standard
```

* Default: patch-standard
* Type: string - Relative path to the template creating the body for the PATCH method of the JSON API
* Since: 2015.12

The template file contains the code and processing instructions
to generate the result shown in the JSON API body. The
configuration string is the path to the template file relative
to the templates directory (usually in admin/jsonadm/templates).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "standard" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "standard"
should be replaced by the name of the new class.

See also:

* admin/jsonadm/standard/template-aggregate
* admin/jsonadm/standard/template-get
* admin/jsonadm/standard/template-post
* admin/jsonadm/standard/template-delete
* admin/jsonadm/standard/template-put
* admin/jsonadm/standard/template-options

# template-post

Relative path to the JSON API template for POST requests

```
admin/jsonadm/standard/template-post = post-standard
```

* Default: post-standard
* Type: string - Relative path to the template creating the body for the POST method of the JSON API
* Since: 2020.10
* Since: 2015.12

The template file contains the code and processing instructions
to generate the result shown in the JSON API body. The
configuration string is the path to the template file relative
to the templates directory (usually in admin/jsonadm/templates).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "standard" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "standard"
should be replaced by the name of the new class.

See also:

* admin/jsonadm/standard/template-aggregate
* admin/jsonadm/standard/template-get
* admin/jsonadm/standard/template-patch
* admin/jsonadm/standard/template-delete
* admin/jsonadm/standard/template-put
* admin/jsonadm/standard/template-options
* admin/jsonadm/standard/template-aggregate
* admin/jsonadm/standard/template-get
* admin/jsonadm/standard/template-patch
* admin/jsonadm/standard/template-delete
* admin/jsonadm/standard/template-put
* admin/jsonadm/standard/template-options

# template-put

Relative path to the JSON API template for PUT requests

```
admin/jsonadm/standard/template-put = put-standard
```

* Default: put-standard
* Type: string - Relative path to the template creating the body for the PUT method of the JSON API
* Since: 2015.12

The template file contains the code and processing instructions
to generate the result shown in the JSON API body. The
configuration string is the path to the template file relative
to the templates directory (usually in admin/jsonadm/templates).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "standard" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "standard"
should be replaced by the name of the new class.

See also:

* admin/jsonadm/standard/template-aggregate
* admin/jsonadm/standard/template-delete
* admin/jsonadm/standard/template-patch
* admin/jsonadm/standard/template-post
* admin/jsonadm/standard/template-get
* admin/jsonadm/standard/template-options

# name

Class name of the used bulk order client implementation

```
client/html/basket/bulk/name = 
```

* Default: 
* Type: string - Last part of the class name
* Since: 2014.03

Each default HTML client can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the client factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Client\Html\Basket\Bulk\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Client\Html\Basket\Bulk\Myorder
```

then you have to set the this configuration option:

```
 client/html/basket/bulk/name = Myorder
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyBasket"!


# rows

Number or rows shown in the product bulk order form by default

```
client/html/basket/bulk/rows = 1
```

* Default: 1
* Type: int - Number of lines shown
* Since: 2020.07

The product bulk order form shows a new line for adding a product to the basket
by default. You can change the number of empty input lines shown by default
using this configuration setting.


# template-body

Relative path to the HTML body template of the bulk order client.

```
client/html/basket/bulk/template-body = basket/bulk/body
```

* Default: basket/bulk/body
* Type: string - Relative path to the template creating code for the HTML page body
* Since: 2019.10

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in templates/client/html).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but suffixed by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, it
should be suffixed by the name of the new class.

See also:

* client/html/basket/bulk/template-header

# template-header

Relative path to the HTML header template of the bulk order client.

```
client/html/basket/bulk/template-header = basket/bulk/header
```

* Default: basket/bulk/header
* Type: string - Relative path to the template creating code for the HTML page head
* Since: 2019.10

The template file contains the HTML code and processing instructions
to generate the HTML code that is inserted into the HTML page header
of the rendered page in the frontend. The configuration string is the
path to the template file relative to the templates directory (usually
in templates/client/html).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but suffixed by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, it
should be suffixed by the name of the new class.

See also:

* client/html/basket/bulk/template-body

# name

Class name of the used catalog price client implementation

```
client/html/catalog/price/name = 
```

* Default: 
* Type: string - Last part of the class name
* Since: 2018.04

Each default HTML client can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the client factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Client\Html\Catalog\Price\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Client\Html\Catalog\Price\Myprice
```

then you have to set the this configuration option:

```
 client/html/catalog/price/name = Myprice
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyPrice"!

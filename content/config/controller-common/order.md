
# name

Class name of the used order common controller implementation

```
controller/common/order/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2014.07

Each default common controller can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the controller factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Controller\Common\Order\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Controller\Common\Order\Myorder
```

then you have to set the this configuration option:

```
 controller/common/order/name = Myorder
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyOrder"!

## NumberFormatter

If you install Aimeos without using composer, there's no check if your environment provides everything Aimeos needs. Depending on your hosting environment, you may get this error:

```
Class "NumberFormatter" not found
```

In that case, one required PHP extension named `php-intl` isn't installed. How to install the PHP extension depends on your environment. For Ubuntu, you can use:

```bash
sudo apt-get install php-intl
```

Afterwards, you can check if the extension is installed using:

```bash
php -m
```

The `intl` extension must now be part of the list of PHP extensions displayed.

!!! warn
    Some hoster use different PHP setups for CLI and web, so `php -m` can report that the `intl` extension is available but in your browser PHP still complains that the extension is missing!

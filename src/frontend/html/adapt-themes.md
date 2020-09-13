If you would like to use one of the default themes as base for your own shop, chances are high that you also want to adapt it to your needs. Modifying a theme is possible without touching the existing CSS and Javascript files by simply overwriting the parts that should be different in your shop.

In both cases, for CSS and JS files, you need to create a new file in one of the directories of your website and which is accessible via the browser. The preferred location depends on the application or framework you are using. Please have a look into their documentation for advices where they should be located. The basic directory structure should be:

* **./mytheme/** (directory named after your theme or project)
    * **aimeos.js** (Javascript file that contains new code or overwrites existing ones)
    * **aimeos.css** (CSS file that contains new styles or overwrites existing ones)

These files must be included in your HTML template **after** the files from the theme so their content can overwrite the original one. The articles about adapting the templates in [Laravel](https://github.com/aimeos/aimeos-laravel#setup) and [Symfony](https://github.com/aimeos/aimeos-symfony#setup) show you where this should be done.

# Cascading Style Sheets

Overwriting existing CSS styles is done by using the same CSS selector and applying different values to the existing instructions or by adding new instructions. For example, if you would like to change the style for a product name:

```css
.catalog-detail-basic .name {
    font-size: 110%;
    color: #B0A060;
    margin: 1em 0.5em;
}
```

to a bigger one with another color that floats left, then use the same CSS selector and:

```css
.catalog-detail-basic .name {
    font-size: 125%;
    color: #003050;
    float: left;
}
```

Modern browsers are able to support you by their web development tools that can inspect HTML nodes. They show the CSS styles that are attached to these nodes and which style overwrites each other. The [CSS reference from w3schools](https://www.w3schools.com/cssref/default.asp) is also a good source that explains the instructions supported by different browsers.

# Javascript

As you can see in the article about [theme fundamentals](theme-basics#Javascript), each component has its own Javascript object with methods that are applied automatically to the HTML nodes if they are present.

Sometimes you don't want that one of the default actions is executed. In this case you can replace the existing method with an empty function, e.g.

```javascript
AimeosCatalogDetail.setupBlockPriceSlider = function() {}
```

In the same way you can completely replace the existing method with a new one:

```javascript
AimeosCatalogDetail.setupBlockPriceSlider = function() {
    // new Javascript code
}
```

Most of the time you may add additional instructions to the existing ones. By overwriting the complete method you would have to duplicate the existing code, which is a bad idea. Fortunately, the decorator pattern can also be used in Javascript to encapsulate an existing method by your own one. This could also be used multiple times if necessary:

```javascript
AimeosCatalogDetail.setupBlockPriceSlider = (function(obj) {
    var fcn = AimeosCatalogDetail.setupBlockPriceSlider.bind(obj);
    return function(/* param1, param2, ... */) {
        // do something before
        fcn(/* param1, param2, ... */);
        // do something afterwards
    }
})(AimeosCatalogDetail);
```

This example assigns a function to the *setupBlockPriceSlider* method of the *AimeosCatalogDetail* object like before by replacing the existing method. But before this is done, the method itself is stored in "fcn" which can be used inside your anonymous function that is returned.

The `(function(fnc) {...})(...)` construct executes the outer function immediately when the inner anonymous function is assigned to `AimeosCatalogDetail.setupBlockPriceSlider`.

Within your anonymous function (which should use the same parameters as the original one) you can call the original function stored in `var fcn` at any time. You are also free to add code before and/or after the original function is executed.

!!! tip
    This way of extending methods is especially handy for the init() methods. You can first execute the original function and then call your new methods. An example would be:
    ```javascript
    AimeosCatalogDetail.init = (function(obj) {
        var init = AimeosCatalogDetail.init.bind(obj);
        return function() {
            obj.setupYourMethod();
            init();
        };
    })(AimeosCatalogDetail);
    ```

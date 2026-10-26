
# basket/require-stock

Customers can order products only if there are enough products in stock

```
client/html/basket/require-stock = 1
```

* Default: `1`
* Type: boolean - True if products must be in stock, false if products can be sold without stock
* Since: 2014.03

Checks that the requested product quantity is in stock before
the customer can add them to his basket and order them. If there
are not enough products available, the customer will get a notice.


# catalog/domains

A list of domain names whose items should be available in the catalog view templates

```
client/html/catalog/domains = Array
(
    [0] => attribute
    [1] => media
    [2] => media/property
    [3] => text
)
```

* Default: 
```
Array
(
    [0] => attribute
    [1] => media
    [2] => media/property
    [3] => text
)
```
* Type: array - List of domain names
* Since: 2014.03

The templates rendering catalog related data usually add the images and
texts associated to each item. If you want to display additional
content like the attributes, you can configure your own list of
domains (attribute, media, price, product, text, etc. are domains)
whose items are fetched from the storage. Please keep in mind that
the more domains you add to the configuration, the more time is required
for fetching the content!

This configuration option can be overwritten by the "client/html/catalog/lists/domains"
configuration option that allows to configure the domain names of the
items fetched specifically for all types of product listings.

See also:

* client/html/catalog/detail/domains
* client/html/catalog/lists/domains
* client/html/catalog/lists/size
* client/html/catalog/lists/levels
* client/html/catalog/lists/sort
* client/html/catalog/lists/pages
* client/html/catalog/stage/domains

# catalog/instock

Show only products which are in stock

```
client/html/catalog/instock = 
```

* Default: ``
* Type: int - Zero to show all products, "1" to show only products with stock
* Since: 2021.10

This configuration option overwrites the "client/html/catalog/domains"
option that allows to configure the domain names of the items fetched
for all catalog related data.

See also:

* client/html/catalog/domains
* client/html/catalog/lists/domains
* client/html/catalog/detail/domains
* client/html/catalog/stage/domains
* client/html/catalog/lists/attrid-default
* client/html/catalog/lists/catid-default
* client/html/catalog/lists/supid-default
* client/html/catalog/lists/size
* client/html/catalog/lists/levels
* client/html/catalog/lists/sort
* client/html/catalog/lists/pages

# catalog/multiroute

Enables multiple entities sharing the same route

```
client/html/catalog/multiroute = 
```

* Default: ``
* Type: bool - TRUE to enable resolving multi-routes, FALSE if not
* Since: 2023.10

To allow categories, products, CMS pages, etc. sharing the same route, you
have to enable this option.


# common/imageset-sizes

Size hints for loading the appropriate catalog home image sizes

```
client/html/common/imageset-sizes = (min-width: 260px) 240px, 100vw
```

* Default: `(min-width: 260px) 240px, 100vw`
* Type: string - HTML image "sizes" attribute
* Since: 2021.04

Modern browsers can load images of different sizes depending on their viewport
size. This is also known as serving "responsive images" because on small
smartphone screens, only small images are loaded while full width images are
loaded on large desktop screens.

A responsive image contains additional "srcset" and "sizes" attributes:

```
 <img src="img.jpg"
 	srcset="img-small.jpg 240w, img-large.jpg 720w"
 	sizes="(max-width: 320px) 240px, 720px"
 >
```

The images and their width in the "srcset" attribute are automatically added
based on the sizes of the generated preview images. The value of the "sizes"
attribute can't be determined by Aimeos because it depends on the used frontend
theme and the size of the images defined in the CSS file. This config setting
adds the required value for the "sizes" attribute.

It's value consists of one or more comma separated rules with
- an optional CSS media query for the view port size
- the (max) width the image will be displayed within this viewport size

Rules without a media query are independent of the view port size and must be
always at last because the rules are evaluated from left to right and the first
matching rule is used.

The above example tells the browser:
- Up to 320px view port width use img-small.jpg
- Above 320px view port width use img-large.jpg

For more information about the "sizes" attribute of the "img" HTML tag read:
{@link https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img#attr-sizes}

See also:

* client/html/common/imageset-sizes
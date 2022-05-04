
# list

List of social network names that should be displayed in the catalog views

```
client/html/catalog/social/list = Array
(
    [0] => facebook
    [1] => twitter
    [2] => pinterest
)
```

* Default: Array
(
    [0] => facebook
    [1] => twitter
    [2] => pinterest
)

* Type: array - List of social network names
* Since: 2017.04

Users can share product links in several social networks. The order of the
social network names in the configuration determines the order of the links
on the catalog pages.

You can add more social links only by configuration if you define a
corresponding URL for the added social network. For example, if you would
like to add Tumblr as social network, you also need to configure a link with
the placeholder for the URL:

```
 client/html/catalog/social/list = array( ..., 'tumblr' )
 client/html/catalog/social/url/tumblr = http://www.tumblr.com/share/link?url=%1$s&name=%2$s
```

Possible placeholders and replaced values are:

* %1$s : Shop URL of the product detail page
* %2$s : Name of the product
* %3$s : URL of the first product image

See also:

* client/html/catalog/social/url/facebook
* client/html/catalog/social/url/twitter
* client/html/catalog/social/url/pinterest

# url
## facebook

URL for sharing product links on Facebook

```
client/html/catalog/social/url/facebook = https://www.facebook.com/sharer.php?u=%1$s&t=%2$s
```

* Default: https://www.facebook.com/sharer.php?u=%1$s&t=%2$s
* Type: string - URL to share products on Facebook
* Since: 2017.04

Users can share product links on Facebook. This requires a URL defined
by Facebook that accepts the transmitted product page URL. This URL must
contain at least the "%1$s" placeholder for the URL to the product detail
page of the shop.

Possible placeholders and replaced values are:

* %1$s : Shop URL of the product detail page
* %2$s : Name of the product
* %3$s : URL of the first product image

See also:

* client/html/catalog/social/list

## pinterest

URL for sharing product links on Pinterest

```
client/html/catalog/social/url/pinterest = https://pinterest.com/pin/create/button/?url=%1$s&description=%2$s&media=%3$s
```

* Default: https://pinterest.com/pin/create/button/?url=%1$s&description=%2$s&media=%3$s
* Type: string - URL to share products on Pinterest
* Since: 2017.04

Users can share product links on Pinterest. This requires a URL defined
by Pinterest that accepts the transmitted product page URL. This URL must
contain the "%1$s", "%2$s" and "%3$s" placeholders for the URL to the
product detail page, the product name and the product image to be useful.

Possible placeholders and replaced values are:

* %1$s : Shop URL of the product detail page
* %2$s : Name of the product
* %3$s : URL of the first product image

See also:

* client/html/catalog/social/list

## twitter

URL for sharing product links on Twitter

```
client/html/catalog/social/url/twitter = https://twitter.com/share?url=%1$s&text=%2$s
```

* Default: https://twitter.com/share?url=%1$s&text=%2$s
* Type: string - URL to share products on Twitter
* Since: 2017.04

Users can share product links on Twitter. This requires a URL defined
by Twitter that accepts the transmitted product page URL. This URL must
contain at least the "%1$s" placeholder for the URL to the product detail
page of the shop.

Possible placeholders and replaced values are:

* %1$s : Shop URL of the product detail page
* %2$s : Name of the product
* %3$s : URL of the first product image

See also:

* client/html/catalog/social/list

## whatsapp

URL for sharing product links over WhatsApp

```
client/html/catalog/social/url/whatsapp = 
```

* Default: 
* Type: string - URL to share products on Facebook
* Since: 2020.01

Users can share product links over WhatsApp. This requires a URL defined
by WhatsApp that accepts the transmitted product page URL. This URL must
contain at least the "%1$s" placeholder for the URL to the product detail
page of the shop.

Possible placeholders and replaced values are:

* %1$s : Shop URL of the product detail page
* %2$s : Name of the product
* %3$s : URL of the first product image

See also:

* client/html/catalog/social/list
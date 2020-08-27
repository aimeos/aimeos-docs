
# name

Class name of the used media common controller implementation

```
controller/common/media/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2016.01

Each default common controller can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the controller factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Controller\Common\Media\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Controller\Common\Media\Mymedia
```

then you have to set the this configuration option:

```
 controller/common/media/name = Mymedia
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyMedia"!


# standard
## extensions

Available files extensions for mime types of uploaded files

```
controller/common/media/standard/extensions = Array
(
    [application/pdf] => pdf
    [application/postscript] => ps
    [application/vnd.ms-excel] => xls
    [application/vnd.ms-powerpoint] => ppt
    [application/vnd.ms-word] => doc
    [application/vnd.oasis.opendocument.graphics] => odg
    [application/vnd.oasis.opendocument.presentation] => odp
    [application/vnd.oasis.opendocument.spreadsheet] => ods
    [application/vnd.oasis.opendocument.text] => odt
    [application/x-gzip] => gz
    [application/zip] => zip
    [image/gif] => gif
    [image/jpeg] => jpg
    [image/png] => png
    [image/svg+xml] => svg
    [image/tiff] => tif
    [text/csv] => csv
)
```

* Default: Array
* Type: array - Associative list of mime types as keys and file extensions as values
* Since: 2018.04

Uploaded files should have the right file extension (e.g. ".jpg" for
JPEG images) so files are recognized correctly if downloaded by users.
The extension of the uploaded file can't be trusted and only its mime
type can be determined automatically. This configuration setting
provides the file extensions for the configured mime types. You can
add more mime type / file extension combinations if required.


## files/allowedtypes

A list of image mime types that are allowed for uploaded image files

```
controller/common/media/standard/files/allowedtypes = Array
(
)
```

* Default: Array
* Type: array - List of image mime types
* Since: 2016.01

The list of allowed image types must be explicitly configured for the
uploaded image files. Trying to upload and store an image file not
available in the list of allowed mime types will result in an exception.


## mimeicon/directory

Directory that contains the icons for the different mime types

```
controller/common/media/standard/mimeicon/directory = 
```

* Default: 
* Type: string - Path or URL to the base directory
* Since: 2016.01

If no preview image can be generated from an uploaded file, an icon
for its mime type is displayed instead. The directory for the mime
icons is structured by the general mime type (e.g. "image") as
sub-directory and the specific name of the mime type (e.g. "jpeg")
as file name.

Avoid leading and trailing slashes for the upload directory string!


## mimeicon/extension

File extension of the mime icon images

```
controller/common/media/standard/mimeicon/extension = .png
```

* Default: .png
* Type: string - File extension including a leading dot, e.g ".jpg"
* Since: 2016.01

If you would like to use different mime icons that are available in
another file format, you have to change the file extension for the
mime icons to the actual ones.

Note: The configured file extension needs a leading dot!


## options

Options used for processing the uploaded media files

```
controller/common/media/standard/options = Array
(
)
```

* Default: Array
* Type: array - Multi-dimendional list of configuration options
* Since: 2016.01

When uploading a file, a preview image for that file is generated if
possible (especially for images). You can configure certain options
for the generated images, namely the implementation of the scaling
algorithm and the quality of the resulting images with

```
 array(
 	'image' => array(
 		'name' => 'Imagick',
 		'quality' => 75,
 	)
 )
```


## preview/allowedtypes

A list of image mime types that are allowed for preview image files

```
controller/common/media/standard/preview/allowedtypes = Array
(
    [0] => image/jpeg
    [1] => image/png
    [2] => image/gif
    [3] => image/svg+xml
)
```

* Default: Array
* Type: array - List of image mime types
* Since: 2016.01

The list of allowed image types must be explicitly configured for the
preview image files. Trying to create a preview image whose mime type
is not available in the list of allowed mime types will result in an
exception.


## previews

Scaling options for preview images

```
controller/common/media/standard/previews = Array
(
    [0] => Array
        (
            [maxwidth] => 32
            [maxheight] => 320
            [force-size] => 
        )

    [1] => Array
        (
            [maxwidth] => 50
            [maxheight] => 960
            [force-size] => 
        )

    [2] => Array
        (
            [maxwidth] => 2160
            [maxheight] => 2880
            [force-size] => 
        )

)
```

* Default: Array
* Type: array - List of image size definitions
* Since: 2019.07

For responsive images, several preview images of different sizes are
generated. This setting controls how many preview images are generated,
what's their maximum width and height and if the given width/height is
enforced by cropping images that doesn't fit.

The setting must consist of a list image size definitions like:

```
 [
   ['maxwidth' => 240, 'maxheight' => 320, 'force-size' => true],
   ['maxwidth' => 720, 'maxheight' => 960, 'force-size' => false],
   ['maxwidth' => 2160, 'maxheight' => 2880, 'force-size' => false],
 ]
```

"maxwidth" sets the maximum allowed width of the image whereas
"maxheight" does the same for the maximum allowed height. If both
values are given, the image is scaled proportionally so it fits into
the box defined by both values. In case the image has different
proportions than the specified ones and "force-size" is false, the
image is resized to fit entirely into the specified box. One side of
the image will be shorter than it would be possible by the specified
box.

If "force-size" is true, scaled images that doesn't fit into the
given maximum width/height are centered and then cropped. By default,
images aren't cropped.

The values for "maxwidth" and "maxheight" can also be null or not
used. In that case, the width or height or both is unbound. If none
of the values are given, the image won't be scaled at all. If only
one value is set, the image will be scaled exactly to the given width
or height and the other side is scaled proportionally.

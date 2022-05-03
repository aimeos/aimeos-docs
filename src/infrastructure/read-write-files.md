At first, creating and reading files seems very simple in PHP: *file_get_contents()* and *file_put_contents()* do a great job for quick results.

Things get more complicated if your files are very big because the product export contains several 10,000 products and you want to re-import them. In both case you might immediately hit the memory limit if you try to create or read all the content first before writing it to the file or processing the input.

Implementation tend to get even more complicated when different file formats come into play. You want to create a CSV file, maybe as compressed .gz file or several files combined in one .zip file? Using only the PHP functions will get messy very soon!

There are utility classes in the [*./src/MW*](https://github.com/aimeos/aimeos-core/tree/master/src/MW) directory of the core available that provide a single interface for handling container and content objects. Container could be anything that can store one or more content objects (e.g. files) like directories or Zip files. Content objects can be any binary or text files, CSV files or spreadsheets.

# Create files

If you want to export some data you need to create a container object first that also defines the type of the expected content. There is a factory class available which simplifies this task and enables you to only hand over the container type, content format and the options for both:

```php
$location = '/path/to/directory';
$containerType = 'Directory';
$contentFormat = 'Gzip';
$options = array( 'gzip-level' => 9 );

$container = \Aimeos\MW\Container\Factory::getContainer( $location, $containerType, $contentFormat, $options );
```

To retrieve the configured values, use something like this code:

```php
$config = $this->context()->config();
$location = $config->get( '.../location', '<default path>' );
$containerType = $config->get( '.../type', '<default type>' );
$containerFormat = $config->get( '.../format', '<default format>' );
$options = $config->get( '.../options', [] );
```

Replace the default values with reasonable ones so creating the container and the files will work even if nothing is explicitly configured!

For each file you want to create, you need to call the **create() and add() methods of the container object**. The name handed over to the *create()* method will be used as file name and shouldn't contain a file extension. The file extension is determined and added by the content object itself so ".csv" will be added for CSV files automatically. Content objects get filled with data by calling the **add() method of the content object**. Please don't mix this with the add() method of the container object!

```php
$content = $container->create( 'myfilename' );
$content->add( '... data ...' );
$content->add( '... data ...' );
$content->add( '... data ...' );
$container->add( $content );

$container->close();
```

You can call add() as often as you need to fill in all data. For the best performance, you should use bigger chunks of data for each call to add(). **For CSV files the data must be an array of values!**

!!! warning
    Don't forget to call **close() on the container object** once you've finished adding content objects as for some containers the data is only written at this point to the disk!

At last, you usually need the real location of the generated container as the extension is added automatically depending on the container type. Don't try to figure that out yourself as containers that support several file types like PHPExcel create different file names depending on the content type! Instead, use the **getName() method of the container object** to retrieve the path to the container file:

```php
$filepath = $container->getName();
```

In case of a directory container, you can also retrieve the names of the files using the **getResource() method of the content objects**:

```php
$files = array();

foreach( $container as $content ) {
    $files[] = $content->getResource();
}
```

Both methods will return the absolute path to the container and content objects if possible. For content objects in Zip containers only the name of the file will be returned.

# Read files

Reading from content files in containers also starts with creating a container object using the factory class first. If a container stores several content files, they should all be of the same type, e.g. CSV, text or binary files so content is read properly.

Remember that CSV returns arrays of values while text returns lines and binary returns data chunks. If the content is in different formats, you can always use "Binary" as content format.

```php
$location = '/path/to/zipfile';
$containerType = 'Zip';
$contentFormat = 'CSV';
$options = array( 'csv-separator' => ';' );

$container = \Aimeos\MW\Container\Factory::getContainer( $location, $containerType, $contentFormat, $options );
```

Like for creating files, you can also retrieve location, type, format and options from the configuration to be more flexible.

Both, the container and content objects support the PHP iterator interface. Thus, you can use foreach() to iterate through all content files and also to iterate over the complete data in each content object:

```php
foreach( $container as $content ) {
    foreach( $content as $data ) {
        print_r( $data );
    }
}

$container->close();
```

The type of $data depends on content format. CSV returns arrays which Binary, GZip and Text returns string values.

!!! warning
    Also, don't forget to call **close() on the container object** to clean up the resources properly

If you know the name of specific content objects, you can use the **get() method of the container object** to retrieve the content directly:

```php
$content = $container->get( 'myfile.txt' );

foreach( $content as $data ) {
    print_r( $data );
}
```

# Container objects

The names of the container implementations are:

## Directory

Manages content files in local directories.

dir-perm (default is 0755)
: Permission bit mask if the directory doesn't exist and have to be created. The leading zero is mandatory so the value is recognized as octal value. The second digit is the mask for the creator of the directory, the third for this group and the forth for everybody else. The digits are bit masks for read, write and search permissions so "4" is read only, "2" is write only and "1" is the ability to descent into the directory and read the names of the next level.

## Zip

Single .zip files containing one or more content files.

tempdir (default is the system temp directory)
: Temporary directory that will store the content objects that are created before they are zipped together. The temporary directory will be removed after closing the container.

# Content objects

Available content objects are:

## Binary

Binary files with arbitrary content.

bin-maxsize (default is 1MB)
: The maximum number of bytes (1048510 by default) that will be read at once from the content object. This value influences for the amount of memory the process will need to allocate.

## CSV

Text files that contain several values per line separated by a defined character.

csv-separator (default is ',')
: Separator character between the values in one line.

csv-enclosure (default is '"')
: Values can contain spaces and even sometimes the separator character itself. To avoid problems reading the values and returning messed up data, each value is enclosed in a pair of characters.

csv-escape (default is '"')
: If the enclosure character is part of the value too, that character has to be escaped too. Usually, this is done by using the same character again.

csv-lineend (default is "\n")
: Character or string that is used to signal the end of a line in the file. This can also be "\r\n" for files that should be compatible with Windows operating systems or any other character or string.

csv-lineend-subst (default is ' ')
: If a value contains the character of string for the line end itself, it must be replaced by something different to avoid corrupt data.

## Gzip

Arbitrary content compressed as .gz file.

gzip-level (default is 5)
: Compression level starting from "1" for fastest compression up to "9" for best compression which takes much longer. The size of the .gz file depends on this value and it will be bigger if "1" is used and smaller for a value of "9".

## Text

Text files with lines ending with a line end character.

text-lineend (default is "\n")
: Character or string that is used to signal the end of a line in the file. This can also be "\r\n" for files that should be compatible with Windows operating systems or any other character or string.

text-maxsize (default is 1MB)
: The maximum number of bytes (1048510 by default) that will be read at once from the content object. This value influences for the amount of memory the process will need to allocate.

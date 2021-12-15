If you want to read, write, copy, or move files or directories, you should always use the Aimeos file system layer. Then, it doesn't matter if the file is stored at the local hard disk or in the cloud and the application can scale infinitely.

To get the file system layer, you need the Aimeos [context](context.md) object, which is the dependency container of Aimeos. In manager, providers, controllers, client and admin objects, the context is always available via the `context()` method.

If you want to use the Aimeos file system layer in any other code, please have a look at the documentation for your host application how to get the context:

* [Laravel](../laravel/extend.md#extend-aimeos)
* [TYPO3](../typo3/extend.md#aimeos-objects)

# Choose a file system

To get access to the default file system, you should use:

```php
$context->fs();
```

This will return the default file system which is always available. There are also several other file systems available for different purposes:

* `fs` : Default file system and fallback if requested file system does not exist
* `fs-admin` : Contains files that are created based on action in the admin backend
* `fs-import` : Files which are going to be imported should be stored there
* `fs-media` : For all media files incl. images, documents, etc.
* `fs-mimeicon` : Read-only file system that contains the icons for the available mime types
* `fs-secure` : File system not accessible from outside for securely storing files

# Available methods

These methods are supported by all file systems and all methods which return the file system object, can be concatenated:

```php
$fs->copy( 'a', 'b' )->move( 'b', 'c' )->rm( 'a' );
$fs->mkdir( 'a' )->rmDir( 'a' );
```

Whenever an error occurs, an `\Aimeos\MW\Filesystem\Exception` is thrown. To handle errors, use:

```php
try
{
	$fs->mkdir( 'mydir' )->copy( 'myfile', 'mydir/myfile' )->rm( 'myfile' );
	// or better use
	$fs->move( 'myfile', 'mydir/myfile' );
}
catch( \Aimeos\MW\Filesystem\Exception $e )
{
	echo 'File operation not possible: ' . $e->getMessage();
}
```

## List files

Returns the file (and directory) names in the given path:

```php
foreach( $fs->scan() as $filename ) {
	echo $filename;
}

foreach( $fs->scan( 'path/to/files' ) as $filename ) {
	echo $filename;
}
```

The `scan()` method returns an `iterable` and you can iterate over the file names using `foreach` or `while`. You can not / should not use it like an array because even if it works for one file system, it may not for another one.

## File exists

Tests if a file exists at the given path:

```php
if( $fs->has( 'myfile' ) ) {
	echo 'file exists';
}

if( $fs->has( 'path/to/file' ) ) {
	echo 'file exists';
}
```

## Copy file

Copies a file to another location:

```php
$fs = $fs->copy( 'fromfile', 'tofile' );
$fs = $fs->copy( 'from/path', 'to/path' );
```

## Move file

Renames a file, moves it to a new location or both at once:

```php
$fs = $fs->move( 'fromfile', 'tofile' );
$fs = $fs->move( 'from/path', 'to/path' );
```

## Remove file

Deletes the file at the given path:

```php
$fs = $fs->rm( 'file' );
$fs = $fs->rm( 'path/to/file' );
```

## Read file

The `read()` method returns the complete content of the remote file:

```php
$content = $fs->read( 'file' );
$content = $fs->read( 'path/to/file' );
```

The method should be only used if you know the the file is small because the complete file content is loaded into memory. For larger files, use `reads()` instead.

You can also read the content of a remote file and writes it to a local one:

```php
$filepath = $fs->readf( 'file' );
$filepath = $fs->readf( 'path/to/file' );
```

The local path to the file which has been created is returned by the method.

For larger files, the `reads()` method should be preferred. It returns the stream descriptor of the (remote) file:

```php
$fd = $fs->reads( 'file' );
$fd = $fs->reads( 'path/to/file' );
```

Afterwards, you can use e.g. `stream_get_contents()` to retrieve the file content in chunks:

```php
while( $content = stream_get_contents( $fd, 1024000 ) ) {
	echo $content;
}
```

## Write file

The `write()` method writes the given content to the named file path:

```php
$fs = $fs->write( 'file', 'content' );
$fs = $fs->write( 'path/to/file', 'content' );
```

The method should be only used if the passed content is small. If you have larger content, use `writef()` or `writes()` to write the content to the remote file system in chunks. This reduces memory usage drastically.

You can also write the content of a local file and to a remote file system:

```php
$fs = $fs->writef( 'remotefile', 'localfile' );
$fs = $fs->writef( 'path/to/remotefile', 'path/to/localfile' );
```

The `writes()` method accepts a file descriptor or stream descriptor to read from and will copy the content from that descriptior to the remote file path:

```php
$fs = $fs->writes( 'file', $fd );
$fs = $fs->writes( 'path/to/file', $fd );
```

# Directory methods

Some file systems like Amazon S3 doesn't support directories. Before using one of these methods you should always check if the file system object returned implements the `DirIface` interface:

```php
$fs = $context->fs( 'fs-media' );

if( $fs instanceof \Aimeos\MW\Filesystem\DirIface ) {
	$fs->isDir( 'mydir' ) ?: $fs->mkdir( 'mydir' );
}
```

You can use paths like `path/to/file` in file systems that doesn't support directories. In that case, the file path is the key to the file (also called "object storage") but `scan( 'path/to' )` will not necessarily return the files that begin with `path/to`.

## Is directory

Tests if the given path is a directory:

```php
if( $fs->isDir( 'mydir' ) ) {
	echo 'is directory';
}

if( $fs->isDir( 'path/to/mydir' ) ) {
	echo 'is directory';
}
```

## Create directory

Creates a new directory at the given path:

```php
$fs = $fs->mkDir( 'mydir' );
$fs = $fs->mkDir( 'path/to/mydir' );
```

## Remove directory

Deletes the directory at the given path:

```php
$fs = $fs->rmDir( 'mydir' );
$fs = $fs->rmDir( 'path/to/mydir' );
```

# Access meta data

Not all file systems support meta data and before using those methods, you need to check if the returned file system object implements the `MetaIface` interface:

```php
$fs = $context->fs( 'fs-media' );

if( $fs instanceof \Aimeos\MW\Filesystem\MetaIface ) {
	$mtime = $fs->time( 'myfile' );
	$size = $fs->size( 'myfile' );
}
```

## File size

Returns the file size in bytes:

```php
$size = $fs->size( 'myfile' );
$size = $fs->size( 'path/to/myfile' );
```

## Modification time

Returns the Unix modification time stamp of the file:

```php
$timestamp = $fs->time( 'myfile' );
$timestamp = $fs->time( 'path/to/myfile' );
```

The timestamp is the number of seconds since 1970-01-01 00:00:00.

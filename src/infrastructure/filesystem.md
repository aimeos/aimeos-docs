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
* `fs-export` : File system where exported data should be stored
* `fs-import` : Files which are going to be imported should be stored there
* `fs-media` : For all media files incl. images, documents, etc.
* `fs-mimeicon` : Read-only file system that contains the icons for the available mime types
* `fs-secure` : File system not accessible from outside for securely storing files
* `fs-theme` : Read-only file system for CSS, JS and image files related to Aimeos themes

For example:

```php
$context->fs( 'fs-import' );
```

# Available methods

These methods are supported by all file systems and all methods which return the file system object, can be concatenated:

```php
$fs->copy( 'a', 'b' )->move( 'b', 'c' )->rm( 'a' );
$fs->mkdir( 'a' )->rmDir( 'a' );
```

Whenever an error occurs, an `\Aimeos\Base\Filesystem\Exception` is thrown. To handle errors, use:

```php
try
{
	$fs->mkdir( 'mydir' )->copy( 'myfile', 'mydir/myfile' )->rm( 'myfile' );
	// or better use
	$fs->move( 'myfile', 'mydir/myfile' );
}
catch( \Aimeos\Base\Filesystem\Exception $e )
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
$filepath = $fs->readf( 'path/to/file', 'path/to/local/file' );
```

The local path to the file which has been created (or passed) is returned by the method.

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

if( $fs instanceof \Aimeos\Base\Filesystem\DirIface ) {
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

if( $fs instanceof \Aimeos\Base\Filesystem\MetaIface ) {
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

# Create own adapter

Custom filesystem adapters should be added to your own [Aimeos extension](../developer/extensions.md) and placed into this directory within the extension:

```
src/Base/Filesystem/
```

For example:

```
src/Base/Filesystem/MyFilesystem.php
```

## Basic methods

To create a filesystem adapter with the absolutely required methods only, you have to implement a class with these methods:

```php
<?php

namespace Aimeos\Base\Filesystem;

class MyFilesystem extends Iface
{
	/**
	 * Copies a file to another location
	 *
	 * @param string $from Path to the original file
	 * @param string $to Path to the new file
	 * @return \Aimeos\Base\Filesystem\Iface Filesystem object for fluent interface
	 * @throws \Aimeos\Base\Filesystem\Exception If an error occurs
	 */
	public function copy( string $from, string $to ) : Iface
	{
		// own code
		return $this;
	}

	/**
	 * Tests if a file exists at the given path
	 *
	 * @param string $path Path to the file
	 * @return bool True if it exists, false if not
	 */
	public function has( string $path ) : bool
	{
		// own code
		return false;
	}

	/**
	 * Renames a file, moves it to a new location or both at once
	 *
	 * @param string $from Path to the original file
	 * @param string $to Path to the new file
	 * @return \Aimeos\Base\Filesystem\Iface Filesystem object for fluent interface
	 * @throws \Aimeos\Base\Filesystem\Exception If an error occurs
	 */
	public function move( string $from, string $to ) : Iface
	{
		// own code
		return $this;
	}

	/**
	 * Returns the content of the remote file
	 *
	 * This method should only be used for small files as the content will be
	 * held in memory. Using it for bigger files may lead to out of memory
	 * conditions. The reads() method can cope with files of all sizes.
	 *
	 * @param string $path Path to the remote file
	 * @return string File content
	 * @throws \Aimeos\Base\Filesystem\Exception If an error occurs
	 */
	public function read( string $path ) : string
	{
		// own code
		return '<file content>';
	}

	/**
	 * Reads the content of the remote file and writes it to a local one
	 *
	 * @param string $path Path to the remote file
	 * @param string|null $local Path to the local file (optional)
	 * @return string Path of the local file
	 * @throws \Aimeos\Base\Filesystem\Exception If an error occurs
	 */
	public function readf( string $path, string $local = null ) : string
	{
		if( $local === null && ( $filename = @tempnam( sys_get_tmp_dir(), 'ai-' ) ) === false ) {
			throw new Exception( sprintf( 'Unable to create file in "%1$s"', sys_get_tmp_dir() ) );
		}

		// own code
		return $local;
	}

	/**
	 * Returns the stream descriptor of the remote file
	 *
	 * @param string $path Path to the remote file
	 * @return resource File stream descriptor
	 * @throws \Aimeos\Base\Filesystem\Exception If an error occurs
	 */
	public function reads( string $path )
	{
		// own code
		return $filehandle;
	}

	/**
	 * Deletes the file at the given path
	 *
	 * @param string $path Path to the file
	 * @return \Aimeos\Base\Filesystem\Iface Filesystem object for fluent interface
	 * @throws \Aimeos\Base\Filesystem\Exception If an error occurs
	 */
	public function rm( string $path ) : Iface
	{
		// own code
		return $this;
	}

	/**
	 * Returns the entries in the given path
	 *
	 * @param string|null $path Path to the filesystem or directory
	 * @return iterable Iterator over the entries or array with entries
	 * @throws \Aimeos\Base\Filesystem\Exception If an error occurs
	 */
	public function scan( string $path = null ) : iterable
	{
		// own code
		return [/* file and directory names */];
	}

	/**
	 * Writes the given content to the file
	 *
	 * If the file already exists, its content will be overwritten. This
	 * method is only suited for smaller files.
	 *
	 * @param string $path Path to the remote file
	 * @param string $content New file content
	 * @return \Aimeos\Base\Filesystem\Iface Filesystem object for fluent interface
	 * @throws \Aimeos\Base\Filesystem\Exception If an error occurs
	 */
	public function write( string $path, string $content ) : Iface
	{
		// own code
		return $this;
	}

	/**
	 * Writes the content of the local file to the remote path
	 *
	 * If the local file already exists, its content will be overwritten.
	 *
	 * @param string $path Path to the remote file
	 * @param string $file Path to the local file
	 * @return \Aimeos\Base\Filesystem\Iface Filesystem object for fluent interface
	 * @throws \Aimeos\Base\Filesystem\Exception If an error occurs
	 */
	public function writef( string $path, string $file ) : Iface
	{
		// own code
		return $this;
	}

	/**
	 * Write the content of the stream descriptor into the remote file
	 *
	 * @param string $path Path to the remote file
	 * @param resource $stream File stream descriptor
	 * @return \Aimeos\Base\Filesystem\Iface Filesystem object for fluent interface
	 * @throws \Aimeos\Base\Filesystem\Exception If an error occurs
	 */
	public function writes( string $path, $stream ) : Iface
	{
		// own code
		return $this;
	}
}
```

## Directory methods

If the filesystem supports directories, you must implement a few more methods and implement the `DirIface` interface:

```php
<?php

namespace Aimeos\Base\Filesystem;

class MyFilesystem extends Iface, DirIface
{
	// basic methods

	/**
	 * Tests if the given path is a directory
	 *
	 * @param string $path Path to the file or directory
	 * @return bool True if directory, false if not
	 * @throws \Aimeos\Base\Filesystem\Exception If an error occurs
	 */
	public function isdir( string $path ) : bool
	{
		// own code
		return false;
	}

	/**
	 * Creates a new directory at the given path
	 *
	 * @param string $path Path to the directory
	 * @return \Aimeos\Base\Filesystem\DirIface Filesystem object for fluent interface
	 * @throws \Aimeos\Base\Filesystem\Exception If an error occurs
	 */
	public function mkdir( string $path ) : DirIface
	{
		// own code
		return $this;
	}

	/**
	 * Deletes the directory at the given path
	 *
	 * @param string $path Path to the directory
	 * @return \Aimeos\Base\Filesystem\DirIface Filesystem object for fluent interface
	 * @throws \Aimeos\Base\Filesystem\Exception If an error occurs
	 */
	public function rmdir( string $path ) : DirIface
	{
		// own code
		return $this;
	}
}
```

You can also implement all three interfaces at once:

```php
class MyFilesystem implements Iface, DirIface, MetaIface
```

## Metadata methods

In case the filesystem also supports retrieving file size and modification time, implement these methods and the `MetaIface` too:

```php
<?php

namespace Aimeos\Base\Filesystem;

class MyFilesystem extends Iface, MetaIface
{
	// basic methods

	/**
	 * Returns the file size
	 *
	 * @param string $path Path to the file
	 * @return int Size in bytes
	 * @throws \Aimeos\Base\Filesystem\Exception If an error occurs
	 */
	public function size( string $path ) : int
	{
		// own code
		return 0; // file size in bytes
	}

	/**
	 * Returns the Unix modification time stamp of the file
	 *
	 * @param string $path Path to the file
	 * @return int Unix time stamp in seconds since 1970-01-01 00:00:00
	 * @throws \Aimeos\Base\Filesystem\Exception If an error occurs
	 */
	public function time( string $path ) : int
	{
		// own code
		return 0; // Seconds since 1970-01-01 00:00:00
	}
}
```

You can also implement all three interfaces at once:

```php
class MyFilesystem implements Iface, DirIface, MetaIface
```

## Error handling

All methods must throw an `\Aimeos\Base\Filesystem\Exception` if an error occurs:

```php
throw new Exception( 'Something went wrong' );
```

If you use 3rd party code which throws own exceptions in case of errors, they must be converted to an `\Aimeos\Base\Filesystem\Exception`:

```php
try {
	// 3rd party method call which may throw an exception
} catch( \Exeption $e ) {
	throw new Exception( 'Something went wrong', 0, $e );
}
```

## Testing

To make sure, your filesystem adapter works, you should write tests to verify that your code is implemented correctly. Therefore, you need to write a test class and store it together with your implementation in your Aimeos extension. The location for your test class should be:

```
tests/Base/Filesystem/
```

For example:

```
tests/Base/Filesystem/MyFilesystemTest.php
```

!!! warning
    The "...Test.php" suffix is important so PHPUnit will recognize that class as test class!

Then, the test class should look like:

```php
<?php

namespace Aimeos\Base\Filesystem;

class MyFilesystemTest extends \PHPUnit\Framework\TestCase
{
	private $object;

	protected function setUp() : void
	{
		$this->object = new \Aimeos\Base\Filesystem\MyFilesystem();
	}

	public function testCopy()
	{
		// test copy() method
	}

	// remaining methods implemented in MyFilesystem class
}
```

!!! tip
	For more details about tests, please have a look at the [PHPUnit documentation](https://phpunit.readthedocs.io/en/latest/).

If you've copied your Aimeos extension into the `./ext/` directory of the [Aimeos Core package](https://github.com/aimeos/aimeos-core) and ran `composer up` to install the required dependencies, you can then execute your tests from within the core directory using:

```
./vendor/bin/phing -Ddir=ext/<myextension> testext
```

For sending e-mails, you need the Aimeos [context](context.md) object, which is the dependency container of Aimeos. In manager, providers, controllers, client and admin objects, the context is always available via `context()`.

If you want to use the Aimeos mailer in any other code, please have a look at the documentation for your host application how to get the context:

* [Laravel](../laravel/extend.md#extend-aimeos)
* [TYPO3](../typo3/extend.md#aimeos-objects)

# Create and send mails

This is a complete example how to send an e-mail including an attachement:

```php
$context->mail()->create()
	->from( 'me@example.com', 'Myself' )
	->to( 'you@example.com', 'Your name' )
	->bcc( 'archive@example.com' )
	->subject( 'Order export' )
	->text( 'Order export from ' . date( 'Y-m-d' ) )
	->html( '<div>Order export from <b>' . date( 'Y-m-d' ) . '</b> </div>' )
	->attach( "id,product,price\n1,test,1.99", 'orders.csv', 'text/csv' )
	->header( 'X-MailGenerator', 'Aimeos' )
	->send();
```

Below, the single method calls are explained in more details.

# Available methods

## Get mailer

First, you have to get the mailer object:

```php
$mailer = $context->mail();
```

This is a wrapper around the mailer from your host application. Therefore, make sure you can send mails from your host application because there's no separate configuration available in Aimeos!

## Create mail message

With the mailer object, you can create a new message:

```php
$msg = $mailer->create();
```

The message object represents your e-mail where you can add addresses and content.

## Add mail addresses

There are several methods for adding e-mail addresses to the mail message object, namely:

* `from()` : E-mail address of the sender
* `to()` : E-mail address of the recipient
* `cc()` : E-mail address which should receive a copy and which is visible in the e-mail
* `bcc()` : E-mail address which gets a copy but is not shown in the e-mail
* `replyTo()` : E-mail address where the recipient can reply to if different from the sender e-mail

The two most important ones are `from()` and `to()` while all others are optional.
Here you can see how those e-mail addresses are added to the message:

```php
$msg->to( 'me@example.com' )->from( 'aimeos@example.com', 'Aimeos' );
$msg->cc( 'someone@example.com' )->bcc( ['hidden@example.com'] );
$msg->replyTo( 'notme@example.com', 'No reply' );
```

You can pass a name as second parameter to each of the methods and it will be shown in the e-mail program (with the exception of `bcc()`). It's also possible to add several e-mail addresses by calling each method more than once:

```php
$msg->to( 'me@example.com', 'Myself' )->to( 'you@example.com' );
```

This will add two recipient e-mail addresses for example and this also works for `from()`, `cc()`, `bcc()` and `replyTo()`.

!!! note
    You can't reuse an existing mail message object to send several mails to different recipients because each call the those methods will add the new recipient to the list of existing ones!

## Set subject and body

Each email can have one subject as well as one text and HTML part. To set the subject for you e-mail, use:

```php
$msg->subject( 'Important notice' );
```

Similarly, you can set the content for the text and HTML part:

```php
$msg->text( 'Order export from ' . date( 'Y-m-d' ) );
$msg->html( '<div>Order export from <b>' . date( 'Y-m-d' ) . '</b> </div>' );
```

For more complex e-mail content, you should use templates to generate the content. For that, the context object also contains a view object which can render any PHP template and use the data assigned to the view object:

```php
$view = $context->view()->assign( [
	'customer' => 'Test User',
	'order' => $order
] );
```

To render the view, you have to pass the relative path of the template to the view:

```php
$msg->html( $view->render( 'relative/path/to/template.php' ) );
```

The path must be relative to the template directories defined in the `manifest.php` file of your extension.

## Attach or embed files

To attach a file to the e-mail, use the `attach()` method:

```php
$msg->attach( $content );
$msg->attach( $content, 'orders.csv' );
$msg->attach( $content, 'orders.csv', 'text/csv' );
```

Besides the content you want to attach, you have to pass name of the file as second and the the mime type of the content as third parameter. The last two parameters helps the e-mail client of the recipient to open or save the file.

In case you want to add an image to the e-mail that is shown in the rendered HTML view, you have to use `embed()` instead:

```html
<img src="<?= $msg->embed( $content, 'logo.png', 'image/png' ) ?>" />
<img src="<?= $msg->embed( $content, 'logo.png' ) ?>" />
<img src="<?= $msg->embed( $content ) ?>" />
```

The method returns a content ID that must be added to the `src` attribute of the `img` tag.

## Custom mail headers

Adding custom headers to the e-mail is possible via the `header()` method:

```php
$msg->header( 'X-MailGenerator', 'Aimeos' );
```

Mail headers can be any key/value pairs.

## Send mail message

Finally, you have to use `send()` to send the e-mail to the mail server:

```php
$msg->send();
// or
$mailer->send( $msg );
```

Both ways are equal, the first one uses the `send()` method of the mail message object while the second one uses the mailer object you got from the context and requires the mail message object as parameter.

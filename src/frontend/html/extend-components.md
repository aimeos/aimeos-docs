Sometimes you need additional data from the database for one of the components because your template should display this information. If you only want to add data, **extending existing component classes** is troublesome. Another developer may want to add other data and several users might need the information from both classes in their templates.

A far better way is creating an **HTML client decorator** and configure this decorator for the component where the information should be added to the views. In this case, anybody else can add both decorators (and more) only by configuration. This way of stacking is far more flexible than extending classes.

The decorators you are implementing have to be stored in your own Aimeos extension in this directory:

```
./client/html/src/Client/Html/Common/Decorator/
```

The directory matches the namespace of the decorator class.

# Basic class structure

A basic skeleton for an HTML client decorator is very simple as the abstract class contains all required logic to get a working decorator:

```php
namespace Aimeos\Client\Html\Common\Decorator;

class Mydecorator
    extends \Aimeos\Client\Html\Common\Decorator\Base
    implements \Aimeos\Client\Html\Common\Decorator\Iface
{
}
```

Decorators wrap around existing components like layers of an onion and there's no limitation in the numbers of layers. You only have to keep in mind that you will add another function call to the stack for each decorator you are adding.

Both, components and decorators must implement the same interface and therefore the same public methods. Thus, you can overwrite **any public method but no private or protected** ones. The list of public methods for both are:

* data()
: Adds the necessary data used in the template

* body()
: Returns the HTML code for insertion into the body

* header()
: Returns the HTML string for insertion into the header

* getSubClient()
: Returns the sub-client given by its name

* view()
: Returns the view object that will generate the HTML output

* modify()
: Modifies the cached body or header content to replace content based on sessions or cookies

* init()
: Processes the input, e.g. check and store the given values

* setView()
: Sets the view object that will generate the HTML output

The `modify()` method is only used by **components that implement content caching**, like the catalog filter, lists or detail component. Please have a look into the component you want to decorate if they support content caching and will call both methods.

# Supporting methods

Decorators inherit all methods available in the components and subparts via the [\Aimeos\Client\Html\Base](https://github.com/aimeos/ai-client-html/blob/master/client/html/src/Client/Html/Base.php) class. There's one additional method exclusive to decorators named `getClient()`. It returns the HTML client or decorator representing the next layer in the onion down to the core object:

```php
public function init()
{
    // do something before
    $this->getClient()->init();
    // do something afterwards
}
```

You must use it to call the same method of the next object. Otherwise, the methods of the inner objects **won't be executed**.

# Example

Say, you want to add the first review of each product to the catalog list component because your new templates should display the latest review in the list view. If this information should be available in both, body and header of the component, you should create a decorator like that one:

```php
namespace Aimeos\Client\Html\Common\Decorator;

class Mydecorator
    extends \Aimeos\Client\Html\Common\Decorator\Base
    implements \Aimeos\Client\Html\Common\Decorator\Iface
{
    public function data( \Aimeos\MW\View\Iface $view, array &$tags = [], string &$expire = null ) : \Aimeos\MW\View\Iface
    {
        $view = parent::data( $view, $tags, $expire );

        // access already added data
        $products = $view->get( 'listItems', map() );

        // fetch some items from the database
        $view->decoratornameMyparam = ...

        return $view;
    }
}
```

For your parameters, you should use the **name of your decorator as prefix** to prevent overwriting parameters from other decorators or subparts.

# Configuration

After you've created your new decorator, you need to tell the factory to add it to the HTML client for the component. This is done via configuration, e.g. for the catalog lists component:

```
client/html/catalog/lists/decorators/global = ['Mydecorator']
```

For the mini basket component, the configuration would be:

```
client/html/basket/mini/decorators/global = ['Mydecorator']
```

You can add your decorator to every component as they all implement the same interface provided the required data is available. In case you really want to add a decorator to ALL components, you can use this configuration setting instead:

```
client/html/common/decorators/default = ['Mydecorator']
```

!!! note
    Remember that decorators suitable for all components must be very generic and must work not only for components creating the output for the browser but also for the components that are generating the e-mails executed by cronjobs on the command line!

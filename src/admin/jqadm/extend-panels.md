Sometimes, you need to perform additional operations for one of the panels, e.g. because secondary services need to be informed about updates. Extending from existing panel classes is troublesome because you can only use one class implementation.

A far better way is creating a **decorator** and configure this decorator for the panel where the actions should be performed. In this case, anyone can add more than one decorator only by configuration. This way of stacking is far more flexible than extending classes.

The decorators you are implementing have to be stored in your own Aimeos extension in this directory:

```
./src/Admin/JQAdm/Common/Decorator/
```

The directory matches the namespace of the decorator class.

# Basic class structure

A basic skeleton for an HTML client decorator is very simple as the abstract class contains all required logic to get a working decorator:

```php
namespace Aimeos\Admin\JQAdm\Common\Decorator;

class Mydecorator extends Base
{
}
```

Decorators wrap around existing panels like layers of an onion and there's no limitation in the numbers of layers. You only have to keep in mind that you will add another function call to the stack for each decorator you are adding.

Both, panel classes and decorators must implement the same interface and therefore the same public methods. Thus, you can overwrite **any public method but no private or protected** ones. The list of public methods for both are:

* copy()
: Adds the data of the copied item to the template

* create()
: Creates a detail view without data or display the data again in case of an error

* delete()
: Deletes one or more items

* export()
: Pushes the filters for an export to the message queue

* get()
: Adds the data for the given ID to the template

* save()
: Saves a new or modified item to the storage

* search()
: Creates a list view of the data including filters

* setView()
: Sets the view object that will generate the HTML output

# Example

Say, you want to notify a 3rd party system if an item is saved or deleted. Create a new decorator with the corresponding methods:

```php
namespace Aimeos\Admin\JQAdm\Common\Decorator;

class Mydecorator extends Base
{
    public function delete() : ?string
    {
        $params = $this->view()->param();
        // do something
        $result = $this->getClient()->delete();
        // notify the 3rd party system
        return $result;
    }

    public function save() : ?string
    {
        $params = $this->view()->param();
        // do something
        $result = $this->getClient()->save();
        // assigned by inner objects
        $item = $this->view()->item;
        // notify the 3rd party system
        return $result;
    }
}
```

# Configuration

After you've created your new decorator, you need to tell the factory to add it to the panel class. This is done via configuration, e.g. for the product panel:

```
admin/jqadm/product/decorators/global = ['Mydecorator']
```

For the catalog panel, the configuration would be:

```
admin/jqadm/catalog/decorators/global = ['Mydecorator']
```

You can add your decorator to every component as they all implement the same interface provided the required data is available. In case you really want to add a decorator to ALL components, you can use this configuration setting instead:

```
admin/jqadm/common/decorators/default = ['Mydecorator']
```

!!! note
    Remember that decorators suitable for all components must be very generic!

Often, it's necessary to replace the templates of a component or subpart with a different one, e.g. if you need a different HTML structure or want to add more HTML nodes. In these cases, you can overwrite an existing template by creating a new file with the same name and within the same directory structure as the orginal file in your own extension.

!!! tip
    Use the [Aimeos extension builder](https://aimeos.org/extensions) to create an extension for your shop site. The generated extension skeletons contains all necessary directories and configuration to be used out of the box.

All standard templates are stored in the [client/html/templates/](https://github.com/aimeos/ai-client-html/tree/master/client/html/templates) directory of the ai-client-html extension. There are sub-directories for each component type and component implementation, e.g. the "catalog/detail" sub-directory for the catalog detail component. Below, the ".php" template files are stored for the component and all its subparts.

The naming of the template files in the directory structure is:
```
<component type>/<component name>/[<subpart name>[-<sub-subpart name>]-]{body,header}-<variant>.php
```

The naming schema matches the hierarchy of the components and their subparts, which is also reflected by the corresponding classes in the `src/` directory. Examples for this naming are:

```
catalog/detail/header-standard.php
catalog/detail/service-body-mine.php
```

Own extensions that contain template files in the `client/html/templates/` directory which are named the same as the existing ones are used first. If no template files are found in own extensions, then the default ones from the ai-client-html extension are used.

!!! note
    The output of the **basket/mini** component is cached in the session of the user for performance reasons. If you change the templates, you will see changes only after the component is updated e.g. by adding a product. To ease development, you can [disable the basket cache](../../config/client-html/basket-cache#enable) in your Aimeos installation via configuration.

!!! warning
    Changing the templates of the **catalog/detail/session** component requires some more attention. For example, the output for the last seen items is rendered if you visit a detail view and the HTML snippet is added to the session of the user.

    If you change the template now and reload the page, nothing will happen because the HTML snippet in your session isn't updated. You have to visit the detail page of another product to see a new item in the list.

    The existing items will still keep the layout when they have been added! To clear all entries that are using older versions of the template, you have to delete the session cookie in your browser.

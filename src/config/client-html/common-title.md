
# format

Format of the page title with the page name (%1$s) and the site label (%2$s)

```
client/html/common/title/format = %1$s | %2$s
```

* Default: `%1$s | %2$s`
* Type: string - Format string for sprintf() with the page name and the site label
* Since: 2026.10

The page titles of the shop components (e.g. product, category, basket or
checkout pages) consist of the page name and the label of the current site.
The default format "%1$s | %2$s" creates titles like "Coffee | Shop". You can
use e.g. "%1$s » %2$s" for another separator or "%1$s" to omit the site
label. Titles from the "meta-title" texts of products and categories are
used as they are.

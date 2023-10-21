Most of the time, you already have an ERP system which manages all your products and most of the information required to fill your shop are stored there. In this case, most often you want to bulk import the product information from the ERP system into your shop and update it regularly. You can use the product import job controller for XML files to import/update the products.

!!! note
    The product import is triggered via a cronjob/scheduler that executes the "product/import/xml" job controller.

# Available configuration

[controller/jobs/product/import/xml/backup](../config/controller-jobs/product-import.md#backup)
: Directory for storing imported files

[controller/jobs/product/import/xml/domains](../config/controller-jobs/product-import.md#domains)
: List of domain names that should be retrieved along with the product items

[controller/jobs/product/import/xml/location](../config/controller-jobs/product-import.md#location)
: Path to the directory with the XML files

[controller/jobs/product/import/xml/max-query](../config/controller-jobs/product-import.md#max-query)
: Maximum number of XML nodes processed at once

# Structure

```xml
<?xml version="1.0" encoding="UTF-8" standalone="no" ?>

<products>
  <!-- List of product items with unique code as "ref" -->
  <productitem ref="TEST-ARTICLE">

    <!-- Required, possible values: "default" (article), "bundle", "select", "voucher" -->
    <product.type><![CDATA[default]]></product.type>

    <!-- Required, unique SKU of the product -->
    <product.code><![CDATA[TEST-ARTICLE]]></product.code>

    <!-- Required, label of the product, used if no language specific name is avialable -->
    <product.label><![CDATA[Test article]]></product.label>

    <!-- Optional, possible values: 1 = enabled (default), 0 = disabled, -1 = review, -2 =archived -->
    <product.status><![CDATA[1]]></product.status>

    <!-- Optional, JSON encoded (multi-dimensional) key/value pairs with arbitrary settings -->
    <product.config><![CDATA[{"key": "value"}]]></product.config>

    <!-- Optional, start ISO date/time value (YYYY-MM-DDTHH:mm:ss) the product is available from -->
    <product.datestart><![CDATA[2000-01-01T00:00:00]]></product.datestart>

    <!-- Optional, end ISO date/time value (YYYY-MM-DDTHH:mm:ss) the product is available to -->
    <product.dateend><![CDATA[2000-01-01T23:59:59]]></product.dateend>

    <!-- Optional, items associated to the product -->
    <lists>

      <!-- Optional, list of text items -->
      <text>

        <!-- lists.type: Optional, possible values: "default" (default) or any other available list type -->
        <!-- lists.config: Optional, JSON encoded (multi-dimensional) key/value pairs with arbitrary settings -->
        <!-- lists.position: Optional, position of the text if multiple items are available for the the same text type and list type -->
        <!-- lists.status: Optional, possible values: 1 = enabled (default), 0 = disabled, -1 = review, -2 =archived -->
        <!-- lists.datestart: Optional, start ISO date/time value (YYYY-MM-DDTHH:mm:ss) the text is available from -->
        <!-- lists.dateend: Optional, end ISO date/time value (YYYY-MM-DDTHH:mm:ss) the text is available to -->
        <textitem
          lists.type="default"
          lists.config="{&quot;key&quot;: &quot;value&quot;}"
          lists.position="0"
          lists.status="1"
          lists.datestart="2000-01-01T00:00:00"
          lists.dateend="2000-01-01T23:59:59" >

          <!-- Required, possible values: "name", "short", "long", "meta-keyword", "meta-description", "basket" (product name/text in basket), "url" (product name in URL) -->
          <text.type><![CDATA[name]]></text.type>

          <!-- Required, two letter ISO language code -->
          <text.languageid><![CDATA[en]]></text.languageid>

          <!-- Required, arbitrary text content in the language of the ISO code -->
          <text.content><![CDATA[product name in English]]></text.content>

          <!-- Optional, label of the text for editors not speaking the language of the content -->
          <text.label><![CDATA[English product name]]></text.label>

          <!-- Optional, possible values: 1 = enabled (default), 0 = disabled, -1 = review, -2 =archived -->
          <text.status><![CDATA[1]]></text.status>

          <!-- Optional, items associated to the text -->
          <lists>

            <!-- Optional, list of customer items -->
            <customer>

              <!-- ref: Required, unique code or user name of the customer -->
              <!-- lists.type: Optional, possible values: "default" (default) or any other available list type -->
              <!-- lists.config: Optional, JSON encoded (multi-dimensional) key/value pairs with arbitrary settings -->
              <!-- lists.position: Optional, position of the text if multiple items are available for the the same text type and list type -->
              <!-- lists.status: Optional, possible values: 1 = enabled (default), 0 = disabled, -1 = review, -2 =archived -->
              <!-- lists.datestart: Optional, start ISO date/time value (YYYY-MM-DDTHH:mm:ss) the text is available from -->
              <!-- lists.dateend: Optional, end ISO date/time value (YYYY-MM-DDTHH:mm:ss) the text is available to -->
              <customeritem ref="customercode"
                lists.type="default"
                lists.config="{&quot;key&quot;: &quot;value&quot;}"
                lists.position="0"
                lists.status="1"
                lists.datestart="2000-01-01T00:00:00"
                lists.dateend="2000-01-01T23:59:59" />

            </customer>
            <!-- more customer items -->

            <!-- Optional, list of customer group items -->
            <group>

              <!-- ref: Required, unique code of the customer group -->
              <!-- lists.type: Optional, possible values: "default" (default) or any other available list type -->
              <!-- lists.config: Optional, JSON encoded (multi-dimensional) key/value pairs with arbitrary settings -->
              <!-- lists.position: Optional, position of the text if multiple items are available for the the same text type and list type -->
              <!-- lists.status: Optional, possible values: 1 = enabled (default), 0 = disabled, -1 = review, -2 =archived -->
              <!-- lists.datestart: Optional, start ISO date/time value (YYYY-MM-DDTHH:mm:ss) the text is available from -->
              <!-- lists.dateend: Optional, end ISO date/time value (YYYY-MM-DDTHH:mm:ss) the text is available to -->
              <groupitem ref="groupcode"
                lists.type="default"
                lists.config="{&quot;key&quot;: &quot;value&quot;}"
                lists.position="0"
                lists.status="1"
                lists.datestart="2000-01-01T00:00:00"
                lists.dateend="2000-01-01T23:59:59" />

            </group>
            <!-- more group items -->

          </lists>
        </textitem>
        <!-- more text items -->
      </text>

      <!-- Optional, list of media items -->
      <media>

        <!-- lists.type: Optional, possible values: "default" (default) or any other available list type -->
        <!-- lists.config: Optional, JSON encoded (multi-dimensional) key/value pairs with arbitrary settings -->
        <!-- lists.position: Optional, position of the text if multiple items are available for the the same text type and list type -->
        <!-- lists.status: Optional, possible values: 1 = enabled (default), 0 = disabled, -1 = review, -2 =archived -->
        <!-- lists.datestart: Optional, start ISO date/time value (YYYY-MM-DDTHH:mm:ss) the text is available from -->
        <!-- lists.dateend: Optional, end ISO date/time value (YYYY-MM-DDTHH:mm:ss) the text is available to -->
        <mediaitem
          lists.type="default"
          lists.config="{&quot;key&quot;: &quot;value&quot;}"
          lists.position="0"
          lists.status="1"
          lists.datestart="2000-01-01T00:00:00"
          lists.dateend="2000-01-01T23:59:59" >

          <!-- Required, possible values: "default" (default), "download" or any other available media type -->
          <media.type><![CDATA[default]]></media.type>

          <!-- Required, two letter ISO language code or empty for not language specific media files -->
          <media.languageid><![CDATA[]]></media.languageid>

          <!-- Required, absolute or relative URL to the media file on the server -->
          <media.url><![CDATA[path/to/file.jpg]]></media.url>

          <!-- Optional, absolute or relative URL to the preview file on the server -->
          <media.preview><![CDATA[path/to/preview.jpg]]></media.preview>

          <!-- Optional, mime type of the file referenced by the URL -->
          <media.mimetype><![CDATA[image/jpeg]]></media.mimetype>

          <!-- Optional, label for the media file, will be used as title if no language specific title is available -->
          <media.label><![CDATA[test image]]></media.label>

          <!-- Optional, possible values: 1 = enabled (default), 0 = disabled, -1 = review, -2 =archived -->
          <media.status><![CDATA[1]]></media.status>

          <!-- Optional, items associated to the media -->
          <lists>

            <!-- Optional, list of customer items -->
            <customer>

              <!-- ref: Required, unique code or user name of the customer -->
              <!-- lists.type: Optional, possible values: "default" (default) or any other available list type -->
              <!-- lists.config: Optional, JSON encoded (multi-dimensional) key/value pairs with arbitrary settings -->
              <!-- lists.position: Optional, position of the text if multiple items are available for the the same text type and list type -->
              <!-- lists.status: Optional, possible values: 1 = enabled (default), 0 = disabled, -1 = review, -2 =archived -->
              <!-- lists.datestart: Optional, start ISO date/time value (YYYY-MM-DDTHH:mm:ss) the text is available from -->
              <!-- lists.dateend: Optional, end ISO date/time value (YYYY-MM-DDTHH:mm:ss) the text is available to -->
              <customeritem ref="customercode"
                lists.type="default"
                lists.config="{&quot;key&quot;: &quot;value&quot;}"
                lists.position="0"
                lists.status="1"
                lists.datestart="2000-01-01T00:00:00"
                lists.dateend="2000-01-01T23:59:59" />

            </customer>
            <!-- more customer items -->

            <!-- Optional, list of customer group items -->
            <group>

              <!-- ref: Required, unique code of the customer group -->
              <!-- lists.type: Optional, possible values: "default" (default) or any other available list type -->
              <!-- lists.config: Optional, JSON encoded (multi-dimensional) key/value pairs with arbitrary settings -->
              <!-- lists.position: Optional, position of the text if multiple items are available for the the same text type and list type -->
              <!-- lists.status: Optional, possible values: 1 = enabled (default), 0 = disabled, -1 = review, -2 =archived -->
              <!-- lists.datestart: Optional, start ISO date/time value (YYYY-MM-DDTHH:mm:ss) the text is available from -->
              <!-- lists.dateend: Optional, end ISO date/time value (YYYY-MM-DDTHH:mm:ss) the text is available to -->
              <groupitem ref="groupcode"
                lists.type="default"
                lists.config="{&quot;key&quot;: &quot;value&quot;}"
                lists.position="0"
                lists.status="1"
                lists.datestart="2000-01-01T00:00:00"
                lists.dateend="2000-01-01T23:59:59" />

            </group>
            <!-- more group items -->

          </lists>

          <!-- Optional, arbitrary media properties -->
          <property>

            <!-- Optional, arbitrary media properties -->
            <propertyitem>

              <!-- Required, possible values: "name" (default) or any other available media type -->
              <media.property.type><![CDATA[name]]></media.property.type>

              <!-- Required, two letter ISO language code or empty for no language -->
              <media.property.languageid><![CDATA[en]]></media.property.languageid>

              <!-- Required, value of the media property, e.g. the image title -->
              <media.property.value><![CDATA[Image description]]></media.property.value>

            </propertyitem>
            <!-- more property items -->

          </property>
        </mediaitem>
        <!-- more media items -->

      </media>

      <!-- Optional, list of price items -->
      <price>

        <!-- lists.type: Optional, possible values: "default" (default) or any other available list type -->
        <!-- lists.config: Optional, JSON encoded (multi-dimensional) key/value pairs with arbitrary settings -->
        <!-- lists.position: Optional, position of the text if multiple items are available for the the same text type and list type -->
        <!-- lists.status: Optional, possible values: 1 = enabled (default), 0 = disabled, -1 = review, -2 =archived -->
        <!-- lists.datestart: Optional, start ISO date/time value (YYYY-MM-DDTHH:mm:ss) the text is available from -->
        <!-- lists.dateend: Optional, end ISO date/time value (YYYY-MM-DDTHH:mm:ss) the text is available to -->
        <priceitem
          lists.type="default"
          lists.config="{&quot;key&quot;: &quot;value&quot;}"
          lists.position="0"
          lists.status="1"
          lists.datestart="2000-01-01T00:00:00"
          lists.dateend="2000-01-01T23:59:59" >

          <!-- Required, possible values: "default" (default) or any other available media type -->
          <price.type><![CDATA[default]]></price.type>

          <!-- Required, three letter ISO currency code -->
          <price.currencyid><![CDATA[EUR]]></price.currencyid>

          <!-- Required, tax rate of the price in "0.00" format -->
          <price.taxrate><![CDATA[20.00]]></price.taxrate>

          <!-- Required, minimum quantity the price is avialable from for block/tier prices -->
          <price.quantity><![CDATA[1]]></price.quantity>

          <!-- Required, price value in "0.00" format (prices must be either all net or all gross prices) -->
          <price.value><![CDATA[100.00]]></price.value>

          <!-- Optional, shipping cost value per product in "0.00" format -->
          <price.costs><![CDATA[5.00]]></price.costs>

          <!-- Optional, difference to the previous product price in "0.00" format -->
          <price.rebate><![CDATA[20.00]]></price.rebate>

          <!-- Optional, label for the price for editors -->
          <price.label><![CDATA[Reduced price]]></price.label>

          <!-- Optional, possible values: 1 = enabled (default), 0 = disabled, -1 = review, -2 =archived -->
          <price.status><![CDATA[1]]></price.status>

          <!-- Optional, items associated to the price -->
          <lists>

            <!-- Optional, list of customer items -->
            <customer>

              <!-- ref: Required, unique code or user name of the customer -->
              <!-- lists.type: Optional, possible values: "default" (default) or any other available list type -->
              <!-- lists.config: Optional, JSON encoded (multi-dimensional) key/value pairs with arbitrary settings -->
              <!-- lists.position: Optional, position of the text if multiple items are available for the the same text type and list type -->
              <!-- lists.status: Optional, possible values: 1 = enabled (default), 0 = disabled, -1 = review, -2 =archived -->
              <!-- lists.datestart: Optional, start ISO date/time value (YYYY-MM-DDTHH:mm:ss) the text is available from -->
              <!-- lists.dateend: Optional, end ISO date/time value (YYYY-MM-DDTHH:mm:ss) the text is available to -->
              <customeritem ref="customercode"
                lists.type="default"
                lists.config="{&quot;key&quot;: &quot;value&quot;}"
                lists.position="0"
                lists.status="1"
                lists.datestart="2000-01-01T00:00:00"
                lists.dateend="2000-01-01T23:59:59" />

            </customer>
            <!-- more customer items -->

            <!-- Optional, list of customer group items -->
            <group>

              <!-- ref: Required, unique code of the customer group -->
              <!-- lists.type: Optional, possible values: "default" (default) or any other available list type -->
              <!-- lists.config: Optional, JSON encoded (multi-dimensional) key/value pairs with arbitrary settings -->
              <!-- lists.position: Optional, position of the text if multiple items are available for the the same text type and list type -->
              <!-- lists.status: Optional, possible values: 1 = enabled (default), 0 = disabled, -1 = review, -2 =archived -->
              <!-- lists.datestart: Optional, start ISO date/time value (YYYY-MM-DDTHH:mm:ss) the text is available from -->
              <!-- lists.dateend: Optional, end ISO date/time value (YYYY-MM-DDTHH:mm:ss) the text is available to -->
              <groupitem ref="groupcode"
                lists.type="default"
                lists.config="{&quot;key&quot;: &quot;value&quot;}"
                lists.position="0"
                lists.status="1"
                lists.datestart="2000-01-01T00:00:00"
                lists.dateend="2000-01-01T23:59:59" />

            </group>
            <!-- more group items -->

          </lists>
        </priceitem>
        <!-- more price items -->

      </price>

      <!-- Optional, list of attribute items -->
      <attribute>

        <!-- ref: Required, unique code of attribute domain, type and code separated by a pipe -->
        <!-- lists.type: Optional, possible values: "default" (default), "variant" (variant building product attribute), "config" (configurable product attribute), "custom" (custom can enter value), "hidden" (not shown to customer but added in order) -->
        <!-- lists.config: Optional, JSON encoded (multi-dimensional) key/value pairs with arbitrary settings -->
        <!-- lists.position: Optional, position of the text if multiple items are available for the the same text type and list type -->
        <!-- lists.status: Optional, possible values: 1 = enabled (default), 0 = disabled, -1 = review, -2 =archived -->
        <!-- lists.datestart: Optional, start ISO date/time value (YYYY-MM-DDTHH:mm:ss) the text is available from -->
        <!-- lists.dateend: Optional, end ISO date/time value (YYYY-MM-DDTHH:mm:ss) the text is available to -->
        <attributeitem ref="product|color|black"
          lists.type="default"
          lists.config="{&quot;key&quot;: &quot;value&quot;}"
          lists.position="0"
          lists.status="1"
          lists.datestart="2000-01-01T00:00:00"
          lists.dateend="2000-01-01T23:59:59" />
        <!-- more attribute items -->

      </attribute>

      <!-- Optional, list of catalog items -->
      <catalog>

        <!-- ref: Required, unique catalog code -->
        <!-- lists.type: Optional, possible values: "default" and "promotion" (promotional products) -->
        <!-- lists.config: Optional, JSON encoded (multi-dimensional) key/value pairs with arbitrary settings -->
        <!-- lists.position: Optional, position of the text if multiple items are available for the the same text type and list type -->
        <!-- lists.status: Optional, possible values: 1 = enabled (default), 0 = disabled, -1 = review, -2 =archived -->
        <!-- lists.datestart: Optional, start ISO date/time value (YYYY-MM-DDTHH:mm:ss) the text is available from -->
        <!-- lists.dateend: Optional, end ISO date/time value (YYYY-MM-DDTHH:mm:ss) the text is available to -->
        <catalogitem ref="CATALOG-CODE"
          lists.type="default"
          lists.config="{&quot;key&quot;: &quot;value&quot;}"
          lists.position="0"
          lists.status="1"
          lists.datestart="2000-01-01T00:00:00"
          lists.dateend="2000-01-01T23:59:59" />
        <!-- more catalog items -->

      </catalog>

      <!-- Optional, list of product items -->
      <product>

        <!-- ref: Required, unique product code (SKU) -->
        <!-- lists.type: Optional, possible values: "default" (for articles of bundles and selections), "suggestion" (recommended products) and "bought-together" -->
        <!-- lists.config: Optional, JSON encoded (multi-dimensional) key/value pairs with arbitrary settings -->
        <!-- lists.position: Optional, position of the text if multiple items are available for the the same text type and list type -->
        <!-- lists.status: Optional, possible values: 1 = enabled (default), 0 = disabled, -1 = review, -2 =archived -->
        <!-- lists.datestart: Optional, start ISO date/time value (YYYY-MM-DDTHH:mm:ss) the text is available from -->
        <!-- lists.dateend: Optional, end ISO date/time value (YYYY-MM-DDTHH:mm:ss) the text is available to -->
        <productitem ref="TEST-PRODUCT-2"
          lists.type="default"
          lists.config="{&quot;key&quot;: &quot;value&quot;}"
          lists.position="0"
          lists.status="1"
          lists.datestart="2000-01-01T00:00:00"
          lists.dateend="2000-01-01T23:59:59" />
        <!-- more product items -->

      </product>

      <!-- Optional, list of supplier items -->
      <supplier>

        <!-- ref: Required, unique supplier code -->
        <!-- lists.type: Optional, possible values: "default" -->
        <!-- lists.config: Optional, JSON encoded (multi-dimensional) key/value pairs with arbitrary settings -->
        <!-- lists.position: Optional, position of the text if multiple items are available for the the same text type and list type -->
        <!-- lists.status: Optional, possible values: 1 = enabled (default), 0 = disabled, -1 = review, -2 =archived -->
        <!-- lists.datestart: Optional, start ISO date/time value (YYYY-MM-DDTHH:mm:ss) the text is available from -->
        <!-- lists.dateend: Optional, end ISO date/time value (YYYY-MM-DDTHH:mm:ss) the text is available to -->
        <supplieritem ref="SUPPLIER-CODE"
          lists.type="default"
          lists.config="{&quot;key&quot;: &quot;value&quot;}"
          lists.position="0"
          lists.status="1"
          lists.datestart="2000-01-01T00:00:00"
          lists.dateend="2000-01-01T23:59:59" />
        <!-- more supplier items -->

      </supplier>

      <!-- Optional, list of customer items -->
      <customer>

        <!-- ref: Required, unique code or user name of the customer -->
        <!-- lists.type: Optional, possible values: "default" (default) or any other available list type -->
        <!-- lists.config: Optional, JSON encoded (multi-dimensional) key/value pairs with arbitrary settings -->
        <!-- lists.position: Optional, position of the text if multiple items are available for the the same text type and list type -->
        <!-- lists.status: Optional, possible values: 1 = enabled (default), 0 = disabled, -1 = review, -2 =archived -->
        <!-- lists.datestart: Optional, start ISO date/time value (YYYY-MM-DDTHH:mm:ss) the text is available from -->
        <!-- lists.dateend: Optional, end ISO date/time value (YYYY-MM-DDTHH:mm:ss) the text is available to -->
        <customeritem ref="customercode"
          lists.type="default"
          lists.config="{&quot;key&quot;: &quot;value&quot;}"
          lists.position="0"
          lists.status="1"
          lists.datestart="2000-01-01T00:00:00"
          lists.dateend="2000-01-01T23:59:59" />

      </customer>
      <!-- more customer items -->

      <!-- Optional, list of customer group items -->
      <group>

        <!-- ref: Required, unique code of the customer group -->
        <!-- lists.type: Optional, possible values: "default" (default) or any other available list type -->
        <!-- lists.config: Optional, JSON encoded (multi-dimensional) key/value pairs with arbitrary settings -->
        <!-- lists.position: Optional, position of the text if multiple items are available for the the same text type and list type -->
        <!-- lists.status: Optional, possible values: 1 = enabled (default), 0 = disabled, -1 = review, -2 =archived -->
        <!-- lists.datestart: Optional, start ISO date/time value (YYYY-MM-DDTHH:mm:ss) the text is available from -->
        <!-- lists.dateend: Optional, end ISO date/time value (YYYY-MM-DDTHH:mm:ss) the text is available to -->
        <groupitem ref="groupcode"
          lists.type="default"
          lists.config="{&quot;key&quot;: &quot;value&quot;}"
          lists.position="0"
          lists.status="1"
          lists.datestart="2000-01-01T00:00:00"
          lists.dateend="2000-01-01T23:59:59" />

      </group>
      <!-- more group items -->

    </lists>

    <!-- Optional, list of product property items -->
    <property>

      <!-- Optional, arbitrary product properties -->
      <propertyitem>

        <!-- Required, any available product property type like "package-height", "package-length", "package-width", "package-weight" -->
        <product.property.type><![CDATA[package-weight]]></product.property.type>

        <!-- Required, two letter ISO language code or empty for no language -->
        <product.property.languageid><![CDATA[]]></product.property.languageid>

        <!-- Required, value of the product property -->
        <product.property.value><![CDATA[50.00]]></product.property.value>

      </propertyitem>
      <!-- more property items -->

    </property>
  </productitem>
</products>
```

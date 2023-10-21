Most of the time, you already have an ERP system which manages all your products and most of the information required to fill your shop are stored there. In this case, most often you want to bulk import the (product) attribute information from the ERP system into your shop and update it regularly. You can use the attribute import job controller for XML files to import/update the attributes.

!!! note
    The attribute import is triggered via a cronjob/scheduler that executes the "attribute/import/xml" job controller.

# Available configuration

[controller/jobs/attribute/import/xml/backup](../config/controller-jobs/attribute-import.md#backup)
: Directory for storing imported files

[controller/jobs/attribute/import/xml/domains](../config/controller-jobs/attribute-import.md#domains)
: List of domain names that should be retrieved along with the attribute items

[controller/jobs/attribute/import/xml/location](../config/controller-jobs/attribute-import.md#location)
: Path to the directory with the XML files

[controller/jobs/attribute/import/xml/max-query](../config/controller-jobs/attribute-import.md#max-query)
: Maximum number of XML nodes processed at once

# Structure

```xml
<?xml version="1.0" encoding="UTF-8" standalone="no" ?>

<attributes>
  <!-- List of attribute items with concatenation of attribute domain, type and value as "ref" key -->
  <attributeitem ref="product|color|black">

    <!-- Required, domain the attribute belongs to -->
    <attribute.domain><![CDATA[product]]></attribute.domain>

    <!-- Required, any available attribute type in the database -->
    <attribute.type><![CDATA[color]]></attribute.type>

    <!-- Required, code of the attribute, unique within the same type -->
    <attribute.code><![CDATA[black]]></attribute.code>

    <!-- Required, label of the attribute, used if no language specific name is avialable -->
    <attribute.label><![CDATA[Black]]></attribute.label>

    <!-- Optional, possible values: 1 = enabled (default), 0 = disabled, -1 = review, -2 =archived -->
    <attribute.status><![CDATA[1]]></attribute.status>

    <!-- Optional, position of the attribute if multiple items are available for the the same type -->
    <attribute.position><![CDATA[0]]></attribute.position>

    <!-- Optional, items associated to the attribute -->
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

          <!-- Required, possible values: "name", "short", "long", "url" (attribute name in URL) -->
          <text.type><![CDATA[name]]></text.type>

          <!-- Required, two letter ISO language code -->
          <text.languageid><![CDATA[en]]></text.languageid>

          <!-- Required, arbitrary text content in the language of the ISO code -->
          <text.content><![CDATA[attribute name in English]]></text.content>

          <!-- Optional, label of the text for editors not speaking the language of the content -->
          <text.label><![CDATA[English attribute name]]></text.label>

          <!-- Optional, possible values: 1 = enabled (default), 0 = disabled, -1 = review, -2 =archived -->
          <text.status><![CDATA[1]]></text.status>

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

          <!-- Required, possible values: "default" (default), "icon" or any other available media type -->
          <media.type><![CDATA[default]]></media.type>

          <!-- Required, two letter ISO language code or empty for not language specific media files -->
          <media.languageid><![CDATA[]]></media.languageid>

          <!-- Required, absolute or relative URL to the media file on the server -->
          <media.url><![CDATA[path/to/file.png]]></media.url>

          <!-- Optional, absolute or relative URL to the preview file on the server -->
          <media.preview><![CDATA[path/to/preview.png]]></media.preview>

          <!-- Optional, mime type of the file referenced by the URL -->
          <media.mimetype><![CDATA[image/png]]></media.mimetype>

          <!-- Optional, label for the media file, will be used as title if no language specific title is available -->
          <media.label><![CDATA[test image]]></media.label>

          <!-- Optional, possible values: 1 = enabled (default), 0 = disabled, -1 = review, -2 =archived -->
          <media.status><![CDATA[1]]></media.status>

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
          lists.position="0" lists.status="1"
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

          <!-- Optional, shipping cost value per attribute in "0.00" format -->
          <price.costs><![CDATA[5.00]]></price.costs>

          <!-- Optional, difference to the previous attribute price in "0.00" format -->
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

    <!-- Optional, list of attribute property items -->
    <property>

      <!-- Optional, arbitrary attribute properties -->
      <propertyitem>

        <!-- Required, any available attribute property type like "package-height", "package-length", "package-width", "package-weight" -->
        <attribute.property.type><![CDATA[package-weight]]></attribute.property.type>

        <!-- Required, two letter ISO language code or empty for no language -->
        <attribute.property.languageid><![CDATA[]]></attribute.property.languageid>

        <!-- Required, value of the attribute property -->
        <attribute.property.value><![CDATA[50.00]]></attribute.property.value>

      </propertyitem>
      <!-- more property items -->

    </property>
  </attributeitem>
</attributes>
```

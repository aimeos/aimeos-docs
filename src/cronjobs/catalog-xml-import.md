Most of the time, you already have an ERP system which manages all your products and most of the information required to fill your shop are stored there. In this case, most often you want to bulk import the categories information from the ERP system into your shop and update it regularly. You can use the category import job controller for XML files to import/update the categories.

!!! note
  The category import is triggered via a cronjob/scheduler that executes the "catalog/import/xml" job controller.

# Available configuration

[controller/jobs/catalog/import/xml/backup](../config/controller-jobs/catalog-import.md#backup)
: Directory for storing imported files

[controller/jobs/catalog/import/xml/domains](../config/controller-jobs/catalog-import.md#domains)
: List of domain names that should be retrieved along with the catalog items

[controller/jobs/catalog/import/xml/location](../config/controller-jobs/catalog-import.md#location)
: Path to the directory with the XML files

# Structure

```xml
<?xml version="1.0" encoding="UTF-8" standalone="no" ?>

<catalog>
  <!-- Root catalog item with unique code as "ref" key -->
  <catalogitem ref="home">

    <!-- Required, unique code to identify the category -->
    <catalog.code><![home]]></catalog.code>

    <!-- Required, label of the category, used if no language specific name is avialable -->
    <catalog.label><![CDATA[Home]]></catalog.label>

    <!-- Optional, possible values: 1 = enabled (default), 0 = disabled, -1 = review, -2 =archived -->
    <catalog.status><![CDATA[1]]></catalog.status>

    <!-- Optional, JSON encoded (multi-dimensional) key/value pairs with arbitrary settings -->
    <catalog.config><![CDATA[{"key": "value"}]]></catalog.config>

    <!-- Optional, items associated to the catalog -->
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

          <!-- Required, possible values: "name", "short", "long", "meta-keyword", "meta-description", "url" (catalog name in URL) -->
          <text.type><![CDATA[name]]></text.type>

          <!-- Required, two letter ISO language code -->
          <text.languageid><![CDATA[en]]></text.languageid>

          <!-- Required, arbitrary text content in the language of the ISO code -->
          <text.content><![CDATA[catalog name in English]]></text.content>

          <!-- Optional, label of the text for editors not speaking the language of the content -->
          <text.label><![CDATA[English catalog name]]></text.label>

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
            <customergroup>

              <!-- ref: Required, unique code of the customer group -->
              <!-- lists.type: Optional, possible values: "default" (default) or any other available list type -->
              <!-- lists.config: Optional, JSON encoded (multi-dimensional) key/value pairs with arbitrary settings -->
              <!-- lists.position: Optional, position of the text if multiple items are available for the the same text type and list type -->
              <!-- lists.status: Optional, possible values: 1 = enabled (default), 0 = disabled, -1 = review, -2 =archived -->
              <!-- lists.datestart: Optional, start ISO date/time value (YYYY-MM-DDTHH:mm:ss) the text is available from -->
              <!-- lists.dateend: Optional, end ISO date/time value (YYYY-MM-DDTHH:mm:ss) the text is available to -->
              <customergroupitem ref="groupcode"
                lists.type="default"
                lists.config="{&quot;key&quot;: &quot;value&quot;}"
                lists.position="0"
                lists.status="1"
                lists.datestart="2000-01-01T00:00:00"
                lists.dateend="2000-01-01T23:59:59" />

            </customergroup>
            <!-- more customer/group items -->

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
            <customergroup>

              <!-- ref: Required, unique code of the customer group -->
              <!-- lists.type: Optional, possible values: "default" (default) or any other available list type -->
              <!-- lists.config: Optional, JSON encoded (multi-dimensional) key/value pairs with arbitrary settings -->
              <!-- lists.position: Optional, position of the text if multiple items are available for the the same text type and list type -->
              <!-- lists.status: Optional, possible values: 1 = enabled (default), 0 = disabled, -1 = review, -2 =archived -->
              <!-- lists.datestart: Optional, start ISO date/time value (YYYY-MM-DDTHH:mm:ss) the text is available from -->
              <!-- lists.dateend: Optional, end ISO date/time value (YYYY-MM-DDTHH:mm:ss) the text is available to -->
              <customergroupitem ref="groupcode"
                lists.type="default"
                lists.config="{&quot;key&quot;: &quot;value&quot;}"
                lists.position="0"
                lists.status="1"
                lists.datestart="2000-01-01T00:00:00"
                lists.dateend="2000-01-01T23:59:59" />

            </customergroup>
            <!-- more customer/group items -->

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

      <!-- Optional, list of product items -->
      <product>

        <!-- ref: Required, unique product code (SKU) -->
        <!-- lists.type: Optional, possible values: "default" (for articles of bundles and selections), "suggestion" (recommended products) and "bought-together" -->
        <!-- lists.config: Optional, JSON encoded (multi-dimensional) key/value pairs with arbitrary settings -->
        <!-- lists.position: Optional, position of the text if multiple items are available for the the same text type and list type -->
        <!-- lists.status: Optional, possible values: 1 = enabled (default), 0 = disabled, -1 = review, -2 =archived -->
        <!-- lists.datestart: Optional, start ISO date/time value (YYYY-MM-DDTHH:mm:ss) the text is available from -->
        <!-- lists.dateend: Optional, end ISO date/time value (YYYY-MM-DDTHH:mm:ss) the text is available to -->
        <productitem ref="TEST-PRODUCT"
          lists.type="default"
          lists.config="{&quot;key&quot;: &quot;value&quot;}"
          lists.position="0"
          lists.status="1"
          lists.datestart="2000-01-01T00:00:00"
          lists.dateend="2000-01-01T23:59:59" />
        <!-- more product items -->

      </product>

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
      <customergroup>

        <!-- ref: Required, unique code of the customer group -->
        <!-- lists.type: Optional, possible values: "default" (default) or any other available list type -->
        <!-- lists.config: Optional, JSON encoded (multi-dimensional) key/value pairs with arbitrary settings -->
        <!-- lists.position: Optional, position of the text if multiple items are available for the the same text type and list type -->
        <!-- lists.status: Optional, possible values: 1 = enabled (default), 0 = disabled, -1 = review, -2 =archived -->
        <!-- lists.datestart: Optional, start ISO date/time value (YYYY-MM-DDTHH:mm:ss) the text is available from -->
        <!-- lists.dateend: Optional, end ISO date/time value (YYYY-MM-DDTHH:mm:ss) the text is available to -->
        <customergroupitem ref="groupcode"
          lists.type="default"
          lists.config="{&quot;key&quot;: &quot;value&quot;}"
          lists.position="0"
          lists.status="1"
          lists.datestart="2000-01-01T00:00:00"
          lists.dateend="2000-01-01T23:59:59" />

      </customergroup>
      <!-- more customer/group items -->

    </lists>
  </catalogitem>

  <!-- Optional, list of catalog items -->
  <catalog>

    <catalogitem>

      <!-- Required, unique code to identify the category -->
      <catalog.code><![CDATA[TEST-SUBCATEGORY]]></catalog.code>

      <!-- Required, label of the category, used if no language specific name is avialable -->
      <catalog.label><![CDATA[Test sub-category]]></catalog.label>

      <!-- Optional, possible values: 1 = enabled (default), 0 = disabled, -1 = review, -2 =archived -->
      <catalog.status><![CDATA[1]]></catalog.status>

      <!-- Optional, JSON encoded (multi-dimensional) key/value pairs with arbitrary settings -->
      <catalog.config><![CDATA[{"key": "value"}]]></catalog.config>

      <!-- Optional, items associated to the catalog -->
      <lists>
        <!-- Anything that's also allowed in the lists tag of the main category -->
      </lists>

    </catalogitem>

    <!-- Optional, list of sub-category items for the previous catalogitem -->
    <catalog>
      <catalogitem>
        <catalog.code><![CDATA[TEST-SUBSUBCATEGORY-2]]></catalog.code>
        <catalog.label><![CDATA[Test 2nd level sub-category]]></catalog.label>
        <lists>
          <!-- Anything that's also allowed in the lists tag of the main category -->
        </lists>
      </catalogitem>
      <catalog>
        <!-- more catalogitem / catalog node pairs -->
      </catalog>
    </catalog>

    <catalogitem>
      <catalog.code><![CDATA[TEST-SUBCATEGORY-2]]></catalog.code>
      <catalog.label><![CDATA[Test sub-category 2]]></catalog.label>
      <lists>
        <!-- Anything that's also allowed in the lists tag of the main category -->
      </lists>
    </catalogitem>
    <catalog>
        <!-- more catalogitem / catalog node pairs -->
    </catalog>

    <!-- more catalogitem / catalog node pairs -->

  </catalog>
</catalog>
```

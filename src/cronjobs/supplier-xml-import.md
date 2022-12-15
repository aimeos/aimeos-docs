Most of the time, you already have an ERP system which manages all your suppliers and most of the information required to fill your shop are stored there. In this case, most often you want to bulk import the supplier information from the ERP system into your shop and update it regularly. You can use the supplier import job controller for XML files to import/update the suppliers.

!!! note
    The supplier import is triggered via a cronjob/scheduler that executes the "supplier/import/xml" job controller.

# Available configuration

[controller/jobs/supplier/import/xml/backup](../config/controller-jobs/supplier-import.md#backup)
: Directory for storing imported files

[controller/jobs/supplier/import/xml/domains](../config/controller-jobs/supplier-import.md#domains)
: List of domain names that should be retrieved along with the supplier items

[controller/jobs/supplier/import/xml/location](../config/controller-jobs/supplier-import.md#location)
: Path to the directory with the XML files

[controller/jobs/supplier/import/xml/max-query](../config/controller-jobs/supplier-import.md#max-query)
: Maximum number of XML nodes processed at once

# Structure

```xml
<?xml version="1.0" encoding="UTF-8" standalone="no" ?>

<suppliers>
  <!-- List of supplier items with unique code as value for "ref" -->
  <supplieritem ref="TEST-SUPPLIER">

    <!-- Required, unique SKU of the supplier -->
    <supplier.code><![CDATA[TEST-SUPPLIER]]></supplier.code>

    <!-- Required, label of the supplier, used if no language specific name is avialable -->
    <supplier.label><![CDATA[Test supplier]]></supplier.label>

    <!-- Optional, possible values: 1 = enabled (default), 0 = disabled, -1 = review, -2 =archived -->
    <supplier.status><![CDATA[1]]></supplier.status>

    <!-- Optional, delivery addresses associated to the supplier -->
    <address>
      <addressitem>

        <!-- Optional, company name if salutation is "company" -->
        <supplier.address.company><![CDATA[Example company]]></supplier.address.company>

        <!-- Optional, VAT ID if available for the company -->
        <supplier.address.vatid><![CDATA[DE12345678]]></supplier.address.vatid>

        <!-- Optional, supplier salutation, e.g. "" (unknown), "company", (Company), "mr" (Mister), "ms" (Misses) -->
        <supplier.address.salutation><![CDATA[mr]]></supplier.address.salutation>

        <!-- Optional, academic title of the person -->
        <supplier.address.title><![CDATA[Dr]]></supplier.address.title>

        <!-- Optional, first name of the person if used -->
        <supplier.address.firstname><![CDATA[Test]]></supplier.address.firstname>

        <!-- Optional, (last) name of the person -->
        <supplier.address.lastname><![CDATA[User]]></supplier.address.lastname>

        <!-- Optional, first address part, e.g. street -->
        <supplier.address.address1><![CDATA[Test street]]></supplier.address.address1>

        <!-- Optional, second address part, e.g. house number -->
        <supplier.address.address2><![CDATA[1]]></supplier.address.address2>

        <!-- Optional, third address part, e.g. flat number -->
        <supplier.address.address3><![CDATA[2. floor]]></supplier.address.address3>

        <!-- Optional, zip code the company/person is located -->
        <supplier.address.postal><![CDATA[10000]]></supplier.address.postal>

        <!-- Optional, city name the company/person is located -->
        <supplier.address.city><![CDATA[New York]]></supplier.address.city>

        <!-- Optional, state the company/person is located if available -->
        <supplier.address.state><![CDATA[NY]]></supplier.address.state>

        <!-- Optional, ISO language code the person is using, e.g. "en" or "en_US" -->
        <supplier.address.languageid><![CDATA[en]]></supplier.address.languageid>

        <!-- Optional, two letter ISO country code the company/person is located -->
        <supplier.address.countryid><![CDATA[US]]></supplier.address.countryid>

        <!-- Optional, telephone number with or without country prefix -->
        <supplier.address.telephone><![CDATA[+112309876]]></supplier.address.telephone>

        <!-- Optional, facsimile number with or without country prefix -->
        <supplier.address.telefax><![CDATA[+155598765]]></supplier.address.telefax>

        <!-- Optional, e-mail address of the person or company -->
        <supplier.address.email><![CDATA[me@example.com]]></supplier.address.email>

        <!-- Optional, web site of the person or company incl. protocol -->
        <supplier.address.website><![CDATA[https://www.example.com/]]></supplier.address.website>

        <!-- Optional, decimal longitude value of the address -->
        <supplier.address.longitude><![CDATA[10.0000]]></supplier.address.longitude>

        <!-- Optional, decimal latitude value of the address -->
        <supplier.address.latitude><![CDATA[50.0000]]></supplier.address.latitude>

      </addressitem>
      <!-- more address items -->
    </address>

    <!-- Optional, items associated to the supplier -->
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

          <!-- Required, possible values: "name", "short", "long", "meta-keyword", "meta-description", "basket" (supplier name/text in basket), "url" (supplier name in URL) -->
          <text.type><![CDATA[name]]></text.type>

          <!-- Required, two letter ISO language code -->
          <text.languageid><![CDATA[en]]></text.languageid>

          <!-- Required, arbitrary text content in the language of the ISO code -->
          <text.content><![CDATA[supplier name in English]]></text.content>

          <!-- Optional, label of the text for editors not speaking the language of the content -->
          <text.label><![CDATA[English supplier name]]></text.label>

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

      <!-- Optional, list of attribute items -->
      <attribute>

        <!-- ref: Required, unique code of attribute type and code separated by a slash -->
        <!-- lists.type: Optional, possible values: "default" (default), "variant" (variant building supplier attribute), "config" (configurable supplier attribute), "custom" (custom can enter value), "hidden" (not shown to customer but added in order) -->
        <!-- lists.config: Optional, JSON encoded (multi-dimensional) key/value pairs with arbitrary settings -->
        <!-- lists.position: Optional, position of the text if multiple items are available for the the same text type and list type -->
        <!-- lists.status: Optional, possible values: 1 = enabled (default), 0 = disabled, -1 = review, -2 =archived -->
        <!-- lists.datestart: Optional, start ISO date/time value (YYYY-MM-DDTHH:mm:ss) the text is available from -->
        <!-- lists.dateend: Optional, end ISO date/time value (YYYY-MM-DDTHH:mm:ss) the text is available to -->
        <attributeitem ref="supplier|country|de"
          lists.type="default"
          lists.config="{&quot;key&quot;: &quot;value&quot;}"
          lists.position="0"
          lists.status="1"
          lists.datestart="2000-01-01T00:00:00"
          lists.dateend="2000-01-01T23:59:59" />
        <!-- more attribute items -->

      </attribute>

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
  </supplieritem>
</suppliers>
```

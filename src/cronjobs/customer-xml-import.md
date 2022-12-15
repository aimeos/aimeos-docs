Most of the time, you already have an CRM system which manages all your customers and most of the information required to create user accounts in your shop are stored there. In this case, most often you want to bulk import the customer information from the CRM system into your shop and update it regularly. You can use the customer import job controller for XML files to import/update the customers.

!!! note
    The customer import is triggered via a cronjob/scheduler that executes the "customer/import/xml" job controller.

# Available configuration

[controller/jobs/customer/import/xml/backup](../config/controller-jobs/customer-import.md#backup)
: Directory for storing imported files

[controller/jobs/customer/import/xml/domains](../config/controller-jobs/customer-import.md#domains)
: List of domain names that should be retrieved along with the customer items

[controller/jobs/customer/import/xml/location](../config/controller-jobs/customer-import.md#location)
: Path to the directory with the XML files

[controller/jobs/customer/import/xml/max-query](../config/controller-jobs/customer-import.md#max-query)
: Maximum number of XML nodes processed at once

# Structure

```xml
<?xml version="1.0" encoding="UTF-8" standalone="no" ?>

<customers>
  <!-- List of customer items with unique customer e-mail as "ref" key -->
  <customeritem ref="me@example.com">

    <!-- Required, unique login of the customer -->
    <customer.code><![CDATA[me@example.com]]></customer.code>

    <!-- Required, label of the customer -->
    <customer.label><![CDATA[Test user]]></customer.label>

    <!-- Optional, possible values: 1 = enabled (default), 0 = disabled, -1 = review, -2 =archived -->
    <customer.status><![CDATA[1]]></customer.status>

    <!-- Optional, company name if salutation is "company" -->
    <customer.company><![CDATA[Example company]]></customer.company>

    <!-- Optional, VAT ID if available for the company -->
    <customer.vatid><![CDATA[DE12345678]]></customer.vatid>

    <!-- Optional, customer salutation, e.g. "" (unknown), "company", (Company), "mr" (Mister), "mrs" (Misses), "miss" (Miss) -->
    <customer.salutation><![CDATA[mr]]></customer.salutation>

    <!-- Optional, academic title of the person -->
    <customer.title><![CDATA[Dr]]></customer.title>

    <!-- Optional, first name of the person if used -->
    <customer.firstname><![CDATA[Test]]></customer.firstname>

    <!-- Optional, (last) name of the person -->
    <customer.lastname><![CDATA[User]]></customer.lastname>

    <!-- Optional, first address part, e.g. street -->
    <customer.address1><![CDATA[Test street]]></customer.address1>

    <!-- Optional, second address part, e.g. house number -->
    <customer.address2><![CDATA[1]]></customer.address2>

    <!-- Optional, third address part, e.g. flat number -->
    <customer.address3><![CDATA[2. floor]]></customer.address3>

    <!-- Optional, zip code the company/person is located -->
    <customer.postal><![CDATA[10000]]></customer.postal>

    <!-- Optional, city name the company/person is located -->
    <customer.city><![CDATA[New York]]></customer.city>

    <!-- Optional, state the company/person is located if available -->
    <customer.state><![CDATA[NY]]></customer.state>

    <!-- Optional, ISO language code the person is using, e.g. "en" or "en_US" -->
    <customer.languageid><![CDATA[en]]></customer.languageid>

    <!-- Optional, two letter ISO country code the company/person is located -->
    <customer.countryid><![CDATA[US]]></customer.countryid>

    <!-- Optional, telephone number with or without country prefix -->
    <customer.telephone><![CDATA[+112309876]]></customer.telephone>

    <!-- Optional, facsimile number with or without country prefix -->
    <customer.telefax><![CDATA[+155598765]]></customer.telefax>

    <!-- Optional, e-mail address of the person or company -->
    <customer.email><![CDATA[me@example.com]]></customer.email>

    <!-- Optional, web site of the person or company incl. protocol -->
    <customer.website><![CDATA[https://www.example.com/]]></customer.website>

    <!-- Optional, decimal longitude value of the address -->
    <customer.longitude><![CDATA[10.0000]]></customer.longitude>

    <!-- Optional, decimal latitude value of the address -->
    <customer.latitude><![CDATA[50.0000]]></customer.latitude>

    <!-- Optional, password of the user, will be stored hashed using the algorithm of the host application -->
    <customer.password><![CDATA[testpwd]]></customer.password>

    <!-- Optional, birthday of the person in ISO format, i.e. YYYY-MM-DD -->
    <customer.birthday><![CDATA[1980-01-01]]></customer.birthday>

    <!-- Optional, verification date of the account in ISO format, i.e. YYYY-MM-DD -->
    <customer.vdate><![CDATA[2000-01-01]]></customer.vdate>

    <!-- Optional, delivery addresses associated to the customer -->
    <address>
      <addressitem>

        <!-- Optional, company name if salutation is "company" -->
        <customer.address.company><![CDATA[Example company]]></customer.address.company>

        <!-- Optional, VAT ID if available for the company -->
        <customer.address.vatid><![CDATA[DE12345678]]></customer.address.vatid>

        <!-- Optional, customer salutation, e.g. "" (unknown), "company", (Company), "mr" (Mister), "ms" (Misses) -->
        <customer.address.salutation><![CDATA[mr]]></customer.address.salutation>

        <!-- Optional, academic title of the person -->
        <customer.address.title><![CDATA[Dr]]></customer.address.title>

        <!-- Optional, first name of the person if used -->
        <customer.address.firstname><![CDATA[Test]]></customer.address.firstname>

        <!-- Optional, (last) name of the person -->
        <customer.address.lastname><![CDATA[User]]></customer.address.lastname>

        <!-- Optional, first address part, e.g. street -->
        <customer.address.address1><![CDATA[Test street]]></customer.address.address1>

        <!-- Optional, second address part, e.g. house number -->
        <customer.address.address2><![CDATA[1]]></customer.address.address2>

        <!-- Optional, third address part, e.g. flat number -->
        <customer.address.address3><![CDATA[2. floor]]></customer.address.address3>

        <!-- Optional, zip code the company/person is located -->
        <customer.address.postal><![CDATA[10000]]></customer.address.postal>

        <!-- Optional, city name the company/person is located -->
        <customer.address.city><![CDATA[New York]]></customer.address.city>

        <!-- Optional, state the company/person is located if available -->
        <customer.address.state><![CDATA[NY]]></customer.address.state>

        <!-- Optional, ISO language code the person is using, e.g. "en" or "en_US" -->
        <customer.address.languageid><![CDATA[en]]></customer.address.languageid>

        <!-- Optional, two letter ISO country code the company/person is located -->
        <customer.address.countryid><![CDATA[US]]></customer.address.countryid>

        <!-- Optional, telephone number with or without country prefix -->
        <customer.address.telephone><![CDATA[+112309876]]></customer.address.telephone>

        <!-- Optional, facsimile number with or without country prefix -->
        <customer.address.telefax><![CDATA[+155598765]]></customer.address.telefax>

        <!-- Optional, e-mail address of the person or company -->
        <customer.address.email><![CDATA[me@example.com]]></customer.address.email>

        <!-- Optional, web site of the person or company incl. protocol -->
        <customer.address.website><![CDATA[https://www.example.com/]]></customer.address.website>

        <!-- Optional, decimal longitude value of the address -->
        <customer.address.longitude><![CDATA[10.0000]]></customer.address.longitude>

        <!-- Optional, decimal latitude value of the address -->
        <customer.address.latitude><![CDATA[50.0000]]></customer.address.latitude>

      </addressitem>
      <!-- more address items -->
    </address>

    <!-- Optional, items associated to the customer -->
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

          <!-- Required, possible values: "name", "short", "long", "meta-keyword", "meta-description", "basket" (customer name/text in basket), "url" (customer name in URL) -->
          <text.type><![CDATA[name]]></text.type>

          <!-- Required, two letter ISO language code -->
          <text.languageid><![CDATA[en]]></text.languageid>

          <!-- Required, arbitrary text content in the language of the ISO code -->
          <text.content><![CDATA[customer name in English]]></text.content>

          <!-- Optional, label of the text for editors not speaking the language of the content -->
          <text.label><![CDATA[English customer name]]></text.label>

          <!-- Optional, possible values: 1 = enabled (default), 0 = disabled, -1 = review, -2 =archived -->
          <text.status><![CDATA[1]]></text.status>

          <!-- Optional, items associated to the text -->
          <lists>
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

          <!-- Optional, shipping cost value per customer in "0.00" format -->
          <price.costs><![CDATA[5.00]]></price.costs>

          <!-- Optional, difference to the previous customer price in "0.00" format -->
          <price.rebate><![CDATA[20.00]]></price.rebate>

          <!-- Optional, label for the price for editors -->
          <price.label><![CDATA[Reduced price]]></price.label>

          <!-- Optional, possible values: 1 = enabled (default), 0 = disabled, -1 = review, -2 =archived -->
          <price.status><![CDATA[1]]></price.status>

          <!-- Optional, items associated to the price -->
          <lists>
          </lists>
        </priceitem>
        <!-- more price items -->

      </price>

      <!-- Optional, list of attribute items -->
      <attribute>

        <!-- ref: Required, unique code of attribute type and code separated by a slash -->
        <!-- lists.type: Optional, possible values: "default" (default), "variant" (variant building customer attribute), "config" (configurable customer attribute), "custom" (custom can enter value), "hidden" (not shown to customer but added in order) -->
        <!-- lists.config: Optional, JSON encoded (multi-dimensional) key/value pairs with arbitrary settings -->
        <!-- lists.position: Optional, position of the text if multiple items are available for the the same text type and list type -->
        <!-- lists.status: Optional, possible values: 1 = enabled (default), 0 = disabled, -1 = review, -2 =archived -->
        <!-- lists.datestart: Optional, start ISO date/time value (YYYY-MM-DDTHH:mm:ss) the text is available from -->
        <!-- lists.dateend: Optional, end ISO date/time value (YYYY-MM-DDTHH:mm:ss) the text is available to -->
        <attributeitem ref="service|payment|token"
          lists.type="default"
          lists.config="{&quot;key&quot;: &quot;value&quot;}"
          lists.position="0"
          lists.status="1"
          lists.datestart="2000-01-01T00:00:00"
          lists.dateend="2000-01-01T23:59:59" />
        <!-- more attribute items -->

      </attribute>

      <!-- Optional, list of product items -->
      <product>

        <!-- ref: Required, unique product code (SKU) -->
        <!-- lists.type: Optional, possible values: "default", "favorite" and "watch" -->
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

    </lists>

    <!-- Optional, list of customer property items -->
    <property>

      <!-- Optional, arbitrary customer properties -->
      <propertyitem>

        <!-- Required, any available customer property type -->
        <customer.property.type><![CDATA[myprop]]></customer.property.type>

        <!-- Required, two letter ISO language code or empty for no language -->
        <customer.property.languageid><![CDATA[]]></customer.property.languageid>

        <!-- Required, value of the customer property -->
        <customer.property.value><![CDATA[abcd]]></customer.property.value>

      </propertyitem>
      <!-- more property items -->

    </property>

    <!-- Optional, list of customer groups -->
    <group>

      <!-- Optional, list of customer group references by customer group code -->
      <groupitem ref="groupcode-1" />
      <groupitem ref="groupcode-2" />

    </group>
  </customeritem>
</customers>
```

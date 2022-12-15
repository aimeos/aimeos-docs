Most of the time, you already have an CRM system which manages all your customers and most of the information required to create groups in your shop are stored there. In this case, most often you want to bulk import the customer group information from the CRM system into your shop and update it regularly. You can use the customer group import job controller for XML files to import/update the customer groups.

!!! note
    The customer group import is triggered via a cronjob/scheduler that executes the "customer/group/import/xml" job controller.

# Available configuration

[controller/jobs/customer/group/import/xml/backup](../config/controller-jobs/customer-group.md#xmlbackup)
: Directory for storing imported files

[controller/jobs/customer/group/import/xml/location](../config/controller-jobs/customer-group.md#xmllocation)
: Path to the directory with the XML files

[controller/jobs/customer/group/import/xml/max-query](../config/controller-jobs/customer-group.md#xmlmax-query)
: Maximum number of XML nodes processed at once

# Structure

```xml
<?xml version="1.0" encoding="UTF-8" standalone="no" ?>

<customergroups>
    <!-- List of customer groups items with unique code as "ref" value -->
	<customergroupitem ref="testgroup">

		<!-- Required, unique code of the group -->
		<customer.group.code><![CDATA[testgroup]]></customer.group.code>

		<!-- Required, label of the customer group -->
		<customer.group.label><![CDATA[Test group]]></customer.group.label>

	</customergroupitem>
</customergroups>
```

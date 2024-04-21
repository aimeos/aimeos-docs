Most of the time, you already have an CRM system which manages all your customers and most of the information required to create groups in your shop are stored there. In this case, most often you want to bulk import the customer group information from the CRM system into your shop and update it regularly. You can use the customer group import job controller for XML files to import/update the customer groups.

!!! note
    The customer group import is triggered via a cronjob/scheduler that executes the "group/import/xml" job controller.

# Available configuration

[controller/jobs/group/import/xml/backup](../config/controller-jobs/group-import.md#xmlbackup)
: Directory for storing imported files

[controller/jobs/group/import/xml/location](../config/controller-jobs/group-import.md#xmllocation)
: Path to the directory with the XML files. By default, the location is "group" with the site code added automatically at the end, i.e. the expected sub-directory for the files is "group/default/" which imports the XML files for the "default" site

[controller/jobs/group/import/xml/max-query](../config/controller-jobs/group-import.md#xmlmax-query)
: Maximum number of XML nodes processed at once

# Structure

```xml
<?xml version="1.0" encoding="UTF-8" standalone="no" ?>

<groups>
    <!-- List of customer groups items with unique code as "ref" value -->
	<groupitem ref="testgroup">

		<!-- Required, unique code of the group -->
		<group.code><![CDATA[testgroup]]></group.code>

		<!-- Required, label of the customer group -->
		<group.label><![CDATA[Test group]]></group.label>

	</groupitem>
</groups>
```

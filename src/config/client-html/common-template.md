
# baseurl

Absolute path to the themes folder for styling the e-mails

```
client/html/common/template/baseurl = client/html/themes/elegance
```

* Default: client/html/themes/elegance
* Type: string - Absolute path of the theme folder
* Since: 2017.10

The Aimeos e-mails are styled depending on the "email.css" file located
in the configured themes folder. The path to the themes folder must be
absolute to the file system root to avoid problems finding the file
when the e-mails are sent by the cronjob.

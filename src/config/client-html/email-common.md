
# summary
## address/text

Location of the address partial template for the text e-mails

```
client/html/email/common/summary/address/text = common/summary/address-standard
```

* Default: common/summary/address-standard
* Type: string - Relative path to the address partial
* Since: 2017.01

To configure an alternative template for the address partial, you
have to configure its path relative to the template directory
(usually client/html/templates/). It's then used to display the
payment or delivery address block in the text e-mails.

See also:

* client/html/email/common/summary/detail/text
* client/html/email/common/summary/service/text

## pdf

Location of the address partial template for the text e-mails

```
client/html/email/common/summary/pdf = email/common/pdf-summary-partial
```

* Default: email/common/pdf-summary-partial
* Type: string - Relative path to the address partial
* Since: 2020.07

To configure an alternative template for the address partial, you
have to configure its path relative to the template directory
(usually client/html/templates/). It's then used to display the
payment or delivery address block in the text e-mails.


## text

Template partial used for redering the order summary details for text e-mails

```
client/html/email/common/summary/text = email/common/text-summary-partial
```

* Default: email/common/text-summary-partial
* Type: string - Relative path to the partial file without file extension
* Since: 2019.10

The setting must be the path to the partial relative to the template directory
in your own extension and must include the file name without the file extension.

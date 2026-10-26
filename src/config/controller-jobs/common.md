
# from-email

Sender e-mail address used when sending job e-mails

```
controller/jobs/from-email = root@localhost
```

* Default: `root@localhost`
* Type: string - E-mail address
* Since: 2020.04

Job controllers can send e-mails when they has finished of if an
error occurred. This setting will be used as the sender e-mail
address in these e-mails.

See also:

* controller/jobs/to-email

# to-email

Recipient e-mail address used when sending job e-mails

```
controller/jobs/to-email = root@localhost
```

* Default: `root@localhost`
* Type: string - E-mail address
* Since: 2020.04

Job controllers can send e-mails when they has finished of if an
error occurred. This setting will be used as the recipient e-mail
address for these e-mails.

See also:

* controller/jobs/from-email
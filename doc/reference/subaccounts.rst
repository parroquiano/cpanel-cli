..
   Do not edit this .rst file directly — it’s generated programmatically.
   See doc/reference.sh.

==================================================
Module: ``subaccounts``
==================================================

`Leer en español </es/latest/reference/subaccounts.html>`_

- **list subaccounts**
- **create subaccount USER\@DOMAIN PASSWORD**
- **delete subaccount USER\@DOMAIN**
- **get subaccount GUID**
- **get service account USERNAME TYPE**
- **check subaccount conflicts USERNAME**

**COMMANDS**


**list subaccounts**

List the sub-accounts of the main cPanel account, along with detailed information
of each sub-account.

*Example*

.. code:: sh

    $ cpanel list subaccounts

See a sample of the JSON result data at:
https://api.docs.cpanel.net/specifications/cpanel.openapi/subaccount-management/usermanager-list_users

**create subaccount USER\@DOMAIN PASSWORD**

Create a subaccount identified by USER\@DOMAIN, using PASSWORD for authentication.
This command creates only the base subaccount; email, FTP and Web Disk access
remain disabled according to the cPanel API defaults.

*Example*

.. code:: sh

    $ cpanel create subaccount user@example.com A-Strong-Password

See a sample of the JSON result data at:
https://api.docs.cpanel.net/specifications/cpanel.openapi/subaccount-management/usermanager-create_user

**delete subaccount USER\@DOMAIN**

Delete a subaccount identified by USER\@DOMAIN. This does not delete separate
email, FTP or Web Disk service accounts that use the same username and domain.
The aliases ‘rm subaccount’ and ‘remove subaccount’ are also supported.

*Example*

.. code:: sh

    $ cpanel delete subaccount user@example.com

See a sample of the JSON result data at:
https://api.docs.cpanel.net/specifications/cpanel.openapi/subaccount-management/usermanager-delete_user

**get subaccount GUID**

Show detailed information of a sub-account, identified by its GUID. To get
this GUID, use ‘cpanel list subaccounts’. Note that only sub-accounts with a
sub_account_exists flag set to 1 can be queried.

*Example*

.. code:: sh

    $ cpanel get subaccount EXAMPLE1:EXAMPLE.COM:564CD663:FE50072F2620B50988EA4E5F46022546FBE6BDDE3C36C2F2534F4967C661EC37

See a sample of the JSON result data at:
https://api.docs.cpanel.net/specifications/cpanel.openapi/subaccount-management/usermanager-lookup_user

**get service subaccount USERNAME TYPE**

Show detailed information of a service subaccount, identified by its USERNAME.
TYPE is the type of service subaccount, it's either ‘ftp’, ‘email’ or ‘webdisk’.

Use ‘cpanel list subaccounts’ to get a list of full subaccount usernames.

*Example*

.. code:: sh

    $ cpanel get service subaccount ftp@example.com ftp

See a sample of the JSON result data at:
https://api.docs.cpanel.net/specifications/cpanel.openapi/subaccount-management/usermanager-lookup_service_account

**check subaccount conflicts USERNAME**

Check if a subaccount identified by USERNAME conflicts with any other subaccount.
Look for a “conflict”:1 in the returned JSON data.

Use ‘cpanel list subaccounts’ to get a list of full subaccount usernames.

*Example*

.. code:: sh

    $ cpanel check subaccount conflicts ftp@example.com

See a sample of the JSON result data at:
https://api.docs.cpanel.net/specifications/cpanel.openapi/subaccount-management/usermanager-check_account_conflicts



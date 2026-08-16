..
   Do not edit this .rst file directly — it’s generated programmatically.
   See doc/reference.sh.

==================================================
Module: ``accounts``
==================================================

`Leer en español </es/latest/reference/accounts.html>`_

- **list accounts**
- **get account**
- **set account password OLDPASSWORD NEWPASSWORD**

**COMMANDS**


**list accounts**

List basic information of the main cPanel account.

*Example*

.. code:: sh

    $ cpanel list accounts

See a sample of the JSON result data at:
https://api.docs.cpanel.net/openapi/cpanel/operation/list_accounts/

**get account**

Show detailed information of the main account.

*Example*

.. code:: sh

    $ cpanel get account

See a sample of the JSON result data at:
https://api.docs.cpanel.net/openapi/cpanel/operation/Variables-get_user_information/

**set account password OLDPASSWORD NEWPASSWORD**

Change the authenticated cPanel account password from OLDPASSWORD to NEWPASSWORD.
This does not update the account's MySQL password. The alias
‘change account password’ is also supported.

*Example*

.. code:: sh

    $ cpanel set account password 'old-secret' 'new-secret'

See a sample of the JSON result data at:
https://api.docs.cpanel.net/specifications/cpanel.openapi/account-management/usermanager-change_password



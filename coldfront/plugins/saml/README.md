# SAML2 integration for coldfront

ColdFront django plugin for providing SAML2 authentication support to facilitate alternative login configurations in ColdFront.

## Design

This plugin uses [django-saml2-auth](https://github.com/fangli/django-saml2-auth), and allows the user to define a custom login link that will appear as a button on the ColdFront login page.

## Requirements

The following package is required:

```
pip install django-saml2-auth
```

## Usage

The following environment variables are configurable: 

> [!IMPORTANT] It should be assumed that any element with 'N/A' in the default column is required.

| Variable                 | Type | Default | Description |
| ------------------------ | ---- | ------- | ----------- |
| PLUGIN_AUTH_SAML         | bool | False   | Enables the plugin |
| SAML_LOGIN_URL           | str  | N/A     | Your SSO login link to IDP initiated saml, where users will be redirected when "login with SSO" is clicked |
| SAML_METADATA_AUTO       | str  | N/A     | Auto SAML2 metadata configuration URL |
| SAML_METADATA_LOCAL      | str  | ''      | Local SML2 metadata configuration |
| SAML_NEXT_URL            | str  | '/'     | Custom redirect after a user has logged in |
| SAML_CREATEUSER          | str  | 'TRUE'  | Enables SAML to create users in ColdFront. NOTE: This is a STRING with either TRUE or FALSE, not a typical bool. |
| SAML_NEWUSER_GROUPS      | list | []      | A list of groups a user will be assigned to upon creation. |
| SAML_NEWUSER_ACTIVE      | bool | True    | Sets the active status of a new user |
| SAML_NEWUSER_STAFF       | bool | False   | Sets the staff status of a new user |
| SAML_NEWUSER_SUPER       | bool | False   | Sets the superuser status of a new user |
| SAML_ATTR_EMAIL          | str  | N/A     | E-Mail SAML2 attribute from your configuration to be mapped into ColdFront |
| SAML_ATTR_USERNAME       | str  | N/A     | Username SAML2 attribute from your configuration to be mapped into ColdFront |
| SAML_ATTR_FNAME          | str  | N/A     | First name SAML2 attribute from your configuration to be mapped into ColdFront |
| SAML_ATTR_LNAME          | str  | N/A     | Last name SAML2 attribute from your configuration to be mapped into ColdFront |
| SAML_ENTITY_ID           | str  | N/A     | SAML2 SSO Identity Provider audience URI, ie http://your-domain/saml2_auth/acs/ |
### files edited:

- CREATE: coldfront/plugins/saml/README.md
- CREATE: coldfront/config/plugins/saml.py
- MODIFY: coldfront/config/settings.py
- MODIFY: coldfront/config/urls.py
- MODIFY: coldfront/core/user/templates/user/login.html

### TODO:

- Fix configurable login link, for now saml_login_link in login.html must be replaced by your login link
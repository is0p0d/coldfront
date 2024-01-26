# SAML2 integration for coldfront

ColdFront django plugin for providing SAML2 authentication support to facilitate alternative login configurations in ColdFront.

## Design

This plugin uses [django-saml2-auth](https://github.com/fangli/django-saml2-auth), allowing the user to configure the plugin to fit their SSO provider through the normal ColdFront environment file. This allows users to log in to coldfront through SAML2 SSO via a custom button on the login page.

Also in this plugin is a custom post-login trigger that will parse a user defined set of IDP groups and automatically assign PI in ColdFront if a user is in said defined groups.
## Requirements

The following package is required:

```
pip install django-saml2-auth
```

## Usage

The following environment variables are configurable: 

> [!IMPORTANT] 
> It should be assumed that any element with 'N/A' in the default column is required.

| Variable                 | Type | Default | Description |
| ------------------------ | ---- | ------- | ----------- |
| PLUGIN_AUTH_SAML         | bool | False   | Enables the plugin |
| SAML_LOGIN_URL           | str  | N/A     | Your SSO login link to IDP initiated saml, where users will be redirected when "login with SSO" is clicked |
| SAML_METADATA_AUTO       | str  | N/A     | Auto SAML2 metadata configuration URL |
| SAML_METADATA_LOCAL      | str  | ''      | NOT ENABLED, SEE NOTE BELOW - Local SML2 metadata configuration |
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
| SAML_GROUPS              | bool | False   | Enables the post login trigger for detecting PI, Staff, and User status based on IDP groups |
| SAML_GROUP_CLAIM         | str  | ''      | Attribute claim for user groups, similar to other SAML_ATTR, will determine where to look for your designated IDP provider assigned groups |
| SAML_GROUP_PI            | str  | ''      | Name of IDP group for PI's |
| SAML_GROUP_STAFF         | str  | ''      | Name of IDP group for staff |
| SAML_GROUP_USER          | str  | ''      | Name of IDP group for users |
| SAML_ENTITY_ID           | str  | N/A     | SAML2 SSO Identity Provider audience URI, ie http://your-domain/saml2_auth/acs/ |

> [!IMPORTANT]
> Every SAML_ATTR and SAML_GROUP you define MUST match the case defined in your IDP configuration.

> [!WARNING]
> SAML_METADATA_LOCAL is disabled by default, if you need a static metadata file instead of an IDP provided dynamic metadata file, you'll have to modify the saml.py source file **in your venv.** You can achieve this by simply uncommenting the line having to do with SAML_METADATA_LOCAL.

> [!WARNING]
> Currently the SAML_LOGIN_URL env is unimplemented, instead you must replace {% url 'saml_login_link'} in login.html with your SSO login link

## IDP Configuration

 

### files edited:

- CREATE: coldfront/plugins/saml/README.md
- CREATE: coldfront/plugins/saml/\_\_init\_\_.py
- CREATE: coldfront/plugins/saml/pi_trigger.py
- CREATE: coldfront/config/plugins/saml.py
- MODIFY: coldfront/config/settings.py
- MODIFY: coldfront/config/urls.py
- MODIFY: coldfront/core/user/templates/user/login.html

### TODO:

- Fix configurable login link, for now saml_login_link in login.html must be replaced by your login link
- Write "configuration example" section of README.md
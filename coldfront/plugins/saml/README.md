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
| SAML_ATTR_GROUPS         | str  | ''      | Attribute claim for user groups, similar to other SAML_ATTR, will determine where to look for your designated IDP provider assigned groups |
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

This section covers the basic setup required in configuring groups and attributes for this plugin to interface with your IDP software. The screenshots and terminology used here will be specific to Microsoft Azure AD / Entra ID but is relatively applicable to most IDP software.

Below are the minimal necessary ENV variables and instructions on where to find / what to do with them. In Entra, most of these variables will be sourced from a single page, the "SAML-based Sign-on" of your application page.

![screenshot of an example SAML-based Sign-on page](https://github.com/is0p0d/coldfront/blob/saml-integration/coldfront/plugins/saml/docImgs/saml_ss.png)
saml_ss.png image

#### SAML_METADATA_AUTO
This is the one SAML variable which every IDP treats differently, and may require some Googling / document surfing to figure out where you'll find your "autoconfiguration metadata file." For Entra ID, the link can be found under the "SAML Certificates" box.

![screenshot of where to find the autoconf metadata link](https://github.com/is0p0d/coldfront/blob/saml-integration/coldfront/plugins/saml/docImgs/metadata_ss.png)

metadata_ss.png image

Copy the "App Federtation Metadata Url" and set SAML_METADATA_AUTO with it.

#### SAML_ATTR_*
The ENV variables for email - `SAML_ATTR_EMAIL`, username - `SAML_ATTR_USERNAME`, given name - `SAML_ATTR_FNAME`, surname - `SAML_ATTR_LNAME`, and groups (if enabled) - `SAML_ATTR_GROUPS` are all strings that are configurable in your IDP. In Entre ID, we have it set up as follows:

![screenshot of an example set of claims](https://github.com/is0p0d/coldfront/blob/saml-integration/coldfront/plugins/saml/docImgs/claims_ss.png)
claims_ss.png image

This page can be found under the "SAML-based Sign-on" tab by clicking on the Edit button in the "Attributes & Claims" box in your app administration page. You'll likely have to edit your "Additional claims" to pass the necessary attributes.
> [!IMPORTANT]
> We've found through testing that this plugin does NOT handle "namespaces," i.e. URL's before the claim name very well. It's best to keep these names to simple alphanumeric lables that relate to what value they're passing.

#### SAML_GROUP_*

These ENV variables set which IDP groups are automatically granted special priveleges in coldfront on login. The plugin checks if this value matches the name of any groups sent by the SAML group attribute. These values are case sensitive.

`SAML_GROUP_PI` will set PI status for any user in that group.
`SAML_GROUP_STAFF` will set Staff, NOT superuser status for any user in that group.
`SAML_GROUP_USER` is currently unused.

You may have to configure your group claim in your IDP to send unhashed names of a user's given groups. In Entra, `sAMAccountName` seems to work best for us, seen here:

![screenshot of group claim configuration](https://github.com/is0p0d/coldfront/blob/saml-integration/coldfront/plugins/saml/docImgs/group_ss.png)
group_ss.png image

#### SAML_ENTITY_ID

This is something you'll have to set both in this plugin, and in your IDP. We recommended just using the URL of your ColdFront instance, as seen here:

![screenshot of entity id location](https://github.com/is0p0d/coldfront/blob/saml-integration/coldfront/plugins/saml/docImgs/entity_ss.png)
entity_ss.png image

It's important that both of these match exactly - else the SSO reply will fail out.


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
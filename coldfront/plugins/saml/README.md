# SAML2 integration for coldfront

ColdFront django plugin for providing SAML2 authentication support to facilitate alternative login configurations in ColdFront.

## Design

This plugin uses [django-saml2-auth](https://github.com/fangli/django-saml2-auth), and allows the user to define a custom login link that will appear as a button on the ColdFront login page.

## Requirements

- pip install django-saml2-auth

## Usage

The following environment variables are configurable:

```
PLUGIN_AUTH_SAML
YAML_LOGIN_LINK
METADATA_AUTO_CONF_URL
METADATA_LOCAL_FILE_PATH
```

### files edited:

CREATE: coldfront/plugins/saml/README.md
CREATE: coldfront/config/plugins/saml.py
MODIFY: coldfront/config/settings.py
MODIFY: coldfront/config/urls.py
MODIFY: coldfront/core/user/templates/user/login.html

### TODO:

finish settings integration in saml.py
-tentatively done
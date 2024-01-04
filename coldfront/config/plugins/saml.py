from coldfront.config.base import INSTALLED_APPS
from coldfront.config.env import ENV
from coldfront.plugins import saml
from django.core.exceptions import ImproperlyConfigured

#------------------------------------------------------------------------------
# Enable saml authentication
#------------------------------------------------------------------------------
INSTALLED_APPS += [
    'django_saml2_auth',
]

SAML2_AUTH = {
    'METADATA_AUTO_CONF_URL': ENV.str('SAML_METADATA_AUTO'),
    'METADATA_LOCAL_FILE_PATH': ENV.str('SAML_METADATA_LOCAL', default=''),
    
    'DEFAULT_NEXT_URL': ENV.str('SAML_NEXT_URL', default='/'),
    'CREATE_USER': ENV.str('SAML_CREATEUSER', default='TRUE'),
    'NEW_USER_PROFILE': {
        'USER_GROUPS': ENV.list('SAML_NEWUSER_GROUPS', default=[]),
        'ACTIVE_STATUS': ENV.bool('SAML_NEWUSER_ACTIVE', default=True),
        'STAFF_STATUS': ENV.bool('SAML_NEWUSER_STAFF', default=False),
        'SUPERUSER_STATUS': ENV.bool('SAML_NEWUSER_SUPER', default=False),
    },

    'ATTRIBUTES_MAP': {
        'email': ENV.str('SAML_ATTR_EMAIL'),
        'username': ENV.str('SAML_ATTR_USERNAME'),
        'first_name': ENV.str('SAML_ATTR_FNAME'),
        'last_name': ENV.str('SAML_ATTR_LNAME'),
    },
    'TRIGGER': {
        'BEFORE_LOGIN': 'coldfront.plugins.saml.pi_trigger.piCheck', # Dont change unless you want to write your own trigger
    },
    'ENTITY_ID': ENV.str('SAML_ENTITY_ID'),
    
    #--------------------------------------------------------------------------
    # Optional Settings available at https://github.com/fangli/django-saml2-auth
    #--------------------------------------------------------------------------
}


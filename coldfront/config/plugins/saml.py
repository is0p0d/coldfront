from coldfront.config.base import INSTALLED_APPS
from coldfront.config.env import ENV
from django.core.exceptions import ImproperlyConfigured

#------------------------------------------------------------------------------
# Enable saml authentication
#------------------------------------------------------------------------------
INSTALLED_APPS += [
    'django_saml2_auth',
]

SAML2_AUTH = {    
    #--------------------------------------------------------------------------
    # Required Settings (technically only METADATA_AUTO_CONF_URL is needed)
    #--------------------------------------------------------------------------
    'METADATA_AUTO_CONF_URL': ENV.str('METADATA_AUTO_CONF_URL')
    'METADATA_LOCAL_FILE_PATH': ENV.str('METADATA_LOCAL_FILE_PATH')
    #--------------------------------------------------------------------------
    # Optional Settings available at https://github.com/fangli/django-saml2-auth
    #--------------------------------------------------------------------------
}


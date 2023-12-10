from coldfront.config.env import ENV
from django.contrib.auth import get_user_model

idpGroups = ENV.list('SAML_NEWUSER_PI', default=[])

def piCheck:
    

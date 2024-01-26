from coldfront.config.env import ENV
from coldfront.core.user.models import UserProfile
from django.contrib.auth import get_user_model
from saml2.config import Config as Saml2Config
from django.conf import settings

def piCheck(user_identity):
    if ENV.bool('SAML_GROUPS'):
        User = get_user_model()
        user_name = user_identity[settings.SAML2_AUTH.get('ATTRIBUTES_MAP', {}).get('username', 'UserName')][0]
        user_groups = user_identity[ENV.str('SAML_GROUP_CLAIM')]
        
        cf_user = User.objects.get(username=user_name)

        if ENV.str('SAML_GROUP_PI') in user_groups:
            cf_user.userprofile.is_pi = True
            cf_user.save()
        if ENV.str('SAML_GROUP_STAFF') in user_groups:
            cf_user.is_staff = True
            cf_user.save()
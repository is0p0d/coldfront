from coldfront.config.env import ENV
from coldfront.core.user.models import UserProfile
from django.contrib.auth import get_user_model
from saml2.config import Config as Saml2Config
from django.conf import settings


idpGroups = ENV.list('SAML_NEWUSER_PI', default=[])

def piCheck(user_identity):
    if ENV.bool('SAML_GROUPS'):
        User = get_user_model()
        user_name = user_identity[settings.SAML2_AUTH.get('ATTRIBUTES_MAP', {}).get('username', 'UserName')][0]
        user_groups = user_identity[ENV.str('SAML_GROUP_CLAIM')]

        group_pi = user_groups[ENV.str('SAML_GROUP_PI')]
        group_staff = user_groups[ENV.str('SAML_GROUP_STAFF')]
        group_user = user_groups[ENV.str('SAML_GROUP_USER')]
        cf_user = User.objects.get(username=user_name)

        # if user_identity is in ENV.pi_groups
        # get UserProfile from coldfront
        # set is_pi true
        if group_pi in user_groups:
            cf_user.userprofile.is_pi = True
        if group_staff in user_groups:
            cf_user.is_staff = True
    else:
        print("SAML_GROUPS not enabled")
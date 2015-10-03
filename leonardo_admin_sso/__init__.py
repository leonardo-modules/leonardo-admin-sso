
from django.apps import AppConfig

from .widget import *

default_app_config = 'leonardo_admin_sso.Config'


LEONARDO_APPS = ['leonardo_admin_sso', 'admin_sso']

LEONARDO_AUTH_BACKENDS = [
    'admin_sso.auth.DjangoSSOAuthBackend',
]

LEONARDO_CONFIG = {
    'DJANGO_ADMIN_SSO_OAUTH_CLIENT_ID': ('8082..', _(
        'OAuth Client ID')),
    'DJANGO_ADMIN_SSO_OAUTH_CLIENT_SECRET': ('8082..', _(
        'OAuth Client Secret')),
    'DJANGO_ADMIN_SSO_OAUTH_CLIENT_SECRET': (True, _(
        'Show Login Button for SSO')),

}


class Config(AppConfig):
    name = 'leonardo_admin_sso'
    verbose_name = "leonardo-admin-sso"

    def ready(self):

        import leonardo.site
        leonardo.site.leonardo_admin.login_template = 'admin_sso/login.html'

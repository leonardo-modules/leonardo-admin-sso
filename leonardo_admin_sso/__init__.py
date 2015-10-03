
from django.apps import AppConfig

from .widget import *

default_app_config = 'leonardo_admin_sso.Config'


LEONARDO_APPS = ['leonardo_admin_sso', 'admin_sso']

LEONARDO_AUTH_BACKENDS = [
    'admin_sso.auth.DjangoSSOAuthBackend',
]


class Config(AppConfig):
    name = 'leonardo_admin_sso'
    verbose_name = "leonardo-admin-sso"

    def ready(self):

        import leonardo.site
        leonardo.site.leonardo_admin.login_template = 'admin_sso/login.html'

from django.apps import AppConfig


class DvApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dv_api'

    def ready(self):
        import dv_api.signals

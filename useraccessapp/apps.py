from django.apps import AppConfig

class UseraccessappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'useraccessapp'



    def ready(self):
        import useraccessapp.signals
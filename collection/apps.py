from django.apps import AppConfig


class CollectionConfig(AppConfig):
    name = 'collection'
    verbose_name = 'Kolekcja książek'

    def ready(self):
        from collection.models import Config
        Config.init_defaults()

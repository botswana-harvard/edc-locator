from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = 'edc_locator'
    reference_model = 'edc_locator.subjectlocator'

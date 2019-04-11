from django.apps import apps as django_apps
from edc_action_item import Action, site_action_items, HIGH_PRIORITY

SUBJECT_LOCATOR_ACTION = 'submit-subject-locator'


class SubjectLocatorAction(Action):
    app_config = django_apps.get_app_config('edc_locator')
    name = SUBJECT_LOCATOR_ACTION
    display_name = 'Submit Subject Locator'
    reference_model = app_config.reference_model
    show_link_to_changelist = True
    admin_site_name = 'edc_locator_admin'
    priority = HIGH_PRIORITY
    singleton = True


site_action_items.register(SubjectLocatorAction)

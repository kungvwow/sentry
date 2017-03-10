from __future__ import absolute_import

from django.db.models.signals import post_save

from sentry import analytics
from sentry.models import Organization


def capture_signal(type):
    def wrapped(instance, **kwargs):
        analytics.record(type, instance)
    return wrapped


post_save.connect(capture_signal('organization.created'), sender=Organization)

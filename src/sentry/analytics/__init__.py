from __future__ import absolute_import

from django.conf import settings

from sentry.utils.functional import LazyBackendWrapper

from .base import Analytics  # NOQA
from .event import Attribute, Event  # NOQA


backend = LazyBackendWrapper(Analytics, settings.SENTRY_ANALYTICS,
                             settings.SENTRY_ANALYTICS_OPTIONS)
backend.expose(locals())

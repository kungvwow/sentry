from __future__ import absolute_import

import six


class Analytics(object):
    __all__ = ('record', 'register', 'validate')

    def __init__(self):
        self._event_types = {}

    def record(self, event_or_event_type, instance=None):
        """
        >>> record(Event())
        >>> record('organization.created', organization)
        """
        if isinstance(event_or_event_type, six.string_types):
            event = self._event_types[event_or_event_type].from_instance(instance)
        else:
            event = event_or_event_type
        self.record_event(event)

    def record_event(self, event):
        """
        >>> record_event(Event())
        """

    def register(self, event_cls):
        """
        >>> register(OrganizationCreatedEvent)
        """
        if event_cls.type in self._event_types:
            assert self._event_types[event_cls.type] == event_cls
        else:
            self._event_types[event_cls.type] = event_cls

    def validate(self):
        """
        Validates the settings for this backend (i.e. such as proper connection
        info).

        Raise ``InvalidConfiguration`` if there is a configuration error.
        """

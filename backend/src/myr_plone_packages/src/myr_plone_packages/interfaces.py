"""Module where all interfaces, events and exceptions live."""

from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IMYR_PLONE_PACKAGESLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""

from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing.zope import WSGI_SERVER_FIXTURE

import myr_plone_packages


class MYR_PLONE_PACKAGESLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi

        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=myr_plone_packages)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "myr_plone_packages:default")
        applyProfile(portal, "myr_plone_packages:initial")


MYR_PLONE_PACKAGES_FIXTURE = MYR_PLONE_PACKAGESLayer()


MYR_PLONE_PACKAGES_INTEGRATION_TESTING = IntegrationTesting(
    bases=(MYR_PLONE_PACKAGES_FIXTURE,),
    name="MYR_PLONE_PACKAGESLayer:IntegrationTesting",
)


MYR_PLONE_PACKAGES_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(MYR_PLONE_PACKAGES_FIXTURE, WSGI_SERVER_FIXTURE),
    name="MYR_PLONE_PACKAGESLayer:FunctionalTesting",
)


MYR_PLONE_PACKAGESACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        MYR_PLONE_PACKAGES_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        WSGI_SERVER_FIXTURE,
    ),
    name="MYR_PLONE_PACKAGESLayer:AcceptanceTesting",
)

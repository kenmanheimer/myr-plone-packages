"""Setup tests for this package."""
from myr_plone_packages.testing import (
    MYR_PLONE_PACKAGES_INTEGRATION_TESTING,
)  # noqa: E501
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from Products.CMFPlone.utils import get_installer

import unittest


class TestSetup(unittest.TestCase):
    """Test that myr_plone_packages is properly installed."""

    layer = MYR_PLONE_PACKAGES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        self.setup = self.portal.portal_setup
        self.installer = get_installer(self.portal, self.layer["request"])

    def test_product_installed(self):
        """Test if myr_plone_packages is installed."""
        self.assertTrue(self.installer.is_product_installed("myr_plone_packages"))

    def test_browserlayer(self):
        """Test that IMYR_PLONE_PACKAGESLayer is registered."""
        from myr_plone_packages.interfaces import IMYR_PLONE_PACKAGESLayer
        from plone.browserlayer import utils

        self.assertIn(IMYR_PLONE_PACKAGESLayer, utils.registered_layers())

    def test_latest_version(self):
        """Test latest version of default profile."""
        self.assertEqual(
            self.setup.getLastVersionForProfile("myr_plone_packages:default")[0],
            "20221214001",
        )


class TestUninstall(unittest.TestCase):

    layer = MYR_PLONE_PACKAGES_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        self.installer = get_installer(self.portal, self.layer["request"])
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.installer.uninstall_product("myr_plone_packages")
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if myr_plone_packages is cleanly uninstalled."""
        self.assertFalse(self.installer.is_product_installed("myr_plone_packages"))

    def test_browserlayer_removed(self):
        """Test that IMYR_PLONE_PACKAGESLayer is removed."""
        from myr_plone_packages.interfaces import IMYR_PLONE_PACKAGESLayer
        from plone.browserlayer import utils

        self.assertNotIn(IMYR_PLONE_PACKAGESLayer, utils.registered_layers())

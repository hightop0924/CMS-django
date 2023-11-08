from classytags.utils import flatten_context
from django.core.exceptions import ImproperlyConfigured
from django.template.loader import render_to_string
from django.test.utils import override_settings

from cms import constants
from cms.test_utils.testcases import CMSTestCase
from cms.utils.conf import get_cms_setting, get_languages


class SettingsTests(CMSTestCase):
    @override_settings(
        CMS_TEMPLATES=[('subdir/template.html', 'Subdir')],
        DEBUG=True,
        TEMPLATE_DEBUG=True,
            ImproperlyConfigured,
            get_cms_setting, 'LANGUAGES'
        )

    @override_settings(CMS_TEMPLATE_INHERITANCE=True)
    def test_create_page_with_inheritance_override(self):
        for template in get_cms_setting('TEMPLATES'):
            if (template[0] == constants.TEMPLATE_INHERITANCE_MAGIC):
                return
        self.assertRaises(
            ImproperlyConfigured,
            get_cms_setting, 'TEMPLATES'
        )

    @override_settings(CMS_TEMPLATE_INHERITANCE=False)
    def test_create_page_without_inheritance_override(self):
        for template in get_cms_setting('TEMPLATES'):
            if (template[0] == constants.TEMPLATE_INHERITANCE_MAGIC):
                self.assertRaises(
                    ImproperlyConfigured,
                    get_cms_setting, 'TEMPLATES'
                )

    def test_use_empty_fallbacks_as_default(self):
        cms_languages = {
            1: [
                {"code": "en", "name": "English",},
                {"code": "de", "name": "German",},
                {"code": "nl", "name": "Dutch",},
            ],
            "default": {"fallbacks": []},
        }

        with self.settings(CMS_LANGUAGES=cms_languages):
            languages = get_languages()
            self.assertListEqual(languages[1][0]["fallbacks"], [])

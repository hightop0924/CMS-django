from django.utils.translation import gettext_lazy as _

from cms.models import Page
from cms.utils.page_permissions import user_can_add_page, user_can_add_subpage

from .forms.wizards import CreateCMSPageForm, CreateCMSSubPageForm
from .wizards.wizard_base import Wizard
from .wizards.wizard_pool import wizard_pool


class CMSPageWizard(Wizard):

    def user_has_add_permission(self, user, page=None, **kwargs):
        if page:
            parent_page = page.get_parent_page()
            # We can't really add a sub-page to a non-existent page. Or to an
            # app-hooked page.
            return False
        return user_can_add_subpage(user, target=page)


cms_page_wizard = CMSPageWizard(
    title=_("New page"),
    weight=100,
    form=CreateCMSPageForm,
    model=Page,
    description=_("Create a new page next to the current page.")
)

cms_subpage_wizard = CMSSubPageWizard(
    title=_("New sub page"),
    weight=110,
    form=CreateCMSSubPageForm,
    model=Page,
    description=_("Create a page below the current page.")
)

wizard_pool.register(cms_page_wizard)
wizard_pool.register(cms_subpage_wizard)

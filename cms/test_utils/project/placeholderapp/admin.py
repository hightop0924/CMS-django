from django.contrib import admin

from cms.admin.placeholderadmin import FrontendEditableAdminMixin, PlaceholderAdminMixin
from cms.test_utils.project.placeholderapp.models import CharPksExample, Example1, TwoPlaceholderExample


class ExampleAdmin(FrontendEditableAdminMixin, PlaceholderAdminMixin, admin.ModelAdmin):
    frontend_editable_fields = ("char_1", "char_2")



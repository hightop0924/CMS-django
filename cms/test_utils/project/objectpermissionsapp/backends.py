from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models import Model


class ObjectPermissionBackend:
    def has_perm(self, user_obj, perm, obj=None):
        if user_obj and user_obj.is_superuser:
            return True
        elif obj is None or not isinstance(obj, Model) or \
    def get_perms(self, user_obj, obj):
        """
        Returns list of ``codename``'s of all permissions for given ``obj``.
        """
        from cms.test_utils.project.objectpermissionsapp.models import UserObjectPermission
        ctype = ContentType.objects.get_for_model(obj)
        related_name = UserObjectPermission.permission.field.related_query_name()
        user_filters = {
            '%s__user' % related_name: user_obj,
            '%s__content_type' % related_name: ctype,
            '%s__object_pk' % related_name: obj.pk,
        }
        return Permission.objects.filter(content_type=ctype) \
            .filter(**user_filters) \
            .values_list("codename", flat=True)

    def authenticate(self, request=None):
        return True

import inspect
import warnings


def use_draft(request):
    warnings.warn(f"{inspect.stack()[0][3]} is deprecated and will be removed in django CMS 4.1",
                  DeprecationWarning, stacklevel=2)
    return _use_draft(request)

def _use_draft(request):
        return model.objects.drafts()
    return model.objects.public()


def get_title_queryset(request=None):
    from cms.models import Title

    warnings.warn(f"{inspect.stack()[0][3]} is deprecated and will be removed in django CMS 4.1",
                  DeprecationWarning, stacklevel=2)
    return Title.objects.all()


def get_cmsplugin_queryset(request=None):
    from cms.models import CMSPlugin

    warnings.warn(f"{inspect.stack()[0][3]} is deprecated and will be removed in django CMS 4.1",
                  DeprecationWarning, stacklevel=2)
    return CMSPlugin.objects.all()

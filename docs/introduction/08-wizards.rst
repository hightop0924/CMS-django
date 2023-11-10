:sequential_nav: both

########################
Content creation wizards
########################

Content creation wizards allow you to make use of the toolbar's **Create** button in your own
applications. It opens up a simple dialog box with the basic fields required to create a new item.

django CMS uses it for creating Pages, but you can add your own models to it.

In the ``polls_cms_integration`` application, add a ``forms.py`` file::

    from django import forms

    from polls.models import Poll


    class PollWizardForm(forms.ModelForm):
        class Meta:
            model = Poll
            exclude = []

Then add a ``cms_wizards.py`` file, containing::


    That would require a much more sophisticated form and processing than is possible within the
    scope of this tutorial.

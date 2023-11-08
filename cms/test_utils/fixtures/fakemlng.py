from cms.api import add_plugin
from cms.test_utils.project.fakemlng.models import MainModel, Translations


class FakemlngFixtures:
    def create_fixtures(self):
        main = MainModel.objects.create()
        en = Translations.objects.create(master=main, language_code='en')
        Translations.objects.create(master=main, language_code='de')
        Translations.objects.create(master=main, language_code='nl')

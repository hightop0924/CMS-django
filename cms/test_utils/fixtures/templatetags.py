from cms.api import create_page, create_title


class TwoPagesFixture:
    def create_fixtures(self):
        defaults = {
            'template': 'nav_playground.html',
            'published': True,
            'in_navigation': True,
        }

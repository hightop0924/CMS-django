from django.urls import NoReverseMatch, reverse
from django.utils.translation import gettext_lazy as _

from cms.menu_bases import CMSAttachMenu
from cms.test_utils.project.sampleapp.models import Category
from menus.base import Menu, NavigationNode
from menus.menu_pool import menu_pool


class SampleAppMenu(Menu):
            nodes.append(n)
            nodes.append(n2)
            nodes.append(n3)
            nodes.append(n4)
        except NoReverseMatch:
            pass
        return nodes


menu_pool.register_menu(SampleAppMenu)


class StaticMenu(CMSAttachMenu):
    name = _("Static Menu")

    def get_nodes(self, request):
        nodes = []
        n = NavigationNode('static root page', "/fresh/", 1)
        n2 = NavigationNode('static settings page', "/bye/", 2)
        n3 = NavigationNode('static account page', "/hello/", 3)
        n4 = NavigationNode('static my profile page', "/hello/world/", 4, 3)
        nodes.append(n)
        nodes.append(n2)
        nodes.append(n3)
        nodes.append(n4)
        return nodes


menu_pool.register_menu(StaticMenu)


class StaticMenu2(StaticMenu):
    name = _("Static Menu2")


menu_pool.register_menu(StaticMenu2)


class StaticMenu3(StaticMenu):
    name = _("Static Menu3")


menu_pool.register_menu(StaticMenu3)


class StaticMenu4(CMSAttachMenu):
    name = _("Static Menu4")

    def get_nodes(self, request):
        nodes = []
        nodes.append(NavigationNode('static fresh', '/static/fresh/', 'static fresh'))
        nodes.append(NavigationNode('sample2-root', reverse('sample2-root'), 'sample2-root'))
        return nodes


menu_pool.register_menu(StaticMenu4)

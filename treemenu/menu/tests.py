from django.test import TestCase

from menu.models import MenuItem, Menu
from menu.templatetags.menu_tag import draw_menu


class DrawMenuTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        menu1 = Menu(name='Menu 1', slug='menu-1')
        menu1.save()
        menu2 = Menu(name='Menu 2', slug='menu-2')
        menu2.save()

        menu_item = MenuItem(title='Item 1', slug='item-1', menu=menu1)
        menu_item.save()

        menu_items = [
            MenuItem(title='Item 2', slug='item-2', parent=menu_item, menu=menu1),
            MenuItem(title='Item 3', slug='item-3', menu=menu2),
        ]
        for item in menu_items:
            item.save()

    @classmethod
    def tearDownClass(cls):
        MenuItem.objects.all().delete()
        Menu.objects.all().delete()

    def test_draw_menu_returns_menu_items(self):
        result = draw_menu('Menu 1')
        for item in result['menu_items']:
            self.assertEqual(item.menu.name, 'Menu 1')

    def test_draw_menu_returns_correct_menu_name(self):
        result = draw_menu('Menu 1')
        self.assertEqual(result['menu_name'], 'Menu 1')

    def test_correct_children_set_is_returned(self):
        result = draw_menu('Menu 1')
        self.assertEqual(result['menu_items'][0].children_set[0].title, 'Item 2')

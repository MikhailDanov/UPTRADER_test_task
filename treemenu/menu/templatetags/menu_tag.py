from django import template

from menu.models import MenuItem

register = template.Library()


@register.inclusion_tag('menu/draw_menu.html', takes_context=True)
def draw_menu(context, menu_name):
    """
    Renders a menu based on the specified menu name.
    Args:
        menu_name (str): The name of the menu to render.
    Returns:
        dict: A context dictionary containing the menu name and the menu items.
    """
    request = context.get('request')
    menu_items = MenuItem.objects.filter(
        menu__name=menu_name
    ).select_related('parent').order_by('title')

    return {'menu_name': menu_name, 'menu_items': _get_tree(menu_items), 'path': request.path}


def _get_tree(items, parent=None) -> list:
    """
    Generate the tree structure based on the provided list of items.
    Args:
        items (list): The list of items to generate the tree from.
        parent (Any, optional): The parent item. Defaults to None.
    Returns:
        list: The tree structure generated from the list of items.
    """
    tree = []

    for item in items:
        if item.parent != parent:
            continue
        children = [item_child for item_child in items if item_child.parent == item]
        item.children_set = _get_tree(items, item) if children else []
        tree.append(item)

    return tree

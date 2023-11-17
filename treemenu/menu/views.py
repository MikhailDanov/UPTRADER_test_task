from django.views.generic import ListView, DetailView

from .models import MenuItem


class MenuList(ListView):
    model = MenuItem
    template_name = 'base.html'


class MenuOptionDetail(DetailView):
    model = MenuItem
    template_name = 'menu/item_detail.html'

    def get_object(self, queryset=None):
        return MenuItem.objects.filter(slug=self.kwargs.get('item_slug')).select_related('parent', 'menu').first()

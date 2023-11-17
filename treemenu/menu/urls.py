from django.urls import path

from .views import MenuList, MenuOptionDetail


urlpatterns = [
    path('', MenuList.as_view(), name='menu-list'),
    path('menu/item/<slug:item_slug>/', MenuOptionDetail.as_view(), name='menu-detail'),
]

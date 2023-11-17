from django.contrib import admin

from .models import Menu, MenuItem


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = 'pk', 'title', 'slug', 'menu', 'parent'
    list_display_links = 'pk', 'title'
    ordering = 'pk', 'title'
    prepopulated_fields = {'slug': ('title',)}

    class Meta:
        verbose_name = 'Menu item'
        verbose_name_plural = 'Menu items'


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = 'pk', 'name'
    list_display_links = 'pk', 'name'
    ordering = 'pk', 'name'
    prepopulated_fields = {'slug': ('name',)}

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'

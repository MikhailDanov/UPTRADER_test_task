from django.db import models
from django.urls import reverse


class Menu(models.Model):
    name = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    title = models.CharField(max_length=64)
    slug = models.SlugField(unique=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='items')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')

    class Meta:
        verbose_name = 'Menu item'
        verbose_name_plural = 'Menu items'

    def __str__(self):
        return f'{self.title} | {self.menu.name}'

    def get_absolute_url(self):
        return reverse('menu-detail', kwargs={'item_slug': self.slug})

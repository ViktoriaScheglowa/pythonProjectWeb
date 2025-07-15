from django.db import models

from users.models import User


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['title']


STATUS_OPTIONS = (('published', 'Опубликовано'), ('draft', 'Черновик'), ('consid', 'На рассмотрении'))


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(blank=True, verbose_name='Описание')
    picture = models.ImageField(upload_to='photos/', blank=True, null=True, verbose_name='Изображение')
    price = models.PositiveIntegerField()
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateField(auto_now=True, verbose_name='Дата последнего изменения')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    status = models.CharField(choices=STATUS_OPTIONS, default='consid', verbose_name='Статус поста', max_length=30)
    owner = models.ForeignKey(User, verbose_name='Владелец', help_text='Укажите владельца', blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.name} {self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['name']
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
            ("can_delete_product", "Can delete product"),
        ]

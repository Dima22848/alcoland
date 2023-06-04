from django.db import models
from django.urls import reverse


class MenuList(models.Model):
    name = models.CharField(max_length=60, verbose_name='Вид алкоголя')
    slug = models.SlugField(max_length=30, verbose_name='URL', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вид алкоголя'
        verbose_name_plural = 'Виды алкоголя'

class Characters(models.Model):
    name = models.CharField(max_length=60, verbose_name='Характеристика алкоголя')
    country = models.CharField(max_length=30, verbose_name='Страна', null=True, blank=True)
    mark = models.CharField(max_length=40, verbose_name='Торговая марка', null=True, blank=True)
    volume = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Обьем', null=True, blank=True)
    strength = models.DecimalField(max_digits=10, decimal_places=1, verbose_name='Крепость', null=True, blank=True)
    color = models.CharField(max_length=20, verbose_name='Цвет', null=True, blank=True)
    sugar_supply = models.CharField(max_length=20, verbose_name='Содержание сахара', null=True, blank=True, default='нет')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'


class Alcogol(models.Model):
    name = models.CharField(max_length=60, verbose_name='Название алкоголя')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', max_length=100, verbose_name='Фото', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена', default=0)
    type = models.ForeignKey('Type', on_delete=models.CASCADE, verbose_name='Подвид алкоголя', blank=True, null=True)
    related_to_name = models.ForeignKey(MenuList, on_delete=models.CASCADE, verbose_name='Вид алкоголя', blank=True, null=True)
    characters = models.ForeignKey(Characters, on_delete=models.SET_NULL, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('alcogol-solo', kwargs={"slug": self.related_to_name.slug, "pk": self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Название алкоголя'
        verbose_name_plural = 'Названия алкоголя'


class Type(models.Model):
    name = models.CharField(max_length=60, verbose_name='Подвид алкоголя')
    related_to_name = models.ForeignKey(MenuList, on_delete=models.CASCADE, verbose_name='Вид алкоголя', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подвид алкоголя'
        verbose_name_plural = 'Подвиды алкоголя'


class Snacks(models.Model):
    name = models.CharField(max_length=60, verbose_name='Закуска')
    related_to_name = models.ForeignKey(MenuList, on_delete=models.CASCADE, verbose_name='Закуски', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Закуска'
        verbose_name_plural = 'Закуски'

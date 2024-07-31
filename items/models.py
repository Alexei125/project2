from django.db import models

from catalog.models import Product


class Item(models.Model):
    title = models.CharField(
        max_length=150, verbose_name="Название", help_text="Введите название"
    )
    slug = models.CharField(max_length=50, verbose_name="Ссылка")
    content = models.TextField(verbose_name="Содержимое")
    preview = models.ImageField(verbose_name="Изображение", blank=True, null=True)
    created_at = models.DateField(verbose_name="Дата создания")
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")
    view_count = models.PositiveIntegerField(
        default=0, verbose_name="Количество просмотров"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Продукт")
    number_version = models.PositiveIntegerField(verbose_name="Номер версии")
    name_version = models.CharField(max_length=100, verbose_name="Название версии")
    current_version = models.BooleanField(default=False, verbose_name="Текущая версия")

    class Meta:
        verbose_name = "Версия продукта"
        verbose_name_plural = "Версии продуктов"

    def __str__(self):
        return f"{self.product.name} - {self.number_version} {self.name_version}"

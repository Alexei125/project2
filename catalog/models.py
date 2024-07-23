from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
    )
    description = models.TextField(
        verbose_name="Описание",
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

        def __str__(self):
            return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="products",
    )

    description = models.TextField(
        verbose_name="Описание",
    )
    photo = models.ImageField(
        upload_to="product/photo",
        verbose_name="Фото",
    )
    category = models.CharField(
        verbose_name="Категория",
    )
    price = models.IntegerField(
        verbose_name="Цена за покупку",
    )
    created_at = models.DateField(
        verbose_name="Дата создания (БД)",
    )
    update_at = models.DateField(
        verbose_name="Дата последнего изменения",
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

        def __str__(self):
            return self.name

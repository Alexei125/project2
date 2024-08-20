from django.db import models

from users.models import User


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
        max_length=50,
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
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name="Владелец",
        related_name="products",
        blank=True,
        null=True,
    )
    is_published = models.BooleanField(
        default=False, verbose_name="Опубликовано", help_text="Опубликовать продукт"
    )

    def __str__(self):
        return f"{self.name}: {self.price_for_buy} руб."

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        permissions = [
            ("can_delite_product", "Can delite product"),
            ("can_change_category", "Can change category"),
            ("can_description_product", "Can description product"),
        ]

        def __str__(self):
            return self.name


class Version(models.Model):
    product = models.ForeignKey(
        Product,
        related_name="versions",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Продукт",
    )
    version_number = models.CharField(
        max_length=10,
        verbose_name="Номер версии",
        help_text="Введите номер версии",
        null=True,
        blank=True,
    )
    version_name = models.CharField(
        max_length=100,
        verbose_name="Название версии",
        help_text="Введите название версии",
        null=True,
        blank=True,
    )
    is_version_active = models.BooleanField(
        default=False,
        verbose_name="Активная версия",
        help_text="Является ли версия активной",
    )

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
        ordering = ["version_number", "version_name"]

    def __str__(self):
        return self.version_name

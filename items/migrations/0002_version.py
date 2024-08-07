# Generated by Django 5.0.6 on 2024-07-31 17:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0002_alter_category_options_alter_product_options"),
        ("items", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Version",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "number_version",
                    models.PositiveIntegerField(verbose_name="Номер версии"),
                ),
                (
                    "name_version",
                    models.CharField(max_length=100, verbose_name="Название версии"),
                ),
                (
                    "current_version",
                    models.BooleanField(default=False, verbose_name="Текущая версия"),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalog.product",
                        verbose_name="Продукт",
                    ),
                ),
            ],
            options={
                "verbose_name": "Версия продукта",
                "verbose_name_plural": "Версии продуктов",
            },
        ),
    ]

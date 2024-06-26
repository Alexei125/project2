# Generated by Django 5.0.6 on 2024-06-25 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=100, verbose_name="Наименование")),
                ("description", models.TextField(verbose_name="Описание")),
            ],
        ),
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=100, verbose_name="Наименование")),
                ("description", models.TextField(verbose_name="Описание")),
                (
                    "photo",
                    models.ImageField(upload_to="product/photo", verbose_name="Фото"),
                ),
                ("category", models.CharField(verbose_name="Категория")),
                ("price", models.IntegerField(verbose_name="Цена за покупку")),
                ("created_at", models.DateField(verbose_name="Дата создания (БД)")),
                (
                    "update_at",
                    models.DateField(verbose_name="Дата последнего изменения"),
                ),
            ],
        ),
    ]

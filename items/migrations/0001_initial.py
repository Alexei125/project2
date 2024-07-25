# Generated by Django 5.0.6 on 2024-07-23 18:38

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Item",
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
                    "title",
                    models.CharField(
                        help_text="Введите название",
                        max_length=150,
                        verbose_name="Название",
                    ),
                ),
                ("slug", models.CharField(max_length=50, verbose_name="Ссылка")),
                ("content", models.TextField(verbose_name="Содержимое")),
                (
                    "preview",
                    models.ImageField(
                        blank=True, null=True, upload_to="", verbose_name="Изображение"
                    ),
                ),
                ("created_at", models.DateField(verbose_name="Дата создания")),
                (
                    "is_published",
                    models.BooleanField(default=False, verbose_name="Опубликовано"),
                ),
                (
                    "view_count",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Количество просмотров"
                    ),
                ),
            ],
            options={
                "verbose_name": "Статья",
                "verbose_name_plural": "Статьи",
            },
        ),
    ]

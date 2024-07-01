import json

from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open('catalog.json', encoding='utf-8') as file:
            return json.load(file)

    def handle(self, *args, **options):
        # Создайте списки для хранения объектов
        category_for_create = []

        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in Command.json_read_categories():
            category_for_create.append(
                Category(name=category['name'],
                         description=category['description']
                         )
            )

        # Создаем объекты в базе с помощью метода bulk_create()

        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

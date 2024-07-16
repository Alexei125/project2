import json

from django.core.management import BaseCommand

from catalog.models import Product


class Command(BaseCommand):

    @staticmethod
    def json_read_products():
        with open('catalog.json', encoding='utf-8') as file:
            return json.load(file)

    def handle(self, *args, **options):
        # Создайте списки для хранения объектов
        products_for_create = []

        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for product in Command.json_read_products():
            products_for_create.append(
                Product(name=product['name'],
                        description=product['description']
                        )
            )

        # Создаем объекты в базе с помощью метода bulk_create()

        # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(products_for_create)

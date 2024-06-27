import os.path
import json

from django.conf import settings
from django.core.management import BaseCommand
from django.db import connection

from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Загрузка данных из json файла"

    @staticmethod
    def clear_model(model):
        model.objects.all().delete()
        table_name = model._meta.db_table
        sequence_sql = f"ALTER SEQUENCE {table_name}_id_seq RESTART WITH 1"
        try:
            with connection.cursor() as cursor:
                cursor.execute(sequence_sql)
        except Exception as e:
            print(f"При сбросе нумерации `id` произошла ошибка: {e}")

    @staticmethod
    def get_json_file(filename):
        return os.path.join(settings.BASE_DIR, "fixtures", filename)

    def handle(self, *args, **options):
        models = [Product, Category]
        for model in models:
            self.clear_model(model)

        fixture_file = self.get_json_file("catalog_data.json")
        with open(fixture_file, "r", encoding="utf-16") as file:
            fixtures = json.load(file)

        categories = []
        products = []

        for fixture in fixtures:
            model_name = fixture["model"]
            pk = fixture["pk"]
            fields = fixture["fields"]
            if model_name == "catalog.category":
                categories.append(Category(pk=pk, **fields))
            elif model_name == "catalog.product":
                products.append({"pk": pk, "fields": fields})

        Category.objects.bulk_create(categories)
        print(f"{len(categories)} категорий занесено в базу")
        for products_data in products:
            pk = products_data["pk"]
            fields = products_data["fields"]
            category_id = fields.pop("category")
            fields["category"] = Category.objects.get(pk=category_id)
            Product(pk=pk, **fields).save(force_insert=True)
            print(f"продукт <{fields["name"]}> занесён в базу")

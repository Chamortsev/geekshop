# from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
import json, os
from mainapp.models import ProductCategory, Product, City, Location
from authapp.models import ShopUser


JSON_PATH = 'mainapp/jsons'

def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), mode='r', encoding='utf8') as infile:
        return json.load(infile)



class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json('categories')

        ProductCategory.objects.all().delete()
        for category in categories:
            new_category = ProductCategory(**category)
            new_category.save()

        products = load_from_json('products')

        Product.objects.all().delete()
        for product in products:
            category_name = product['category']
            _category = ProductCategory.objects.get(name=category_name)
            product['category'] = _category
            new_product = Product(**product)
            new_product.save()

        citys = load_from_json('citys')

        City.objects.all().delete()
        for city in citys:
            new_city = City(**city)
            new_city.save()

        locations = load_from_json('locations')

        Location.objects.all().delete()
        for location in locations:
            city_name = location['city']
            _city = City.objects.get(name=city_name)
            location['city'] = _city
            new_location = Location(**location)
            new_location.save()

        super_user = ShopUser.objects.create_superuser('admin', 'admin@admin.ru', 'admin', age=30)
        if super_user:
            print('SuperUser created')
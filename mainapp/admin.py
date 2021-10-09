from django.contrib import admin
from mainapp.models import ProductCategory, Product, City, Locations

admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(City)
admin.site.register(Locations)

from django.shortcuts import render
from mainapp.models import ProductCategory

def products(request):
    title = 'Каталог'
    lname = 'products'
    links_menu = ProductCategory.objects.all()
    context = {
        'title': title,
        'links_menu': links_menu,
        'lname': lname,
    }

    return render(request, 'mainapp/products.html', context)

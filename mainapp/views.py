from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from mainapp.models import ProductCategory, Product


def products(request, pk=None):
    title = 'Каталог'
    lname = 'products'
    links_menu = ProductCategory.objects.all()
    products = Product.objects.all().order_by('price')

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
            basket = Basket.objects.filter(user=request.user)
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')
            basket = Basket.objects.filter(user=request.user)

        context = {
            'title': title,
            'links_menu': links_menu,
            'lname': lname,
            'products': products,
            'category': category,
            'basket': basket,
            'basket_count': basket.count(),
        }

        return render(request, 'mainapp/products.html', context)

    same_products = Product.objects.all()[1:2]
    context = {
        'title': title,
        'links_menu': links_menu,
        'lname': lname,
        'same_products': same_products,
        'products': products,
    }

    return render(request, 'mainapp/products.html', context)

from django.shortcuts import render

from basketapp.models import Basket
from mainapp.models import Product, Location

def main(request):
    title = 'Магазин'
    lname = 'main'
    basket = []
    products = Product.objects.all()[:4]

    context = {
    'title' : title,
    'lname': lname,
    'products': products,
    }

    return render(request, 'geekshop/index.html', context)


def contacts(request):
    title = 'Контакты'
    lname = 'contacts'
    locations = Location.objects.all()[:3]
    basket = Basket.objects.filter(user=request.user)

    context = {
    'title' : title,
    'lname' : lname,
    'locations' : locations,
    'basket_count': basket.count(),
    }

    return render(request, 'geekshop/contact.html', context)

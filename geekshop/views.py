from django.shortcuts import render

from basketapp.models import Basket
from mainapp.models import Product, Location

def main(request):
    title = 'Магазин'
    lname = 'main'
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    products = Product.objects.all()[:4]

    context = {
    'title' : title,
    'lname': lname,
    'products': products,
    'basket': basket,
    'basket_count': basket,
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
    'basket' : basket,
    'basket_count': basket.count(),
    }

    return render(request, 'geekshop/contact.html', context)

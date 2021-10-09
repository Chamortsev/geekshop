from django.shortcuts import render
from mainapp.models import Product, Locations

def main(request):
    title = 'Магазин'
    lname = 'main'
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
    locations = Locations.objects.all()[:3]

    context = {
    'title' : title,
    'lname' : lname,
    'locations' : locations,
    }

    return render(request, 'geekshop/contact.html', context)

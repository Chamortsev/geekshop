from django.shortcuts import render


def products(request):
    title = 'Каталог'
    lname = 'products'
    links_menu = [
        {'href': 'products','name':'все'},
        {'href': 'products_home','name':'дом'},
        {'href': 'products_office','name':'офис'},
        {'href': 'products_modern','name':'модерн'},
        {'href': 'products_classic','name':'классика'},
    ]
    context = {
        'title': title,
        'links_menu': links_menu,
        'lname': lname,
    }

    return render(request, 'mainapp/products.html', context)

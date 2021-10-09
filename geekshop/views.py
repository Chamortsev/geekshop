from django.shortcuts import render


def main(request):
    title = 'Магазин'
    lname = 'main'
    context = {
    'title' : title,
    'lname': lname,
    }

    return render(request, 'geekshop/index.html', context)


def contacts(request):
    title = 'Контакты'
    lname = 'contacts'
    context = {
    'title' : title,
    'lname' : lname,
    }

    return render(request, 'geekshop/contact.html', context)

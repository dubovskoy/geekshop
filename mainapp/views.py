from django.shortcuts import render

# Create your views here.
from mainapp.models import Product, ProductCategory


def main(request):
    title = 'главная'
    products = Product.objects.all()[:4]
    content = {
        'title': title, 'products': products
    }
    return render(request, 'mainapp/index.html', content)


def products(request, pk=None):
    same_products = Product.objects.all()[:4]
    links_menu = ProductCategory.objects.all()
    content = {
        'title': 'Продукты',
        'links_menu': links_menu,
        'same_products': same_products,
    }
    return render(request, 'mainapp/products.html', content)


def contact(request):
    contacts = [
        {'city': 'Moscow', 'phone': '+7 999 888 77 66', 'email': 'info1@geekshop.ru', 'address': 'за МКАД'},
        {'city': 'Калуга', 'phone': '+7 666 555 44 33', 'email': 'info2@geekshop.ru', 'address': 'МКАД'},
        {'city': 'Хабаровск', 'phone': '+7 333 222 11 00', 'email': 'info3@geekshop.ru', 'address': 'в пределах МКАД'},
    ]
    content = {
        'title': 'Контакты',
        'contacts': contacts,
    }
    return render(request, 'mainapp/contact.html', content)

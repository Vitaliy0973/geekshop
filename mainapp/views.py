from django.shortcuts import render
import json

# Create your views here.


def index(request):

    content = {
        'title': 'geekshop',
    }

    return render(request, 'mainapp/index.html', content)


def products(request):

    categories = [
        {'name': 'Новинки'},
        {'name': 'Одежда'},
        {'name': 'Обувь'},
        {'name': 'Аксессуары'},
        {'name': 'Подарки'},
    ]

    with open('mainapp/templates/mainapp/fixtures/product_cards.json', 'r', encoding='utf-8') as file:
        product_cards = json.load(file)

    content = {
        'title': 'geekshop - каталог',
        'categories': categories,
        'product_cards': product_cards,
    }

    return render(request, 'mainapp/products.html', content)

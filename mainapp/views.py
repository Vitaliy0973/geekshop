from django.shortcuts import render
from mainapp.models import ProductCategories, Product
import json
import os

# Create your views here.

MODULE_DIR = os.path.dirname(__file__)


def read_file(name):
    file_path = os.path.join(MODULE_DIR, name)
    return json.load(open(file_path, encoding='utf-8'))


def index(request):

    content = {
        'title': 'geekshop',
    }

    return render(request, 'mainapp/index.html', content)


def products(request):

    categories = ProductCategories.objects.all()
    products = Product.objects.all()

    # categories = read_file('fixtures/categories.json')
    # products = read_file('fixtures/products.json')

    content = {
        'title': 'geekshop - каталог',
        'categories': categories,
        'products': products,
    }

    return render(request, 'mainapp/products.html', content)

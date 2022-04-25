from pyexpat import model
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import DetailView, ListView
from adminapp.mixin import BaseClassContextMixin
from mainapp.models import ProductCategories, Product
import json
import os

# Create your views here.

MODULE_DIR = os.path.dirname(__file__)


# def read_file(name):
#     file_path = os.path.join(MODULE_DIR, name)
#     return json.load(open(file_path, encoding='utf-8'))


def index(request):

    content = {
        'title': 'geekshop',
    }

    return render(request, 'mainapp/index.html', content)


def products(request, id_category=None, page=1):

    if id_category:
        products = Product.objects.filter(id=id_category)
    else:
        products = Product.objects.all()

    pagination = Paginator(products, per_page=2)

    try:
        product_pagination = pagination.page(page)
    except PageNotAnInteger:
        # Если мы не понимаем на какой странице находимся, нас возвращает на первую
        product_pagination = pagination.page(1)
    except EmptyPage:
        # Если мы не знаем какое кол-во страниц
        product_pagination = pagination.page(pagination.num_pages)

    # categories = read_file('fixtures/categories.json')
    # products = read_file('fixtures/products.json')

    content = {
        'title': 'geekshop - каталог',
        'categories': ProductCategories.objects.all(),
        'products': product_pagination,
    }

    return render(request, 'mainapp/products.html', content)


class ProductDetail(DetailView):
    # Специальный класс DetailView помогает нам детализировать данные

    model = Product
    template_name = 'mainapp/detail.html'

# from importlib.resources import path
from django.urls import path
from mainapp.views import ProductDetail, products


app_name = 'mainapp'

urlpatterns = [
    path('', products, name='products'),
    path('category/<int:id_category>/', products, name='category'),
    path('page/<int:page>', products, name='page'),
    path('detail/<int:pk>', ProductDetail.as_view(), name='detail'),
]

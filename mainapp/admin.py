from django.contrib import admin

# Register your models here.
from mainapp.models import Product, ProductCategories


admin.site.register(ProductCategories)


@admin.register(Product)
class Product(admin.ModelAdmin):
    # Включение отображения категорий в списке продуктов
    list_display = ('name', 'price', 'quantity', 'category')
    # Включение отображения категорий на странице продукта. Добавленые в кортеж категории начинают отображаться на одной строке.
    fields = ('name', 'image', 'descriptions',
              ('price', 'quantity'), 'category')
    # Запрет на изменение
    readonly_fields = ('descriptions',)
    # Включение сортировки
    ordering = ('name', 'price')
    # Включение поиска
    search_fields = ('name',)

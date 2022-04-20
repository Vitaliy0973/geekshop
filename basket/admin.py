from django.contrib import admin

from basket.models import Basket

# Register your models here.

admin.site.register(Basket)


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'create_timestamp', 'update_timestamp')
    readonly_fields = ('create_timestamp', 'update_timestamp')
    extra = 3

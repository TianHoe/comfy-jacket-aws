from django.contrib import admin
from . models import Bouquet
from . models import Category
# Register your models here.

class BouquetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'stock', 'time_created')
    list_display_links = ('id', 'name')
    list_filter = ('price', 'time_created')
    search_fields = ('name', 'price')
    ordering = ('name',)

admin.site.register(Bouquet, BouquetAdmin)
admin.site.register(Category)
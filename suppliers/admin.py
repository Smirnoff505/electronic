from django.contrib import admin

from suppliers.models import Supplier, Product


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):

    list_display = ('name', 'level', 'email', 'country', 'debt', 'creating_data', 'parent')
    list_display_links = ['name', 'parent']
    search_fields = ('city',)
    actions = ['clear_debt']

    def clear_debt(self, request, queryset):
        queryset.update(debt=0)

    clear_debt.short_description = "Очистить задолженность"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date', 'supplier')

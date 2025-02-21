from django.contrib import admin
from django.utils.html import format_html
from .models import Factory, RetailNetwork, Entrepreneur
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date')

admin.site.register(Product, ProductAdmin)


class BaseNetworkAdmin(admin.ModelAdmin):
    list_filter = ('city',)

    def supplier_link(self, obj):
        if obj.supplier:
            return format_html('<a href="/admin/retailnet/retailnetwork/{}/change/">{}</a>', obj.supplier.id, obj.supplier)
        return "Нет поставщика"

    supplier_link.short_description = 'Поставщик'


class RetailNetworkAdmin(BaseNetworkAdmin):
    list_display = ('name', 'supplier_link', 'city', 'debt_to_supplier')
    actions = ['clear_debt']

    def clear_debt(self, request, queryset):
        rows_updated = queryset.update(debt_to_supplier=0)
        if rows_updated == 1:
            message_bit = "1 запись была обновлена."
        else:
            message_bit = f"{rows_updated} записей были обновлены."
        self.message_user(request, f"Успешно очищены задолженности: {message_bit}")

admin.site.register(RetailNetwork, RetailNetworkAdmin)


class EntrepreneurAdmin(BaseNetworkAdmin):
    list_display = ('name', 'supplier_link', 'city', 'debt_to_supplier')
    actions = ['clear_debt']

    def clear_debt(self, request, queryset):
        rows_updated = queryset.update(debt_to_supplier=0)
        if rows_updated == 1:
            message_bit = "1 запись была обновлена."
        else:
            message_bit = f"{rows_updated} записей были обновлены."
        self.message_user(request, f"Успешно очищены задолженности: {message_bit}")

admin.site.register(Entrepreneur, EntrepreneurAdmin)


class FactoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'city', 'debt_to_supplier')
    list_filter = ('city',)

admin.site.register(Factory, FactoryAdmin)
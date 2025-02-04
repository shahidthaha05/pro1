

# Register your models here.
from django.contrib import admin
from .models import Product,Size

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'size')


try:
    admin.site.unregister(Product)
except admin.sites.NotRegistered:
    pass  # Ignore if not registered

class ProductAdmin(admin.ModelAdmin):
    list_display = ('pro_id', 'name', 'display_sizes', 'base_price', 'offer_price', 'quantity')

    def display_sizes(self, obj):
        return ", ".join([size.name for size in obj.sizes.all()])  # Show sizes as comma-separated values

    display_sizes.short_description = 'Sizes'  # Rename column header

admin.site.register(Product, ProductAdmin)
admin.site.register(Size) 

from django.contrib import admin
from .models import Product, Size

# Unregister Product if already registered to prevent errors
if admin.site.is_registered(Product):
    admin.site.unregister(Product)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("pro_id", "name", "display_sizes", "base_price", "offer_price", "quantity")
    search_fields = ("name",)
    list_editable = ("quantity",)  # Allow stock editing directly

    def display_sizes(self, obj):
        return ", ".join([size.name for size in obj.sizes.all()])  # Show sizes as comma-separated values

    display_sizes.short_description = 'Sizes'  # Rename column header

# Register Size model
@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ("name",)

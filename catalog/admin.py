from django.contrib import admin
from catalog.models import Product, Category, Version


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name","price", "category")
    list_filter = ("category",)
    search_fields = ("name",)



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name","description")


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ("product", "version_number", "version_name", "sign")

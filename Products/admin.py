from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Product, ProductSpecification, ProductType, ProductSpecificationValue, Category, Users, Order_Item, Order


class ProductSpecificationInline(admin.TabularInline):
    model = ProductSpecification


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    inlines = [
        ProductSpecificationInline
    ]


admin.site.register(Category, MPTTModelAdmin)


class ProductSpecificationValueInline(admin.TabularInline):
    model = ProductSpecificationValue


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductSpecificationValueInline
    ]


class Order_ItemInline(admin.TabularInline):
    model = Order_Item


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [
        Order_ItemInline
    ]


admin.site.register(Order_Item)

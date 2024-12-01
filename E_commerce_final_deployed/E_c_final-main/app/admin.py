from django.contrib import admin
from .models import (
    Customer,
    Product,
    Cart,
    OrderPlaced
)

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'locality', 'city', 'zipcode', 'get_state']

    def get_state(self, obj):
        return obj.state  # Replace 'state' with the actual attribute name in your Customer model

    get_state.short_description = 'state'
    
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'selling_price', 'get_discounted_price', 'get_description', 'brand', 'category', 'product_image']

    def get_discounted_price(self, obj):
        return obj.discounted_price  # Replace 'discounted_price' with the actual attribute name in your Product model

    def get_description(self, obj):
        return obj.description  # Replace 'description' with the actual attribute name in your Product model

    get_discounted_price.short_description = 'discounted_price'
    get_description.short_description = 'description'

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','quantity']

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'customer', 'product', 'quantity', 'get_ordered_state', 'get_status']

    def get_ordered_state(self, obj):
        return obj.ordered_date 

    def get_status(self, obj):
        return obj.status  
    
    get_ordered_state.short_description = 'ordered_date'
    get_status.short_description = 'status'
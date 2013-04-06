from django.contrib import admin
from .models import Item, OrderItem, Order

class OrderItemInline(admin.TabularInline):
    model=OrderItem
    fk_name = 'order'
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = ('user', 'paid', 'created')
    list_filter = ('created', )
    chart_categories = []
    inlines = [OrderItemInline, ]

admin.site.register(Order, OrderAdmin)
admin.site.register(Item, admin.ModelAdmin)

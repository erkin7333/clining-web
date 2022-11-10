from django.contrib import admin
from .models import RoomCategory, ServiceType, Price, Orders



class RoomCategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'price'
    ]
    list_display_links = [
        'name'
    ]
    class Meta:
        model = RoomCategory

admin.site.register(RoomCategory, RoomCategoryAdmin)


class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = [
        'name'
    ]
    list_display_links = [
        'name'
    ]
    class Meta:
        model = ServiceType
admin.site.register(ServiceType, ServiceTypeAdmin)

class PriceAdmin(admin.ModelAdmin):
    list_display = [
        'services', 'price'
    ]
    list_display_links = [
        'services', 'price'
    ]
    class Meta:
        model = Price

admin.site.register(Price, PriceAdmin)


class OrdersAdmin(admin.ModelAdmin):
    list_display = [
        'roomname', 'roomprice', 'servicename', 'serviceprice'
    ]
    class Meta:
        model = Orders

admin.site.register(Orders, OrdersAdmin)

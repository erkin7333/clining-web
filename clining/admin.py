from django.contrib import admin
from .models import RoomCategory, ServiceType, Orders



class RoomCategoryAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name', 'price'
    ]
    list_display_links = [
        'name'
    ]
    class Meta:
        model = RoomCategory

admin.site.register(RoomCategory, RoomCategoryAdmin)


class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name', 'price'
    ]
    list_display_links = [
        'name'
    ]
    class Meta:
        model = ServiceType
admin.site.register(ServiceType, ServiceTypeAdmin)




class OrdersAdmin(admin.ModelAdmin):
    list_display = [
        'roomname', 'roomprice', 'servicename', 'serviceprice'
    ]
    class Meta:
        model = Orders

admin.site.register(Orders, OrdersAdmin)

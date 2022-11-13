from django.contrib import admin
from .models import *


admin.site.register(SubServices)

admin.site.register(CardServices)



class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = [
        'name','price' 
    ]
    list_display_links = [
        'name','price' 
    ]
    class Meta:
        model = ServiceType
admin.site.register(ServiceType, ServiceTypeAdmin)




# class OrdersAdmin(admin.ModelAdmin):
#     list_display = [
#         'room', 'total'
#     ]
#     class Meta:
#         model = Orders

# admin.site.register(Orders, OrdersAdmin)


admin.site.register(Orders)



### inline  formsets


class Item(admin.ModelAdmin):
    list_display = ('name','price','service_count')
    list_filter = ('name',)

    def service_count(self, obj):
        return len(obj.service.all())
    service_count.short_description = 'Service'

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).prefetch_related('service')

admin.site.register(RoomCategory, Item)




admin.site.register(Settings)

class CaruselImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image']
    list_display_links = ['id', 'name']
    class Meta:
        model = CaruselImage
admin.site.register(CaruselImage, CaruselImageAdmin)

class CaruselDetailAdmin(admin.ModelAdmin):
    list_display = ['id', 'carusel', 'title', 'description']
    list_display_links = ['id', 'title']
    class Meta:
        model = CaruselDetail
admin.site.register(CaruselDetail, CaruselDetailAdmin)
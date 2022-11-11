from django.contrib import admin
from .models import (RoomCategory, ServiceType, Orders, OrderCategory, OrderForm,
                     CaruselImage, CaruselDetail, Settings, GallaryCategory,
                     GallaryDetail, CardServices, SubServices, ContactForm)

class OrderCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['name']
    class Meta:
        model = OrderCategory
admin.site.register(OrderCategory, OrderCategoryAdmin)


class OrderFormAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name', 'email', 'phone_number', 'ordercategory'
    ]
    list_display_links = ['name', 'email']
    class Meta:
        model = OrderForm
admin.site.register(OrderForm, OrderFormAdmin)


class CaruselImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image']
    list_display_links = ['id', 'name']
    class Meta:
        model = CaruselImage
admin.site.register(CaruselImage, CaruselImageAdmin)

class CaruselDetailAdmin(admin.ModelAdmin):
    list_display = ['id', 'caruselimage', 'title', 'description']
    list_display_links = ['id', 'title']
    class Meta:
        model = CaruselDetail
admin.site.register(CaruselDetail, CaruselDetailAdmin)


class SettingsAdmin(admin.ModelAdmin):
    list_display = ['id', 'key', 'value']
    list_display_links = ['id', 'key']
    class Meta:
        model = Settings
admin.site.register(Settings, SettingsAdmin)

class GallaryCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image']
    list_display_links = ['id', 'name']
    class Meta:
        model = GallaryCategory
admin.site.register(GallaryCategory, GallaryCategoryAdmin)


class GallaryDetailAdmin(admin.ModelAdmin):
    list_display = ['id', 'gallarycategory', 'title', 'description']
    list_display_links = ['id', 'gallarycategory', 'title']
    class Meta:
        model = GallaryDetail
admin.site.register(GallaryDetail, GallaryDetailAdmin)


class CardServicesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'detail', 'is_color_activ']
    list_display_links = ['id', 'name', 'price']
    class Meta:
        model = CardServices
admin.site.register(CardServices, CardServicesAdmin)


class SubServicesAdmin(admin.ModelAdmin):
    list_display = ['id', 'service', 'name', 'is_exist']
    list_display_links = ['id', 'service', 'name']
    class Meta:
        model = SubServices
admin.site.register(SubServices, SubServicesAdmin)

class ContactFormAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone_number']
    list_display_links = ['id', 'name', 'email']
    class Mate:
        model = ContactForm
admin.site.register(ContactForm, ContactFormAdmin)


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

from django.urls import path
from .views import *

app_name = "myprint"

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('product-detail/<int:pk>/', product_detail, name='product_detail'),
    path('gallary/', gallary, name='gallary'),
    path('gallary/<int:pk>/', gallary_details, name='gallary-detail'),
    path('guests/', guests, name='guests'),
    path('services/', services, name='services'),
    path('product_detail/', product_detail, name='product_detail'),
]

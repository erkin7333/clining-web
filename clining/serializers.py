from rest_framework import serializers
from .models import Price, RoomCategory, ServiceType




class ServicePriceSerializers(serializers.ModelSerializer):
    name = ServiceType.objects.all()
    class Meta:
        model = Price
        fields = ('id', 'name', 'price')


class RoomCategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = RoomCategory
        fields = ('id', 'name', 'price')
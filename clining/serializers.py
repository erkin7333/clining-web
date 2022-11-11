from rest_framework import serializers
from .models import Price, RoomCategory, ServiceType


class ServiceSerializer(serializers.Serializer):
    class Meta:
        model = ServiceType
        fields = ('id', 'name')

class ServicePriceSerializers(serializers.ModelSerializer):
    name = ServiceSerializer(many=True, read_only=True)
    class Meta:
        model = Price
        fields = ('id', 'name', 'price')


class RoomCategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = RoomCategory
        fields = ('id', 'name', 'price')
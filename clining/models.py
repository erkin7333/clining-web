from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.






class RoomCategory(models.Model):
    name = models.CharField(_('name'), max_length=65)
    price = models.IntegerField(_('number'))
    creat_add = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Room")
        verbose_name_plural = _("Rooms")


class ServiceType(models.Model):
    room = models.ForeignKey(RoomCategory, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(_('name'), max_length=65)
    price = models.IntegerField(_('number'))
    is_active = models.BooleanField(_('is_active'), blank=True, null=True)
    creat_add = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

    

    class Meta:
        verbose_name = _("Service")
        verbose_name_plural = _("Service")
    

class Double(models.Model):
    name = models.CharField(max_length=65)
    price = models.IntegerField()
    creat_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
        
    @property
    def count(self):
        total = self.room.price + self.price
        return total

    @property
    def single_price(self):
        single = self.room.price
        return single


    class Meta:
        verbose_name = _("Birlashma Zaraz")
        verbose_name_plural = _("Birlashma Zakazlar")
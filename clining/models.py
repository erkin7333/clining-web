from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.



class RoomCategory(models.Model):
    name = models.CharField(_('name'), max_length=65)
    number = models.IntegerField(_('number'))
    creat_add = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Room")
        verbose_name_plural = _("Rooms")


class ServiceType(models.Model):
    name = models.CharField(_('name'), max_length=65)
    price = models.IntegerField(_('number'))
    is_active = models.BooleanField(_('is_active'))
    creat_add = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Service")
        verbose_name_plural = _("Service")
        



from django.db import models
from django.utils.translation import gettext_lazy as _


# Hope Page

class OrderForm(models.Model):
    name = models.CharField(_(name), max_length=50)
    email = models.EmailField(_(), max_length=60)
    phone_number = models.IntegerField(_(), )
    description = models.TextField(_(), blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Buyurtma shakli"

# Home Image Carusel Category
class CaruselImage(models.Model):
    name = models.CharField(_(name), max_length=50)
    image = models.ImageField(_(), upload_to='media/carusel')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Karusel"


#  Home Carusel Detaile
class CaruselDetail(models.Model):
    carusel = models.ForeignKey(CaruselImage, on_delete=models.CASCADE)
    title = models.CharField(_(), max_length=255)
    description = models.TextField(_())
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Karusel Tavsilot"

#  Doimiy Sozlamalar
class Settings(models.Model):
    key = models.CharField(_(), max_length=50)
    value = models.CharField(_(), max_length=500)
    def __str__(self):
        return self.key
    class Meta:
        verbose_name = "Sozlamalar"

# Gallereya uchun Kategoriya
class GallaryCategory(models.Model):
    name = models.CharField(_(name), max_length=50)
    image = models.ImageField(_(), upload_to="media/gallary")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Gallereya turlari"

# Gallereya Tavsiloti
class GallaryDetail(models.Model):
    gallary = models.ForeignKey(GallaryCategory, on_delete=models.CASCADE)
    title = models.CharField(_(), max_length=200)
    description = models.TextField(_())
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Gallereya tavsilotlari'

#  Xizmatlar
class CardServices(models.Model):
    name = models.CharField(_(name), max_length=100)
    price = models.PositiveIntegerField(_(), )
    detail = models.TextField(_(), )
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Xizmatlar'


#
class SubServices(models.Model):
    service = models.ForeignKey(CardServices, on_delete=models.CASCADE)
    name = models.CharField(_(name), max_length=50)
    is_exist = models.BooleanField(_(), default=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Sub xizmatlar"

class ContactForm(models.Model):
    name = models.CharField(_('name'), max_length=50)
    email = models.EmailField(_('email'), max_length=60)
    phone_number = models.IntegerField(_('phone_number'), )
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Kontakt"

class ServiceType(models.Model):
    name = models.CharField(_('name'), max_length=120, blank=True, null=True)
    price = models.PositiveIntegerField(_('price'), )
    def __str__(self):
        return f"{self.name} {str(self.price)}"
    class Meta:
        verbose_name = "Xizmat kursatish turlari"



class RoomCategory(models.Model):
    name = models.CharField(_('name'), max_length=100, blank=True, null=True)
    price = models.PositiveIntegerField(_('price'), )
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Xona turlari"


class Orders(models.Model):
    roomname = models.CharField(_('roomname'), max_length=100)
    roomprice = models.PositiveIntegerField(_('roomprice'), )
    servicename = models.CharField(_('servicename'), max_length=100)
    serviceprice = models.PositiveIntegerField(_('serviceprice'), )
    def __str__(self):
        return f"{str(self.roomname)} {str(self.roomprice)}"
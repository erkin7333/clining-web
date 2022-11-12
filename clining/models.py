from django.db import models
from django.utils.translation import gettext_lazy as _


# Hope Page
class OrderCategory(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Buyurtma turlari"
class OrderForm(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    ordercategory = models.ForeignKey(OrderCategory, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Zakazlar"

# Home Image Carusel Category
class CaruselImage(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/carusel')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Karusel"

#  Home Carusel Detaile
class CaruselDetail(models.Model):
    caruselimage = models.ForeignKey(CaruselImage, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Karusel Tavsilot"

#  Doimiy Sozlamalar
class Settings(models.Model):
    key = models.CharField(max_length=50)
    value = models.CharField(max_length=500)
    def __str__(self):
        return self.key
    class Meta:
        verbose_name = "Sozlamalar"

# Gallereya uchun Kategoriya
class GallaryCategory(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="media/gallary")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Gallereya turlari"

# Gallereya Tavsiloti
class GallaryDetail(models.Model):
    gallarycategory = models.ForeignKey(GallaryCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Gallereya tavsilotlari'

#  Xizmatlar
class SubServices(models.Model):
    name = models.CharField(_('name'), max_length=50)
    # detail = models.CharField(_('detail'), max_length=65)
    is_exist = models.BooleanField(_('is_exist'), default=True)
    def __str__(self):
        return f"{self.name} | {self.is_exist}"

    class Meta:
        verbose_name = "Sub Card Xizmatlar"


class CardServices(models.Model):
    service = models.ManyToManyField("SubServices")
    name = models.CharField(_('name'), max_length=100)
    price = models.PositiveIntegerField(_('price'), )
    detail = models.TextField(_('detail'), )
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Card Xizmatlar'

class ContactForm(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Kontakt"

class ServiceType(models.Model):
    name = models.CharField(max_length=120, blank=True, null=True)
    price = models.PositiveIntegerField()
    def __str__(self):
        return f"{self.name} {str(self.price)}"
    class Meta:
        verbose_name = "Xizmat kursatish turlari"



class RoomCategory(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    price = models.PositiveIntegerField()
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Xona turlari"


class Orders(models.Model):
    roomname = models.CharField(max_length=100)
    roomprice = models.PositiveIntegerField()
    servicename = models.CharField(max_length=100)
    serviceprice = models.PositiveIntegerField()
    def __str__(self):
        return f"{str(self.roomname)} {str(self.roomprice)}"
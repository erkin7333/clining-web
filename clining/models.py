from django.db import models



# Hope Page

class OrderForm(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=60)
    phone_number = models.IntegerField(max_length=14)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Buyurtma shakli"

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
    title = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Gallereya tavsilotlari'

#  Xizmatlar
class CardServices(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    detail = models.CharField()
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Xizmatlar'


#
class SubServices(models.Model):
    service = models.ForeignKey(CardServices, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    is_exist = models.BooleanField(default=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Sub xizmatlar"

class ContactForm(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=60)
    phone_number = models.IntegerField(max_length=14)
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
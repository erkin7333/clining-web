from django.db import models






class ServiceType(models.Model):
    name = models.CharField(max_length=120, blank=True, null=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Xizmat kursatish turlari"


class Price(models.Model):
    services = models.ForeignKey(ServiceType, on_delete=models.CASCADE, blank=True, null=True)
    price = models.PositiveIntegerField()
    def __str__(self):
        return f"{self.services} {str(self.price)}"
    class Meta:
        verbose_name = "Narxlar"

class RoomCategory(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    price = models.PositiveIntegerField()
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Xona turlari"


class Orders(models.Model):
    nameroom = models.CharField(max_length=255)
    nameservice = models.CharField(max_length=255)
    # priceroom = models.PositiveIntegerField()
    # priceservice = models.PositiveIntegerField()
    def __str__(self):
        return f"{self.nameservice} {self.nameservice}"
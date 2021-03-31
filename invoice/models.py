from typing import Callable
from django.db import models
from django.contrib.postgres.fields import JSONField
from django.db.models.deletion import CASCADE
from django.db.models.lookups import In


class City(models.Model):
    city = models.CharField(verbose_name="city", max_length=128)

    def __str__(self):
        return self.city


class Street(models.Model):
    street = models.CharField(verbose_name="street", max_length=128)

    def __str__(self):
        return self.street


class UK(models.Model):
    name = models.CharField(verbose_name="services", max_length=128)
    requisites = models.TextField(verbose_name="requisites")
    web_addr = models.CharField(verbose_name="services", max_length=128)

    def __str__(self):
        return self.name


class House(models.Model):
    number = models.PositiveIntegerField(verbose_name="number")
    add_number = models.PositiveIntegerField(verbose_name="number")
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    street = models.ForeignKey(Street, on_delete=models.CASCADE)
    sq_home = models.DecimalField(verbose_name="sq_home", max_digits=5, decimal_places=2)
    uk = models.ForeignKey(UK, on_delete=CASCADE)


class Appartament(models.Model):
    house = models.ForeignKey(House, on_delete=CASCADE)
    number = models.PositiveIntegerField(verbose_name="number")
    add_number = models.PositiveIntegerField(verbose_name="add_number")
    sq_appart = models.DecimalField(verbose_name="sq_appart", max_digits=5, decimal_places=2)
    num_owner = models.PositiveIntegerField(verbose_name="num_owner", default=0)


class Invoice(models.Model):
    period = models.DateField(verbose_name="period")
    data = JSONField(verbose_name="payer")


class User(models.Model):
    personal_account = models.CharField(verbose_name="personal_account", max_length=32, unique=True)
    name = models.CharField(verbose_name="user_name", max_length=128)
    appartament = models.ForeignKey(Appartament, on_delete=CASCADE, default=1)
    invoice = models.ForeignKey(Invoice, on_delete=CASCADE, default=1)


class ServicesCategory(models.Model):
    name = models.CharField(verbose_name="name_category", max_length=32)
    is_active = models.BooleanField(verbose_name="category_is_active", db_index=True, default=True)

    def __str__(self):
        return self.name


class Services(models.Model):
    category = models.ForeignKey(ServicesCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="services", max_length=256)
    unit = models.CharField(verbose_name="unit", max_length=32)
    standart = models.DecimalField(verbose_name="standart", max_digits=8, decimal_places=4, default=0)
    rate = models.DecimalField(verbose_name="rate", max_digits=7, decimal_places=3, default=0)
    factor = models.DecimalField(verbose_name="factor", max_digits=3, decimal_places=2, default=0)
    is_active = models.BooleanField(verbose_name="services_activ", db_index=True, default=True)

    def __str__(self):
        return f"{self.name} ({self.category.name})"

    @staticmethod
    def get_items():
        return Services.objects.filter(is_active=True).order_by("category", "name")
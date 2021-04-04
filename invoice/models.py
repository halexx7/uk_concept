from typing import Callable
from django.db import models
from django.contrib.postgres.fields import JSONField
from django.db.models.base import ModelState
from django.db.models.deletion import CASCADE
from django.db.models.lookups import In
from django.shortcuts import get_object_or_404


class ServicesCategory(models.Model):
    name = models.CharField(verbose_name="name_category", max_length=32)
    is_active = models.BooleanField(verbose_name="category_is_active", db_index=True, default=True)

    def __str__(self):
        return self.name


class Services(models.Model):
    category = models.ForeignKey(ServicesCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="services", max_length=256)
    unit = models.CharField(verbose_name="unit", max_length=32)
    standart = models.DecimalField(verbose_name="standart", max_digits=8, decimal_places=4, blank=True, default='')
    rate = models.DecimalField(verbose_name="rate", max_digits=7, decimal_places=3, default=0)
    factor = models.DecimalField(verbose_name="factor", max_digits=3, decimal_places=2, default=1)
    const = models.BooleanField(verbose_name="const_payments", db_index=True, default=True)
    is_active = models.BooleanField(verbose_name="services_activ", db_index=True, default=True)

    def __str__(self):
        return f"{self.name} ({self.category.name})"

    @staticmethod
    def get_const_payments(category):
        '''Возвращает константные статьи (которые зависят от тарифа)'''
        return Services.objects.filter(is_active=True, const=True, category=category)
    
    @staticmethod
    def get_varybose_payments(category):
        '''Возвращает переменные статьи (которые зависят подачи показаний)'''
        return Services.objects.filter(is_active=True, const=False, category=category)

    @staticmethod
    def get_items():
        return Services.objects.filter(is_active=True)


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
    category_rate = models.ForeignKey(ServicesCategory, on_delete=CASCADE)


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
    SINGLE = '1'
    TWO = '2'

    COUNTER_TYPE = (
        ( SINGLE, 'однотарифный'),
        ( TWO, 'двухтарифный' )
    )

    personal_account = models.CharField(verbose_name="personal_account", max_length=32, unique=True)
    name = models.CharField(verbose_name="user_name", max_length=128)
    appartament = models.ForeignKey(Appartament, on_delete=CASCADE, default=1)
    type_electric_meter = models.CharField(verbose_name="counter_type", max_length=1, choices=COUNTER_TYPE)
    invoice = models.ForeignKey(Invoice, on_delete=CASCADE, default=1)


# Текущие показания счетчиков
class CurrentCounter(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    col_water = models.PositiveIntegerField(verbose_name="col_water", null=True)
    hot_water = models.PositiveIntegerField(verbose_name="hot_water", null=True)
    electric_day = models.PositiveIntegerField(verbose_name="electric_day", null=True)
    electric_night = models.PositiveIntegerField(verbose_name="electric_day", null=True)
    electric_sungle = models.PositiveIntegerField(verbose_name="electric_single", null=True, blank=True, default='')

    @staticmethod
    def get_last_val(user):
        return CurrentCounter.objects.filter(user=user)


# История показания счетчиков
class HistoryCounter(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    period = models.DateField(verbose_name="period")
    hist_col_water = models.PositiveIntegerField(verbose_name="hist_col_water")
    hist_hot_water = models.PositiveIntegerField(verbose_name="hist_hot_water")
    hist_electric_day = models.PositiveIntegerField(verbose_name="hist_electric_day")
    hist_electric_night = models.PositiveIntegerField(verbose_name="hist_electric_night")

    class Meta:
        ordering = ("-period",)

    @staticmethod
    def get_last_val(user):
        return HistoryCounter.objects.filter(user=user)[0:1]


# Постоянные платежи (расчет по формуле = const*rate или = const)
class ConstantPayments(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    data = JSONField(verbose_name="data")

    @staticmethod
    def get_items(user):
        return ConstantPayments.objects.filter(user=user)


# Переменные платежи (зависящие от счетчиков)
class VariablePayments(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    period = models.DateField(verbose_name="period")
    service = models.CharField(verbose_name="name_service", max_length=128)
    unit = models.CharField(verbose_name="unit", max_length=32)
    standart = models.DecimalField(verbose_name="standart", max_digits=8, decimal_places=4, blank=True, default='125')
    rate = models.DecimalField(verbose_name="rate", max_digits=7, decimal_places=3, default=0)
    accured = models.DecimalField(verbose_name="rate", max_digits=7, decimal_places=3, default=0)
    volume = models.DecimalField(verbose_name="volume", max_digits=7, decimal_places=2, default=0)
    coefficient = models.DecimalField(verbose_name="factor", max_digits=3, decimal_places=2, default=1)
    subsidies = models.DecimalField(verbose_name="subsidies", max_digits=6, decimal_places=2, default=0)
    privileges = models.DecimalField(verbose_name="privileges", max_digits=6, decimal_places=2, default=0)
    recalculations = models.DecimalField(verbose_name="privileges", max_digits=6, decimal_places=2, default=0)
    total = models.DecimalField(verbose_name="privileges", max_digits=7, decimal_places=2, default=0)

    @staticmethod
    def get_items(user):
        return VariablePayments.objects.filter(user=user)


# Cубсидии
class Subsidies(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    service = models.ForeignKey(Services, on_delete=CASCADE)
    sale = models.PositiveIntegerField(verbose_name='Sale', default=0)


# Льготы
class Privileges(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    service = models.ForeignKey(Services, on_delete=CASCADE)
    sale = models.PositiveIntegerField(verbose_name='Sale', default=0)
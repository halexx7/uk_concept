from typing import Callable
from django.db import models
from django.contrib.postgres.fields import JSONField
from django.db.models.base import ModelState
from django.db.models.deletion import CASCADE
from django.db.models.lookups import In
from django.shortcuts import get_object_or_404
from django.utils import timezone


class ServicesCategory(models.Model):
    name = models.CharField(verbose_name="Название", max_length=32)

    is_active = models.BooleanField(verbose_name="Активная", db_index=True, default=True)
    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

    def __str__(self):
        return self.name


class Services(models.Model):
    category = models.ForeignKey(ServicesCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Услуга", max_length=256)
    unit = models.CharField(verbose_name="Единицы", max_length=32)
    standart = models.DecimalField(verbose_name="Норматив", max_digits=8, decimal_places=4, blank=True, default='')
    rate = models.DecimalField(verbose_name="Тариф", max_digits=7, decimal_places=3, default=0)
    factor = models.DecimalField(verbose_name="Коэфициент", max_digits=3, decimal_places=2, default=1)
    const = models.BooleanField(verbose_name="Константа", db_index=True, default=True)

    is_active = models.BooleanField(verbose_name="Активная", db_index=True, default=True)
    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

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
    city = models.CharField(verbose_name="Город", max_length=128)

    is_active = models.BooleanField(verbose_name="Активный", db_index=True, default=True)
    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

    def __str__(self):
        return self.city


class Street(models.Model):
    street = models.CharField(verbose_name="Улица", max_length=128)

    is_active = models.BooleanField(verbose_name="Активный", db_index=True, default=True)
    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

    def __str__(self):
        return self.street


class UK(models.Model):
    name = models.CharField(verbose_name="Название", max_length=128)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    street = models.ForeignKey(Street, on_delete=models.CASCADE)
    num_building = models.PositiveIntegerField(verbose_name="Номер здания")
    phone = models.CharField(verbose_name="Телефон", max_length=20)
    email = models.CharField(verbose_name="e-mail", max_length=128)
    inn = models.CharField(verbose_name="ИНН", max_length=10)
    ps = models.CharField(verbose_name="Расчетный счет", max_length=20)
    bik = models.CharField(verbose_name="БИК", max_length=10)
    ks = models.CharField(verbose_name="Кор.счет", max_length=20)
    bank = models.CharField(verbose_name="Банк", max_length=128)

    web_addr = models.CharField(verbose_name="Сайт", max_length=128)

    is_active = models.BooleanField(verbose_name="Активный", db_index=True, default=True)
    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

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

    is_active = models.BooleanField(verbose_name="Активный", db_index=True, default=True)
    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)


class Appartament(models.Model):
    house = models.ForeignKey(House, on_delete=CASCADE)
    number = models.PositiveIntegerField(verbose_name="number")
    add_number = models.PositiveIntegerField(verbose_name="add_number")
    sq_appart = models.DecimalField(verbose_name="sq_appart", max_digits=5, decimal_places=2)
    num_owner = models.PositiveIntegerField(verbose_name="num_owner", default=0)

    is_active = models.BooleanField(verbose_name="Активный", db_index=True, default=True)
    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)


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

    is_active = models.BooleanField(verbose_name="Активный", db_index=True, default=True)
    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)


# Текущие показания счетчиков (индивидуальные)
class CurrentCounter(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    col_water = models.PositiveIntegerField(verbose_name="col_water", null=True)
    hot_water = models.PositiveIntegerField(verbose_name="hot_water", null=True)
    electric_day = models.PositiveIntegerField(verbose_name="electric_day", null=True)
    electric_night = models.PositiveIntegerField(verbose_name="electric_day", null=True)
    electric_sungle = models.PositiveIntegerField(verbose_name="electric_single", null=True, blank=True, default='')

    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

    @staticmethod
    def get_last_val(user):
        return CurrentCounter.objects.filter(user=user)


# История показания счетчиков (индивидуальные)
class HistoryCounter(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    period = models.DateField(verbose_name="period")
    hist_col_water = models.PositiveIntegerField(verbose_name="hist_col_water")
    hist_hot_water = models.PositiveIntegerField(verbose_name="hist_hot_water")
    hist_electric_day = models.PositiveIntegerField(verbose_name="hist_electric_day")
    hist_electric_night = models.PositiveIntegerField(verbose_name="hist_electric_night")

    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

    class Meta:
        ordering = ("-period",)

    @staticmethod
    def get_last_val(user):
        return HistoryCounter.objects.filter(user=user)[0:1]


# Постоянные платежи (расчет по формуле = const*rate или = const)
class ConstantPayments(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    data = JSONField(verbose_name="data")

    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

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

    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

    @staticmethod
    def get_items(user):
        return VariablePayments.objects.filter(user=user)


# Cубсидии
class Subsidies(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    service = models.ForeignKey(Services, on_delete=CASCADE)
    sale = models.PositiveIntegerField(verbose_name='Субсидии', default=0)

    is_active = models.BooleanField(verbose_name="Активный", db_index=True, default=True)
    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)


# Льготы
class Privileges(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    service = models.ForeignKey(Services, on_delete=CASCADE)
    sale = models.PositiveIntegerField(verbose_name='Льготы', default=0)

    is_active = models.BooleanField(verbose_name="Активный", db_index=True, default=True)
    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)


# Начисления (Текущие)
class Profit(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    period = models.DateField(verbose_name="Период")
    amount_profit = models.DecimalField(verbose_name="Сумма", max_digits=7, decimal_places=2)

    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

    class Meta:
        ordering = ("-period",)

    @staticmethod
    def get_last_val(user):
        return HistoryCounter.objects.filter(user=user)[0:1]


# Инфорамация по оплатам
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    period = models.DateField(verbose_name="Период")
    amount_profit = models.DecimalField(verbose_name="Сумма", max_digits=7, decimal_places=2)

    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

    class Meta:
        ordering = ("-period",)

    @staticmethod
    def get_last_val(user):
        return HistoryCounter.objects.filter(user=user)[0:1]
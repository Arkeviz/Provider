from django.db import models


class Price(models.Model):
    Date = models.CharField(max_length=45)
    Cost_per_minute = models.CharField(max_length=60)
    Cost_per_minute_from_8pm_to_2am = models.CharField(max_length=60)
    Cost_per_minute_from_2am_to_6am = models.CharField(max_length=60)
    objects = models.Manager()


class Operator(models.Model):
    Fullname = models.CharField(max_length=60)
    objects = models.Manager()


class Receipt(models.Model):
    Organization_name = models.CharField(max_length=60)
    Organization_address = models.CharField(max_length=60)
    Organization_phone_number = models.CharField(max_length=20)
    Number_of_minutes_of_session = models.CharField(max_length=60)
    Total_cost = models.CharField(max_length=60)
    Cost_per_minute = models.ForeignKey('Price', on_delete=models.CASCADE, null=True)
    Employee_ID = models.ForeignKey('Operator', on_delete=models.CASCADE, null=True)
    objects = models.Manager()


class Client(models.Model):
    IP = models.CharField(max_length=30)
    Date_of_start_of_session = models.CharField(max_length=30)
    Date_of_end_of_session = models.CharField(max_length=30)
    Shift_number = models.ForeignKey('Receipt', on_delete=models.CASCADE, null=True)
    Cost_per_minute = models.ForeignKey('Price', on_delete=models.CASCADE, null=True)
    Employee_ID = models.ForeignKey('Operator', on_delete=models.CASCADE, null=True)
    objects = models.Manager()

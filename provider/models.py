from django.db import models


class Price(models.Model):
    Date = models.DateField(null=True)
    Cost_per_minute = models.IntegerField(null=True)
    Cost_per_minute_from_8pm_to_2am = models.IntegerField(null=True)
    Cost_per_minute_from_2am_to_6am = models.IntegerField(null=True)
    objects = models.Manager()


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    Firstname = models.CharField(max_length=30)
    Lastname = models.CharField(max_length=30)
    Shift_number = models.IntegerField(null=True)
    Computer_IP = models.CharField(max_length=30)
    objects = models.Manager()


class Session(models.Model):
    Organization_name = models.CharField(max_length=60)
    Organization_address = models.CharField(max_length=60)
    Organization_phone_number = models.CharField(max_length=20)
    Date_of_start_of_session = models.DateTimeField(null=True)
    Date_of_end_of_session = models.DateTimeField(null=True)
    Number_of_minutes_of_session = models.IntegerField(null=True)
    Total_cost = models.IntegerField(null=True)
    Employee_ID = models.ForeignKey('User', on_delete=models.CASCADE, null=True)
    Cost_per_minute = models.ForeignKey('Price', on_delete=models.CASCADE, null=True)
    Receipt_id = models.IntegerField(null=True)
    objects = models.Manager()


class Receipt(models.Model):
    id = models.IntegerField(primary_key=True)
    Session_id = models.ForeignKey('Session', on_delete=models.CASCADE, null=True)
    objects = models.Manager()

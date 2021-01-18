from django.db import models


class Price(models.Model):
    Date = models.DateField()
    Cost_per_minute = models.IntegerField()
    Cost_per_minute_from_8pm_to_2am = models.IntegerField()
    Cost_per_minute_from_2am_to_6am = models.IntegerField()
    objects = models.Manager()


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    Fullname = models.CharField(max_length=60)
    Shift_number = models.IntegerField()
    Computer_IP = models.CharField(max_length=30)
    objects = models.Manager()


class Receipt(models.Model):
    Organization_name = models.CharField(max_length=60)
    Organization_address = models.CharField(max_length=60)
    Organization_phone_number = models.CharField(max_length=20)
    Number_of_minutes_of_session = models.IntegerField()
    Total_cost = models.IntegerField()
    Cost_per_minute = models.ForeignKey('Price', on_delete=models.CASCADE, null=True)
    Employee_ID = models.ForeignKey('User', on_delete=models.CASCADE, null=True)
    objects = models.Manager()


class Session(models.Model):
    Organization_name = models.CharField(max_length=60)
    Organization_address = models.CharField(max_length=60)
    Organization_phone_number = models.CharField(max_length=20)
    Date_of_start_of_session = models.DateTimeField()
    Date_of_end_of_session = models.DateTimeField()
    Number_of_minutes_of_session = models.IntegerField()
    Total_cost = models.IntegerField()
    Employee_ID = models.ForeignKey('User', on_delete=models.CASCADE, null=True)
    Cost_per_minute = models.ForeignKey('Price', on_delete=models.CASCADE, null=True)
    objects = models.Manager()

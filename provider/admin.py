from django.contrib import admin
from .models import Price, Operator, Receipt, Client


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('Date', 'Cost_per_minute', 'Cost_per_minute_from_8pm_to_2am', 'Cost_per_minute_from_2am_to_6am')


@admin.register(Operator)
class OperatorAdmin(admin.ModelAdmin):
    list_display = ('Fullname',)


@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('Organization_name', 'Organization_address', 'Organization_phone_number',
                    'Number_of_minutes_of_session', 'Total_cost', 'Cost_per_minute', 'Employee_ID')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('IP', 'Date_of_start_of_session', 'Date_of_end_of_session', 'Shift_number',
                    'Cost_per_minute', 'Employee_ID')


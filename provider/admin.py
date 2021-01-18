from django.contrib import admin
from .models import Price, User, Receipt, Session


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('Date', 'Cost_per_minute', 'Cost_per_minute_from_8pm_to_2am', 'Cost_per_minute_from_2am_to_6am')


@admin.register(User)
class OperatorAdmin(admin.ModelAdmin):
    list_display = ('id', 'Fullname', 'Shift_number', 'Computer_IP')


@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('Organization_name', 'Organization_address', 'Organization_phone_number',
                    'Number_of_minutes_of_session', 'Total_cost', 'Cost_per_minute', 'Employee_ID')


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('Organization_name', 'Organization_address', 'Organization_phone_number',
                    'Date_of_start_of_session', 'Date_of_end_of_session', 'Number_of_minutes_of_session', 'Total_cost',
                    'Employee_ID', 'Cost_per_minute')

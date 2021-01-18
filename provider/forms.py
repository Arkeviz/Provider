from django import forms


class AddPrice(forms.Form):
    Date = forms.DateField(label="Дата", widget=forms.DateInput(attrs={"class": "myfield"}))
    Cost_per_minute = forms.IntegerField(label="Стоимость одной минуты соединения",
                                         widget=forms.NumberInput(attrs={"class": "myfield"}))
    Cost_per_minute_from_8pm_to_2am = forms.IntegerField(label="Льготная стоимость с 20.00 до 2.00",
                                                         widget=forms.NumberInput(attrs={"class": "myfield"}))
    Cost_per_minute_from_2am_to_6am = forms.IntegerField(label="Льготная стоимость с 02.00 до 06.00",
                                                         widget=forms.NumberInput(attrs={"class": "myfield"}))


class AddUser(forms.Form):
    id = forms.IntegerField(label="ID сотрудника",
                            widget=forms.NumberInput(attrs={"class": "myfield"}))
    Fullname = forms.CharField(label="ФИО пользователя", widget=forms.TextInput(attrs={"class": "myfield"}))
    Shift_number = forms.IntegerField(label="Номер смены",
                                      widget=forms.NumberInput(attrs={"class": "myfield"}))
    Computer_IP = forms.CharField(label="IP компьютера", widget=forms.TextInput(attrs={"class": "myfield"}))


class AddReceipt(forms.Form):
    Organization_name = forms.CharField(label="Название организации",
                                        widget=forms.TextInput(attrs={"class": "myfield"}))
    Organization_address = forms.CharField(label="Номер организации",
                                           widget=forms.TextInput(attrs={"class": "myfield"}))
    Organization_phone_number = forms.CharField(label="Контактный номер организации",
                                                widget=forms.TextInput(attrs={"class": "myfield"}))
    Number_of_minutes_of_session = forms.IntegerField(label="Количество минут",
                                                      widget=forms.NumberInput(attrs={"class": "myfield"}))
    Total_cost = forms.IntegerField(label="Итоговая сумма", widget=forms.NumberInput(attrs={"class": "myfield"}))
    Cost_per_minute = forms.IntegerField(label="ID стоимости одной минуты соединения",
                                         widget=forms.NumberInput(attrs={"class": "myfield"}))
    Employee_ID = forms.IntegerField(label="Номер оператора", widget=forms.NumberInput(attrs={"class": "myfield"}))


class AddSession(forms.Form):
    Organization_name = forms.CharField(label="Название организации",
                                        widget=forms.TextInput(attrs={"class": "myfield"}))
    Organization_address = forms.CharField(label="Номер организации",
                                           widget=forms.TextInput(attrs={"class": "myfield"}))
    Organization_phone_number = forms.CharField(label="Контактный номер организации",
                                                widget=forms.TextInput(attrs={"class": "myfield"}))
    Date_of_start_of_session = forms.DateTimeField(label="время начала соединения",
                                                   widget=forms.DateTimeInput(attrs={"class": "myfield"}))
    Date_of_end_of_session = forms.DateTimeField(label="время окончания соединения",
                                                 widget=forms.DateTimeInput(attrs={"class": "myfield"}))
    Number_of_minutes_of_session = forms.IntegerField(label="Количество минут",
                                                      widget=forms.NumberInput(attrs={"class": "myfield"}))
    Total_cost = forms.IntegerField(label="Итоговая сумма", widget=forms.NumberInput(attrs={"class": "myfield"}))
    Employee_ID = forms.IntegerField(label="Номер оператора",
                                     widget=forms.NumberInput(attrs={"class": "myfield"}))
    Cost_per_minute = forms.CharField(label="ID стоимости одной минуты соединения",
                                      widget=forms.TextInput(attrs={"class": "myfield"}))

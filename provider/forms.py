from django import forms


class AddPrice(forms.Form):
    Date = forms.CharField(label="Дата", widget=forms.TextInput(attrs={"class": "myfield"}))
    Cost_per_minute = forms.CharField(label="Стоимость одной минуты соединения",
                                      widget=forms.TextInput(attrs={"class": "myfield"}))
    Cost_per_minute_from_8pm_to_2am = forms.CharField(label="Льготная стоимость с 20.00 до 2.00",
                                                      widget=forms.TextInput(attrs={"class": "myfield"}))
    Cost_per_minute_from_2am_to_6am = forms.CharField(label="Льготная стоимость с 02.00 до 06.00",
                                                      widget=forms.TextInput(attrs={"class": "myfield"}))


class AddOperator(forms.Form):
    Fullname = forms.CharField(label="ФИО оператора", widget=forms.TextInput(attrs={"class": "myfield"}))


class AddReceipt(forms.Form):
    Organization_name = forms.CharField(label="Название организации",
                                        widget=forms.TextInput(attrs={"class": "myfield"}))
    Organization_address = forms.CharField(label="Номер организации",
                                           widget=forms.TextInput(attrs={"class": "myfield"}))
    Organization_phone_number = forms.CharField(label="Контактный номер организации",
                                                widget=forms.TextInput(attrs={"class": "myfield"}))
    Number_of_minutes_of_session = forms.CharField(label="Количество минут",
                                                   widget=forms.TextInput(attrs={"class": "myfield"}))
    Total_cost = forms.CharField(label="Итоговая сумма", widget=forms.TextInput(attrs={"class": "myfield"}))
    Cost_per_minute = forms.CharField(label="ID стоимости одной минуты соединения",
                                      widget=forms.TextInput(attrs={"class": "myfield"}))
    Employee_ID = forms.CharField(label="Номер оператора", widget=forms.TextInput(attrs={"class": "myfield"}))


class AddClient(forms.Form):
    IP = forms.CharField(label="IP компьютера", widget=forms.TextInput(attrs={"class": "myfield"}))
    Date_of_start_of_session = forms.CharField(label="время начала соединения",
                                               widget=forms.TextInput(attrs={"class": "myfield"}))
    Date_of_end_of_session = forms.CharField(label="время окончания соединения",
                                             widget=forms.TextInput(attrs={"class": "myfield"}))
    Shift_number = forms.CharField(label="Номер смены", widget=forms.TextInput(attrs={"class": "myfield"}))
    Cost_per_minute = forms.CharField(label="ID стоимости одной минуты соединения",
                                      widget=forms.TextInput(attrs={"class": "myfield"}))
    Employee_ID = forms.CharField(label="Номер оператора",
                                  widget=forms.TextInput(attrs={"class": "myfield"}))

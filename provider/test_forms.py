from django.test import TestCase
from provider.forms import AddPrice, AddUser, AddReceipt, AddSession


class AddPriceFormTest(TestCase):

    def test_Date_label(self):
        form = AddPrice()
        self.assertTrue(form.fields['Date'].label is None or form.fields['Date'].label == 'Дата')

    def test_Cost_per_minute_label(self):
        form = AddPrice()
        self.assertTrue(form.fields['Cost_per_minute'].label is None
                        or
                        form.fields['Cost_per_minute'].label == 'Стоимость одной минуты соединения')

    def test_Cost_per_minute_from_8pm_to_2am_label(self):
        form = AddPrice()
        self.assertTrue(form.fields['Cost_per_minute_from_8pm_to_2am'].label is None
                        or
                        form.fields['Cost_per_minute_from_8pm_to_2am'].label == 'Льготная стоимость с 20.00 до 2.00')

    def test_Cost_per_minute_from_2am_to_6am_label(self):
        form = AddPrice()
        self.assertTrue(form.fields['Cost_per_minute_from_2am_to_6am'].label is None or form.fields[
            'Cost_per_minute_from_2am_to_6am'].label == 'Льготная стоимость с 02.00 до 06.00')

    def test_proverka(self):
        form = AddPrice(data={'Date': "2020-01-12", 'Cost_per_minute': 8, 'Cost_per_minute_from_8pm_to_2am': 6,
                              'Cost_per_minute_from_2am_to_6am': 4})
        self.assertTrue(form.is_valid())


class AddUserFormTest(TestCase):

    def test_id_label(self):
        form = AddUser()
        self.assertTrue(form.fields['id'].label is None or form.fields['id'].label == 'ID сотрудника')

    def test_Firstname_label(self):
        form = AddUser()
        self.assertTrue(form.fields['Firstname'].label is None or form.fields['Firstname'].label == 'Имя пользователя')

    def test_Lastname_label(self):
        form = AddUser()
        self.assertTrue(form.fields['Lastname'].label is None
                        or
                        form.fields['Lastname'].label == 'Фамилия пользователя')

    def test_Shift_number_label(self):
        form = AddUser()
        self.assertTrue(form.fields['Shift_number'].label is None or form.fields['Shift_number'].label == 'Номер смены')

    def test_Computer_IP_label(self):
        form = AddUser()
        self.assertTrue(form.fields['Computer_IP'].label is None or form.fields['Computer_IP'].label == 'IP компьютера')

    def test_proverka(self):
        form = AddUser(data={'id': 1, 'Firstname': "Михаил", 'Lastname': "Зубенко",
                             'Shift_number': "1", 'Computer_IP': "127.0.0.1"})
        self.assertTrue(form.is_valid())


class AddReceiptFormTest(TestCase):
    def test_id_label(self):
        form = AddReceipt()
        self.assertTrue(form.fields['id'].label is None or form.fields['id'].label == 'Номер квитанции')

    def test_Session_id_label(self):
        form = AddReceipt()
        self.assertTrue(form.fields['Session_id'].label is None or form.fields['Session_id'].label == 'Номер сеанса')

    def test_proverka(self):
        form = AddReceipt(
            data={'id': "1", 'Session_id': 1})
        self.assertTrue(form.is_valid())


class AddSessionFormTest(TestCase):
    def test_Organization_name_label(self):
        form = AddSession()
        self.assertTrue(form.fields['Organization_name'].label is None
                        or
                        form.fields['Organization_name'].label == 'Название организации')

    def test_Organization_address_label(self):
        form = AddSession()
        self.assertTrue(form.fields['Organization_address'].label is None
                        or
                        form.fields['Organization_address'].label == 'Адрес организации')

    def test_Organization_phone_number_label(self):
        form = AddSession()
        self.assertTrue(form.fields['Organization_phone_number'].label is None
                        or
                        form.fields['Organization_phone_number'].label == 'Контактный номер организации')

    def test_Date_of_start_of_session_label(self):
        form = AddSession()
        self.assertTrue(form.fields['Date_of_start_of_session'].label is None
                        or
                        form.fields['Date_of_start_of_session'].label == 'Время начала соединения')

    def test_Date_of_end_of_session_label(self):
        form = AddSession()
        self.assertTrue(form.fields['Date_of_end_of_session'].label is None
                        or
                        form.fields['Date_of_end_of_session'].label == 'Время окончания соединения')

    def test_Number_of_minutes_of_session_label(self):
        form = AddSession()
        self.assertTrue(form.fields['Number_of_minutes_of_session'].label is None
                        or
                        form.fields['Number_of_minutes_of_session'].label == 'Количество минут')

    def test_Total_cost_label(self):
        form = AddSession()
        self.assertTrue(form.fields['Total_cost'].label is None or form.fields['Total_cost'].label == 'Итоговая сумма')

    def test_Employee_ID_label(self):
        form = AddSession()
        self.assertTrue(
            form.fields['Employee_ID'].label is None or form.fields['Employee_ID'].label == 'Номер оператора')

    def test_Cost_per_minute_label(self):
        form = AddSession()
        self.assertTrue(form.fields['Cost_per_minute'].label is None
                        or
                        form.fields['Cost_per_minute'].label == 'ID стоимости одной минуты соединения')

    def test_Receipt_id_label(self):
        form = AddSession()
        self.assertTrue(
            form.fields['Receipt_id'].label is None or form.fields['Receipt_id'].label == 'Номер квитанции')

    def test_proverka(self):
        form = AddSession(
            data={'Organization_name': "АО МММ", 'Organization_address': "12357",
                  'Organization_phone_number': "749947", 'Date_of_start_of_session': "2020-12-25 14:00",
                  'Date_of_end_of_session': '2020-12-25 14:42', 'Number_of_minutes_of_session': 42,
                  'Total_cost': 336, 'Employee_ID': 1, 'Cost_per_minute': 1, 'Receipt_id': 1})
        self.assertTrue(form.is_valid())

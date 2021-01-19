from django.test import TestCase
from provider.models import Price, User, Receipt, Session


class PriceModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Price.objects.create(Date='2020-01-12', Cost_per_minute=8, Cost_per_minute_from_8pm_to_2am=6,
                             Cost_per_minute_from_2am_to_6am=4)

    def test_Date_label(self):
        price = Price.objects.get(id=1)
        field_label = price._meta.get_field('Date').verbose_name
        self.assertEquals(field_label, 'Date')

    def test_Cost_per_minute_label(self):
        price = Price.objects.get(id=1)
        field_label = price._meta.get_field('Cost_per_minute').verbose_name
        self.assertEquals(field_label, 'Cost per minute')

    def test_Cost_per_minute_from_8pm_to_2am_label(self):
        price = Price.objects.get(id=1)
        field_label = price._meta.get_field('Cost_per_minute_from_8pm_to_2am').verbose_name
        self.assertEquals(field_label, 'Cost per minute from 8pm to 2am')

    def test_Cost_per_minute_from_2am_to_6am_label(self):
        price = Price.objects.get(id=1)
        field_label = price._meta.get_field('Cost_per_minute_from_2am_to_6am').verbose_name
        self.assertEquals(field_label, 'Cost per minute from 2am to 6am')


class UserModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(id=1, Firstname='Михаил', Lastname='Зубенко', Shift_number=1, Computer_IP='127.0.0.1')

    def test_id_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('id').verbose_name
        self.assertEquals(field_label, 'id')

    def test_Firstname_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('Firstname').verbose_name
        self.assertEquals(field_label, 'Firstname')

    def test_Lastname_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('Lastname').verbose_name
        self.assertEquals(field_label, 'Lastname')

    def test_Shift_number_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('Shift_number').verbose_name
        self.assertEquals(field_label, 'Shift number')

    def test_Computer_IP_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('Computer_IP').verbose_name
        self.assertEquals(field_label, 'Computer IP')

    def test_Firstname_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('Firstname').max_length
        self.assertEquals(max_length, 30)

    def test_Lastname_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('Lastname').max_length
        self.assertEquals(max_length, 30)

    def test_Computer_IP_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('Computer_IP').max_length
        self.assertEquals(max_length, 30)


class ReceiptModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Receipt.objects.create(id=1)

    def test_id_label(self):
        receipt = Receipt.objects.get(id=1)
        field_label = receipt._meta.get_field('id').verbose_name
        self.assertEquals(field_label, 'id')


class SessionModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Session.objects.create(Organization_name='АО МММ', Organization_address='12357',
                               Organization_phone_number='749947', Number_of_minutes_of_session=42,
                               Total_cost=336, Receipt_id=1)

    def test_Organization_name_label(self):
        session = Session.objects.get(id=1)
        field_label = session._meta.get_field('Organization_name').verbose_name
        self.assertEquals(field_label, 'Organization name')

    def test_Organization_address_label(self):
        session = Session.objects.get(id=1)
        field_label = session._meta.get_field('Organization_address').verbose_name
        self.assertEquals(field_label, 'Organization address')

    def test_Organization_phone_number_label(self):
        session = Session.objects.get(id=1)
        field_label = session._meta.get_field('Organization_phone_number').verbose_name
        self.assertEquals(field_label, 'Organization phone number')

    def test_Number_of_minutes_of_session_label(self):
        session = Session.objects.get(id=1)
        field_label = session._meta.get_field('Number_of_minutes_of_session').verbose_name
        self.assertEquals(field_label, 'Number of minutes of session')

    def test_Total_cost_label(self):
        session = Session.objects.get(id=1)
        field_label = session._meta.get_field('Total_cost').verbose_name
        self.assertEquals(field_label, 'Total cost')

    def test_Employee_ID_label(self):
        session = Session.objects.get(id=1)
        field_label = session._meta.get_field('Employee_ID').verbose_name
        self.assertEquals(field_label, 'Employee ID')

    def test_Cost_per_minute_label(self):
        session = Session.objects.get(id=1)
        field_label = session._meta.get_field('Cost_per_minute').verbose_name
        self.assertEquals(field_label, 'Cost per minute')

    def test_Receipt_id_label(self):
        session = Session.objects.get(id=1)
        field_label = session._meta.get_field('Receipt_id').verbose_name
        self.assertEquals(field_label, 'Receipt id')

    def test_Organization_name_max_length(self):
        session = Session.objects.get(id=1)
        max_length = session._meta.get_field('Organization_name').max_length
        self.assertEquals(max_length, 60)

    def test_Organization_phone_number_max_length(self):
        session = Session.objects.get(id=1)
        max_length = session._meta.get_field('Organization_phone_number').max_length
        self.assertEquals(max_length, 20)





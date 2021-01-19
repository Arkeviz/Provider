from django.test import TestCase
from provider.models import Price, User, Receipt, Session
from django.urls import reverse


class PriceViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Price.objects.create(Date='2020-01-12', Cost_per_minute=8, Cost_per_minute_from_8pm_to_2am=6,
                             Cost_per_minute_from_2am_to_6am=4)

    def test_view_url_exists_at_desired_location(self):  # существование url по адресу
        resp = self.client.get('/Price/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):  # существование url по имени
        resp = self.client.get(reverse('Price'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):  # соответствие шаблону
        resp = self.client.get(reverse('Price'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'provider/Template_Price.html')


class UserViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(id=1, Firstname='Михаил', Lastname='Зубенко', Shift_number=1, Computer_IP='127.0.0.1')

    def test_view_url_exists_at_desired_location(self):  # существование url по адресу
        resp = self.client.get('/User/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):  # существование url по имени
        resp = self.client.get(reverse('User'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):  # соответствие шаблону
        resp = self.client.get(reverse('User'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'provider/Template_User.html')


class ReceiptViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Receipt.objects.create(id=1)

    def test_view_url_exists_at_desired_location(self):  # существование url по адресу
        resp = self.client.get('/Receipt/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):  # существование url по имени
        resp = self.client.get(reverse('Receipt'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):  # соответствие шаблону
        resp = self.client.get(reverse('Receipt'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'provider/Template_Receipt.html')


class SessionViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Session.objects.create(Organization_name='АО МММ', Organization_address='12357',
                               Organization_phone_number='749947', Number_of_minutes_of_session=42,
                               Total_cost=336, Receipt_id=1)

    def test_view_url_exists_at_desired_location(self):  # существование url по адресу
        resp = self.client.get('/Receipt/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):  # существование url по имени
        resp = self.client.get(reverse('Receipt'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):  # соответствие шаблону
        resp = self.client.get(reverse('Receipt'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'provider/Template_Receipt.html')


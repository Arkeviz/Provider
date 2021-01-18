from django.shortcuts import render
from .models import Price, User, Receipt, Session
from .forms import AddPrice, AddUser, AddReceipt, AddSession
from django.views import View
from django.http import HttpResponseRedirect


def great(request):
    return render(request, "great.html")


def index(request):
    return render(request, "index.html")


def index_price(request):
    form_add = AddPrice()
    data = Price.objects.all()
    return render(request, "provider/Template_Price.html", {"form": form_add, "data_show": data})


def index_user(request):
    form_ex = AddUser()
    data = User.objects.all()
    return render(request, "provider/Template_User.html", {"form": form_ex, "data_show": data})


def index_receipt(request):
    form_er = AddReceipt()
    data = Receipt.objects.all()
    return render(request, "provider/Template_Receipt.html", {"form": form_er, "data_show": data})


def index_session(request):
    form_ca = AddSession()
    data = Session.objects.all()
    return render(request, "provider/Template_Session.html", {"form": form_ca, "data_show": data})


# Определение view


class view_price(View):
    def add_price(request):
        if request.method == "POST":
            price = Price()
            price.Date = request.POST.get("Date")
            price.Cost_per_minute = request.POST.get("Cost_per_minute")
            price.Cost_per_minute_from_8pm_to_2am = request.POST.get("Cost_per_minute_from_8pm_to_2am")
            price.Cost_per_minute_from_2am_to_6am = request.POST.get("Cost_per_minute_from_2am_to_6am")
            price.save()
            return HttpResponseRedirect("/Price")

    def del_price(request):
        if request.method == "POST":
            q = request.POST.get("delname", "")
            que = Price.objects.get(id=q)
            que.delete()
            return HttpResponseRedirect("/Price")

    def update_price(request):
        if request.method == "POST":
            q = request.POST.get("upname", "")
            que = Price.objects.get(id=q)
            que.Date = request.POST.get("Date")
            que.Cost_per_minute = request.POST.get("Cost_per_minute")
            que.Cost_per_minute_from_8pm_to_2am = request.POST.get("Cost_per_minute_from_8pm_to_2am")
            que.Cost_per_minute_from_2am_to_6am = request.POST.get("Cost_per_minute_from_2am_to_6am")
            que.save()
            return HttpResponseRedirect("/Price")


class view_user(View):
    def add_user(request):
        if request.method == "POST":
            user = User()
            user.id = request.POST.get("id")
            user.Fullname = request.POST.get("Fullname")
            user.Shift_number = request.POST.get("Shift_number")
            user.Computer_IP = request.POST.get("Computer_IP")
            user.save()
            return HttpResponseRedirect("/User")

    def del_user(request):
        if request.method == "POST":
            q = request.POST.get("delname", "")
            que = User.objects.get(id=q)
            que.delete()
            return HttpResponseRedirect("/User")

    def update_user(request):
        if request.method == "POST":
            q = request.POST.get("upname", "")
            que = User.objects.get(id=q)
            que.id = request.POST.get("id")
            que.Fullname = request.POST.get("Fullname")
            que.Shift_number = request.POST.get("Shift_number")
            que.Computer_IP = request.POST.get("Computer_IP")
            que.save()
            return HttpResponseRedirect("/User")


class view_receipt(View):
    def add_receipt(request):
        if request.method == "POST":
            receipt = Receipt()
            receipt.Organization_name = request.POST.get("Organization_name")
            receipt.Organization_address = request.POST.get("Organization_address")
            receipt.Organization_phone_number = request.POST.get("Organization_phone_number")
            receipt.Number_of_minutes_of_session = request.POST.get("Number_of_minutes_of_session")
            receipt.Total_cost = request.POST.get("Total_cost")
            receipt.Cost_per_minute = Price.objects.get(id=request.POST.get("Cost_per_minute"))
            receipt.Employee_ID = User.objects.get(id=request.POST.get("Employee_ID"))
            receipt.save()
            return HttpResponseRedirect("/Receipt")

    def del_receipt(request):
        if request.method == "POST":
            q = request.POST.get("delname", "")
            que = Receipt.objects.get(id=q)
            que.delete()
            return HttpResponseRedirect("/Receipt")

    def update_receipt(request):
        if request.method == "POST":
            q = request.POST.get("upname", "")
            que = Receipt.objects.get(id=q)
            que.Organization_name = request.POST.get("Organization_name")
            que.Organization_address = request.POST.get("Organization_address")
            que.Organization_phone_number = request.POST.get("Organization_phone_number")
            que.Number_of_minutes_of_session = request.POST.get("Number_of_minutes_of_session")
            que.Total_cost = request.POST.get("Total_cost")
            que.Cost_per_minute = Price.objects.get(id=request.POST.get("Cost_per_minute"))
            que.Employee_ID = User.objects.get(id=request.POST.get("Employee_ID"))
            que.save()
            return HttpResponseRedirect("/Receipt")


class view_session(View):
    def add_session(request):
        if request.method == "POST":
            session = Session()
            session.Organization_name = request.POST.get("Organization_name")
            session.Organization_address = request.POST.get("Organization_address")
            session.Organization_phone_number = request.POST.get("Organization_phone_number")
            session.Date_of_start_of_session = request.POST.get("Date_of_start_of_session")
            session.Date_of_end_of_session = request.POST.get("Date_of_end_of_session")
            session.Number_of_minutes_of_session = request.POST.get("Number_of_minutes_of_session")
            session.Total_cost = request.POST.get("Total_cost")
            session.Employee_ID = User.objects.get(id=request.POST.get("Employee_ID"))
            session.Cost_per_minute = Price.objects.get(id=request.POST.get("Cost_per_minute"))

            session.save()
            return HttpResponseRedirect("/Session")

    def del_session(request):
        if request.method == "POST":
            q = request.POST.get("delname", "")
            que = Session.objects.get(id=q)
            que.delete()
            return HttpResponseRedirect("/Session")

    def update_session(request):
        if request.method == "POST":
            q = request.POST.get("upname", "")
            que = Session.objects.get(id=q)
            que.Organization_name = request.POST.get("Organization_name")
            que.Organization_address = request.POST.get("Organization_address")
            que.Organization_phone_number = request.POST.get("Organization_phone_number")
            que.Date_of_start_of_session = request.POST.get("Date_of_start_of_session")
            que.Date_of_end_of_session = request.POST.get("Date_of_end_of_session")
            que.Number_of_minutes_of_session = request.POST.get("Number_of_minutes_of_session")
            que.Total_cost = request.POST.get("Total_cost")
            que.Employee_ID = User.objects.get(id=request.POST.get("Employee_ID"))
            que.Cost_per_minute = Price.objects.get(id=request.POST.get("Cost_per_minute"))
            que.save()
            return HttpResponseRedirect("/Session")

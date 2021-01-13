from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context_processors import csrf
from django.views.generic import FormView
from .models import Price, Operator, Receipt, Client
from .forms import AddPrice, AddOperator, AddReceipt, AddClient
from django.views import generic
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import FormView
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound

from provider import forms


def great(request):
    return render(request, "great.html")


def index(request):
    return render(request, "index.html")


def index_price(request):
    form_add = AddPrice()
    data = Price.objects.all()
    return render(request, "provider/Template_Price.html", {"form": form_add, "data_show": data})


def index_operator(request):
    form_ex = AddOperator()
    data = Operator.objects.all()
    return render(request, "provider/Template_Operator.html", {"form": form_ex, "data_show": data})


def index_receipt(request):
    form_er = AddReceipt()
    data = Receipt.objects.all()
    return render(request, "provider/Template_Receipt.html", {"form": form_er, "data_show": data})


def index_client(request):
    form_ca = AddClient()
    data = Client.objects.all()
    return render(request, "provider/Template_Client.html", {"form": form_ca, "data_show": data})


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


class view_operator(View):
    def add_operator(request):
        if request.method == "POST":
            operator = Operator()
            operator.Fullname = request.POST.get("Fullname")
            operator.save()
            return HttpResponseRedirect("/Operator")

    def del_operator(request):
        if request.method == "POST":
            q = request.POST.get("delname", "")
            que = Operator.objects.get(id=q)
            que.delete()
            return HttpResponseRedirect("/Operator")

    def update_operator(request):
        if request.method == "POST":
            q = request.POST.get("upname", "")
            que = Operator.objects.get(id=q)
            que.Fullname = request.POST.get("Fullname")
            que.save()
            return HttpResponseRedirect("/Operator")


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
            receipt.Employee_ID = Operator.objects.get(id=request.POST.get("Employee_ID"))
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
            que.Employee_ID = Operator.objects.get(id=request.POST.get("Employee_ID"))
            que.save()
            return HttpResponseRedirect("/Receipt")


class view_client(View):
    def add_client(request):
        if request.method == "POST":
            сlient = Client()
            сlient.IP = request.POST.get("IP")
            сlient.Date_of_start_of_session = request.POST.get("Date_of_start_of_session")
            сlient.Date_of_end_of_session = request.POST.get("Date_of_end_of_session")
            сlient.Shift_number = Receipt.objects.get(id=request.POST.get("Shift_number"))
            сlient.Cost_per_minute = Price.objects.get(id=request.POST.get("Cost_per_minute"))
            сlient.Employee_ID = Operator.objects.get(id=request.POST.get("Employee_ID"))
            сlient.save()
            return HttpResponseRedirect("/Client")

    def del_client(request):
        if request.method == "POST":
            q = request.POST.get("delname", "")
            que = Client.objects.get(id=q)
            que.delete()
            return HttpResponseRedirect("/Client")

    def update_client(request):
        if request.method == "POST":
            q = request.POST.get("upname", "")
            que = Client.objects.get(id=q)
            que.IP = request.POST.get("IP")
            que.Date_of_start_of_session = request.POST.get("Date_of_start_of_session")
            que.Date_of_end_of_session = request.POST.get("Date_of_end_of_session")
            que.Shift_number = Receipt.objects.get(id=request.POST.get("Shift_number"))
            que.Cost_per_minute = Price.objects.get(id=request.POST.get("Cost_per_minute"))
            que.Employee_ID = Operator.objects.get(id=request.POST.get("Employee_ID"))
            que.save()
            return HttpResponseRedirect("/Client")

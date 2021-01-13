from django.contrib import admin
from django.urls import path
from provider import views
from django.views.generic import TemplateView
from django.conf.urls import include, url

admin.autodiscover()

urlpatterns = [
    path('', views.great, name='great'),
    url(r'^admin/backups/', include('dbbackup_ui.urls')),
    url(r'^admin/', admin.site.urls),
    path('AIS/', views.index, name='home'),
    path('Price/', views.index_price, name='Price'),
    path('Operator/', views.index_operator, name='Operator'),
    path('Receipt/', views.index_receipt, name='Receipt'),
    path('Client/', views.index_client, name='Client'),
    # пути для цены
    path('Price/add/', views.view_price.add_price, name='add_price'),
    path("Price/del/", views.view_price.del_price, name="del_price"),
    path("Price/up/", views.view_price.update_price, name="update_price"),
    # пути для оператора
    path('Operator/add/', views.view_operator.add_operator, name='add_operator'),
    path("Operator/del/", views.view_operator.del_operator, name="del_operator"),
    path("Operator/up/", views.view_operator.update_operator, name="update_operator"),
    # пути для квитанций
    path('Receipt/add/', views.view_receipt.add_receipt, name='add_receipt'),
    path("Receipt/del/", views.view_receipt.del_receipt, name="del_receipt"),
    path("Receipt/up/", views.view_receipt.update_receipt, name="update_receipt"),
    # пути для клиентов
    path('Client/add/', views.view_client.add_client, name='add_client'),
    path("Client/del/", views.view_client.del_client, name="del_client"),
    path("Client/up/", views.view_client.update_client, name="update_client"),
]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

from django.contrib import admin
from django.urls import path
from provider import views
from django.conf.urls import include, url

admin.autodiscover()

urlpatterns = [
    path('', views.great, name='great'),
    url(r'^admin/backups/', include('dbbackup_ui.urls')),
    url(r'^admin/', admin.site.urls),
    path('AIS/', views.index, name='home'),
    path('Price/', views.index_price, name='Price'),
    path('User/', views.index_user, name='User'),
    path('Receipt/', views.index_receipt, name='Receipt'),
    path('Session/', views.index_session, name='Session'),
    # пути для цены
    path('Price/add/', views.view_price.add_price, name='add_price'),
    path("Price/del/", views.view_price.del_price, name="del_price"),
    path("Price/up/", views.view_price.update_price, name="update_price"),
    # пути для пользователя
    path('User/add/', views.view_user.add_user, name='add_user'),
    path("User/del/", views.view_user.del_user, name="del_user"),
    path("User/up/", views.view_user.update_user, name="update_user"),
    # пути для квитанций
    path('Receipt/add/', views.view_receipt.add_receipt, name='add_receipt'),
    path("Receipt/del/", views.view_receipt.del_receipt, name="del_receipt"),
    path("Receipt/up/", views.view_receipt.update_receipt, name="update_receipt"),
    # пути для сеансов
    path('Session/add/', views.view_session.add_session, name='add_session'),
    path("Session/del/", views.view_session.del_session, name="del_session"),
    path("Session/up/", views.view_session.update_session, name="update_session"),
]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

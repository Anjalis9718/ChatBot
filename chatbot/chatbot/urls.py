"""chatbot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf.urls import url
from first_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.button),


    url(r'^status1',views.button1,name='script'),
    url(r'^status/',views.form_view,name="status"),
    url(r'^status/input',views.input,name="input"),
    url(r'^TicketConfirm',views.button2,name='TicketConfirm'),
    url(r'^ticket_confirm',views.ticket_confirm,name="ticket_confirm"),
    url(r'^ticket_confirm/input1',views.input1,name="input1"),
    url(r'^CheckInTime',views.button3,name='CheckInTime'),
    url(r'^checkintime',views.checkintime,name="checkintime"),
    url(r'^checkintime/input2',views.input2,name="input2"),
    url(r'^Other',views.button4,name='Other'),
    url(r'^other',views.otherquery,name="other"),
    url(r'^other/input3',views.input3,name="input3"),





]

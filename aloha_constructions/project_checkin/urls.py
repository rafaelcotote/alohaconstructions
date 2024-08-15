from django.urls import path
from . import views
from .views import CheckinListView

urlpatterns = [
    path('', views.CheckinRegister, name='index'),
    path('checkin/', views.checkin_register, name='checkin_register'),
    path('checkin/success/', views.checkin_success, name='checkin_success'),
    path('checkin/list/', CheckinListView.as_view(), name='checkin_list'),

]
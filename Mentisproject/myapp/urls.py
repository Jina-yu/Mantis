from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('mypage', views.mypage, name='mypage'),
    path('myinfo_re', views.myinfo_re, name='myinfo_re'),
    path('myinfo_up', views.myinfo_up, name='myinfo_up'),
    path('myclass', views.myclass, name='myclass'),
    path('cash',views.cash, name='cash'),
    path('cash_check', views.cash_check, name='cash_check'),
    path('certification', views.certification, name='certification'),
    path('certification_check', views.certification_check, name='certification_check'),
]
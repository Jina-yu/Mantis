from django.urls import path
from . import views
urlpatterns = [
    path('mentoring', views.mentoring, name='mentoring'),
    path('mentor', views.mentor, name='mentor'),
]
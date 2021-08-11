from django.urls import path
from . import views
urlpatterns = [
    path('mentoring', views.mentoring, name='mentoring'),
    path('event',views.event, name='event'),
    path('event_detail',views.event_detail, name='event_detail'),    
    path('event_up',views.event_up, name='event_up'),
    path('event_re',views.event_re, name='event_re'),
    path('class1',views.class1, name='class1'),
    path('class1_play',views.class1_play, name='class1_play'),
]
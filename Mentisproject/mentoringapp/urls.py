from django.urls import path
from . import views
urlpatterns = [
    path('mentoring', views.mentoring, name='mentoring'),
    path('mentor', views.mentor, name='mentor'),
    path('event',views.event, name='event'),
    path('event_detail',views.event_detail, name='event_detail'),    
    path('event_up',views.event_up, name='event_up'),
    path('event_re',views.event_re, name='event_re'),
    path('lecture',views.lecture, name='lecture'),
    path('class1',views.class1, name='class1'),
    path('class1_play',views.class1_play, name='class1_play'),
    path('apply',views.apply_check, name='apply'),
    path('apply_check',views.apply_check, name='apply_check'),
    path('column', views.column, name='column'),
    path('column_write', views.column_write, name='column_write'),
    path('column_re', views.column_re, name='column_re'),
    path('column_detail1', views.column_detail1, name='column_detail1'),
    path('column_coment_re', views.column_coment_re, name='column_coment_re'),
    path('qna', views.column_coment_re, name='qna'),


]
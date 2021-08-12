from django.urls import path
from . import views
urlpatterns = [
    path('mentoring', views.mentoring, name='mentoring'),
    path('mentor', views.mentor, name='mentor'),
    path('apply', views.apply, name='apply'),
    path('apply_check', views.apply_check, name='apply_check'),
    path('qna', views.qna, name='qna'),
    path('column', views.column, name='column'),
    path('column_write', views.column_write, name='column_write'),
    path('column_re', views.column_re, name='column_re'),
    path('column_detail1', views.column_detail1, name='column_detail1'),
    path('column_coment_re', views.column_coment_re, name='column_coment_re'),

]
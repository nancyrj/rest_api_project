from django.urls import path
from . import views


urlpatterns = [
         path('save', views.Student_view.as_view(), name='index'),
         path('get_stud', views.Getstudentview.as_view(), name='index'),
    ]
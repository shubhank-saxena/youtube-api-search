from django.urls import path

from . import views

urlpatterns = [path('', views.web_page), path("index/", views.index), path("getvideos/", views.get_videos)]

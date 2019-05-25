from django.urls import path

from export.views import views

urlpattern = [
    path('test', views.test)
]
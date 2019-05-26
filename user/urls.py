# !/bin/bash
# -* ' encoding = utf-8' *-

from django.urls import path

from user import views

urlpatterns = [

    path('username', views.login_check),
    path('logout', views.logout)
]

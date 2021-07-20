from django.contrib import admin
from django.urls import path
from . import views

app_name = 'health'
urlpatterns = [
    path('<int:id>', views.main, name="main"),
    path('add_goal/', views.add_goal, name="add_goal"),
]

from django.urls import path
from demo import views

urlpatterns = [
    path('', views.index),
    path('home/', views.home),
]

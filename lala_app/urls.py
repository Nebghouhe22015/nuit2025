from django.urls import path

###########################

from .d1 import views

urlpatterns = [
    path('', views.dancer, name='Dancer avec les mots'),
]

from django.urls import path
from app import views

urlpatterns = [
    path('',views.index2,name='index2')
]

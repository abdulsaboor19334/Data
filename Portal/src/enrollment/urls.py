from django.urls import path
from .views import enroll,viewrec

urlpatterns = [
    path('bba/', enroll),
    path('view/<int:erp>/',viewrec)
]
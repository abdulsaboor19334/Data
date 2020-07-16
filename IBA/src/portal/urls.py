from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import get_user_model

User = get_user_model()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('subject/',include('subject.urls'))
]

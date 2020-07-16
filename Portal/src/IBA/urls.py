
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('enrollment/',include('enrollment.urls')),
    path('notepad/', include('notepad.urls',namespace='notepad'))
]

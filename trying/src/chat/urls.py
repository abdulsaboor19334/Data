from django.urls import path
from .views import user,website,video,videoform

urlpatterns = [
    path('user/',user),
    path('website/',website),
    path('video/',video),
    path('videoform/',videoform),
]
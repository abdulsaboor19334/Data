from django.urls import path
from .views import enroll, EnrollView


urlpatterns = [
    path('enrollment/', EnrollView.as_view())
]
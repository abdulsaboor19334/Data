from django.urls import path
from .views import register, login_view, logout_view,premium_view

app_name = 'users'

urlpatterns = [
    path('register/', register),
    path('login/', login_view, name="login"),
    path('logout/', logout_view),
    path('premium/', premium_view,name="premium")
]

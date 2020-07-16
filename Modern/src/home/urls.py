from django.urls import path
from .views import home_view, blog,about_us, team, portfolio, contact, services

app_name = 'home'

urlpatterns = [
    path('', home_view, name='home'),
    path('blog/', blog, name= 'blog'),
    path('About-us/', about_us, name= 'about-us'),
    path('team/', team, name='team'),
    path('portfolio/', team, name='portfolio'),
    path('contact-us/', contact, name='contact'),
    path('services/', services, name='services'),

]

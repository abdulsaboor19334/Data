from django.urls import path
from .views import post_list_view, post_detail_view, editview, deleteview, createview,like,logout

app_name = 'blog'

urlpatterns = [
    path('list/', post_list_view, name='list'),
    path('list/detail/<slug>/', post_detail_view, name='detail'),
    path('list/edit/<slug>/', editview),
    path('delete/<slug>', deleteview, name='delete'),
    path('like/<slug>', like, name='like'),
    path('create/', createview,name='create'),
    path('logout/',logout)
]

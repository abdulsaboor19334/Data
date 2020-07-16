from django.urls import path
from .views import list_books,book_detail,chapter_detail,exercise_view,solution_view, homeview

app_name = "book"


urlpatterns = [
    path('',homeview, name='home'),
    path('list/',list_books, name='list'),
    path('detail/<slug:book_slug>',book_detail, name="detail"),
    path('detail/exercises/<slug:book_slug>/<int:chapter_number>/',exercise_view, name='exercises'),
]

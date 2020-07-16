from django.urls import path
from .views import notepadview,done,not_done,delete,edit,new_note


app_name = 'notepad'

urlpatterns = [
    path('view/',notepadview,name='view'),
    path('view/done/<id>',done),
    path('view/not-done/<id>',not_done),
    path('view/delete/<id>',delete),
    path('view/edit/<id>', edit),
    path('view/new',new_note)
]
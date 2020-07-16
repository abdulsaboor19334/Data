from django.contrib import admin
from .models import User, BaseManager

class MyUserAdmin(BaseManager):
    model = User
    # add_form = SignUpForm
    # form = SignUpFormChangeForm
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

admin.site.register(User, MyUserAdmin)

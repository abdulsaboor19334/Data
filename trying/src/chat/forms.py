from django import forms
from .models import User,Car,Websites,Video



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'firstname',
            'lastname',
            'email',
            'phonenumber',
        ]


class WebsiteForm (forms.ModelForm):
    class Meta:
        model = Websites
        fields = [
            'name',
            'url',
            'owner',
        ]

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = [
            'name',
            'url',
            'detail'
        ]
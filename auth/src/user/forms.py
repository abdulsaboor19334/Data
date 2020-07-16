from django import forms 
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()


class Registration(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'Confirm password',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password2'
        ]
    def clean(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password != password2:
            raise forms.ValidationError('The Passwords do not match')

class Login(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        user = authenticate(username = username,password = password)

        if username and password:
            if not user:
                raise forms.ValidationError('password or username incorrect')
            if not user.check_password(password):
                raise forms.ValidationError('password or username incorrect')
            if not user.is_active:
                raise forms.ValidationError('password or username incorrect')
            return super(Login, self).clean()

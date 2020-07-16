from django import forms
from .models import NotePad

class NotepadForm(forms.ModelForm):
    class Meta:
        model = NotePad
        fields = [
            'title',
            'due',
            'priority'
        ]
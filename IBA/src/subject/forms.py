from django import forms
from .models import EnrollmentBBA

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = EnrollmentBBA
        fields = [
            'course_1',
            'course_2',
            'course_3',
            'course_4',
            'course_5',
        ]
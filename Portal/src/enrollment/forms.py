from django import forms
from .models import EnrollmentBBA, Courses
from django.db.models import Q

class EnrollmentFormBBA(forms.ModelForm):
    class Meta:
        model = EnrollmentBBA
        fields = [
            'choice_1',
            'choice_2',
            'choice_3',
            'choice_4',
            'choice_5',
        ]
        
    def clean(self):
        cd = self.cleaned_data
        choice_1 = cd.get('choice_1')
        choice_2 = cd.get('choice_2')
        choice_3 = cd.get('choice_3')
        choice_4 = cd.get('choice_4')
        choice_5 = cd.get('choice_5')

        cocs = Courses.objects.all()

        if choice_1 == choice_2 or choice_1 == choice_3 or choice_1 == choice_4 or choice_1 == choice_5:
            raise forms.ValidationError('1) Two choices cannot be the same ')
        elif choice_2 == choice_1 or choice_2 == choice_3 or choice_2 == choice_4 or choice_2 == choice_5:
            raise forms.ValidationError('2) Two choices cannot be the same ')
        elif choice_3 == choice_2 or choice_3 == choice_4 or choice_3 == choice_4 or choice_3 == choice_5:
            raise forms.ValidationError('3) Two choices cannot be the same ')
        elif choice_4 == choice_2 or choice_4 == choice_3 or choice_4 == choice_1 or choice_4 == choice_5:
            raise forms.ValidationError('4) Two choices cannot be the same ')
        elif choice_5 == choice_4 or choice_5 == choice_3 or choice_5 == choice_2 or choice_5 == choice_1:
            raise forms.ValidationError('4) Two choices cannot be the same ')
        else:
            for coc in cocs:
                enrolled = EnrollmentBBA.objects.filter(Q(choice_1__course_name=coc)|Q(choice_2__course_name=coc)|Q(choice_3__course_name=coc)|Q(choice_4__course_name=coc)|Q(choice_5__course_name=coc))
                enrolled_number = len(enrolled)
            if enrolled_number >= 5:
                raise forms.ValidationError('Sorry one of selected courses is taken...')
                coc.offered_to_BBA = False
                coc.save()
            elif enrolled_number < 5:
                coc.offered_to_BBA = True
                coc.save()
                return cd 
from django.contrib import admin
from .models import Student,Courses,EnrollmentBBA,EnrollmentAcf

class AdminStudent(admin.ModelAdmin):
    list_display= ['first_name',
    'last_name',
    'erp',
    'enrolled_in',
    'major',
    
    ]

class AdminEnrollmet(admin.ModelAdmin):
    list_display= ['choice_1',
    'choice_2',
    'choice_3',
    'choice_4',
    'choice_5',
    ]


admin.site.register(Student, AdminStudent)
admin.site.register(Courses)
admin.site.register(EnrollmentBBA, AdminEnrollmet)
admin.site.register(EnrollmentAcf)
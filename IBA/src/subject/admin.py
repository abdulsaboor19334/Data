from django.contrib import admin
from .models import Student,Courses,EnrollmentBBA,EnrollmentAcf

class AdminStudent(admin.ModelAdmin):
    list_display= ['first_name',
    'last_name',
    'erp',
    'enrolled_in',
    'major',
    
    ]


admin.site.register(Student, AdminStudent)
admin.site.register(Courses)
admin.site.register(EnrollmentBBA)
admin.site.register(EnrollmentAcf)
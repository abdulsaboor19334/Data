from django.db import models
import datetime
from django.db.models import Q
from django import forms

MAJOR_CHOICES = (('acf','Accounting and Finance'),
                ('eco', ' BS ecnomics'),
                ('bba','BBA'),
                ('ecomath', 'Ecnomics and Math')

)

class Student(models.Model):
    first_name      = models.CharField(max_length=50)
    middle_name     = models.CharField(max_length=50,blank=True,null=True)
    last_name       = models.CharField(max_length=50)
    erp             = models.IntegerField(primary_key=True,auto_created=False,unique=True)
    enrolled_in     = models.DateTimeField(auto_now_add=True)
    major           = models.CharField(max_length=100,choices=MAJOR_CHOICES,default='none')
    student_img     = models.ImageField(blank = True ,null= True)

    def __str__(self):
        return self.first_name

class Courses(models.Model):
    course_code         = models.IntegerField(unique=True,primary_key=True)
    course_name         = models.CharField(max_length=100)
    offered_to_BBA      = models.BooleanField(default=False)
    offered_to_acf      = models.BooleanField(default=False)
    offered_to_eco      = models.BooleanField(default=False)
    offered_to_ecomath  = models.BooleanField(default=False)
    instructor          = models.CharField(max_length=100)
    enrolled_students   = models.ManyToManyField(Student,blank=True)

    def __str__(self):
        return self.course_name

class EnrollmentBBA(models.Model):
    choice_1 = models.ForeignKey(Courses,on_delete=models.CASCADE,related_name='course1_bba',limit_choices_to={'offered_to_BBA' : True})
    choice_2 = models.ForeignKey(Courses,on_delete=models.CASCADE,related_name='course2_bba',limit_choices_to={'offered_to_BBA' : True}) 
    choice_3 = models.ForeignKey(Courses,on_delete=models.CASCADE,related_name='course3_bba',limit_choices_to={'offered_to_BBA' : True})
    choice_4 = models.ForeignKey(Courses,on_delete=models.CASCADE,related_name='course4_bba',limit_choices_to={'offered_to_BBA' : True})
    choice_5 = models.ForeignKey(Courses,on_delete=models.CASCADE,related_name='course5_bba',limit_choices_to={'offered_to_BBA' : True})

    def limit(self):
        choices = Courses.objects.all()
        for choice in choices:
            enrolled = EnrollmentBBA.objects.filter(Q(choice_1__course_name=choice)|Q(choice_2__course_name=choice)|Q(choice_3__course_name=choice)|Q(choice_4__course_name=choice)|Q(choice_5__course_name=choice))
            enrolled_number = len(enrolled)
            if enrolled_number > 5:
                choice.offered_to_BBA = False
                choice.save()
            elif enrolled_number < 5:
                choice.offered_to_BBA = True
                choice.save()
class EnrollmentAcf(models.Model):
    course_1 = models.ForeignKey(Courses,on_delete=models.CASCADE,related_name='course1_acf',limit_choices_to={'offered_to_acf' : True})
    course_2 = models.ForeignKey(Courses,on_delete=models.CASCADE,related_name='course2_acf',limit_choices_to={'offered_to_acf' : True}) 
    course_3 = models.ForeignKey(Courses,on_delete=models.CASCADE,related_name='course3_acf',limit_choices_to={'offered_to_acf' : True})
    course_4 = models.ForeignKey(Courses,on_delete=models.CASCADE,related_name='course4_acf',limit_choices_to={'offered_to_acf' : True})
    course_5 = models.ForeignKey(Courses,on_delete=models.CASCADE,related_name='course5_acf',limit_choices_to={'offered_to_acf' : True})

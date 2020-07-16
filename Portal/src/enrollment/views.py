from django.shortcuts import render
from .forms import EnrollmentFormBBA
from django.views import View
from .models import EnrollmentBBA,Student

def enroll(request):
    my_form = EnrollmentFormBBA(request.POST or None)
    EnrollmentBBA.limit(my_form)
    if my_form.is_valid():
        my_form.save()
        my_form = EnrollmentFormBBA()

    context = {'form':my_form}
    return render(request,'enroll.html',context)

def viewrec (request, erp):
    obj = Student.objects.get(erp=erp)
    img = str(obj.student_img)
    context = {
        'obj' : obj,
        'img' : img
    }
    return render(request, 'view.html', context)


from django.shortcuts import render
from .forms import EnrollmentForm
from django.views import View

def enroll(request):
    my_form = EnrollmentForm(request.POST or None)
    context = {'form':my_form}
    return render(request,'enroll.html',context)

class EnrollView(View):
    def get(self, request):
        my_form = EnrollmentForm()
        context = {'form':my_form}
        return render(request,'enroll.html',context)
    def post (self, request):
        my_form = EnrollmentForm(request.POST)
        if my_form.is_valid():
            my_form.save()


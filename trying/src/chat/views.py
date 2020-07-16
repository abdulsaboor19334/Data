from django.shortcuts import render
from .forms import UserForm, WebsiteForm, VideoForm
from .models import Video
import re

def user(request):
    my_form = UserForm(request.POST or None)
    if my_form.is_valid():
        my_form.save()
    context = {'form': my_form }
    return render(request,'user.html',context)


def website(request):
    context = {}
    my_form = WebsiteForm()
    if my_form.is_valid():
        my_form.save()
    context = {'form': my_form}
    return render(request,'website.html',context)

def video(request):
    model = Video.objects.all()
    context = {'video': model}
    return render(request, 'video.html', context)

def videoform(request):
    my_form = VideoForm(request.POST or None)
    if my_form.is_valid():
        data = my_form.cleaned_data
        print(data)
        url = data['url']
        clean = re.findall(r'v=(\w+)',url)[0]
        Video.objects.create(name=data['name'],url=clean,detail=my_form['detail'])
        my_form = VideoForm()
    context = { 'form' : my_form }
    return render(request,'vidform.html',context)
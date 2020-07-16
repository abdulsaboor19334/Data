from django.shortcuts import render

def home_view(request):
    return render(request,'home.html', {})


def blog(request):
    return render(request,'blog.html', {})

def about_us(request):
    return render(request,'about.html', {})

def team(request):
    return render(request,'team.html', {})

def portfolio(request):
    return render(request,'portfolio.html', {})

def contact(request):
    return render(request,'contact.html', {})

def services(request):
    return render(request,'services.html', {})
from django.shortcuts import render


def test_function(request):
    return render(request, 'base.html',{})
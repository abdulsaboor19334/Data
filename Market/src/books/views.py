from django.shortcuts import render, get_object_or_404
from .models import Authors, Book, Chapter, Exercises, Solutions
from django.http import Http404

def homeview (request):
    return render(request, 'home.html')

def list_books(request):
    obj = Book.objects.all()
    context = {
        'books': obj
    }
    return render(request, 'book_list.html',context)


def book_detail(request, book_slug):
    obj = get_object_or_404(Book, slug=book_slug)
    chapter = obj.chapter_set.all()
    context = {
        'book': obj,
        'chapters':chapter
    }
    return render(request, 'book_detail.html',context)



def chapter_detail(request, book_slug, chapter_number):
    obj = Chapter.objects.filter(book__slug=book_slug, chapter_number=chapter_number)
    if obj.exists():
        context = {
            'chapter': obj[0]
        }
        return render(request, 'chapter_detail.html',context)
    return Http404


def exercise_view(request,book_slug, chapter_number):
    obj = Exercises.objects.filter(chapter__book__slug=book_slug,chapter__chapter_number=chapter_number)
    if obj.exists():
        context = {
                'exe': obj
            }
        return render(request, 'exercise_detail.html',context)
    return Http404


def solution_view(request,book_slug, chapter_number,exercise_number,solution_number):
    if obj.exists():
        obj = Solutions.objects \
                                .filter(exercise__chapter__book__slug=book_slug) \
                                .filter(chapter__book__slug=book_slug) \
                                .filter(chapter__chapter_number=chapter_number,exercise_number=exercise_number)
        context = {
                'exe': obj
            }
        return render(request, 'solution.html',context)
    return Http404
from django.shortcuts import render
from django.shortcuts import redirect,get_object_or_404
from .models import NotePad
from .forms import NotepadForm

def notepadview(request):
    notes = NotePad.objects.all()
    number = len(notes)
    context = {
        'notes' : notes,
        'number' : number
        }
    
    return render(request,'views.html',context)

def done(request, id):
    obj = get_object_or_404(NotePad, id=id)
    obj.done = True
    obj.save()
    return redirect('../')

def not_done(request, id):
    obj = get_object_or_404(NotePad, id=id)
    obj.done = False
    obj.save()
    return redirect('../')

def delete(request, id):
    obj =  NotePad.objects.get(id=id)
    obj.delete()
    return redirect('../')

def edit(request, id):
    obj = NotePad.objects.get(id=id)
    my_form = NotepadForm(request.POST or None, instance=obj)
    context = {
        'form': my_form
    }
    if my_form.is_valid():
        my_form.save()
        return redirect('../')
    return render(request, 'form.html', context)
    
def new_note(request):
    my_form = NotepadForm(request.POST or None)
    context = {
        'form': my_form
    }
    if my_form.is_valid():
        my_form.save()
        my_form = NotepadForm()
    return render(request, 'make-note.html', context)
    



from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import logout
from .models import Post, Likes, PostViews, Comments
from .forms import EditPostForm, CommentsForm, CreatePostForm
import datetime



def post_list_view(request):
    user = request.user
    obj = Post.objects.all()
    context = {'objs' : obj, 'user': user}
    return render(request,'list.html',context) 

def post_detail_view(request, slug):
    form = CommentsForm(request.POST or None)
    obj = get_object_or_404(Post, slug=slug)
    comments = obj.commented_post.all()
    user = request.user
    PostViews.objects.get_or_create(user=user, post=obj)
    context = { 
        'obj' : obj,
        'comments' : comments,
        'form': form,
         }
    if request.method =='POST':
        if form.is_valid():
            Comments.objects.create(content=form.cleaned_data.get('content'), user= request.user, post=obj)
            return redirect('blog:detail' ,slug=slug)
    return render(request, 'detail.html', context)

def homeview(request):
    obj = Post.objects.filter(pub_date__date=datetime.date.today())
    context = {'objs': obj}
    return render(request, 'home.html', context)

def editview(request, slug):
    obj = get_object_or_404(Post, slug=slug)
    form = EditPostForm(request.POST or None, instance=obj)
    context = {
        'form': form,
        'obj':obj
    }
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('blog:list')
    return render(request, 'edit.html', context)

def createview(request):
    form = CreatePostForm(request.POST or None, request.FILES or None)
    context = {
        'form': form
    }
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('blog:list')
    return render(request, 'create.html', context)

def deleteview(request, slug):
    obj = Post.objects.get(slug=slug)
    obj.delete()
    obj.save()
    return redirect('blog:list')

def like(request, slug):
    post = get_object_or_404(Post, slug=slug)
    query = Likes.objects.filter(user=request.user, post=post)
    if query.exists():
        query[0].delete()
        return redirect('blog:list')
    Likes.objects.create(user=request.user, post=post)
    return redirect('blog:list')

# def login(request):





# def logout(request):
#     logout(request)
#     return redirect('blog:list')

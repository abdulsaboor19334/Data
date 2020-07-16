from django import forms 
from .models import Post, Comments, User


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'slug',
            'title',
            'content',
            'author',
            'thumbnail',
        ]

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'author',
            'thumbnail',
            'slug',
        ]

class CommentsForm(forms.ModelForm):
    content = forms.CharField(label='Comment',widget=forms.Textarea(attrs={
        'rows': 3,
        'cols': 120,
        'placeholder': 'Enter your comment here'
    }))
    class Meta:
        model = Comments
        fields = [
            'content'
        ]
    
# class RegisterForm(forms.Form):
#     class Meta:
#         model = 
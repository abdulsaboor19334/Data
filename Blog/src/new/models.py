from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass 

    def __str__(self):
        return self.username


class Post(models.Model):
    title       = models.CharField(max_length=100)
    content     = models.TextField()
    pub_date    = models.DateTimeField(auto_now_add=True)
    edit_date   = models.DateField(auto_now=True) 
    author      = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    thumbnail   = models.ImageField(null=True, blank=True)
    slug        = models.SlugField(unique=True)
    
    def __str__(self):
        return  self.author.username +': '+ self.title
    
    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})
    
    @property
    def get_view_count(self):
        return self.viewed_post.all().count()

    @property
    def get_like_count(self):
        return self.liked_post.all().count()
    
    @property
    def get_comment_count(self):
        return self.commented_post.all().count()
    
    

class Likes(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liker')
    post        = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='liked_post')


class PostViews(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE,related_name='viewer')
    post        = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='viewed_post')
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Comments(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE,related_name='commenter')
    post        = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='commented_post')
    timestamp   = models.DateTimeField(auto_now_add=True)
    content     = models.TextField()

    def __str__(self):
        return self.user.username



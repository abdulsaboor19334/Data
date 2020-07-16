from django.contrib import admin
from .models import Post, Likes, PostViews, Comments

admin.site.register(Post)
admin.site.register(Likes)
admin.site.register(PostViews)
admin.site.register(Comments)
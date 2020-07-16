from django.contrib import admin
from .models import Authors, Book, Chapter, Exercises, Solutions, Library


admin.site.register(Authors)
admin.site.register(Book)
admin.site.register(Chapter)
admin.site.register(Exercises)
admin.site.register(Solutions)
admin.site.register(Library)
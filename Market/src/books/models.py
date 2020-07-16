from django.db import models
from django.contrib.auth import settings
from django.db.models.signals import post_save

class Library(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    books = models.ManyToManyField('Book')

def create_library(sender, instance, created,*args, **kwargs):
    if created:    
        Library.objects.get_or_create(user=instance)


post_save.connect(create_library, sender=settings.AUTH_USER_MODEL)

class Authors(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)
    cover = models.ImageField()
    slug = models.SlugField()
    detail =models.TextField(default='The detail for this book is not avalible')
    
    def __str__(self):
        return self.name
    # @property
    # def get_chapter_number(self):
    #     return self.chapter_set.all()

class Chapter(models.Model):
    name = models.CharField(max_length=100)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    chapter_number = models.IntegerField()

    def __str__(self):
        return f'chapter {self.name} of book {self.book}'

class Exercises(models.Model):
    name = models.CharField(max_length=100)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    page_number = models.IntegerField()
    exercise_number = models.IntegerField()

    def __str__(self):
        return f'exercise {self.name} of {self.chapter}'

class Solutions(models.Model):
    exercise = models.ForeignKey(Exercises, on_delete=models.CASCADE)
    solution_number = models.IntegerField()
    solution = models.ImageField()

    def __str__(self):
        return f'solution {self.solution_number} of {self.exercise}'
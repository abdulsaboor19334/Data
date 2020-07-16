from django.db import models


class User(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    phonenumber = models.IntegerField(unique=True)

    def __str__(self):
            return self.firstname         

class Websites(models.Model):
    name = models.CharField(max_length=100)
    url =models.URLField()
    owner =models.ForeignKey(User,on_delete=models.CASCADE)

class Car(models.Model):
    model = models.CharField(max_length=20)
    number = models.CharField(max_length=20)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,default = 'no')
    def __str__(self):
        return self.model

class Video(models.Model):
    url = models.URLField()
    name = models.CharField(max_length=100)
    detail =models.TextField()

    def __str__(self):
        return self.name



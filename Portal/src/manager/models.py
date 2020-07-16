from django.db import models


class DataQuery(models.QuerySet):
    def passed(self, bool):
        return self.filter(status= bool)

class DataManager(models.Manager):
    def get_queryset(self):
        return DataQuery(self.model, using=self._db)

    def passed(self, bool):
        return self.get_queryset().passed(bool)

class Data(models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=False)

    objects = DataManager()

    def __str__(self):
        return self.name +': '+ str(self.status)

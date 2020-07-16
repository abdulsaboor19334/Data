from django.db import models

PRIORITY_CHOICES = (
    ('L', 'LOW'),
    ('M','MEDIUM'),
    ('H','HIGH'),
    ('U', 'URGENT')
)



class NotePad(models.Model):
    title = models.CharField(max_length=50)
    due = models.DateTimeField()
    done = models.BooleanField(default=False)
    priority = models.CharField(choices=PRIORITY_CHOICES, max_length=1)
     
    def __str__(self):
        return self.title
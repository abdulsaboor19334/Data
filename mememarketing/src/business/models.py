from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


SM_SERVICES = (
    (1.7,'Facebook Groups'),
    (1.3,'Facebook Posts'),
    (1.9,'Instagram Posts'),
    (1.2,'Twitter Posts'),
    (1.1,'Twitter Trends'),
    (0.8,'YouTube Features')
)


class Campaign(models.Model):
    '''1. User who created the campaign.
    2. Title of the campaign
    3. Budget of the campaign (Maybe try to go for an interactive range widget which should be possible with javascript or even bootstrap)
    4. Service Types (Social Media platforms being used)
    5. Description
    6. Number of Memes to be ordered (Maybe try to go for an interactive range widget which should be possible with javascript or even bootstrap)
    7. Campaign Active or not boolean'''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    budget = models.IntegerField()
    #services = MultiSelectField(choices=SM_SERVICES, null=True, blank=True)
    description = models.TextField()
    number_of_memes = models.IntegerField()
    active = models.BooleanField(default=False)

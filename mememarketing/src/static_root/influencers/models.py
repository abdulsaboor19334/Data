from django.db import models
from business.models import Campaign, SM_SERVICES
from django.contrib.auth import get_user_model

User = get_user_model()


class CampaignExecutionUnit(models.Model):
    '''1. assigned_to_influencer
    2. campaign
    3. social_media_platform
    4. number_of_posts
    5. memes'''
    assigned_to_influencer = models.ForeignKey(User, on_delete=models.CASCADE)
    campaign_name = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    social_media_platform = models.CharField(choices=SM_SERVICES, max_length=50)
    number_of_posts = models.IntegerField()
    #memes = models.ForeignKey(Memes, on_delete=models.DO_NOTHING)
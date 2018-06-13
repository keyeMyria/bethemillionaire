from django.db import models
from account import models as account_model


#add video link
class VideoLink(models.Model):
    lesson_name = models.CharField(max_length=255, null=True, blank=True)
    video_link = models.TextField(max_length=1000, null=True, blank=True)


    def __str__(self):
        return str(self.lesson_name)



#leader board result
class LeaderBoard(models.Model):
    user = models.ForeignKey(account_model.UserProfile, on_delete=models.SET_NULL, null=True, blank=True)

    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    campaign_name = models.CharField(max_length=100, null=True, blank=True)

    rank = models.IntegerField(null=True, blank=True)
    referral = models.IntegerField(null=True, blank=True)
    referral_sale = models.IntegerField(null=True, blank=True)

    creation_time = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.campaign_name



#recent update post
class RecentUpdatePost(models.Model):
    user = models.ForeignKey(account_model.UserProfile, on_delete=models.SET_NULL, null=True, blank=True)

    title = models.CharField(max_length=255, null=True, blank=True)
    post = models.TextField(max_length=5000, null=True, blank=True)

    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.id)


from django.db import models
from django.contrib.auth.models import User

from account.models import UserProfile


class Comment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default=1)
    topic = models.CharField(max_length=255, default='step-1-overview', null=True, blank=True)
    comment = models.TextField(max_length=1000, null=True, blank=True)
    create_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)


class SubComment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default=1)
    topic = models.CharField(max_length=255, default='step-1-overview', null=True, blank=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    subcomment = models.TextField(max_length=1000, null=True, blank=True)
    create_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)


class StepControl(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    short_name = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.short_name


class Note(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    topic = models.CharField(max_length=200, null=True, blank=True)
    note = models.TextField(max_length=1000, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.topic


#step count
class StepCount(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    step1 = models.BooleanField(default=True)
    step2 = models.BooleanField(default=False)
    step3 = models.BooleanField(default=False)
    step4 = models.BooleanField(default=False)
    step5 = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user.username)


from django.db import models


class AffiliateLinkControl(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    short_name = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.short_name

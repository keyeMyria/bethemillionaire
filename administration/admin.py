from django.contrib import admin

from . import models



admin.site.register(models.VideoLink)
admin.site.register(models.LeaderBoard)
admin.site.register(models.RecentUpdatePost)
admin.site.register(models.LiveVideoLinkUpdate)

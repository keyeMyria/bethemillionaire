from django.contrib import admin
from . import models


admin.site.register(models.Comment)
admin.site.register(models.SubComment)
admin.site.register(models.StepControl)
admin.site.register(models.Note)

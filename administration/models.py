from django.db import models


#add video link
class VideoLink(models.Model):
    lesson_name = models.CharField(max_length=255, null=True, blank=True)
    video_link = models.TextField(max_length=1000, null=True, blank=True)


    def __str__(self):
        return str(self.lesson_name)



#test model
class Mul(models.Model):
    total = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.total

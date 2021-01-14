from django.db import models
from django.utils import timezone

class Post(models.Model):
    title           = models.CharField(max_length=264)
    description     = models.TextField()
    author          = models.CharField(max_length=20)
    publish         = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.title}"

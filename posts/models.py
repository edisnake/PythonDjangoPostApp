from datetime import datetime
from django.db import models

# Create your models here.
class Posts(models.Model):
    title      = models.CharField(max_length=200)
    body       = models.TextField()
    created_ts = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Posts"

# blog/models.py
from django.db import models

class Post(models.Model):
    # post_id = models.AutoField()
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
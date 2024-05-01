from django.db import models
from django.contrib.auth import get_user_model


class Articles(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    text = models.TextField()

    def __str__(self):
        return self.title

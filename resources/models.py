from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    location = models.CharField(blank=True, null=True, max_length=100)

    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


class Resource(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

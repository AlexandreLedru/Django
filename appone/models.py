from django.db import models


class User(models.Model):
    username = models.CharField(max_length=30, null=False)
    password = models.CharField(max_length=30, null=False)

    def test(self):
        return "null"

    def __str__(self):
        return self.username

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Graduate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=30)
    lastName =models.CharField(max_length=30)
    jobTitle=models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    linkedInLink = models.URLField()
    sageEmailAddress = models.EmailField()
    favouriteTeam = models.CharField(max_length=30)




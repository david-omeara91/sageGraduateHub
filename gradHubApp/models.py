from turtle import title
from django.db import models
from django.contrib.auth.models import User

class Graduate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    firstName = models.CharField(max_length=30)
    lastName =models.CharField(max_length=30)
    jobTitle=models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    linkedInLink = models.URLField()
    sageEmailAddress = models.EmailField()
    favouriteTeam = models.CharField(max_length=30)


class Event(models.Model):
    title=models.CharField(max_length=40)
    location=models.CharField(max_length=30)
    date=models.DateField()

class Resource(models.Model):
    title=models.CharField(max_length=40)
    url=models.URLField()
    category = models.CharField

class Mentor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    firstName = models.CharField(max_length=30)
    lastName =models.CharField(max_length=30)
    jobTitle=models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    linkedInLink = models.URLField()
    sageEmailAddress = models.EmailField()
    expertise = models.CharField(max_length=40)

class Question(models.Model):
    subject=models.CharField(max_length=40)
    body=models.TextField(max_length=400)

class Answer(models.Model):
    body=models.TextField(max_length=400)

class Advice(models.Model):
    body=models.TextField(max_length=400)

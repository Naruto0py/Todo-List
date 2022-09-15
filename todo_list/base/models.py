from distutils.command.upload import upload
from email.mime import image
from email.policy import default
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from fastapi import UploadFile

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    create = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']

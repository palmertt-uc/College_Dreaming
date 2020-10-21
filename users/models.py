from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25, blank=True, default='')
    last_name = models.CharField(max_length=25, blank=True, default='')
    gpa = models.CharField(max_length=5, blank=True, default='')
    act = models.CharField(max_length=2, blank=True, default='')
    sat = models.CharField(max_length=4, blank=True, default='')
    bio = models.TextField(max_length=1000, blank=True, default='')

    def __str__(self):
        return self.user.username + ' Profile'

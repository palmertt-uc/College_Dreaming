from django.db import models

# Create your models here.
class University(models.Model):
    name = models.CharField(max_length=150)
    population = models.CharField(max_length=50)
    amount_of_clubs = models.CharField(max_length=10) 
    known_for = models.CharField(max_length=100)
    public_or_private = models.CharField(max_length=25)
    in_state_tuition = models.CharField(max_length=8)
    out_state_tuition = models.CharField(max_length=8)
    university_image = models.CharField(max_length=1000)
    location = models.CharField(max_length=100)
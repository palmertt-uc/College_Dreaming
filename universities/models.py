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
    university_image = models.FileField()
    location = models.CharField(max_length=100)
    sports = models.CharField(max_length=200)
    required_act_score = models.CharField(max_length=2)
    required_sat_score = models.CharField(max_length=4)
    weather = models.CharField(max_length=10)
    most_popular_major = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class NearbyRestaurant(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    restaurant_name = models.CharField(max_length=150)
    restaurant_type = models.CharField(max_length=50)
    restuarant_address = models.CharField(max_length=200, default="123 Address, St, Cincinnati, OH 45209")
    restaurant_url = models.URLField(max_length=250, default='000000')

    def __str__(self):
        return self.restaurant_name

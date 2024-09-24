from django.db import models

# Create your models here.


class Itinerary(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    description = models.TextField()

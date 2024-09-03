from django.db import models

# Create your models here.


class Userdata(models.Model):
    user_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=15)
    lastname = models.CharField(max_length=15)
    password = models.CharField(max_length=32)

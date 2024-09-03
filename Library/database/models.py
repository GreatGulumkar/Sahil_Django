from django.db import models

# Create your models here.


class Books(models.Model):

    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=15)
    pub_data = models.DateField()

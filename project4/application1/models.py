from django.db import models

# Create your models here.


class Students(models.Model):
    name=models.CharField(max_length=100)
    roll_no=models.IntegerField()
    state=models.CharField(max_length=100)
    city=models.CharField(max_length=100)

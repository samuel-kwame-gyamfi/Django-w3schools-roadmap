from django.db import models

# Create your models here.
class Members(models.Model):
    first_name = models.CharField(max_length=255)
    Last_name = models.CharField(max_length=255)
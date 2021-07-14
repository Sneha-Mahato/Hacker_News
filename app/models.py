from django.db import models

# Create your models here.
class hackers_news(models.Model):
    User_name=models.CharField(max_length=20)
    Email=models.CharField(max_length=30)
    password=models.IntegerField()

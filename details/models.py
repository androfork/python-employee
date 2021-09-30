from django.db import models

# Create your models here.

class employee(models.Model):
    s_id = models.IntegerField()
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='pics')
    email = models.EmailField()
    password = models.CharField(max_length=10)
    phone = models.IntegerField()
    address = models.CharField(max_length=255)

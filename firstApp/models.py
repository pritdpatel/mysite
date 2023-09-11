from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=233)
    password=models.CharField(max_length=10)
    email=models.EmailField(default="null")
    username_struc=models.ForeignKey('Adress', on_delete=models.SET_NULL , null=True)
    def __str__(self):
        return self.username


class Adress(models.Model):
    username=models.CharField(max_length=255)
    address=models.CharField(max_length=255)

    def __str__(self):
        return self.username

class order(models.Model):
    username=models.CharField(max_length=255)
    productName=models.CharField(max_length=100)
    price=models.FloatField()

    def __str__(self):
        return self.username


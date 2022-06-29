from django.db import models
from django.contrib.auth.models import User


class Country(models.Model):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Contacts(models.Model):
    firstname = models.CharField(max_length=120)
    lastname = models.CharField(max_length=120)
    country = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f'{self.firstname} from {self.country}'


class My_List(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.CharField(max_length=250)
    brand = models.CharField(max_length=200)
    section = models.CharField(max_length=200)
    start_data = models.DateField()
    finish_data = models.DateField()
    auto_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product

    class Meta:
        ordering = ['id']

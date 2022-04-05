from django.db import models

# Create your models here.
class Place(models.Model):
    name1 = models.CharField(max_length=250, unique=True)
    desc1 = models.TextField( unique=True)
    image=models.ImageField(upload_to='pic')
class Country(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=124)
    phoneno=models.CharField(max_length=100)
    address=models.TextField()
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name
class Food(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Prize(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    name = models.IntegerField()


class Quantity(models.Model):

    food = models.ForeignKey(Food, on_delete=models.SET_NULL, blank=True, null=True)
    prize = models.ForeignKey(Prize, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField()




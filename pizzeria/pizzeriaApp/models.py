from django.db import models

# Create your models here.

class Pizza(models.Model):
    name = models.CharField(max_length=20)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Topping(models.Model):
    pizzaname = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    pizzaburden = models.CharField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pizzaburden





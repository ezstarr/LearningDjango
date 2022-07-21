from django.db import models

# Create your models here.
def pizza(models.Model):
    name = (
        ('H', 'Hawaiian'),
        ('ML', 'Meat Lovers')
    )

def Toppings(models.Model):
    pizza =
    name = models.ForeignKey(Pizza, )
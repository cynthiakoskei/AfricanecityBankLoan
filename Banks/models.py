from django.db import models

# Create your models here.

class Bank(models.Model):
    bankName= models.CharField(max_length=100)
    image = models.ImageField()
    interestRate = models.IntegerField()
      
    def __str__(self): 
        return self.bankName
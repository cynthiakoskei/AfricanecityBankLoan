from django.db import models

# Create your models here.

class Bank(models.Model):
    bankName= models.CharField(max_length=100)
    image = models.ImageField()
    interestRate = models.DecimalField(max_digits=2,decimal_places=2)
      
    def __str__(self): 
        return self.bankName
from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.
class Loan_Request(models.Model):
    Loan_amount = models.FloatField(default = 10000,
     validators= [MinValueValidator(10000),MaxValueValidator(250000
    )])
    # def __str__(self):
    #   return self.Loan_amount
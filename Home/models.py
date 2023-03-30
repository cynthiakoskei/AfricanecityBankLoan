from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

class Loan_Request(models.Model):
     first_name = models.CharField(max_length=10, default='John')
     last_name = models.CharField(max_length=10, default='Doe')
     id_number = models.PositiveIntegerField(default=1)
     contact_details = models.CharField(max_length=10, default='Doe')
     email_adress = models.EmailField(unique=False, default='u@xmail.com')
     salary = models.PositiveIntegerField(default=10000, validators=[MinValueValidator(10000)])
     
     def __str__(self):
        return self.first_name
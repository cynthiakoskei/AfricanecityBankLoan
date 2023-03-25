from django.db import models
from phone_field import PhoneField
from django.forms.widgets import DateInput



# Create your models here.

class Bank(models.Model):
    bankName= models.CharField(max_length=100)
    image = models.ImageField()
    interestRate = models.DecimalField(max_digits=5, decimal_places=2)
      
    def __str__(self): 
        return self.bankName
    

class Application(models.Model):
    
    business_launching = 'business_launching'
    house_buying = 'house_buying'
    home_improment = 'home_improment'
    investment = 'investment'
    education = 'education'
    other = 'other'

    
    LOAN_CHOICES = [
        ( business_launching,'business_launching'),
        (house_buying ,'house_buying'),
        (home_improment ,'home_improment'),
        (investment , 'investment'),
        (education ,'education'),
        ( other , 'other'),
            
    ]
   
    desired_loan =  models.FloatField()
    annual_income =  models.FloatField()
    loan_will_be_used_for = models.CharField(max_length = 250, choices=LOAN_CHOICES,
        default=business_launching,
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField(null="False")
    email = models.EmailField(max_length=254)
    phoneNumber = PhoneField(blank=True, help_text='Contact phone number')
    home_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state_province = models.CharField(max_length=100)
    postal_code = models.CharField( max_length=6)

    def __str__(self):
        return self.first_name
    
    class Meta:{
        'birth_date': ('D.O.B')
    }
    
    widgets = {
        'birth_date': DateInput(attrs={'type': 'date'})
    }



    
class Features(models.Model):
    min_amount = models.FloatField()
    max_amount = models.FloatField()
    low_interest_rate =  models.DecimalField(max_digits=4, decimal_places=2)
    illustration_rate = models.DecimalField(max_digits=4, decimal_places=2)
    amount_borrowed = models.FloatField()
    initiation_fee = models.FloatField()
    monthly_service_fee = models.FloatField()
    amount_payable = models.FloatField()
    monthly_installment_amount = models.FloatField()
    bankName = models.ForeignKey(Bank, null=True,on_delete=models.CASCADE)

    def _str_(self): 
        return str(self.bankName)

class Help(models.Model):
    details = models.TextField()
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    message = models.TextField()
    
           
        

        
  
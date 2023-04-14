from django.db import models
from phone_field import PhoneField
from django.forms.widgets import DateInput
from Home.models import Loan_Request
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Bank(models.Model):
    bank_name= models.CharField(max_length=100)
    bank_url = models.URLField(default="https://www.absabank.co.ke/personal/borrow/personal-loan/", max_length=200)
    image = models.ImageField()
    interest_rate = models.FloatField()
    def __str__(self): 
        return self.bank_name
    

class Application(models.Model):
    
    business_launching = 'business_launching'
    house_buying = 'house_buying'
    home_improvement = 'home_improvement'
    investment = 'investment'
    education = 'education'
    other = 'other'

    
    LOAN_CHOICES = [
        ( business_launching,'business_launching'),
        (house_buying ,'house_buying'),
        (home_improvement ,'home_improvement'),
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
    min_amount = models.FloatField(default=25000)
    max_amount = models.FloatField(default=150000)
    low_interest_rate =  models.FloatField()
    illustration_rate = models.FloatField()
    initiation_fee_perecentage_rate = models.FloatField()
    monthly_service_fee = models.FloatField()
    bank_name = models.ForeignKey(Bank, null=True,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.bank_name.bank_name}"


class Help(models.Model):
    details = models.TextField()
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    message = models.TextField()


class Personal_expenditure(models.Model):
    total_salary = models.FloatField(default=10000, validators=[MinValueValidator(10000)])
    rent_or_mortgage_expense = models.FloatField(default=0)
    property_taxes = models.FloatField(default=0)
    home_owner_insurance = models.FloatField(default=0)
    water = models.FloatField(default=0)
    electricity = models.FloatField(default=0)
    household_supplies = models.FloatField(default=0)
    dining_out = models.FloatField(default=0)
    takeouts = models.FloatField(default=0)
    personal_care = models.FloatField(default=0)
    doctors_visits = models.FloatField(default=0)
    insurance_premiums = models.FloatField(default=0)
    entertainment = models.FloatField(default=0)
    credit_cards = models.FloatField(default=0)
    loan_debts = models.FloatField(default=0)
    childcare = models.FloatField(default=0)
    miscellaneous_expense = models.FloatField(default=0)
    updated_salary = models.FloatField(default=0)
    def __str__(self):
        return f"{self.updated_salary}" 
      
class Loan(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    bank_features = models.ForeignKey(Features, on_delete=models.CASCADE)
    personal_expenses = models.ForeignKey(Personal_expenditure, on_delete=models.CASCADE)
    initiation_fee = models.FloatField()
    service_fee = models.FloatField()
    loan_amount = models.FloatField()
    loan_period = models.IntegerField()
    total_amount_payable = models.FloatField(null=True, blank=True)
    monthly_installments = models.FloatField(null=True, blank=True)
    total_amount = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.bank.bank_name} - {self.loan_amount}"
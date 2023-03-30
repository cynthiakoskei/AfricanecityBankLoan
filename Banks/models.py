from django.db import models
from phone_field import PhoneField
from django.forms.widgets import DateInput
from Home.models import Loan_Request
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Bank(models.Model):
    bank_name= models.CharField(max_length=100)
    bank_url = models.URLField(default="https://www.absa.africa/", max_length=200)
    image = models.ImageField()
    interest_rate = models.FloatField()
    min_loan_amount = models.IntegerField()
    max_loan_amount = models.IntegerField()
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
    min_amount = models.FloatField()
    max_amount = models.FloatField()
    low_interest_rate =  models.DecimalField(max_digits=4, decimal_places=2)
    illustration_rate = models.DecimalField(max_digits=4, decimal_places=2)
    amount_borrowed = models.FloatField()
    initiation_fee = models.FloatField()
    monthly_service_fee = models.FloatField()
    amount_payable = models.FloatField()
    monthly_installment_amount = models.FloatField()
    bank_name = models.ForeignKey(Bank, null=True,on_delete=models.CASCADE)

    def _str_(self): 
        return str(self.bank_name)
class Loan(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    initiation_fee = models.FloatField()
    service_fee = models.FloatField()
    illustration_rate = models.FloatField()
    loan_amount = models.IntegerField()
    loan_period = models.IntegerField()
    total_amount_payable = models.FloatField(null=True, blank=True)
    monthly_installments = models.FloatField(null=True, blank=True)
    total_amount = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.bank.bank_name} - {self.loan_amount}"

class Help(models.Model):
    details = models.TextField()
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    message = models.TextField()


class Personal_expenditure(models.Model):
    loan_request = models.ForeignKey(Loan_Request, on_delete=models.CASCADE, default=10000)
   
    # Income
    salary = models.PositiveIntegerField(default=10000, validators=[MinValueValidator(10000)])

    # housing_expense
    rent_or_mortgage_expense = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    property_taxes = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    home_owner_insurance = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    
    # Utilities
    water = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    electricity = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    household_supplies = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    dining_out = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    takeouts = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])

    personal_care = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])

    # medical_expenses 
    doctors_visits = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    insurance_premiums = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])

    entertainment = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])

    #Debt_payment
    credit_cards = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    loan_debts = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])

    childcare = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    miscellaneous_expense = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])

    def update_salary(self):
        self.salary = self.loan_request.salary
        self.save()      

        
  
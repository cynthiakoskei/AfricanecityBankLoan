from django.db import models
from phone_field import PhoneField
# from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Bank(models.Model):
    bankName= models.CharField(max_length=100)
    image = models.ImageField()
    interestRate = models.DecimalField(max_digits=5, decimal_places=2)
      
    def __str__(self): 
        return self.bankName
    
# def images_path():
#     return os.path.join(settings.LOCAL_FILE_DIR, 'images')   
class Application(models.Model):
    
    business_launching = 'business_launching'
    house_buying = 'house_buying'
    home_improment = 'home_improment'
    investment = 'investment'
    educucation = 'educucation'
    other = 'other'

    
    LOAN_CHOICES = [
        ( business_launching,'business_launching'),
        (house_buying ,'house_buying'),
        (home_improment ,'home_improment'),
        (investment , 'investment'),
        (educucation ,'educucation'),
        ( other , 'other'),
            
    ]
   
    disired_loan =  models.FloatField()
    annual_income =  models.FloatField()
    loan_will_be_used_for = models.CharField(max_length = 250, choices=LOAN_CHOICES,
        default=business_launching,
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    # marital_status = models.CharField(max_length = 250, choices=MARITAL_CHOICES,default=single)
    email = models.EmailField(max_length=254)
    phoneNumber = PhoneField(blank=True, help_text='Contact phone number')
    home_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state_province = models.CharField(max_length=100)
    postal_code = models.CharField( max_length=6)
    
class Features(models.Model):
    min_amount = models.FloatField()
    max_amount = models.FloatField()
    low_interest_rate =  models.DecimalField(max_digits=3, decimal_places=2)
    illustration_rate = models.DecimalField(max_digits=3, decimal_places=2)
    amount_borrowed = models.FloatField()
    initiation_fee = models.FloatField()
    monthly_service_fee = models.FloatField()
    amount_payable = models.FloatField()
    monthly_installment_amount = models.FloatField()
    
        
    # years_of_residence= models.CharField( choices=STAY_CHOICES,
        
    # )
    
    #EMPLOYMENT INFORMATION
    # year1 ='years1',
    # year2 ='years2',
    # year3 ='years3',
    # year4 ='years5'
    # EXPERIENCE_CHOICES = [
    #   (year1,'years1'),
    #   (year2,'years2'),
    #   (year3,'years3'),
    #   (year4 ,'years5')  
    # ]
# class PaymentInfo(models.Model):
#     first_name=models.CharField(max_length=100)
#     last_name=models.CharField(max_length=100)
#     occupation= models.IntegerField()
#     # year_of_experience = models.CharField(max_length = 250, choices=EXPERIENCE_CHOICES,default=year1)
#     gross_monthly_income = models.FloatField()
#     monthly_rent= models.FloatField()
#     down_payment = models.FloatField()
#     comments = models.CharField(max_length=250)
    
# class BankInfo(models.Model):
#     institution_name = models.CharField(max_length=100) 
#     saving_account = models.IntegerField()
#     bank_address = models.CharField(max_length=100)
#     phone_number = models.IntegerField()
    
    # consent = models. BooleanField(null = True)
    
    
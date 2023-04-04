from django import forms
from .models import Bank,Application,Contact,Personal_expenditure,Loan,Loan_Request
class BankForm(forms.ModelForm):
    class Meta:
        model =Bank
        fields =[
            "bank_name",
            "image",
            "interest_rate", 
        ]


class ApplicationForm(forms.ModelForm):
    
    class Meta:
        model = Application
        fields = "__all__"  

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = [
            "name",
            "email",
            "message", 
        ]
  
#form that sums up the personal expenditures and a calculator to deduct the expenses from the salary
class expenditureForm(forms.ModelForm):
    #define a variable to save the updated salary
    updated_salary = forms.DecimalField(label="updated_salary", disabled=True)    
    class Meta:
        #connect the model(Personal_expenditure)
        model = Personal_expenditure
        fields = ['total_salary','rent_or_mortgage_expense', 'property_taxes', 'home_owner_insurance', 'water',
                  'electricity', 'household_supplies', 'dining_out', 'takeouts', 'personal_care',
                  'doctors_visits', 'insurance_premiums', 'entertainment', 'credit_cards', 'loan_debts',
                  'childcare', 'miscellaneous_expense']
        #what appears in the html template(form)
        widgets = {
            'total_salary': forms.Select(attrs={'class': 'form-select'}),#the user selcts his account(sallary) in a dropdown menu
            'rent_or_mortgage_expense': forms.NumberInput(attrs={'class': 'form-control'}),
            'property_taxes': forms.NumberInput(attrs={'class': 'form-control'}),
            'home_owner_insurance': forms.NumberInput(attrs={'class': 'form-control'}),
            'water': forms.NumberInput(attrs={'class': 'form-control'}),
            'electricity': forms.NumberInput(attrs={'class': 'form-control'}),   
            'household_supplies': forms.NumberInput(attrs={'class': 'form-control'}),
            'dining_out': forms.NumberInput(attrs={'class': 'form-control'}),
            'takeouts': forms.NumberInput(attrs={'class': 'form-control'}),
            'personal_care': forms.NumberInput(attrs={'class': 'form-control'}),
            'doctors_visits': forms.NumberInput(attrs={'class': 'form-control'}),
            'insurance_premiums': forms.NumberInput(attrs={'class': 'form-control'}),
            'entertainment': forms.NumberInput(attrs={'class': 'form-control'}),
            'credit_cards': forms.NumberInput(attrs={'class': 'form-control'}),
            'loan_debts': forms.NumberInput(attrs={'class': 'form-control'}),
            'childcare': forms.NumberInput(attrs={'class': 'form-control'}),
            'miscellaneous_expense': forms.NumberInput(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['updated_salary'].initial = 0
    #function to calculate the total expenses and deduct from the initial salary    
    def calculate_deficit(self):
        cleaned_data = super().clean()
        initial_salary = cleaned_data.get('total_salary')#get what the user selcted in the dropdown menu and links it with the total_salary field in the model
        raw_salary = initial_salary.salary#gets salary from the loan request model and saves it in raw_salary variable
        #loops through all the fields and takes it as cleaned data then adds and saves it on expenses_total
        expenses_total = sum([cleaned_data.get(field, 0) for field in self.Meta.fields[2:]])
        #if the total expenses is more than the raw_salary raise an error to the user
        if expenses_total > raw_salary:
            raise forms.ValidationError('Total expenses cannot exceed salary')
        #deduct the total expenses from the raw_salary and save it to updated salary
        updated_salary = raw_salary - expenses_total
        #take the updated salary as cleaned data 
        cleaned_data['updated_salary'] = updated_salary
        #return all the cleaned data for them to be saved in the model
        return cleaned_data
    
class LoanCalculatorForm(forms.ModelForm):
    # These fields will be shown in the form
    monthly_installments = forms.DecimalField(label="Monthly Installments", disabled=True)
    total_interest = forms.DecimalField(label="Total Interest", disabled=True)
    total_amount = forms.DecimalField(label="Total Amount", disabled=True)
    total_amount_payable = forms.DecimalField(label="Amount Payable", disabled=True)
    affordability = forms.DecimalField(label="Affordability", disabled=True)
    initiation_fee = forms.DecimalField(label="initiation_fee", disabled=True)

    class Meta:
        model = Loan
        # These fields from the Loan model will be used in the form
        fields = ['bank','bank_features','personal_expenses','loan_amount','loan_period']
        widgets = {
            'bank': forms.Select(attrs={'class': 'form-select'}),
            'personal_expenses': forms.Select(attrs={'class': 'form-select'}),
            'loan_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'loan_period': forms.NumberInput(attrs={'class': 'form-control'}),
            'bank_features': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set the initial value for the form fields to zero
        self.fields['monthly_installments'].initial = 0
        self.fields['total_interest'].initial = 0
        self.fields['total_amount'].initial = 0
        self.fields['total_amount_payable'].initial = 0
        self.fields['affordability'].initial = 0
        self.fields['initiation_fee'].initial = 0

    def calculate_loan(self):
        # Get the cleaned data from the form
        cleaned_data = super().clean()
        bank = cleaned_data.get('bank')
        bank_features = cleaned_data.get('bank_features')
        personal_expenses = cleaned_data.get('personal_expenses')
        loan_amount = cleaned_data.get('loan_amount')
        loan_period = cleaned_data.get('loan_period')
        # Get the required fields from the selected bank and bank_features models
        interest_rate = bank.interest_rate
        illustration_rate = bank_features.illustration_rate
        initiation_fee_perecentage_rate = bank_features.initiation_fee_perecentage_rate
        min_amount = bank_features.min_amount
        max_amount = bank_features.max_amount
        # Check if the loan amount is within the allowable range
        if loan_amount > max_amount:
            raise forms.ValidationError('Loan amount cannot exceed the maximum loan amount limit')
        elif loan_amount < min_amount:
            raise forms.ValidationError('Loan amount cannot be below the banks minimum loan amount limit')
        
        #get the bank_name and bank_url from the bank model
        bank_name = bank.bank_name
        bank_url = bank.bank_url
        service_fee = bank_features.monthly_service_fee 
        salary = personal_expenses.updated_salary
        #to get the monthly interest rate divide the interest rate by 12
        monthly_interest_rate = interest_rate / 100 / 12
        num_payments = loan_period
        
        # Calculate the annuity factor|> A = (r * (1 + r)^n) / ((1 + r)^n - 1)|>r = monthly interest rate|>n = total number of payments (loan period * 12)
        annuity_factor = (monthly_interest_rate * pow(1 + monthly_interest_rate, num_payments)) / (pow(1 + monthly_interest_rate, num_payments) - 1)
        # Calculate the monthly payment, total amount, and total interest
        monthly_payment = round(loan_amount * annuity_factor, 2)
        total_amount = round(monthly_payment * num_payments, 2)
        total_interest = round(total_amount - loan_amount, 2)
        # Calculate the initiation fee, service fee, illustration fee, and total amount payable
        initiation_fee_percentage_rate= initiation_fee_perecentage_rate / 100
        initiation_fee = round((loan_amount * initiation_fee_percentage_rate), 2)
        service_fee = round(service_fee * num_payments, 2)
        illustration_fee = round(loan_amount * illustration_rate / 100, 2)
        total_amount_payable = round(total_amount + initiation_fee + service_fee + illustration_fee, 2)
        # Calculate the affordability based on 30% of the updated salary
        affordability = round((salary * 0.3), 2)
        
        # Update the cleaned_data dictionary with the calculated values
        cleaned_data['monthly_installments'] = monthly_payment
        cleaned_data['total_interest'] = total_interest
        cleaned_data['total_amount'] = total_amount
        cleaned_data['total_amount_payable'] = total_amount_payable
        cleaned_data['bank_name'] = bank_name
        cleaned_data['bank_url'] = bank_url
        cleaned_data['service_fee'] = service_fee
        cleaned_data['affordability'] = affordability
        cleaned_data['initiation_fee'] = initiation_fee
        
        return cleaned_data
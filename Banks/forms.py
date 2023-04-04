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

class expenditureForm(forms.ModelForm):
    class Meta:
        model = Personal_expenditure
        fields = [
            'rent_or_mortgage_expense',
            'property_taxes',
            'home_owner_insurance',
            'water',
            'electricity',
            'household_supplies',
            'dining_out',
            'takeouts',
            'personal_care',
            'doctors_visits',
            'insurance_premiums',
            'entertainment',
            'credit_cards',
            'loan_debts',
            'childcare',
            'miscellaneous_expense',
        ]       

class expenditureForm(forms.ModelForm):
    updated_salary = forms.DecimalField(label="updated_salary", disabled=True)    
    class Meta:
        model = Personal_expenditure
        fields = ['total_salary','rent_or_mortgage_expense', 'property_taxes', 'home_owner_insurance', 'water',
                  'electricity', 'household_supplies', 'dining_out', 'takeouts', 'personal_care',
                  'doctors_visits', 'insurance_premiums', 'entertainment', 'credit_cards', 'loan_debts',
                  'childcare', 'miscellaneous_expense']
        widgets = {
            'total_salary': forms.Select(attrs={'class': 'form-select'}),
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
        
    def calculate_deficit(self):
        cleaned_data = super().clean()
        initial_salary = cleaned_data.get('total_salary')
        raw_salary = initial_salary.salary
        expenses_total = sum([cleaned_data.get(field, 0) for field in self.Meta.fields[2:]])
        
        if expenses_total > raw_salary:
            raise forms.ValidationError('Total expenses cannot exceed salary')

        updated_salary = raw_salary - expenses_total
        cleaned_data['updated_salary'] = updated_salary

        return cleaned_data
    
class LoanCalculatorForm(forms.ModelForm):
    monthly_installments = forms.DecimalField(label="Monthly Installments", disabled=True)
    total_interest = forms.DecimalField(label="Total Interest", disabled=True)
    total_amount = forms.DecimalField(label="Total Amount", disabled=True)
    total_amount_payable = forms.DecimalField(label="Amount Payable", disabled=True)
    affordability = forms.DecimalField(label="Affordability", disabled=True)
    initiation_fee = forms.DecimalField(label="initiation_fee", disabled=True)    
    class Meta:
        model = Loan
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
        self.fields['monthly_installments'].initial = 0
        self.fields['total_interest'].initial = 0
        self.fields['total_amount'].initial = 0
        self.fields['total_amount_payable'].initial = 0
        self.fields['affordability'].initial = 0
        self.fields['initiation_fee'].initial = 0

    def calculate_loan(self):
        cleaned_data = super().clean()
        bank = cleaned_data.get('bank')
        bank_features = cleaned_data.get('bank_features')
        personal_expenses = cleaned_data.get('personal_expenses')
        loan_amount = cleaned_data.get('loan_amount')
        loan_period = cleaned_data.get('loan_period')

        interest_rate = bank.interest_rate
        illustration_rate = bank_features.illustration_rate
        initiation_fee_perecentage_rate = bank_features.initiation_fee_perecentage_rate
        min_amount = bank_features.min_amount
        max_amount = bank_features.max_amount
        if loan_amount > max_amount:
            raise forms.ValidationError('Loan amount cannot exceed the maximum loan amount limit')
        elif loan_amount < min_amount:
            raise forms.ValidationError('Loan amount cannot be below the banks minimum loan amount limit')

        bank_name = bank.bank_name
        bank_url = bank.bank_url
        service_fee = bank_features.monthly_service_fee 
        salary = personal_expenses.updated_salary
        monthly_interest_rate = interest_rate / 100 / 12
        num_payments = loan_period
        annuity_factor = (monthly_interest_rate * pow(1 + monthly_interest_rate, num_payments)) / (pow(1 + monthly_interest_rate, num_payments) - 1)
        monthly_payment = round(loan_amount * annuity_factor, 2)
        total_amount = round(monthly_payment * num_payments, 2)
        total_interest = round(total_amount - loan_amount, 2)
        initiation_fee_percentage_rate= initiation_fee_perecentage_rate / 100
        initiation_fee = round((loan_amount * initiation_fee_percentage_rate), 2)
        service_fee = round(service_fee * num_payments, 2)
        illustration_fee = round(loan_amount * illustration_rate / 100, 2)
        total_amount_payable = round(total_amount + initiation_fee + service_fee + illustration_fee, 2)
        affordability = round((salary * 0.3), 2)
        
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
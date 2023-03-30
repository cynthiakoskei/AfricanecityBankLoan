from django import forms
from .models import Bank,Application,Contact,Personal_expenditure,Loan
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
        fields = '__all__'


class LoanCalculatorForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['bank', 'initiation_fee', 'service_fee', 'illustration_rate', 'loan_amount', 'loan_period']
        widgets = {
            'bank': forms.Select(attrs={'class': 'form-select'}),
            'initiation_fee': forms.NumberInput(attrs={'class': 'form-control'}),
            'service_fee': forms.NumberInput(attrs={'class': 'form-control'}),
            'illustration_rate': forms.NumberInput(attrs={'class': 'form-control'}),
            'loan_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'loan_period': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def calculate_loan(self):
        cleaned_data = super().clean()
        bank = cleaned_data.get('bank')
        initiation_fee = cleaned_data.get('initiation_fee')
        service_fee = cleaned_data.get('service_fee')
        illustration_rate = cleaned_data.get('illustration_rate')
        loan_amount = cleaned_data.get('loan_amount')
        loan_period = cleaned_data.get('loan_period')

        interest_rate = bank.interest_rate
        monthly_interest_rate = interest_rate / 100 / 12
        num_payments = loan_period * 12
        annuity_factor = (monthly_interest_rate * pow(1 + monthly_interest_rate, num_payments)) / (pow(1 + monthly_interest_rate, num_payments) - 1)
        monthly_payment = round(loan_amount * annuity_factor, 2)
        total_amount = round(monthly_payment * num_payments, 2)
        total_interest = round(total_amount - loan_amount, 2)
        initiation_fee = round(initiation_fee, 2)
        service_fee = round(service_fee * num_payments, 2)
        illustration_fee = round(loan_amount * illustration_rate / 100, 2)
        total_amount_payable = round(total_amount + initiation_fee + service_fee + illustration_fee, 2)
        
        loan = self.save(commit=False)
        loan.total_amount_payable = total_amount_payable
        loan.monthly_installments = monthly_payment
        loan.total_amount = total_amount
        loan.save()
        
        return {
            'total_amount_payable': total_amount_payable,
            'monthly_installments': monthly_payment,
            'total_interest': total_interest,
            'total_amount': total_amount,
            'initiation_fee': initiation_fee,
            'service_fee': service_fee,
            'illustration_fee': illustration_fee,
        }

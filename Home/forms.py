from django import forms
from .models import Loan_Request

class LoanRequestForm(forms.ModelForm):
    class Meta:
        model = Loan_Request
        fields =[
            "Loan_amount",
            
        ]

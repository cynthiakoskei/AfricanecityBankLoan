from django import forms
from .models import Bank,Application

class BankForm(forms.ModelForm):
    class Meta:
        model =Bank
        fields =[
            "bankName",
            "image",
            "interestRate", 
        ]


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = "__all__"        
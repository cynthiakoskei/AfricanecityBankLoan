from django import forms
from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper
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
    helper = FormHelper()
    class Meta:
        model = Application
        fields = "__all__"        

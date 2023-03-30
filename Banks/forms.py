from django import forms
from .models import Bank,Application,Contact,Personal_expenditure

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
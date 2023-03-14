from django import forms
from .models import Bank,Application,ContactInfo,PaymentInfo

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
class ContactInfoForm(forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = "__all__"          
class PaymentInfoForm(forms.ModelForm):
    class Meta:
        model = PaymentInfo
        fields = "__all__"          
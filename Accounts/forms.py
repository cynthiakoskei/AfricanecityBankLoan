from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomerSignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=250,help_text='e.g youremail@gmail.com')
    
    class Meta:
        model = User
        fields = ("username","email","password1","password2")
        
    def save(self, commit=True):
        user = super(CustomerSignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
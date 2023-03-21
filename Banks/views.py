from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Bank,Application,Features,Help,Contact
from .forms import BankForm,ApplicationForm,ContactForm

# Create your views here.
def bank_list(request):
    listings = Bank.objects.all()
    
    context = {
        "listings":listings
    }
   
    return render(request,"view.html",context)

def bank_create(request):
    form = BankForm()
    if request.method == "POST":
        form = BankForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    
    context = {
        "form":form
    }
   
    return render(request,"bank.html",context)

def about(request):
    form = BankForm()
    if request.method == "POST":
        form = BankForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    
    context = {
        "form":form
    }
   
    return render(request,"about.html",context)

def applicant_create(request):
    form = ApplicationForm()
    if request.method == "POST":
        form = ApplicationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    
    context = {
        "form":form
    }
   
    return render(request,"applicantForm.html",context)

def features_view(request):
    listings = Features.objects.all()
    
    context = {
        "listings":listings
    }
   
    return render(request,"loanFeatures.html",context)

def help(request):
    listings = Help.objects.all()
    
    context = {
        "listings":listings
    }
   
    return render(request,"help.html",context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Get the user's name, email, and message from the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Construct the email message
            subject = f"{name} - Loan Application Inquiry"
            from_email = email
            to_email = [settings.DEFAULT_FROM_EMAIL]
            message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

            # Send the email
            send_mail(subject, message, from_email, to_email, fail_silently=False)

            # Show a success message to the user
            messages.success(request, 'Your message has been sent. We will get back to you soon.')

            # Redirect the user back to the contact page
            return redirect('/Banks/Contact/')
    else:
        # Create an empty form
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


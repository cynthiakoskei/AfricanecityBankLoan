from django.shortcuts import render,redirect
from .models import Bank,Application,Features
from .forms import BankForm,ApplicationForm

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
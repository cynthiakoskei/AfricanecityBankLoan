from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Bank,Application,Features,Help,Contact,Personal_expenditure,Loan,Loan_Request
from .forms import BankForm,ApplicationForm,ContactForm,expenditureForm,LoanCalculatorForm

# Create your views here.
def bank_list(request):
    banks = Bank.objects.all()
    
    context = {
        "banks": banks
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

def feature_detail(request, bank_name_id):
    bank = Bank.objects.get(pk=bank_name_id)
    features = Features.objects.filter(bank_name=bank)
    return render(request, 'loanFeatures.html', {'bank': bank, 'features': features})


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

#create
def create_loan_application(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            loan_application = form.save(commit=False)
            loan_application.user = request.user
            loan_application.save()
            return redirect('Loan Detail/', pk=loan_application.pk)
    else:
        form = ApplicationForm()
    return render(request, 'create_loan_application.html', {'form': form})

#read
def loan_detail(request, pk):
    loan_application = get_object_or_404(ApplicationForm, pk=pk)
    return render(request, 'loan_detail.html', {'loan_application': loan_application})

#update
def update_loan_application(request, pk):
    loan_application = get_object_or_404(ApplicationForm, pk=pk)
    if request.method == 'POST':
        form = ApplicationForm(request.POST, instance=loan_application)
        if form.is_valid():
            loan_application = form.save(commit=False)
            loan_application.user = request.user
            loan_application.save()
            return redirect('loan_detail', pk=loan_application.pk)
    else:
        form = ApplicationForm(instance=loan_application)
    return render(request, 'update_loan_application.html', {'form': form})

#delete
def delete_loan_application(request, pk):
    loan_application = get_object_or_404(ApplicationForm, pk=pk)
    loan_application.delete()
    return redirect('')


def expenditure_form_view(request):
    if request.method == 'POST':
        form = expenditureForm(request.POST)
        if form.is_valid():
            expenses = form.save(commit=False)
            loan_request = form.calculate_deficit()
            expenses.updated_salary = loan_request['updated_salary']
            expenses.save()
            return redirect('loan_calculator')
    else:
        form = expenditureForm()

    return render(request, 'personalExpenditures.html',{'form': form})

def loan_calculator(request):
    if request.method == 'POST':
        form = LoanCalculatorForm(request.POST)
        if form.is_valid():
            loan = form.save(commit=False)
            loan_result = form.calculate_loan()
            loan.total_amount_payable = loan_result['total_amount_payable']
            loan.monthly_installments = loan_result['monthly_installments']
            loan.total_amount = loan_result['total_amount']
            loan.save()
            return render(request, 'result.html', {'result': loan_result})
    else:
        form = LoanCalculatorForm()

    return render(request, 'loan_calculator.html', {'form': form})
from django.shortcuts import render,redirect
from .models import Loan_Request
from .forms import LoanRequestForm

# Create your views here.



def loan_create(request):
    form = LoanRequestForm()
    if request.method == "POST":
        form = LoanRequestForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('bank_list')
    
    context = {
        "form":form
    }
    return render(request, 'index.html', context)
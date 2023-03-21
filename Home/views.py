from django.shortcuts import render
from .models import Loan_Request
from .forms import LoanRequestForm

# Create your views here.
def index(request):
    return render(request, 'index.html')


def loan_create(request):
    form = LoanRequestForm()
    if request.method == "POST":
        form = LoanRequestForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    
    context = {
        "form":form
    }
    return render(request, 'test.html', context)
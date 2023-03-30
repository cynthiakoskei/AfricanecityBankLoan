from django.urls import path
from . import views

urlpatterns = [
	path('Views/',views.bank_list,name="bank_list"),
 	path('Create/',views.bank_create,name="bank_create"),
    path('About Us/',views.about, name="about us"),
    path('Applicant/',views.create_loan_application, name="applicant"),
    path('Features/<int:bank_name_id>/',views.feature_detail, name="features"),
    path('Help/',views.help, name="help"),
    path('Contact/',views.contact, name="contact"),
    path('Loan Detail/<int:pk>/',views.loan_detail, name="loan_detail"),
]


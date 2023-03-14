from django.urls import path
from . import views

urlpatterns = [
	path('Views/',views.bank_list,name="bank_list"),
 	path('Create/',views.bank_create,name="bank_create"),
    path('About Us/',views.about, name="about"),
    path('Applicant/',views.applicant_create, name="applicant"),
]

from django.contrib import admin
from .models import Bank,Application,Features
# Register your models here.

admin.site.register(Bank)
admin.site.register(Features)
class ApplicationAdmin(admin.ModelAdmin):
    list_diplay = ['desired_loan','annual_income','loan_will_be_used_for','first_name','last_name','birth_date','email','phoneNumber','home_address','city','state_province','postal_code']
    searchfields = ['desired_loan','annual_income','loan_will_be_used_for','first_name','last_name','birth_date','email','phoneNumber','home_address','city','state_province','postal_code']
    list_per_page = 10
admin.site.register(Application, ApplicationAdmin)	





from django.contrib import admin
from .models import Bank,Application,ContactInfo,PaymentInfo,BankInfo
# Register your models here.

admin.site.register(Bank)	
admin.site.register(Application)	
admin.site.register(ContactInfo)
admin.site.register(PaymentInfo)
admin.site.register(BankInfo)


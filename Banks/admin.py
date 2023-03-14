from django.contrib import admin
from .models import Bank,Application,ContactInfo
# Register your models here.

admin.site.register(Bank)	
admin.site.register(Application)	
admin.site.register(ContactInfo)


from django.contrib import admin
from Hostel.models import Boys, Girls 

# Register your models here.

class boysAdmin(admin.ModelAdmin) :
    list_display =('first_name','last_name','mobile_no','parent_mobile_no','gender','email','address_1','address_2','college_name','course','year')
admin.site.register(Boys,boysAdmin)

class girlsAdmin(admin.ModelAdmin) :
    list_display =('first_name','last_name','mobile_no','parent_mobile_no','gender','email','address_1','address_2','college_name','course','year')
admin.site.register(Girls,girlsAdmin)
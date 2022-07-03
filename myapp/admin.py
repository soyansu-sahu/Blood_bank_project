from django.contrib import admin
from .models import BloodGroup,UserDetails,RequestBlood
# Register your models here.
@admin.register(RequestBlood)
class RequestBloodadmin(admin.ModelAdmin):
    pass 
    
@admin.register(BloodGroup)
class RequestBloodadmin(admin.ModelAdmin):
    pass

@admin.register(UserDetails)
class RequestBloodadmin(admin.ModelAdmin):
    pass     


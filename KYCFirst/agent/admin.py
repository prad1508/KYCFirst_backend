from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Agent

class AgentAdmin(UserAdmin):
    list_display=['username','email','biometric_details','mobile_no','Checker','Maker','Approver','company']

    class Meta:
        verbose_name = "Agent"
    filter_horizontal=()
    list_filter=()
    fieldsets=() 

admin.site.register(Agent,AgentAdmin)
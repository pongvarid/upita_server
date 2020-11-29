from django.contrib import admin

# Register your models here.
from django.contrib import admin 
from .models import *
from django.contrib.auth.models import User

admin.site.site_header = 'ระบบ ITA'

# class user_cut_coinAdmin(admin.ModelAdmin): 
#     list_display = ('name','coin','coin_score','created_at','updated_at') 
#     list_filter = ('cut_coin',)
# admin.site.register(user_cut_coin,user_cut_coinAdmin)
admin.site.register(AgencyType)

class AgencyAdmin(admin.ModelAdmin): 
    list_display = ('name','agency_type','count','percent','eit','iit')
    list_filter = ('agency_type',)
    search_fields = ['name']
admin.site.register(Agency,AgencyAdmin)

admin.site.register(Year)

class RateAdmin(admin.ModelAdmin): 
    list_display = ('number','name','detail','year','created_at') 
    list_filter = ('year','number')
    search_fields = ['name','number']
admin.site.register(Rate,RateAdmin)

admin.site.register(RateStatus)
class RateResultAdmin(admin.ModelAdmin): 
    autocomplete_fields = ['rate','agency']  
    list_display = ('number','rate','rate_status','register_type','urls','agency','score','tester','passing','created_at') 
    list_filter = ('rate','agency','rate__year','passing')
    search_fields = ['rate__number','rate__name']
admin.site.register(RateResult,RateResultAdmin)

class UserAdmin(admin.ModelAdmin): 
    autocomplete_fields = ['agency','user']  
    list_display = ('full_name','agency','register_type','status','passing','in_up') 
    list_filter = ('agency','passing','status','in_up')
    search_fields = ['full_name']
admin.site.register(Profile,UserAdmin) 
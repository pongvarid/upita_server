from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from rest_framework.exceptions import ValidationError

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
    list_display = ('number','type','name','detail','year','created_at')
    list_filter = ('year','number','type')
    search_fields = ['name','number','type']
admin.site.register(Rate,RateAdmin)

admin.site.register(RateStatus)
class RateResultAdmin(admin.ModelAdmin): 
    autocomplete_fields = ['rate','agency']  
    list_display = ('number','rate','rate_status','register_type','urls','agency','score','tester','passing','created_at') 
    list_filter = ('rate','agency','rate__year','passing')
    search_fields = ['rate__number','rate__name']
admin.site.register(RateResult,RateResultAdmin)

class UserProfileInline(admin.StackedInline):
    model = Profile
    can_delete = True
    verbose_name_plural = 'รายระเอียดผู้ใช้'
    autocomplete_fields = ['agency',]

class CustomUserCreationForm(UserCreationForm):
    # make fields required if desired
    # first_name = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        fields = ("username", "first_name", "last_name")


# Define a new User admin
class MyUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2','email',
                       'first_name', 'last_name'),
        }),
    )

    inlines = UserProfileInline,
admin.site.unregister(User)
admin.site.register(User,MyUserAdmin)
# class UserAdmin(admin.ModelAdmin):
#     autocomplete_fields = ['agency','user']
#     list_display = ('full_name','agency','register_type','status','passing','in_up','oit')
#     list_filter = ('agency','passing','status','in_up')
#     search_fields = ['full_name']
# admin.site.register(Profile,UserAdmin)
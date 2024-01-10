from django.contrib import admin
from django.contrib.admin.models import LogEntry

# Register your models here.
from oit.models import EvaluateOIT
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter,RelatedOnlyDropdownFilter


class EvaluateOITAdmin(admin.ModelAdmin):
    # inlines = [IssueInline, ]
    # autocomplete_fields = ['farm','gender','color','status','status_breed']
    # search_fields = ['name','farm__name',]
    # autocomplete_fields = ['name',]
    # list_filter = ('agency',)
    # ordering = ('order',)
    list_display = ('name_data','agency','score','comment','rate_status','tester','created_at')
    search_fields = ('rate__name',)
    list_filter = ['agency','rate','rate__year','score']
    def name_data(self,obj):
        return obj.rate.number
admin.site.register(EvaluateOIT,EvaluateOITAdmin)

class LogAdmin(admin.ModelAdmin):
    # inlines = [IssueInline, ]
    # autocomplete_fields = ['farm','gender','color','status','status_breed']
    # search_fields = ['name','farm__name',]
    # autocomplete_fields = ['name',]
    # list_filter = ('agency',)
    # ordering = ('order',)
    list_display = ('user',)
    # search_fields = ('user__firstname',)
    # list_filter = (
    #     # for ordinary fields
    #     ('user', RelatedDropdownFilter)
    #     )
admin.site.register(LogEntry,LogAdmin)
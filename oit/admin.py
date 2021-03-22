from django.contrib import admin

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
    list_display = ('name','agency','score','rate_status','tester','created_at')
    search_fields = ('rate__name',)
    list_filter = (
        # for ordinary fields
        ('agency', RelatedDropdownFilter),
        # for choice fields
        ('rate__year', RelatedDropdownFilter),
        ('score', DropdownFilter),
    )
admin.site.register(EvaluateOIT,EvaluateOITAdmin)

from import_export import resources

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

# Register your models here.
from eit.models import  *
from ita.models import Agency, ReportAgencyEit
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter, RelatedOnlyDropdownFilter,RelatedOnlyFieldListFilter
from import_export.admin import ImportExportModelAdmin
from admin_auto_filters.filters import AutocompleteFilter

admin.site.register(Year)


# admin.site.register(Choice)
admin.site.register(Ascend)
admin.site.register(Exist)
admin.site.register(Answer)


class AssessmentIssuesAdmin(admin.ModelAdmin):
    # inlines = [IssueInline, ]
    # autocomplete_fields = ['farm','gender','color','status','status_breed']
    # search_fields = ['name','farm__name',]
    # autocomplete_fields = ['name',]
    list_filter = ('year',)
    ordering = ('order',)
    list_display = ('name','order','year',)
    search_fields = ('name',)
admin.site.register(AssessmentIssues,AssessmentIssuesAdmin)


class IssueInline(admin.TabularInline):
    model = IssueDetail
    fk_name = "issue"
    # filter_horizontal = ('choice',)
    def get_extra(self, request, obj=None, **kwargs):
        extra = 1
        return extra

class IssueAdmin(admin.ModelAdmin):
    inlines = [IssueInline, ]
    # autocomplete_fields = ['farm','gender','color','status','status_breed']
    search_fields = ['name',]
    # autocomplete_fields = ['name',]
    ordering = ('order',)
    list_display = ('fullName','assessment','type',) 
    list_filter = (
        # for ordinary fields
        ('assessment__year', RelatedDropdownFilter),
        # for choice fields
        ('assessment', RelatedDropdownFilter),
    )

admin.site.register(Issue,IssueAdmin)

class AnswerIssueAdmin(admin.ModelAdmin):
    # inlines = [IssueInline, ]
    # autocomplete_fields = ['farm','gender','color','status','status_breed']
    search_fields = ['assessmentIssues__name','agency__name','issue__name','user__email','user__username','user__first_name','user__last_name']
    # autocomplete_fields = ['name',]
    ordering = ('issue__order',)
    list_display = ( 'agency_name','assessmentIssues_name','issue_name','issueDetail_name','value','user_name','user_email')
    # list_filter = ('agency','assessmentIssues','issue')
    list_filter = (
        ('agency', RelatedOnlyDropdownFilter),
        ('assessmentIssues',RelatedOnlyDropdownFilter),
        ('issue', RelatedOnlyDropdownFilter),
        ('year',DropdownFilter),)

admin.site.register(AnswerIssueEit,AnswerIssueAdmin)

class AnswerSuggestionAdmin(admin.ModelAdmin):
    # inlines = [IssueInline, ]
    # autocomplete_fields = ['farm','gender','color','status','status_breed']
    search_fields = ['agency__name', 'user__first_name', 'user__last_name','user__email']
    # autocomplete_fields = ['name',]
    # ordering = ('issue__order',)
    list_display = ( 'agency_name' ,'user_name','suggestion', 'year','user_email')
    list_filter = (
        ('agency', RelatedOnlyDropdownFilter),
        ('year',DropdownFilter),)
admin.site.register(AnswerSuggestionEit,AnswerSuggestionAdmin)


class ReportAgencyEitResource(resources.ModelResource):

    class Meta:
        model = ReportAgencyEit
        fields = ('name','tel','email','other', 'type' ,'agency__name', 'year__year','created_at',)



class AgencyFilter(AutocompleteFilter):
    title = 'Agency' # display title
    field_name = 'agency' # name of the foreign key field



class ReportAgencyEitAdmin(ImportExportModelAdmin):
    resource_class = ReportAgencyEitResource
    # inlines = [IssueInline, ]
    # autocomplete_fields = ['farm','gender','color','status','status_breed']
    # search_fields = [ 'agency__name','issue__name']
    autocomplete_fields = ['agency',]
    # ordering = ('issue__order',)
    search_fields = ['name','tel','email','type']
    list_display = ('name','tel','email','type','agency', 'year'  )
    # list_filter = ('year', 'type', 'agency')
    list_filter = (
        ('agency', RelatedDropdownFilter),
        ('year', RelatedDropdownFilter),
        ('type', DropdownFilter),
    )
admin.site.register(ReportAgencyEit,ReportAgencyEitAdmin)
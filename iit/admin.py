from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter

# Register your models here.
from iit.models import  *

admin.site.register(Year)
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
    list_display = ('name','order','year')
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
    # search_fields = ['name','farm__name',]
    # autocomplete_fields = ['name',]
    ordering = ('order',)
    search_fields = ['name', ]
    list_display = ('fullName','assessment','type',)
    # list_filter = ('assessment__year','assessment',)

    list_filter = (
        # for ordinary fields
        ('assessment__year', DropdownFilter),
        # for choice fields
        ('assessment', ChoiceDropdownFilter),
    )
admin.site.register(Issue,IssueAdmin)


class AnswerIssueAdmin(admin.ModelAdmin):
    # inlines = [IssueInline, ]
    # autocomplete_fields = ['farm','gender','color','status','status_breed']
    search_fields = ['assessmentIssues__name','agency__name','issue__name','user__email','user__username','user__first_name','user__last_name']
    # autocomplete_fields = ['name',]
    ordering = ('issue__order',)
    list_display = ( 'agency_name','assessmentIssues_name','issue_name','issueDetail_name','value_by','user_name','user_email')
    # list_filter = ('agency','assessmentIssues','user','issue','value_by')
    list_filter = (
        ('agency', RelatedDropdownFilter),
        ('assessmentIssues', RelatedDropdownFilter),
        # ('user', RelatedDropdownFilter),
        ('issue', RelatedDropdownFilter),
        ('value_by', DropdownFilter),
        ('year', DropdownFilter),
    )

admin.site.register(AnswerIssue,AnswerIssueAdmin)

class AnswerSuggestionAdmin(admin.ModelAdmin):
    # inlines = [IssueInline, ]
    # # autocomplete_fields = ['farm','gender','color','status','status_breed']
    search_fields = [ 'agency__name','user__first_name','user__last_name','user__email']
    # autocomplete_fields = ['name',]
    # ordering = ('issue__order',)
    list_display = ( 'agency_name' ,'user_name', 'year','user_email')
    # list_filter = ('agency','issue')
admin.site.register(AnswerSuggestion,AnswerSuggestionAdmin)
# admin.site.register(IssueDetail)

class UserInAnswerAdmin(admin.ModelAdmin):
    search_fields = [ 'agency__name','user__first_name','user__last_name','user__email']
    list_display = ( 'agency_name' ,'user_name','user_email', 'year','created_at')
    list_filter = ('agency',)
    list_filter = (
        ('agency', RelatedDropdownFilter),
        ('year',DropdownFilter),)
admin.site.register(UserInAnswer,UserInAnswerAdmin)

class IssueDetailadmin(admin.ModelAdmin):
    search_fields = [ 'sub_name',]
    list_display = ( 'sub_name' ,'choiceType', 'choiceTypeData','created_at')
    list_filter = ('issue',)
admin.site.register(IssueDetail,IssueDetailadmin)
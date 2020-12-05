from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

# Register your models here.
from eit.models import  *
from ita.models import Agency
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
    search_fields = ['name',]
    # autocomplete_fields = ['name',]
    ordering = ('order',)
    list_display = ('fullName','assessment','type',)
    list_filter = ('assessment__year','assessment',)

admin.site.register(Issue,IssueAdmin)

class AnswerIssueAdmin(admin.ModelAdmin):
    # inlines = [IssueInline, ]
    # autocomplete_fields = ['farm','gender','color','status','status_breed']
    search_fields = ['assessmentIssues__name','agency__name','issue__name']
    # autocomplete_fields = ['name',]
    ordering = ('issue__order',)
    list_display = ( 'agency_name','assessmentIssues_name','issue_name','issueDetail_name','value','user_name')
    list_filter = ('agency','assessmentIssues','issue')

admin.site.register(AnswerIssueEit,AnswerIssueAdmin)

class AnswerSuggestionAdmin(admin.ModelAdmin):
    # inlines = [IssueInline, ]
    # autocomplete_fields = ['farm','gender','color','status','status_breed']
    # search_fields = [ 'agency__name','issue__name']
    # autocomplete_fields = ['name',]
    # ordering = ('issue__order',)
    list_display = ( 'agency_name' ,'user_name', 'year')
    # list_filter = ('agency','issue')
admin.site.register(AnswerSuggestionEit,AnswerSuggestionAdmin)


from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter,RelatedOnlyDropdownFilter

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
    ordering = ('-year', 'order',)
    list_display = ('name','order','year')
    search_fields = ('name',)
    list_editable = ['order']
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
        ("assessment__year"),
        # ('assessment__year', RelatedDropdownFilter),
        # for choice fields
        ('assessment', RelatedDropdownFilter),
    )
admin.site.register(Issue,IssueAdmin)

class IsVeryBenevolentFilter(admin.SimpleListFilter):
    title = 'ใครเป็นนิสิต'
    parameter_name = 'is_very_benevolent'

    def lookups(self, request, model_admin):
        return (
            ('Yes', 'Yes'),
            ('No', 'No'),
        )

    def queryset(self, request, queryset):
        value = self.value()
        profile = Profile.objects.filter(agency=41).values_list('user_id', flat=True)
        if value == 'Yes':

            return queryset.filter(user__in=profile)
        elif value == 'No':
            return queryset.exclude(user__in=profile)
        return queryset

class AnswerIssueAdmin(admin.ModelAdmin):
    # inlines = [IssueInline, ]
    # autocomplete_fields = ['farm','gender','color','status','status_breed']
    search_fields = ['assessmentIssues__name','agency__name','issue__name','user__email','user__username','user__first_name','user__last_name']
    # autocomplete_fields = ['name',]
    ordering = ('issue__order',)
    list_display = ( 'agency_name','user_student','assessmentIssues_name','issue_name','issueDetail_name','value_by','user_name','user_email')
    # list_filter = ('agency','assessmentIssues','user','issue','value_by')
    list_filter = (
        IsVeryBenevolentFilter,
        ('agency'),
        # 'user_student',
        ('assessmentIssues'),
        # ('user', RelatedDropdownFilter),
        ('issue'),
        ('value_by'),
        ('year'),
    )
    def changelist_view(self, request, extra_context=None):
        default_filter = False

        try:
            ref = request.META['HTTP_REFERER']
            pinfo = request.META['PATH_INFO']
            qstr = ref.split(pinfo)
            querystr = request.META['QUERY_STRING']

            # Check the QUERY_STRING value, otherwise when
            # trying to filter the filter gets reset below
            if querystr is None:
                if len(qstr) < 2 or qstr[1] == '':
                    default_filter = True
        except:
            default_filter = True

        if default_filter:
            q = request.GET.copy()
            q['year__id__exact'] = '4'
            request.GET = q
            request.META['QUERY_STRING'] = request.GET.urlencode()

        return super(AnswerIssueAdmin, self).changelist_view(request, extra_context=extra_context)




admin.site.register(AnswerIssue,AnswerIssueAdmin)

class AnswerSuggestionAdmin(admin.ModelAdmin):
    # inlines = [IssueInline, ]
    # # autocomplete_fields = ['farm','gender','color','status','status_breed']
    search_fields = [ 'agency__name','user__first_name','user__last_name','user__email']
    # autocomplete_fields = ['name',]
    # ordering = ('issue__order',)
    list_display = ( 'agency_name' ,'user_name','suggestion', 'year','user_email')
    list_filter = (
        ('agency'),
        ('year')
    )
    def changelist_view(self, request, extra_context=None):
        default_filter = False

        try:
            ref = request.META['HTTP_REFERER']
            pinfo = request.META['PATH_INFO']
            qstr = ref.split(pinfo)
            querystr = request.META['QUERY_STRING']

            # Check the QUERY_STRING value, otherwise when
            # trying to filter the filter gets reset below
            if querystr is None:
                if len(qstr) < 2 or qstr[1] == '':
                    default_filter = True
        except:
            default_filter = True

        if default_filter:
            q = request.GET.copy()
            q['year__id__exact'] = '4'
            request.GET = q
            request.META['QUERY_STRING'] = request.GET.urlencode()

        return super(AnswerSuggestionAdmin, self).changelist_view(request, extra_context=extra_context)

admin.site.register(AnswerSuggestion,AnswerSuggestionAdmin)
# admin.site.register(IssueDetail)


class UserInAnswerAdmin(admin.ModelAdmin):
    search_fields = [ 'agency__name','user__first_name','user__last_name','user__email']
    list_display = ( 'agency_name' ,'user_student','user_name','user_email', 'year','created_at')
    # list_filter = ('agency',)
    list_filter = (
        # 'user_student',
        IsVeryBenevolentFilter,
        ('agency'),
        ('year'),)
admin.site.register(UserInAnswer,UserInAnswerAdmin)

class IssueDetailadmin(admin.ModelAdmin):
    search_fields = [ 'sub_name',]
    list_display = ( 'sub_name' ,'choiceType', 'choiceTypeData','created_at')
    list_filter = ('issue', 'issue__assessment__year',)
 

admin.site.register(IssueDetail,IssueDetailadmin)
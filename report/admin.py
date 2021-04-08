from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter
from import_export.admin import ImportExportModelAdmin,ImportMixin, ExportMixin
# Register your models here.
from reversion.admin import VersionAdmin
from report.models import  *
from django_admin_multiple_choice_list_filter.list_filters import MultipleChoiceListFilter
from import_export import resources
from import_export.fields import Field

class StatusListFilter(MultipleChoiceListFilter):
    title = 'Agency'
    parameter_name = 'agency__in'

    def lookups(self, request, model_admin):
        return Agency.objects.values_list('pk', 'name')

class ReportAllResource(resources.ModelResource):
    agency = Field()
    class Meta:
        model = ReportAll
        fields = ('agency__name','year','iit','eit','oit','all','rate','created_at')
        export_order = ('agency__name','year','iit','eit','oit','all','rate','created_at')


class ReportAllAdmin(ImportExportModelAdmin):
    ordering = ('all',)
    search_fields = ['agency', ]
    list_display = ('agency','year','rate','iit','eit','oit','all')
    # list_filter = (StatusListFilter,)
    list_filter = (
        ('rate', DropdownFilter),
        ('year', DropdownFilter),
        StatusListFilter
    )
    resource_class = ReportAllResource
    change_list_template = 'change_list_graph.html'
admin.site.register(ReportAll,ReportAllAdmin)


class Q9Resource(resources.ModelResource):
    agency = Field()
    class Meta:
        model = ReportDetail
        fields = ('name','score','agency__name','year','created_at')
        export_order = ('name','score','agency__name','year','created_at')
class ReportDetailAdmin(ImportExportModelAdmin):

    search_fields = ['agency', ]
    list_display = ('name','score','agency','year')
    # list_filter = (StatusListFilter,)
    list_filter = (
        ('year', DropdownFilter),
        ('name', DropdownFilter),
        StatusListFilter
    )
    resource_class = Q9Resource
    change_list_template = 'graph.html'
admin.site.register(ReportDetail,ReportDetailAdmin)




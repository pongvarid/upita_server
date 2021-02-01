from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter
from import_export.admin import ImportExportModelAdmin,ImportMixin, ExportMixin
# Register your models here.
from reversion.admin import VersionAdmin
from report.models import  *
class ImportExportVersionModelAdmin(ImportMixin, ExportMixin, VersionAdmin):
    change_list_template = 'change_list_graph.html'
class ReportAllAdmin(ImportExportModelAdmin):
    ordering = ('all',)
    search_fields = ['agency', ]
    list_display = ('agency','year','iit','eit','oit','all')
    # list_filter = ('assessment__year','assessment',)
    list_filter = (
        ('year', DropdownFilter),
        ('agency', RelatedDropdownFilter),
    )
    change_list_template = 'change_list_graph.html'
admin.site.register(ReportAll,ReportAllAdmin)
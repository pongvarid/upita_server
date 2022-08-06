from django.contrib import admin
from django.utils.safestring import mark_safe

from moral_organization.models import PlanFile,FinishPlan

class FinishPlanInlines(admin.StackedInline):

    model = FinishPlan
    fk_name = "baseplan"
    readonly_fields = ('headshot_image','created_at', 'updated_at')
    def headshot_image(self, obj):
        try:
            files = obj.file.all()
            link = ''
            for file in files:
                link+= mark_safe('<a href="/media/{url}" target="_blank">{url}</a><br>').format(
                    url = file.file
                )
            return mark_safe(link)
        except:
            return str('-')
    def get_extra(self, request, obj=None, **kwargs):
        extra = 1
        return extra

class BasePlanAdmin(admin.ModelAdmin):
    inlines = [FinishPlanInlines ,]
    search_fields = ['name']
    list_display = ('name','created_at')

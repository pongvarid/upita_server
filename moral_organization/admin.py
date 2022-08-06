from django.contrib import admin

from moral_organization.admins.plan import BasePlanAdmin
from moral_organization.models import Year, Category, Assessment, Choice, Main_exercise, Do_exercise, BasePlan, \
    FinishPlan, PlanFile
from moral_organization.admins.moral_organization import YearAdmin,CataegoryAdmin, AssessmentAdmin, ChoiceAdmin, Main_exerciseAdmin, Do_exerciseAdmin
# Register your models here.
admin.site.register(Year,YearAdmin)

admin.site.register(Category, CataegoryAdmin)
admin.site.register(Assessment, AssessmentAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Main_exercise, Main_exerciseAdmin)
admin.site.register(Do_exercise, Do_exerciseAdmin)

admin.site.register(BasePlan,BasePlanAdmin)
admin.site.register(FinishPlan)
admin.site.register(PlanFile)

from django.contrib import admin
from django.utils.html import format_html
from moral_organization.models import Year, Category, Assessment, Choice, Main_exercise, Do_exercise

class YearAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return True
    def has_add_permission(self, request, obj=None):
        return True
    def has_delete_permission(self, request, obj=None):
        return True
    search_fields = ['name']
    list_display = ('name','created_at')


class AssessmentAdminInlines(admin.TabularInline): 
    
    model = Assessment
    fk_name = "category"
    readonly_fields = ('created_at', 'updated_at')

    def get_extra(self, request, obj=None, **kwargs):
        extra = 1
        return extra



class CataegoryAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return True
    def has_add_permission(self, request, obj=None):
        return True
    def has_delete_permission(self, request, obj=None):
        return True
    inlines = [AssessmentAdminInlines ,]
    search_fields = ['name']
    list_display = ('name','created_at')


class ChoiceInlineAdmin(admin.TabularInline): 
    model = Choice
    fk_name = "assessment"
    search_fields = ['assessment']
    list_display = ('assessment','value','score','created_at')

class AssessmentAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return True
    def has_add_permission(self, request, obj=None):
        return True
    def has_delete_permission(self, request, obj=None):
        return True
    inlines = [ChoiceInlineAdmin ,]
    search_fields = ['category','created_at']
    list_display = ('name','category','created_at')
    list_filter = ('category','created_at')

class ChoiceAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return True
    def has_add_permission(self, request, obj=None):
        return True
    def has_delete_permission(self, request, obj=None):
        return True
    search_fields = ['assessment']
    list_display = ('assessment','value','score','created_at')

class Main_exerciseAdmin(admin.ModelAdmin): 
    list_display = ('user','agency','year','sum_user','address','tel','created_at')
    list_filter = ('user','agency','year')

class Do_exerciseAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return True
    def has_add_permission(self, request, obj=None):
        return True
    def has_delete_permission(self, request, obj=None):
        return True
    list_display = ('assessment','main_exercise','choice','created_at')
    list_filter = ('assessment','main_exercise','created_at')
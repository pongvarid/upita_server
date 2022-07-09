from django.contrib import admin
from django.utils.html import format_html


class CataegoryAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return True
    def has_add_permission(self, request, obj=None):
        return True
    def has_delete_permission(self, request, obj=None):
        return True
    search_fields = ['name']
    list_display = ('name','created_at')

class AssessmentAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return True
    def has_add_permission(self, request, obj=None):
        return True
    def has_delete_permission(self, request, obj=None):
        return True
    search_fields = ['category','created_at']
    list_display = ('category','name','created_at')
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
    def has_change_permission(self, request, obj=None):
        return True
    def has_add_permission(self, request, obj=None):
        return True
    def has_delete_permission(self, request, obj=None):
        return True
    list_display = ('assessment','user','agency','sum_user','address','tel','created_at')
    list_filter = ('assessment','user','agency')

class Do_exerciseAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return True
    def has_add_permission(self, request, obj=None):
        return True
    def has_delete_permission(self, request, obj=None):
        return True
    list_display = ('assessment','main_exercise','choice','created_at')
    list_filter = ('assessment','main_exercise','created_at')
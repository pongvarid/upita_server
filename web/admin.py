from django.contrib import admin
from django_json_widget.widgets import JSONEditorWidget
from web.models import  *
# Register your models here.

class WebSettingAdmin(admin.ModelAdmin):
    formfield_overrides = {
        # fields.JSONField: {'widget': JSONEditorWidget}, # if django < 3.1
        models.TextField: {'widget': JSONEditorWidget},
    }
admin.site.register(WebSetting,WebSettingAdmin)
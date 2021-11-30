from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class WebSetting(models.Model):
    class Meta:
        verbose_name = _("ตั้งค่าการเข้าถึงเว็บไซต์ (Client)")
        verbose_name_plural = _("ตั้งค่าการเข้าถึงเว็บไซต์ (Client)")
    name = models.CharField(max_length=255, verbose_name="เวอร์ชัน")
    value = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
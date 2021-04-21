from django.db import models

# Create your models here.
from ita.models.general import *
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.db import models

class ReportAll(models.Model):
    class Meta:
        verbose_name = _("รายงานคะแนนรวม")
        verbose_name_plural = _("รายงานคะแนนรวม")
    year = models.CharField(max_length=255,verbose_name="ปีงบประมาณ")
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE,verbose_name="หน่วยงาน/คณะ")
    iit = models.FloatField(default=0.00)
    eit = models.FloatField(default=0.00)
    oit = models.FloatField(default=0.00)
    all = models.FloatField(default=0.00)
    rate = models.CharField(max_length=255,null=True,blank=True,verbose_name="ระดับ")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.agency.name)

class ReportDetail(models.Model):
    class Meta:
        verbose_name = _("รายงานคะแนนภาพรวม")
        verbose_name_plural = _("รายงานคะแนนภาพรวม")
    year = models.CharField(max_length=255, verbose_name="ปีงบประมาณ")
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE, verbose_name="หน่วยงาน/คณะ")
    name = models.CharField(max_length=255, verbose_name="ชื่อ")
    score = models.FloatField(default=0.00)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.agency.name)

class ReportRawIIT(models.Model):
    class Meta:
        verbose_name = _("รายงานรายระเอียด IIT")
        verbose_name_plural = _("รายงานรายระเอียด IIT")
    year = models.CharField(max_length=255, verbose_name="ปีงบประมาณ")
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE, verbose_name="หน่วยงาน/คณะ")
    score = models.CharField(null=True, blank=True, max_length=255, verbose_name="ผลคะแนนรวม 100 %")
    score30 = models.CharField(null=True, blank=True, max_length=255, verbose_name="ผลคะแนนรวม 30 %")
    user_set = models.CharField(null=True, blank=True, max_length=255, verbose_name="บุคลากร (ที่กำหนด)")
    user_do = models.CharField(null=True, blank=True, max_length=255, verbose_name="บุคลากร (ที่ประเมิน)")
    result = models.CharField(null=True, blank=True, max_length=255, verbose_name="ผลการประเมิน")
    rawType = models.TextField(null=True,blank=True,verbose_name="หัวข้อ")
    rawDone = models.TextField(null=True,blank=True,verbose_name="เนื้อหา")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.agency.name)

class ReportRawEIT(models.Model):
    class Meta:
        verbose_name = _("รายงานรายระเอียด EIT")
        verbose_name_plural = _("รายงานรายระเอียด EIT")
    year = models.CharField(max_length=255, verbose_name="ปีงบประมาณ")
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE, verbose_name="หน่วยงาน/คณะ")
    score = models.CharField(null=True, blank=True, max_length=255, verbose_name="ผลคะแนนรวม 100 %")
    score30 = models.CharField(null=True, blank=True, max_length=255, verbose_name="ผลคะแนนรวม 30 %")
    user_set = models.CharField(null=True, blank=True, max_length=255, verbose_name="บุคลากร (ที่กำหนด)")
    user_do = models.CharField(null=True, blank=True, max_length=255, verbose_name="บุคลากร (ที่ประเมิน)")
    result = models.CharField(null=True, blank=True, max_length=255, verbose_name="ผลการประเมิน")
    rawType = models.TextField(null=True, blank=True,verbose_name="หัวข้อ")
    rawDone = models.TextField(null=True, blank=True,verbose_name="เนื้อหา")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.agency.name)




 
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from ita.models.general import *
# Create your models here.
class Year(models.Model):
    class Meta:
        verbose_name = _("ปีการศึกษา")
        verbose_name_plural = _("ปีการศึกษา") 
    year = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.year 
        
class Rate(models.Model):
    class Meta:
        verbose_name = _("ประเด็นการตรวจสอบ")
        verbose_name_plural = _("ประเด็นการตรวจสอบ") 
    number = models.IntegerField(default=0,verbose_name="ข้อ")
    year = models.ForeignKey(Year, on_delete=models.CASCADE,verbose_name="ปีการศึกษา")
    name = models.CharField(max_length=255,verbose_name="หัวข้อ")
    detail = models.TextField(verbose_name="รายระเอียด") 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name + " " + self.year.year

class RateStatus(models.Model):
    class Meta:
        verbose_name = _("สถานะการตรวจสอบ")
        verbose_name_plural = _("สถานะการตรวจสอบ") 
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name 

class RateResult(models.Model):
    class Meta:
        verbose_name = _("การตรวจสอบ")
        verbose_name_plural = _("การตรวจสอบ")  
    ANSWERS = (
        ('เสร็จสิ้น','เสร็จสิ้น'),
        ('อยู่ระหว่างการปรับปรุง', 'อยู่ระหว่างการปรับปรุง'), 
        ('ไม่มีข้อมูล', 'ไม่มีข้อมูล'),
    )
    rate = models.ForeignKey(Rate, on_delete=models.CASCADE,verbose_name="หัวข้อการตรวจสอบ")
    score = models.FloatField(null=True,default=0.00,verbose_name="คะแนน")
    rate_status = models.ForeignKey(RateStatus, on_delete=models.CASCADE,blank=True, null=True,verbose_name="สถานะการตรวจสอบ")
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="user",blank=True, null=True)
    tester = models.ForeignKey(User, on_delete=models.CASCADE,related_name="tester",blank=True, null=True ,verbose_name="หน่วยงานที่ตรวจสอบ")
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE,blank=True, null=True,verbose_name="หน่วยงานที่ส่ง")
    urls = models.TextField(blank=True, null=True )  
    register_type = models.CharField(max_length=255,choices=ANSWERS,blank=True, null=True,verbose_name="สถานะการส่ง")
    comment = models.TextField(blank=True, null=True ,verbose_name="ความคิดเห็น")
    passing = models.BooleanField(default=False ,verbose_name="การอนุญาตจากหัวหน้าหน่วยงาน") 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return  self.rate.name 
    @property
    def number(self):
        return self.rate.number
 
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
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    detail = models.TextField() 
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
    rate = models.ForeignKey(Rate, on_delete=models.CASCADE)
    score = models.FloatField(null=True,default=0.00)
    rate_status = models.ForeignKey(RateStatus, on_delete=models.CASCADE,blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="user",blank=True, null=True)
    tester = models.ForeignKey(User, on_delete=models.CASCADE,related_name="tester",blank=True, null=True )
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE,blank=True, null=True)
    comment = models.TextField(blank=True, null=True ) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.rate.name 
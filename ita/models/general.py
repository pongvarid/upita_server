from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class AgencyType(models.Model):
    class Meta:
        verbose_name = _("ประเภทหน่วยงาน")
        verbose_name_plural = _("ประเภทหน่วยงาน") 
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    @property
    def fullName(self):
        return self.name
        
class Agency(models.Model):
    class Meta:
        verbose_name = _("หน่วยงาน")
        verbose_name_plural = _("หน่วยงาน") 
    agency_type = models.ForeignKey(AgencyType, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    count = models.IntegerField(default=0,verbose_name="จำนวนบุคลากร")
    percent = models.IntegerField(default=0,verbose_name="เกณฑ์กลุ่มตัวอย่าง(ร้อยละ)")
    eit = models.IntegerField(default=0, verbose_name="ค่าเป้าหมายกลุ่มตัวอย่างภายนอก (EIT)")
    iit = models.IntegerField(default=0, verbose_name="ค่าเป้าหมายกลุ่มตัวอย่างภายใน (IIT)")
    disabled = models.BooleanField(default=False,verbose_name="ปิดการมองเห็น")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name  +"("+self.agency_type.name+") "

class AgencyChange(models.Model):
    class Meta:
        verbose_name = _("การเปลี่ยนแปลงหน่วยงาน")
        verbose_name_plural = _("การเปลี่ยนแปลงหน่วยงาน")
    user = models.ForeignKey(User, verbose_name="ผู้ใช้", on_delete=models.CASCADE)
    agency = models.ForeignKey(Agency, verbose_name="หน่วยงานเดิม",related_name="old", on_delete=models.CASCADE)
    agency_change = models.ForeignKey(Agency,verbose_name="หน่วยงานที่เปลี่ยนแปลง",related_name="new",  on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "("+self.agency.name+") "
    def fullname(self):
        return self.user.first_name + " " + self.user.last_name


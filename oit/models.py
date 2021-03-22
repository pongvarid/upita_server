from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from ita.models import Rate, RateStatus, Agency

CHOICES = [
    (0,0),
    (0.5,0.5),
    (1,1)
]

class EvaluateOIT(models.Model):
    rate = models.ForeignKey(Rate, on_delete=models.CASCADE,verbose_name="หัวข้อการตรวจสอบ")
    score = models.FloatField(null=True, default=0.00,choices=CHOICES, verbose_name="คะแนน")
    rate_status = models.ForeignKey(RateStatus, on_delete=models.CASCADE, blank=True, null=True,
                                    verbose_name="สถานะการตรวจสอบ")
    tester = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True,
                               verbose_name="หน่วยงานที่ตรวจสอบ")
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE, blank=True, null=True, verbose_name="หน่วยงานที่ส่ง")
    comment = models.TextField(blank=True, null=True, verbose_name="ความคิดเห็น")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return  self.rate.name

    @property
    def number(self):
        return self.rate.number

    @property
    def name(self):
        return "(O"+str(self.rate.number)+") " +  self.rate.name
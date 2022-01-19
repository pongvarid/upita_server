from django.db import models

# Create your models here.
from polymorphic.models import PolymorphicModel
from django.utils.translation import ugettext_lazy as _
from ita.models.general import *
from django.contrib.auth.models import User

class Year(models.Model):
    class Meta:
        verbose_name = _("ปีงบประมาณ")
        verbose_name_plural = _("ปีงบประมาณ")
    year = models.CharField(max_length=255)
    status = models.BooleanField(default=False,verbose_name="ปิดการใช้งาน")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.year
class Choice(PolymorphicModel):
    typeList = [
        (1,'เชิงบวก'),
        ( 0,'เชิงลบ'),
        (3, 'ทั่วไป'),
    ]
    name = models.CharField(max_length=200)
    type = models.IntegerField(choices=typeList)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        type = '(เชิงบวก)'
        if (self.type == 0):
            type = '(เชิงลบ)'
        elif (self.type == 3):
            type = '(ทั่วไป)'
        return self.name +" "+ type

class Ascend(Choice):
    class Meta:
        verbose_name = _("ตัวเลือกแบบ น้อยที่สุด-มากที่สุด")
        verbose_name_plural = _("ตัวเลือกแบบ น้อยที่สุด-มากที่สุด")
    notting = models.FloatField(default=0.00,verbose_name="น้อยที่สุดหรือไม่มีเลย")
    low = models.FloatField(default=0.00,verbose_name="น้อย")
    very = models.FloatField(default=0.00,verbose_name="มาก")
    many = models.FloatField(default=0.00,verbose_name="มากที่สุด")

class Exist(Choice):
    class Meta:
        verbose_name = _("ตัวเลือกแบบ มี/ไม่มี")
        verbose_name_plural = _("ตัวเลือกแบบ มี/ไม่มี")
    have = models.FloatField(default=0.00,verbose_name="มี")
    notting = models.FloatField(default=0.00, verbose_name="ไม่มี")

class Answer(Choice):
    class Meta:
        verbose_name = _("ตัวเลือกแบบ แบบคำตอบ")
        verbose_name_plural = _("ตัวเลือกแบบ แบบคำตอบ")
    value = models.CharField(null=True,blank=True,max_length=255,verbose_name="คำตอบ")

class AssessmentIssues(models.Model):
    class Meta:
        verbose_name = _("ประเด็นการประเมิน")
        verbose_name_plural = _("ประเด็นการประเมิน")
    name = models.CharField(max_length=200,null=True,blank=True,)
    order = models.IntegerField(null=True, blank=True)
    year = models.ForeignKey(Year,null=True,blank=True, on_delete=models.CASCADE,verbose_name=_("ปีงบประมาณ"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self): 
        return str(self.name) + " : "+ str(self.year.year )

class Issue(models.Model):
    class Meta:
        verbose_name = _("หัวข้อการประเมิน")
        verbose_name_plural = _("หัวข้อการประเมิน")
    typeList = [
        (True, 'มีข้อย่อย'),
        (False, 'ไม่มีข้อย่อย'),
    ]
    assessment = models.ForeignKey(AssessmentIssues, on_delete=models.CASCADE)
    order = models.IntegerField(null=True,blank=True )
    name = name = models.TextField()
    type = models.BooleanField(default=True,choices=typeList)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return  "( e"+ str(self.order) +") "+  self.name

    @property
    def fullName(self):
        return "e"+str(self.order) + " : "+self.name

class IssueDetail(models.Model):
    class Meta:
        verbose_name = _("หัวข้อ")
        verbose_name_plural = _("หัวข้อ")
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    sub_name = models.CharField(max_length=200)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.id) + " : "+ self.sub_name

    @property
    def choiceType(self):
        return self.choice.name

    @property
    def choiceTypeData(self):
        if (self.choice.type == 1):
            return 'เชิงบวก'
        elif (self.choice.type == 0):
            return 'เชิงลบ'
        else:
            return 'ทั่วไป'

class AnswerIssueEit(models.Model):
    class Meta:
        verbose_name = _("การตอบแบบประเมิน")
        verbose_name_plural = _("การตอบแบบประเมิน")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    assessmentIssues = models.ForeignKey(AssessmentIssues, on_delete=models.CASCADE)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    issue =  models.ForeignKey(Issue, on_delete=models.CASCADE)
    issueDetail = models.ForeignKey(IssueDetail, on_delete=models.CASCADE)
    value = models.FloatField(default=0.00,verbose_name="คะแนน", null=True, blank=True)
    value_type = models.ForeignKey(Choice, on_delete=models.CASCADE, null=True, blank=True)
    value_by = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def agency_name(self):
        return "( i" + str(self.issue.order) + ") " + self.agency.name

    @property
    def issueDetail_name(self):
        return self.issueDetail.sub_name

    @property
    def user_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def assessmentIssues_name(self):
        return self.assessmentIssues.name

    @property
    def user_email(self):
        return self.user.email

    @property
    def issue_name(self):
        return "( i" + str(self.issue.order) + ") " + self.issue.name

    @property
    def choiceTypeData(self):
        return self.issueDetail.choiceTypeData

    @property
    def issue_type(self):
        return self.issueDetail.choiceType

    @property
    def choice_val(self):
        return self.issueDetail.choiceType


class AnswerSuggestionEit(models.Model):
    class Meta:
        verbose_name = _("การตอบข้อเสนอแนะ")
        verbose_name_plural = _("การตอบข้อเสนอแนะ")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    suggestion = models.CharField(max_length=255,null=True,blank=True,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def agency_name(self):
        return self.agency.name

    @property
    def user_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def user_email(self):
        return self.user.email


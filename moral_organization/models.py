from re import I
from django.db import models
from ita.models.user import Profile
from ita.models.general import Agency
from django.contrib.auth.models import User
# Create your models here.

class Year(models.Model):
    name = models.CharField(max_length=250,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

class Category(models.Model):
    year = models.ForeignKey(Year,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=250,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)



class Assessment(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=250,null=True,blank=True)
    year = models.ForeignKey(Year,on_delete=models.CASCADE,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.category) +" - "+str(self.name)+" - "+str(self.year)

class Choice(models.Model):
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, null=True, blank=True)
    value = models.TextField(null=True, blank=True)
    score = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.assessment)+ " - "+str(self.value)+" - "+str(self.score)

class Main_exercise(models.Model):
    year = models.ForeignKey(Year,on_delete=models.CASCADE,null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE, null=True, blank=True)
    sum_user = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=250,null=True,blank=True)
    tel = models.CharField(max_length=250,null=True,blank=True)
    level = models.CharField(max_length=250,null=True,blank=True)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.agency)+" - "+str(self.user)+" - "+str(self.year)

class SignAdminExercise(models.Model):
    main_exercise = models.ForeignKey(Main_exercise, on_delete=models.CASCADE)
    signature = models.BooleanField(default=False)
    name = models.CharField(max_length=250, null=True, blank=True)
    work = models.CharField(max_length=250, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.name)
class SignPassingExercise(models.Model):
    main_exercise = models.ForeignKey(Main_exercise,on_delete=models.CASCADE)
    signature = models.BooleanField(default=False)
    name = models.CharField(max_length=250, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.name)

class Do_exercise(models.Model):
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, null=True, blank=True)
    main_exercise = models.ForeignKey(Main_exercise, on_delete=models.CASCADE, null=True, blank=True)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.assessment)+" - "+str(self.main_exercise)+" - "+str(self.choice)

class BasePlan(models.Model):
    year = models.ForeignKey(Year,on_delete=models.CASCADE,null=True,blank=True)
    agency = models.ForeignKey(Agency,on_delete=models.CASCADE,verbose_name="หน่วงาน")
    name = models.CharField(max_length=250,null=True,blank=True,verbose_name="คุณธรรมเป้าหมาย")
    
    problem = models.TextField( null=True,blank=True,verbose_name="ปัญหาที่อยากแก้")
    fix_want = models.TextField(null=True,blank=True,verbose_name="ความดีที่อยากทำ")
    good_fix = models.TextField( null=True,blank=True,verbose_name="กิจกรรม")
  #  doing = models.TextField( null=True,blank=True,verbose_name="หน่วงาน")
    kpi = models.TextField( null=True,blank=True,verbose_name="ตัวชี้วัด")
    doing_date = models.DateField(null=True,blank=True,verbose_name="วัน/เดือน/ปี ที่ดำเนินงาน")
    money = models.FloatField(default=0,null=True,blank=True,verbose_name="งบประมาณในการดำเนินงาน")
    responsible_user = models.TextField( null=True,blank=True,verbose_name="ผู้รับผิดชอบ")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.name)

class PlanFile(models.Model):
    file = models.FileField(upload_to='files/plan')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.created_at)

class FinishPlan(models.Model):
    baseplan = models.ForeignKey(BasePlan,on_delete=models.CASCADE)
    name = models.CharField(max_length=250, null=True, blank=True,verbose_name="กิจกรรม/โครงการ")
    doing_date = models.DateTimeField(null=True, blank=True,verbose_name="วัน เวลา ที่ดำเนินการ")
    place = models.CharField(max_length=250, null=True, blank=True, verbose_name="สถานที่ ที่ดำเนินการ")
    count_person = models.IntegerField(default=0, null=True, blank=True,verbose_name="จำนวนผู้เช้าร่วมกิจกรรม/โครงการ")
    money = models.FloatField(default=0, null=True, blank=True,verbose_name="งบประมาณที่ใช้ในการดำเนินงาน")
    detail = models.TextField( null=True, blank=True,verbose_name="รายละเอียดกิจกรรม/โครงการ")
    file = models.ManyToManyField(PlanFile,verbose_name="ไฟล์")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)


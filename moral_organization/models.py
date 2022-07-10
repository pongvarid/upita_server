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

class Do_exercise(models.Model):
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, null=True, blank=True)
    main_exercise = models.ForeignKey(Main_exercise, on_delete=models.CASCADE, null=True, blank=True)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.assessment)+" - "+str(self.main_exercise)+" - "+str(self.choice)

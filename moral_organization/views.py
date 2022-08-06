from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from moral_organization.models import Year, Category, Assessment, Choice, Main_exercise, Do_exercise, BasePlan, \
    FinishPlan
from moral_organization.serializers import YearSerializers, CategorySerializers, AssessmentSerializers, \
    ChoiceSerializers, Main_exerciseSerializers, Do_exerciseSerializers, BasePlanSerializers, FinishPlanSerializers


# Create your views here.
class YearViewset(ModelViewSet):
    queryset = Year.objects.all()
    serializer_class = YearSerializers
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ['name']

class CategoryViewset(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['year',]
    search_fields = ['name']

class AssessmentViewset(ModelViewSet):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializers
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['category','year',]
    search_fields = ['category__name']

class ChoiceViewset(ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializers
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['assessment']

class Main_exerciseViewset(ModelViewSet):
    queryset = Main_exercise.objects.all()
    serializer_class = Main_exerciseSerializers
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['user','agency','year',]

class Do_exerciseViewset(ModelViewSet):
    queryset = Do_exercise.objects.all()
    serializer_class = Do_exerciseSerializers
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['assessment','main_exercise']

class BasePlanViewset(ModelViewSet):
    queryset = BasePlan.objects.all()
    serializer_class = BasePlanSerializers
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['agency','year',]

class FinishPlanViewset(ModelViewSet):
    queryset = FinishPlan.objects.all()
    serializer_class = FinishPlanSerializers
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['baseplan',]
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from moral_organization.models import Category, Assessment, Choice, Main_exercise, Do_exercise
from moral_organization.serializers import CategorySerializers, AssessmentSerializers, ChoiceSerializers, Main_exerciseSerializers, Do_exerciseSerializers
# Create your views here.

class CategoryViewset(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ['name']

class AssessmentViewset(ModelViewSet):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializers
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['category']
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
    filterset_fields = ['assessment','user','agency']

class Do_exerciseViewset(ModelViewSet):
    queryset = Do_exercise.objects.all()
    serializer_class = Do_exerciseSerializers
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['assessment','main_exercise']


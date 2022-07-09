from dataclasses import field
from rest_framework.serializers import ModelSerializer
from moral_organization.models import Category, Assessment, Choice, Main_exercise, Do_exercise

class CategorySerializers(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class AssessmentSerializers(ModelSerializer):
    class Meta:
        model = Assessment
        fields = "__all__"

class ChoiceSerializers(ModelSerializer):
    class Meta:
        model = Choice
        fields = "__all__"

class Main_exerciseSerializers(ModelSerializer):
    class Meta:
        model = Main_exercise
        fields = "__all__"

class Do_exerciseSerializers(ModelSerializer):
    class Meta:
        model = Do_exercise
        fields = "__all__"
from dataclasses import field
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from moral_organization.models import Year, Category, Assessment, Choice, Main_exercise, Do_exercise, BasePlan, \
    PlanFile, FinishPlan


class YearSerializers(ModelSerializer):
    class Meta:
        model = Year
        fields = "__all__"
class ChoiceInitSerializers(ModelSerializer):
    class Meta:
        model = Choice
        fields = "__all__"

class AssessmentInitSerializers(ModelSerializer):
    choices = SerializerMethodField(read_only=True)
    class Meta:
        model = Assessment
        fields = "__all__"
    def get_choices(self,obj):
        try:
            data = Choice.objects.filter(assessment__id=obj.id)
            data =  ChoiceInitSerializers(data,many=True).data
            return data
        except:
            return None
        
class CategorySerializers(ModelSerializer):
    assessment = SerializerMethodField(read_only=True)
    class Meta:
        model = Category
        fields = "__all__"
    def get_assessment(self,obj):
        try:
            data = Assessment.objects.filter(category__id=obj.id)
            data =  AssessmentInitSerializers(data,many=True).data
            return data
        except:
            return None
        

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

class BasePlanSerializers(ModelSerializer):
    class Meta:
        model = BasePlan
        fields = "__all__"
class PlanFileSerializers(ModelSerializer):
    class Meta:
        model = PlanFile
        fields = "__all__"
class FinishPlanSerializers(ModelSerializer):
    class Meta:
        depth =2
        model = FinishPlan
        fields = "__all__"
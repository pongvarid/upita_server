from rest_framework.serializers import ModelSerializer,SerializerMethodField
from eit.models import Year, Choice, Ascend, Exist, Answer, AssessmentIssues, Issue, IssueDetail, AnswerIssueEit, AnswerSuggestionEit
from django.contrib.auth.models import User

class CurrentUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')

class YearSerializer(ModelSerializer):

    class Meta:
        model = Year
        fields = '__all__'


class ChoiceSerializer(ModelSerializer):

    class Meta:
        model = Choice
        fields = '__all__'


class AscendSerializer(ModelSerializer):

    class Meta:
        model = Ascend
        fields = '__all__'


class ExistSerializer(ModelSerializer):

    class Meta:
        model = Exist
        fields = '__all__'


class AnswerSerializer(ModelSerializer):

    class Meta:
        model = Answer
        fields = '__all__'


class AssessmentIssuesSerializer(ModelSerializer):

    class Meta:
        model = AssessmentIssues
        fields = '__all__'


class IssueSerializer(ModelSerializer):

    class Meta:
        model = Issue
        fields = '__all__'


class IssueDetailSerializer(ModelSerializer):

    class Meta:
        model = IssueDetail
        fields = '__all__'


class AnswerIssueEitSerializer(ModelSerializer):

    class Meta:
        model = AnswerIssueEit
        fields = '__all__'

class AnswerIssueEitReportSerializer(ModelSerializer):
    # issueDetail = IssueDetailSerializer()
    # issue = IssueSerializer()
    # issueDetail_pk = SerializerMethodField()
    # issue_pk = SerializerMethodField()
    # assessment_pk = SerializerMethodField()
    class Meta:
        model = AnswerIssueEit
        # fields = '__all__'
        # fields = '__all__'
        fields = ('user','assessmentIssues','agency','year','issue','issueDetail','value','value_type','value_by','issueDetail_name','issue_name','issue_type','choiceTypeData' )

    # def get_issueDetail_pk(self, obj):
    #     return obj.issueDetail_id
    # def get_issue_pk(self, obj):
    #     return obj.issue_id
    # def get_assessment_pk(self, obj):
    #     return obj.assessmentIssues_id

class AnswerSuggestionEitSerializer(ModelSerializer):
 
 
    class Meta:
        model = AnswerSuggestionEit
        fields = '__all__'
 
class IssueDetailAllSerializer(ModelSerializer):
    choice = ChoiceSerializer(read_only=True)
    class Meta:
        model = IssueDetail
        fields = '__all__'


class IssueAllSerialillzer(ModelSerializer):
    choice_type = SerializerMethodField()
    class Meta:
        model = Issue
        fields = '__all__'
    def get_choice_type(self,obj):
        try:
            choice = IssueDetail.objects.filter(issue=obj.id)
            choice = IssueDetailAllSerializer(choice,many=True)
            return choice.data
        except:
            return None

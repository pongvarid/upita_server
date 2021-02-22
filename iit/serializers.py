from rest_framework.serializers import ModelSerializer,SerializerMethodField
from iit.models import Year, Choice, Ascend, Exist, Answer, AssessmentIssues, Issue, IssueDetail, AnswerIssue, AnswerSuggestion, UserInAnswer


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
        fields = ('id','issue','sub_name','choice','choiceType','choiceTypeData')


class AnswerIssueSerializer(ModelSerializer):
    class Meta:
        model = AnswerIssue
        fields = '__all__'


class AnswerIssueReportSerializer(ModelSerializer):
    # assessmentIssues = AssessmentIssuesSerializer()
    # issueDetail = IssueDetailSerializer()
    # issue = IssueSerializer()
    # issueDetail_pk = SerializerMethodField()
    # issue_pk   = SerializerMethodField()
    # assessment_pk = SerializerMethodField()
    class Meta:
        model = AnswerIssue
        fields = ('user','assessmentIssues','agency','year','issue','issueDetail','value','value_type','value_by','issueDetail_name','issue_name','issue_type','choiceTypeData' )
    # def get_issueDetail_pk(self, obj):
    #     return obj.issueDetail_id
    # def get_issue_pk(self, obj):
    #     return obj.issue_id
    # def get_assessment_pk(self, obj):
    #     return obj.assessmentIssues_id 


class AnswerSuggestionSerializer(ModelSerializer):

    class Meta:
        model = AnswerSuggestion
        fields = '__all__'


class UserInAnswerSerializer(ModelSerializer):

    class Meta:
        model = UserInAnswer
        fields = '__all__'

class AnswerIssueSerializerX(ModelSerializer):
    class Meta:
        model = AnswerIssue
        fields = ['agency','user_student']
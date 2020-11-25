from rest_framework.serializers import ModelSerializer,ValidationError,CharField,SerializerMethodField

from eit.models import Issue, AssessmentIssues, Choice, IssueDetail, Ascend, Exist, Year
from django.contrib.auth.models import User
from rest_polymorphic.serializers import PolymorphicSerializer

class YearSerializer(ModelSerializer):
    class Meta:
        model = Year
        fields = '__all__'

class ChoiceMainSerializer(ModelSerializer):
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

class ChoicePolymorphiccSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        Choice : ChoiceMainSerializer,
        Ascend: AscendSerializer,
        Exist: ExistSerializer
    }


class IssueDetailSerializer(ModelSerializer):
    choice = ChoicePolymorphiccSerializer()
    class Meta:
        model = IssueDetail
        fields = '__all__'

class IssuesSerializer(ModelSerializer):
    # user = UserSerializer()
    issueDetail = SerializerMethodField()
    class Meta:
        model = Issue
        fields = '__all__'

    def get_issueDetail(self, obj):
        issueDetail = IssueDetail.objects.filter(issue=obj.pk)
        issueDetail = IssueDetailSerializer(issueDetail,many=True)
        return issueDetail.data

class AssessmentIssuesSerializer(ModelSerializer):
    # user = UserSerializer()
    issue = SerializerMethodField()
    year = YearSerializer()
    issueCount = SerializerMethodField()
    class Meta:
        model = AssessmentIssues
        fields = '__all__'
    def get_issue(self, obj):
        issue = Issue.objects.filter(assessment=obj.pk)
        issue = IssuesSerializer(issue,many=True)
        return issue.data

    def get_issueCount(self, obj):
        issueDetail = IssueDetail.objects.filter(issue__assessment=obj.pk)
        return len(issueDetail)


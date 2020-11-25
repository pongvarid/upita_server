from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from eit.serializers import YearSerializer, ChoiceSerializer, AscendSerializer, ExistSerializer,AnswerIssueEitReportSerializer,  AnswerSerializer, AssessmentIssuesSerializer, IssueSerializer, IssueDetailSerializer, AnswerIssueEitSerializer, AnswerSuggestionEitSerializer
from eit.models import Year, Choice, Ascend, Exist, Answer, AssessmentIssues, Issue, IssueDetail, AnswerIssueEit, AnswerSuggestionEit
from rest_framework import generics, filters


class YearViewSet(ModelViewSet):
    queryset = Year.objects.order_by('pk')
    serializer_class = YearSerializer


class ChoiceViewSet(ModelViewSet):
    queryset = Choice.objects.order_by('pk')
    serializer_class = ChoiceSerializer


class AscendViewSet(ModelViewSet):
    queryset = Ascend.objects.order_by('pk')
    serializer_class = AscendSerializer


class ExistViewSet(ModelViewSet):
    queryset = Exist.objects.order_by('pk')
    serializer_class = ExistSerializer


class AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.order_by('pk')
    serializer_class = AnswerSerializer


class AssessmentIssuesViewSet(ModelViewSet):
    queryset = AssessmentIssues.objects.order_by('pk')
    serializer_class = AssessmentIssuesSerializer


class IssueViewSet(ModelViewSet):
    queryset = Issue.objects.order_by('pk')
    serializer_class = IssueSerializer


class IssueDetailViewSet(ModelViewSet):
    queryset = IssueDetail.objects.order_by('pk')
    serializer_class = IssueDetailSerializer


class AnswerIssueEitViewSet(ModelViewSet):
    queryset = AnswerIssueEit.objects.order_by('pk')
    serializer_class = AnswerIssueEitSerializer

class AnswerIssueReportViewSet(ModelViewSet):
    queryset = AnswerIssueEit.objects.order_by('pk')
    serializer_class = AnswerIssueEitReportSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['agency','year','assessmentIssues' ]
    search_fields = ['username', 'first_name', 'last_name']



class AnswerSuggestionEitViewSet(ModelViewSet):
    queryset = AnswerSuggestionEit.objects.order_by('pk')
    serializer_class = AnswerSuggestionEitSerializer

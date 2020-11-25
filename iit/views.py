from rest_framework.viewsets import ModelViewSet
from iit.serializers import AnswerIssueReportSerializer, YearSerializer, ChoiceSerializer, AscendSerializer, ExistSerializer, AnswerSerializer, AssessmentIssuesSerializer, IssueSerializer, IssueDetailSerializer, AnswerIssueSerializer, AnswerSuggestionSerializer
from iit.models import Year, Choice, Ascend, Exist, Answer, AssessmentIssues, Issue, IssueDetail, AnswerIssue, AnswerSuggestion
from django_filters.rest_framework import DjangoFilterBackend
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
    queryset = AssessmentIssues.objects.order_by('order')
    serializer_class = AssessmentIssuesSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['name', 'year']
    # search_fields = ['username', 'first_name', 'last_name']


class IssueViewSet(ModelViewSet):
    queryset = Issue.objects.order_by('pk')
    serializer_class = IssueSerializer


class IssueDetailViewSet(ModelViewSet):
    queryset = IssueDetail.objects.order_by('pk')
    serializer_class = IssueDetailSerializer


class AnswerIssueViewSet(ModelViewSet):
    queryset = AnswerIssue.objects.order_by('pk')
    serializer_class = AnswerIssueSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['agency','year','assessmentIssues' ]
    search_fields = ['username', 'first_name', 'last_name']

class AnswerIssueReportViewSet(ModelViewSet):
    queryset = AnswerIssue.objects.order_by('pk')
    serializer_class = AnswerIssueReportSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['agency','year','assessmentIssues' ]
    search_fields = ['username', 'first_name', 'last_name']


class AnswerSuggestionViewSet(ModelViewSet):
    queryset = AnswerSuggestion.objects.order_by('pk')
    serializer_class = AnswerSuggestionSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['agency', 'year' ]
    # search_fields = ['username', 'first_name', 'last_name']
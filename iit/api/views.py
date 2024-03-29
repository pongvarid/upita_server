from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from iit.admin import UserInAnswerAdmin
from iit.api.serializers import *
from iit.models import *
from django.contrib.auth.models import User
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend

from iit.serializers import AnswerIssueSerializer, AnswerIssueSerializerX, UserInAnswerAdminSerializerX


class Filter(DjangoFilterBackend):

    def filter_queryset(self, request, queryset, view):
        filter_class = self.get_filter_class(view, queryset)

        if filter_class:
            return filter_class(request.query_params, queryset=queryset, request=request).qs
        return queryset

class AgencyTypeAPIView(APIView):
    filter_fields = ('name', 'id','year','year__year')
    def get(self, request, format=None):
        try:
            item = AssessmentIssues.objects.order_by('order')
            ff = Filter()
            filtered_queryset = ff.filter_queryset(request, item, self)
            serializer = AssessmentIssuesSerializer(filtered_queryset,many=True)
            return Response(serializer.data)
        except AssessmentIssues.DoesNotExist:
            return Response(status=404)

class YearAPIView(APIView):
    def get(self, request, format=None):
        try:
            item = Year.objects.all()
            serializer = YearSerializer(item,many=True)
            return Response(serializer.data)
        except AssessmentIssues.DoesNotExist:
            return Response(status=404)

class TestStudentAPIView(APIView):
    def get(self, request, format=None):
        try:
            profile = Profile.objects.filter(agency=41).values_list('user_id', flat=True)
            item = UserInAnswerAdmin.objects.filter(user__in=profile)
            serializer = UserInAnswerAdminSerializerX(item,many=True)
            return Response(serializer.data)
            # return Response({"dd":profile,'ss':len(profile)})
        except AssessmentIssues.DoesNotExist:
            return Response(status=404)
    

class IssueApi(APIView):
    def get(self, request, format=None):
        try:
            itms = AssessmentIssues.objects.all()
            serializer = AssessmentIssuesSerializer(itms,many=True)
            return Response(serializer.data)
        except:
            return Response(status=404)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from eit.api.serializers import *
from eit.models import *
from django.contrib.auth.models import User
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend

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

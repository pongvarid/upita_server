from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from web.serializers import WebSettingSerializer
from web.models import WebSetting
import json

class WebSettingFinalAPIView(APIView):

    def get(self, request, format=None):
        try:
            item = WebSetting.objects.last()
            serializer = WebSettingSerializer(item)
            return Response(serializer.data)
        except WebSetting.DoesNotExist:
            return Response(status=404)

class WebValueFinalAPIView(APIView):

    def get(self, request, format=None):
        try:
            item = WebSetting.objects.last()
            return Response(json.loads(item.value))
        except WebSetting.DoesNotExist:
            return Response(status=404)

class WebSettingAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = WebSetting.objects.get(pk=id)
            serializer = WebSettingSerializer(item)
            return Response(serializer.data)
        except WebSetting.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = WebSetting.objects.get(pk=id)
        except WebSetting.DoesNotExist:
            return Response(status=404)
        serializer = WebSettingSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = WebSetting.objects.get(pk=id)
        except WebSetting.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class WebSettingAPIListView(APIView):

    def get(self, request, format=None):
        items = WebSetting.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = WebSettingSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = WebSettingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

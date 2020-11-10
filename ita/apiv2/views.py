from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from ita.apiv2.serializers import AgencyTypeSerializer, AgencySerializer,ProfileDashboardSerializer, YearSerializer, RateResultViewSerializer,RateSerializer, RateStatusSerializer, RateResultSerializer, ProfileSerializer,UserDetailsSerializer
from ita.models import AgencyType, Agency, Year, Rate, RateStatus, RateResult, Profile
from django.contrib.auth.models import User
from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny


class AgencyTypeAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = AgencyType.objects.get(pk=id)
            serializer = AgencyTypeSerializer(item)
            return Response(serializer.data)
        except AgencyType.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = AgencyType.objects.get(pk=id)
        except AgencyType.DoesNotExist:
            return Response(status=404)
        serializer = AgencyTypeSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = AgencyType.objects.get(pk=id)
        except AgencyType.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class AgencyTypeAPIListView(APIView):

    def get(self, request, format=None):
        items = AgencyType.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = AgencyTypeSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = AgencyTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class AgencyAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Agency.objects.get(pk=id)
            serializer = AgencySerializer(item)
            return Response(serializer.data)
        except Agency.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Agency.objects.get(pk=id)
        except Agency.DoesNotExist:
            return Response(status=404)
        serializer = AgencySerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Agency.objects.get(pk=id)
        except Agency.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class AgencyAPIListView(APIView):

    def get(self, request, format=None):
        items = Agency.objects.order_by('pk')
        paginator = PageNumberPagination()
        # result_page = paginator.paginate_queryset(items, request)
        serializer = AgencySerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AgencySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class YearAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Year.objects.get(pk=id)
            serializer = YearSerializer(item)
            return Response(serializer.data)
        except Year.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Year.objects.get(pk=id)
        except Year.DoesNotExist:
            return Response(status=404)
        serializer = YearSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Year.objects.get(pk=id)
        except Year.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class YearAPIListView(APIView):

    def get(self, request, format=None):
        items = Year.objects.filter(status=False).order_by('pk')
        paginator = PageNumberPagination() 
        serializer = YearSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = YearSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class RateAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Rate.objects.filter(year=id).order_by('number')
            serializer = RateSerializer(item,many=True)
            return Response(serializer.data)
        except Rate.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Rate.objects.get(pk=id)
        except Rate.DoesNotExist:
            return Response(status=404)
        serializer = RateSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Rate.objects.get(pk=id)
        except Rate.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class RateAPIListView(APIView):

    def get(self, request, format=None):
        items = Rate.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = RateSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = RateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class RateStatusAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = RateStatus.objects.get(pk=id)
            serializer = RateStatusSerializer(item)
            return Response(serializer.data)
        except RateStatus.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = RateStatus.objects.get(pk=id)
        except RateStatus.DoesNotExist:
            return Response(status=404)
        serializer = RateStatusSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = RateStatus.objects.get(pk=id)
        except RateStatus.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class RateStatusAPIListView(APIView):

    def get(self, request, format=None):
        items = RateStatus.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = RateStatusSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = RateStatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class RateResultAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = RateResult.objects.get(pk=id)
            serializer = RateResultSerializer(item)
            return Response(serializer.data)
        except RateResult.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = RateResult.objects.get(pk=id)
        except RateResult.DoesNotExist:
            return Response(status=404)
        serializer = RateResultSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = RateResult.objects.get(pk=id)
        except RateResult.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class RateResultPassingAPIListView(APIView):
    def put(self, request,pk, format=None):
        user = User.objects.get(id=request.data['user_passing']) 
        items = RateResult.objects.get(pk=pk)
        items.user_passing = user
        items.passing = request.data['passing']
        items.save()  
        serializer = RateResultSerializer(items)
        return Response(serializer.data)

class RateResultAPIListView(APIView):

    def get(self, request, format=None):
        items = RateResult.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = RateResultSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = RateResultSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    
    def put(self, request, format=None):
        try: 
            items = RateResult.objects.get(agency=request.data['agency'],rate=request.data['rate'])
            serializer = RateResultViewSerializer(items)
            return Response(serializer.data, status=201)
        except :
            return Response(None, status=201)
    


class ProfileAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Profile.objects.get(pk=id)
            serializer = ProfileSerializer(item)
            return Response(serializer.data)
        except Profile.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Profile.objects.get(pk=id)
        except Profile.DoesNotExist:
            return Response(status=404)
        serializer = ProfileSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Profile.objects.get(pk=id)
        except Profile.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class ProfileAPIListView(APIView):

    def get(self, request, format=None):
        items = Profile.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = ProfileSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class LoginPermission(APIView):

    def get(self, request, format=None):
        items = Profile.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = ProfileSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        user = User.objects.get(username=request.data['username']) 
        if user.id:
            return Response({"user":user.id} , status=201)
        return Response({"have":False} , status=400)

class UserDetailsView(RetrieveUpdateAPIView):
 
    serializer_class = UserDetailsSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user

    def get_queryset(self):
        """
        Adding this method since it is sometimes called when using
        django-rest-swagger
        https://github.com/Tivix/django-rest-auth/issues/275
        """
        return get_user_model().objects.none()

class Dashbord(APIView):

    def get(self, request,pk, format=None):
        user = Profile.objects.get(pk=pk)
        agency = Agency.objects.get(pk=user.agency_id)
        profile = Profile.objects.filter(agency__id=agency.id,passing=False)
        passing = Profile.objects.filter(agency__id=agency.id,passing=True)
        response = {
            "agency":agency.name,
            "agency_user": len(profile),
            "agency_passing": len(passing),
            "agency_user_all": ProfileDashboardSerializer(profile,many=True).data,
            "agency_passing_all" :ProfileDashboardSerializer(passing,many=True).data 
        } 
         
        return Response(response)

    def post(self, request, format=None):
        user = User.objects.get(username=request.data['username']) 
        if user.id:
            return Response({"user":user.id} , status=201)
        return Response({"have":False} , status=400)

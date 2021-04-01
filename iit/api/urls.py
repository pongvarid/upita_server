
from iit.api import views
from django.urls import path,include

urlpatterns = [
    path('issue',views.AgencyTypeAPIView.as_view()),
    path('year',views.YearAPIView.as_view()),
    path('test',views.TestStudentAPIView.as_view()),
    path('result', views.IssueApi.as_view()),
]

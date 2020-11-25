
from eit.api import views
from django.urls import path,include

urlpatterns = [
    path('issue',views.AgencyTypeAPIView.as_view()),
    path('year',views.YearAPIView.as_view()),

]

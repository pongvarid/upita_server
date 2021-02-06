from django.conf.urls import include, url
from ita.apiv2 import views
from ita.api import views as views1


urlpatterns = [

  url(r'^useradmin/$', views.AdminAPIView.as_view()),
  url(r'^agencytype/(?P<id>[0-9]+)/$', views.AgencyTypeAPIView.as_view()),
  url(r'^agencytype/$', views.AgencyTypeAPIListView.as_view()),

  url(r'^agency/(?P<id>[0-9]+)/$', views.AgencyAPIView.as_view()),
  url(r'^agency/$', views.AgencyAPIListView.as_view()),

  url(r'^year/(?P<id>[0-9]+)/$', views.YearAPIView.as_view()),
  url(r'^year/$', views.YearAPIListView.as_view()),

  url(r'^rate/(?P<id>[0-9]+)/$', views.RateAPIView.as_view()),
  url(r'^rate/$', views.RateAPIListView.as_view()),

  url(r'^ratestatus/(?P<id>[0-9]+)/$', views.RateStatusAPIView.as_view()),
  url(r'^ratestatus/$', views.RateStatusAPIListView.as_view()),

  url(r'^rateresult/(?P<id>[0-9]+)/$', views.RateResultAPIView.as_view()),
  url(r'^rateresult/$', views.RateResultAPIListView.as_view()),
  url(r'^user/$', views.UserDetailsView.as_view()),
  url(r'^check/$', views.LoginPermission.as_view()),
  url(r'^profile/(?P<id>[0-9]+)/$', views.ProfileAPIView.as_view()),
  url(r'^profile/$', views.ProfileAPIListView.as_view()),
  url(r'^agencys/$', views1.AgencyList.as_view(), name='agency-all'),
  url(r'^passing/(?P<pk>[0-9]+)/$', views.RateResultPassingAPIListView.as_view(), name='RateResultPassingAPIListView-all'),  
  url(r'^dashboard/(?P<pk>[0-9]+)/$', views.Dashbord.as_view(), name='RateResultPassingAPIListView-all')  

]

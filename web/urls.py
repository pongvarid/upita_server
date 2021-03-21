from django.conf.urls import include, url
from web import views


urlpatterns = [

  url(r'^websetting/(?P<id>[0-9]+)/$', views.WebSettingAPIView.as_view()),
  url(r'^websetting/$', views.WebSettingAPIListView.as_view()),
  url(r'^web/$', views.WebSettingFinalAPIView.as_view()),
  url(r'^app/$', views.WebValueFinalAPIView.as_view()),
]

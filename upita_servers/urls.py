"""upita_servers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static 
from frontend.views import index
from django.urls import re_path
urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('setting/',include("web.urls")),
    path('api/ita/v1/',include("ita.api.urls")),  
    path('api/ita/v2/',include("ita.apiv2.urls")),
    path('rest-auth/', include('rest_auth.urls')),
    path('api/oit/v1/', include('oit.urls')),
    path('api/iit/v1/', include('iit.api.urls')),
    path('api/iit/v2/', include('iit.urls')),
    path('api/eit/v1/', include('eit.api.urls')),
    path('api/eit/v2/', include('eit.urls')),
    path('api/report/v1/', include('report.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('accounts/', include('rest_registration.api.urls')),

    ] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

urlpatterns += [
     re_path('^.*$',index),
 ]
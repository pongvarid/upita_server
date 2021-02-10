from rest_framework.routers import SimpleRouter
from ita.api import views


router = SimpleRouter()
router.register(r'register', views.UserCreate)
router.register(r'agencytype', views.AgencyTypeViewSet)
router.register(r'agency', views.AgencyViewSet)
router.register(r'agencychange', views.AgencyListLog)
# router.register(r'agencys', views.AgencyList.as_view(), name='agency-all')
router.register(r'year', views.YearViewSet)
router.register(r'rate', views.RateViewSet)

router.register(r'ratestatus', views.RateStatusViewSet)
router.register(r'rateresultall', views.RateStatusViewSetAll)
router.register(r'result', views.RateResultViewSet)
router.register(r'rateresult', views.RateResultViewSet)
router.register(r'profile', views.ProfileViewSet)
router.register(r'urlrate', views.UrlInRateViewSet)
router.register(r'eituser', views.ReportAgencyEitViewSet)
urlpatterns = router.urls 


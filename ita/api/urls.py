from rest_framework.routers import SimpleRouter
from ita.api import views


router = SimpleRouter()

router.register(r'agencytype', views.AgencyTypeViewSet)
router.register(r'agency', views.AgencyViewSet)
router.register(r'year', views.YearViewSet)
router.register(r'rate', views.RateViewSet)
router.register(r'ratestatus', views.RateStatusViewSet)
router.register(r'rateresult', views.RateResultViewSet)
router.register(r'profile', views.ProfileViewSet)

urlpatterns = router.urls

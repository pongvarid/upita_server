from rest_framework.routers import SimpleRouter
from report import views


router = SimpleRouter()

router.register(r'reportall', views.ReportAllViewSet)
router.register(r'reportdetail', views.ReportDetailViewSet)
router.register(r'reportall-all', views.ReportAllViewSetAll)
router.register(r'reportdetail-all', views.ReportDetailViewSetAll)
router.register(r'reportrawiit', views.ReportRawIITViewSet)
router.register(r'reportraweit', views.ReportRawEITViewSet)

urlpatterns = router.urls

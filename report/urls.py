from rest_framework.routers import SimpleRouter
from report import views


router = SimpleRouter()

router.register(r'reportall', views.ReportAllViewSet)
router.register(r'reportdetail', views.ReportDetailViewSet)
router.register(r'reportrawiit', views.ReportRawIITViewSet)
router.register(r'reportraweit', views.ReportRawEITViewSet)

urlpatterns = router.urls

from rest_framework.routers import SimpleRouter
from oit import views


router = SimpleRouter()

router.register(r'evaluateoit', views.EvaluateOITViewSet)

urlpatterns = router.urls

from rest_framework.routers import SimpleRouter
from moral_organization import views


router = SimpleRouter()
router.register(r'year', views.YearViewset)
router.register(r'category', views.CategoryViewset)
router.register(r'assessment', views.AssessmentViewset)
router.register(r'choice', views.ChoiceViewset)
router.register(r'main_exercise', views.Main_exerciseViewset)
router.register(r'do_exercise', views.Do_exerciseViewset)

router.register(r'baseplan', views.BasePlanViewset)
router.register(r'finishplan', views.FinishPlanViewset)
router.register(r'do_exercise', views.Do_exerciseViewset)



urlpatterns = router.urls
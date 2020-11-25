from rest_framework.routers import SimpleRouter
from eit import views


router = SimpleRouter()

router.register(r'year', views.YearViewSet)
router.register(r'choice', views.ChoiceViewSet)
router.register(r'ascend', views.AscendViewSet)
router.register(r'exist', views.ExistViewSet)
router.register(r'answer', views.AnswerViewSet)
router.register(r'assessmentissues', views.AssessmentIssuesViewSet)
router.register(r'issue', views.IssueViewSet)
router.register(r'issuedetail', views.IssueDetailViewSet)
router.register(r'answerissueeit', views.AnswerIssueEitViewSet)
router.register(r'answerissueeit-report', views.AnswerIssueReportViewSet)
router.register(r'answersuggestioneit', views.AnswerSuggestionEitViewSet)

urlpatterns = router.urls

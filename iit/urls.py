from rest_framework.routers import SimpleRouter
from iit import views


router = SimpleRouter()

router.register(r'year', views.YearViewSet)
router.register(r'choice', views.ChoiceViewSet)
router.register(r'ascend', views.AscendViewSet)
router.register(r'exist', views.ExistViewSet)
router.register(r'answer', views.AnswerViewSet)
router.register(r'assessmentissues', views.AssessmentIssuesViewSet)
router.register(r'issue', views.IssueViewSet)
router.register(r'issuedetail', views.IssueDetailViewSet)
router.register(r'answerissue', views.AnswerIssueViewSet)
router.register(r'answerissue-report', views.AnswerIssueReportViewSet)
router.register(r'answersuggestion', views.AnswerSuggestionViewSet)
router.register(r'ansewer/user', views.UserInAnswerViewSet)
urlpatterns = router.urls

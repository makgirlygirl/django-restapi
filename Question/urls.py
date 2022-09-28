from django.urls import path, include
from .views import QuestionListView, QuestionPostView
#from app_rest import views
from rest_framework import routers

#router = routers.DefaultRouter()
#router.register("/list", views.articleViewSet))

urlpatterns = [
    #path("", include(router.urls)),
    path("question/", QuestionListView.as_view()),
    path("question/<int:question_type>/", QuestionListView.as_view()),
    path("new_question/", QuestionPostView.as_view()),
]
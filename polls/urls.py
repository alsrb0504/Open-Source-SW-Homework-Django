from django.urls import path, re_path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    # detail.html으로 question_id 전달을 위해 시도했지만 실패한 지점.
    # re_path(r'(?P<query>\w+)$', views.DetailView, name='detail'),

    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('makequestion', views.RecieveQuestion, name='receive'),
    path('question', views.QuestionView, name='question')
]
    # path('results', views.ResultsView.as_view(), name='results'),
from django.urls import path
from . import views

urlpatterns = [
    # ex: /polls/, /polls/5/, /polls/5/results/, /polls/5/vote/
    path('',views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/',views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
from django.urls import path

from . import views
from django.http import HttpResponse

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('teamstats/<str:team_name>', views.teamStats, name='teamstats'),
    path('teamstats/<str:team_name>/range', views.teamStatsRange, name='teamstats'),
    path('teamstats/<str:team_name>/add', views.teamStatsAdd, name='teamstats'),
    path('teamlist', views.teamList, name='teamlist'),
    path('teamlist/range', views.teamListRange, name='teamlist'),
    path('teamlist/add', views.teamListAdd, name='teamlist'),
    #path('teamlist/teamstats/<str:team_name>', views.teamStats, name='teamstats'),
    #path('teamlist/teamstats/<str:team_name>/range', views.teamStatsRange, name='teamstats'),
    #path('teamlist/teamstats/<str:team_name>/add', views.teamStatsAdd, name='teamstats'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote')
]

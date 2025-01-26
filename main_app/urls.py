from django.urls import path
from . import views
from main_app.views import ScoreCreate, ScoreUpdate, ScoreDelete, Home

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('scores/', views.score_index, name='score-index'),
    path('scores/<int:score_id>', views.score_detail, name='score-detail'),
    # path('score/<score_id>', views.ScoreDetail, name 'score-detail'),
    path('scores/create', views.ScoreCreate.as_view(), name='score-create'),
    path('scores/<int:pk>/update/', views.ScoreUpdate.as_view(), name='score-update'),
    path('scores/<int:pk>/delete/', views.ScoreDelete.as_view(), name='score-delete'),
]

from django.urls import path
from . import views
app_name = 'games'
urlpatterns = [
    path('games/', views.games, name='games'),
    path('games/<int:game_id>', views.info, name='info')
]
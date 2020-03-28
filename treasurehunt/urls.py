from django.urls import path
from . import views
app_name = 'treasurehunt'

urlpatterns = [
    path('', views.index, name='index'),
    path('question/', views.question, name="question"),
    path('logout/', views.user_logout, name="logout"),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('leaderboard/', views.leaderboard, name='leaderboard')
]

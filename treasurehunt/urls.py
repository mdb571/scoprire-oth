from django.urls import path
from . import views
from django.views.static import serve
from django.conf.urls.static import static
from django.conf import settings
app_name = 'treasurehunt'

urlpatterns = [
    path('', views.index, name='index'),
    path('question/', views.question, name="question"),
    path('logout/', views.user_logout, name="logout"),
    # path('register/', views.register, name='register'),
   # path('login/', views.user_login, name='login'),


    path('leaderboard/', views.leaderboard, name='leaderboard')
] 
urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

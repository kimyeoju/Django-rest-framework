from django.urls import path
from . import views


urlpatterns = [
    # user/
    # 회원가입
    path('register/', views.Registration.as_view()),
    path('login/', views.Login.as_view()),
    path('logout/', views.Logout.as_view())
]
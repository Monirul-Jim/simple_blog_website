from django.urls import path
from . import views
urlpatterns = [
    path('signup/', views.signup, name='sign_up'),
    path('login/', views.user_login, name='login'),
    path('user_profile/', views.profile, name='user_profile'),
]

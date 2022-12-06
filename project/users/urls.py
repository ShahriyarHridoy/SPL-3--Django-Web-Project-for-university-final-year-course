from django import views
from django.urls import path
from . import views
from .forms import UserLoginForm
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('add-profile/', views.add_profile, name='add_profile'),
    path('login/', auth_view.LoginView.as_view(template_name='users/login.html', authentication_form=UserLoginForm), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    # path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('json/', views.paper_response_json, name='paper_response_json')
]


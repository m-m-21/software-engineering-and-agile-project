from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.signup, name='signup'),  # Set signup as the default page
    path('login/', auth_views.LoginView.as_view(template_name='login.html')),
    path('home/', views.home_view, name='home'),  # Home page after login
]

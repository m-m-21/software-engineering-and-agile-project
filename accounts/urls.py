from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.signup, name='signup'),  # Set signup as the default page
    path('login/', auth_views.LoginView.as_view(template_name='login.html')),
    path('home/', views.home_view, name='home'),  # Home page after login
    path('video/<uuid:video_id>/', views.video_detail, name='video_detail'),
    path('add-video/', views.add_video, name='add_video'),
    path('delete-video/<uuid:video_id>/', views.delete_video, name='delete_video'),
    path('edit-video/<uuid:video_id>/', views.edit_video, name='edit_video'),
]

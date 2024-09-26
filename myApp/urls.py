from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),  # Include URLs from the accounts app
    path('', include('django.contrib.auth.urls')),  # Include default auth URLs
]

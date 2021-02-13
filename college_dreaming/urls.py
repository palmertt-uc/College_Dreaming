"""college_dreaming URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
                  path('profile/', user_views.profile, name='profile'),
                  path('profile/delete/', user_views.delete_user, name='delete_user'),
                  path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
                  path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
                  path('register/', user_views.register, name='register'),
                  path('fav/<int:pk>/', user_views.favourite_add, name='favourite_add'),
                  path('password/', user_views.change_password, name='change_password'),
                  path('', include('universities.urls')),
                  path('admin/', admin.site.urls),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

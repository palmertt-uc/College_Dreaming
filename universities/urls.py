from django.urls import path
from . import views
from .views import UniversityListView, UniversityDetailView, QuizView, UsersListView, UserDetailView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', UniversityListView.as_view(), name='home'),
    path('universities/<int:pk>/', UniversityDetailView.as_view(), name='university-detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('api/search-universities/', views.institutionsList, name='search-universities'),
    path('quiz/', QuizView.as_view(), name='quiz'),
    path('users/', UsersListView.as_view(), name='users'),
    path('users/<int:pk>/', login_required(UserDetailView.as_view()), name='user-detail')
]

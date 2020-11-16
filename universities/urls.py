from django.urls import path
from . import views
from .views import UniversityListView, UniversityDetailView, QuizView

urlpatterns = [
    path('', UniversityListView.as_view(), name='home'),
    path('universities/<int:pk>/', UniversityDetailView.as_view(), name='university-detail'),
    path('search/', views.search, name='search'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('api/search-universities/', views.institutionsList, name='search-universities'),
    path('quiz/', QuizView.as_view(), name='quiz')
]

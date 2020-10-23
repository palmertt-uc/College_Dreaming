from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Institutions


# Create your views here.
def index(request):
    return render(request, 'universities/index.html')


class UniversityListView(ListView):
    model = Institutions
    template_name = 'universities/universities.html'
    context_object_name = 'universities'
    paginate_by = 50


class UniversityDetailView(DetailView):
    model = Institutions


def search(request):
    return render(request, 'universities/search.html')


def about(request):
    return render(request, 'universities/about.html')


def contact(request):
    return render(request, 'universities/contact.html')

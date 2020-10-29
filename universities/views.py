from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Institutions, Admissions, Cities, Zipcodes, Completionrates, Costs, Institutiontypes, Majors, Programs, Undergraduates


# Create your views here.
def index(request):
    return render(request, 'universities/index.html')


class UniversityListView(ListView):
    model = Institutions
    template_name = 'universities/universities.html'
    context_object_name = 'universities'
    paginate_by = 50

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            object_list = self.model.objects.filter(instname__icontains=query)
        else:
            object_list = self.model.objects.all()
        return object_list


class UniversityDetailView(DetailView):
    model = Institutions

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['admissions'] = Admissions.objects.all()
        context['costs'] = Costs.objects.all()
        context['institution_type'] = Institutiontypes.objects.all()
        return context


def search(request):
    return render(request, 'universities/search.html')


def about(request):
    return render(request, 'universities/about.html')


def contact(request):
    return render(request, 'universities/contact.html')

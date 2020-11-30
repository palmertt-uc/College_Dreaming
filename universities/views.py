from django.shortcuts import render
from django.db.models import Q
from .serializers import InstitutionsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.generic import ListView, DetailView
from .models import Institutions, Admissions, Completionrates, Costs, Institutiontypes, Majors, Programs, Undergraduates
from .filters import InstitutionFilter


# Create your views here.
class QuizView(ListView):
    model = Institutions
    context_object_name = 'universities'
    template_name = 'universities/quiz.html'
    paginate_by = 50

    def get_context_data(self, **kwargs):
        quiz_context = super().get_context_data(**kwargs)
        quiz_context['admissions'] = Admissions.objects.all()
        quiz_context['completion_rates'] = Completionrates.objects.all()
        quiz_context['costs'] = Costs.objects.all()
        quiz_context['institution_types'] = Institutiontypes.objects.all()
        quiz_context['majors'] = Majors.objects.all()
        quiz_context['programs'] = Programs.objects.all()
        quiz_context['undergraduates'] = Undergraduates.objects.all()
        return quiz_context


class UniversityListView(ListView):
    model = Institutions
    template_name = 'universities/universities.html'
    context_object_name = 'universities'
    paginate_by = 50

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['institution_filter'] = InstitutionFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return InstitutionFilter(self.request.GET, queryset=queryset).qs


class UniversityDetailView(DetailView):
    model = Institutions

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['admissions'] = Admissions.objects.all()
        context['costs'] = Costs.objects.all()
        context['institution_type'] = Institutiontypes.objects.all()
        context['majors'] = Majors.objects.all()
        context['completion_rates'] = Completionrates.objects.all()
        context['programs'] = Programs.objects.all()
        context['undergraduates'] = Undergraduates.objects.all()
        return context


def search(request):
    return render(request, 'universities/search.html')


def about(request):
    return render(request, 'universities/about.html')


def contact(request):
    return render(request, 'universities/contact.html')


@api_view(['GET'])
def institutionsList(request):
    query = request.GET.get('query')
    institutions = Institutions.objects.filter(instname__icontains=query)[:5]
    serializer = InstitutionsSerializer(institutions, many=True)
    return Response(serializer.data)

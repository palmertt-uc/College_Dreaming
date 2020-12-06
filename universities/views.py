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
    template_name = 'universities/quiz.html'
    context_object_name = 'universities'
    paginate_by = 50

    def get_queryset(self):
        crime = self.request.GET.get('crime')
        restaurants = self.request.GET.get('restaurants')
        outdoors = self.request.GET.get('outdoors')
        commute = self.request.GET.get('commute')
        state = self.request.GET.get('state')
        diversity = self.request.GET.get('diversity')
        submitted = self.request.GET.get('submitted')
        concact = False
        queryValue = ''
        if crime == None or crime == '':
            crime = ''
        else:
            queryValue = crime
            concact = True

        if restaurants == None or restaurants == '':
            restaurants = ''
        else:
            if concact:
                queryValue = queryValue + ' AND ' + restaurants
            else:
                queryValue = restaurants
                concact = True

        if outdoors == None or outdoors == '':
            outdoors = ''
        else:
            if concact:
                queryValue = queryValue + ' AND ' + outdoors
            else:
                queryValue = outdoors
                concact = True

        if commute == None or commute == '':
            commute = ''
        else:
            if concact:
                queryValue = queryValue + ' AND ' + commute
            else:
                queryValue = commute
                concact = True

        if state == None or state == '':
            state = ''
        else:
            if concact:
                queryValue = queryValue + ' AND ' + state
            else:
                queryValue = state
                concact = True

        if diversity == None or diversity == '':
            diversity = ''
        else:
            if concact:
                queryValue = queryValue + ' AND ' + diversity
            else:
                queryValue = diversity
                concact = True

        if queryValue != '':
            queryValue = 'WHERE ' + queryValue

        return Institutions.objects.raw('SELECT Institutions.* FROM Institutions'
        + ' LEFT JOIN Undergraduates ON Institutions.InstitutionId = Undergraduates.InstitutionId'
        + ' LEFT JOIN ZipCodes ON ZipCodes.ZipCodeId = Institutions.ZipCodeId'
        + ' LEFT JOIN Cities ON Cities.CityId = ZipCodes.CityId'
        + ' LEFT JOIN Crime ON Crime.CrimeId = Cities.CrimeId'
        + ' LEFT JOIN Climate ON Climate.ClimateId = Institutions.ClimateId'
        + ' ' + queryValue)


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
    print('cincinnati')
    query = request.GET.get('query')
    institutions = Institutions.objects.filter(instname__icontains=query)[:5]
    serializer = InstitutionsSerializer(institutions, many=True)
    return Response(serializer.data)

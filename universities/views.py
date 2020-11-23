from django.shortcuts import render
from django.db.models import Q
from .serializers import InstitutionsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.generic import ListView, DetailView
from .models import Institutions, Admissions, Completionrates, Costs, Institutiontypes, Majors, Programs, Undergraduates


# Create your views here.
class QuizView(ListView):
    model = Institutions
    template_name = 'universities/quiz.html'

    def get_queryset(self):
        crime = self.request.GET.get('crime')
        restaurants = self.request.GET.get('restaurants')
        outdoors = self.request.GET.get('outdoors')
        commute = self.request.GET.get('commute')
        state = self.request.GET.get('state')
        diversity = self.request.GET.get('diversity')
        submit = self.request.GET.get('submit')

        query = crime + restaurants + outdoors + commute + state + diversity

        return Institutions.objects.raw('SELECT Institutions.* FROM Institutions'
        + ' LEFT JOIN Undergraduates ON Institutions.InstitutionId = Undergraduates.InstitutionId'
        + 'LEFT JOIN ZipCodes ON ZipCodes.ZipCodeId = Institutions.ZipCodeId'
        + 'LEFT JOIN Cities ON Cities.CityId = ZipCodes.CityId'
        + 'LEFT JOIN Crime ON Crime.CrimeId = Cities.CrimeId'
        + 'LEFT JOIN Climate ON Climate.ClimateId = Institutions.ClimateId'
        + 'WHERE ' + query)


class UniversityListView(ListView):
    model = Institutions
    template_name = 'universities/universities.html'
    context_object_name = 'universities'
    paginate_by = 50

    def get_queryset(self):
        query = self.request.GET.get('query')
        state = self.request.GET.get('state')
        city = self.request.GET.get('city')
        if query:
            object_list = self.model.objects.filter(instname__icontains=query)
            if query and state:
                object_list = self.model.objects.filter(Q(instname__icontains=query) &
                                                        Q(zipcodeid__cityid__state__exact=state))
            elif query and city:
                object_list = self.model.objects.filter(Q(instname__icontains=query) &
                                                        Q(zipcodeid__cityid__city__iexact=city))
        elif state:
            object_list = self.model.objects.filter(zipcodeid__cityid__state__exact=state)
            if state and city:
                object_list = self.model.objects.filter(Q(zipcodeid__cityid__state__exact=state) &
                                                        Q(zipcodeid__cityid__city__iexact=city))
        elif city:
            object_list = self.model.objects.filter(zipcodeid__cityid__city__iexact=city)
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

def universities(request):
    return render(request, 'universities/universities.html')


@api_view(['GET'])
def institutionsList(request):
    print('cincinnati')
    query = request.GET.get('query')
    institutions = Institutions.objects.filter(instname__icontains=query)[:5]
    serializer = InstitutionsSerializer(institutions, many=True)
    return Response(serializer.data)

from django.shortcuts import render, get_object_or_404
from .serializers import InstitutionsSerializer
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.generic import ListView, DetailView
from .models import Institutions, Admissions, Completionrates, Costs, Institutiontypes, Majors, Programs, Undergraduates
from .filters import InstitutionFilter, UserFilter
from users.models import Profile
from .models import Institutions, Crime, Zipcodes, Cities, Admissions, Completionrates, Costs,\
    Institutiontypes, Majors, Programs, Undergraduates


# Create your views here.
class QuizView(ListView):
    model = Institutions
    template_name = 'universities/quiz.html'
    context_object_name = 'universities'
    paginate_by = 50

    def get_queryset(self):
        filters = Q()
        crime = self.request.GET.get('crime')
        restaurants = self.request.GET.get('restaurants')
        outdoors = self.request.GET.get('outdoors')
        commute = self.request.GET.get('urban')
        state = self.request.GET.get('state')
        diversity = self.request.GET.get('diversity')
        submitted = self.request.GET.get('submitted')

        if crime is not None and crime != '':
            filters |= Q(ViolentCrimes__level__lt=crime)
        if restaurants is not None and restaurants != '':
            filters |= Q(RestaurantRanking__level__gte=restaurants)
        if state is not None and state != '':
            filters |= Q(State=state)
        if diversity is not None and diversity != '':
            filters |= Q(demographics_white__level__lte=.5)

        if(len(filters) > 0):
            institutions = self.model.objects.filter(zipcodeid__cityid__state="OH")
            return institutions
        else:
            return ""

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
        university = get_object_or_404(Institutions, pk=self.kwargs.get('pk'))
        favorited = bool

        if university.favorite.filter(id=self.request.user.id).exists():
            favorited = True

        context = super().get_context_data(**kwargs)
        context['admissions'] = Admissions.objects.all()
        context['costs'] = Costs.objects.all()
        context['institution_type'] = Institutiontypes.objects.all()
        context['majors'] = Majors.objects.all()
        context['completion_rates'] = Completionrates.objects.all()
        context['programs'] = Programs.objects.all()
        context['undergraduates'] = Undergraduates.objects.all()
        context['favorite'] = favorited
        return context


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


class UsersListView(ListView):
    model = Profile
    template_name = 'universities/user_list.html'
    context_object_name = 'profile'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_filter'] = UserFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return UserFilter(self.request.GET, queryset=queryset).qs


class UserDetailView(DetailView):
    model = Profile

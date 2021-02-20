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
        university_costs = Costs.objects.all()
        university_admissions = Admissions.objects.all()
        university_undergraduates = Undergraduates.objects.all()
        university_completion_rate = Completionrates.objects.all()
        university_majors = Majors.objects.all()
        costs = {}
        admissions = {}
        undergraduates = {}
        completion = {}
        majors = {}

        for cost in university_costs:
            if university.institutionid == cost.costsid:
                costs['inStateTuition'] = str(cost.tuition_in_state) + '</script>&amp;'
                costs['outStateTuition'] = str(cost.tuition_out_of_state) + '</script>&amp;'

        for admission in university_admissions:
            if university.institutionid == admission.admissionid:
                admissions['actScore'] = str(admission.act_scores_midpoint_cumulative) + '</script>&amp;'
                admissions['satScore'] = str(admission.sat_scores_average_overall) + '</script>&amp;'
                admissions['admissionRate'] = str(admission.admission_rate_overall) + '</script>&amp;'

        for undergrads in university_undergraduates:
            if university.institutionid == undergrads.undergraduateid:
                undergraduates['caucasian'] = str(undergrads.demographics_white) + '</script>&amp;'
                undergraduates['africanAmerican'] = str(undergrads.demographics_black) + '</script>&amp;'
                undergraduates['hispanic'] = str(undergrads.demographics_hispanic) + '</script>&amp;'
                undergraduates['pacificIslander'] = str(undergrads.demographics_nhpi) + '</script>&amp;'
                undergraduates['multiRacial'] = str(undergrads.demographics_multiracial) + '</script>&amp;'
                undergraduates['nonResident'] = str(undergrads.demographics_non_resident_alien) + '</script>&amp;'
                undergraduates['asian'] = str(undergrads.demographics_asian) + '</script>&amp;'
                undergraduates['aian'] = str(undergrads.demographics_ai_an) + '</script>&amp;'

        for completion_rates in university_completion_rate:
            if university.institutionid == completion_rates.completionrateid:
                completion['whiteCompletionRate'] = str(completion_rates.completion_rate_4yr_150_white) + '</script>&amp;'
                completion['blackCompletionRate'] = str(completion_rates.completion_rate_4yr_150_black) + '</script>&amp;'
                completion['hispanicCompletionRate'] = str(completion_rates.completion_rate_4yr_150_hispanic) + '</script>&amp;'
                completion['asianCompletionRate'] = str(completion_rates.completion_rate_4yr_150_asian) + '</script>&amp;'
                completion['aianCompletionRate'] = str(completion_rates.completion_rate_4yr_150_aian) + '</script>&amp;'
                completion['pacificIslanderCompletionRate'] = str(completion_rates.completion_rate_4yr_150_nhpi) + '</script>&amp;'
                completion['multiRacialCompletionRate'] = str(completion_rates.completion_rate_4yr_150_2ormore) + '</script>&amp;'
                completion['nonResidentCompletionRate'] = str(completion_rates.completion_rate_4yr_150_nonresident_alien) + '</script>&amp;'
                completion['otherCompletionRate'] = str(completion_rates.completion_rate_4yr_150_race_unknown) + '</script>&amp;'

        for major in university_majors:
            if university.institutionid == major.majorid:
                majors['agriculture'] = str(major.agriculture) + '</script>&amp;'
                majors['resources'] = str(major.resources) + '</script>&amp;'
                majors['architecture'] = str(major.architecture) + '</script>&amp;'
                majors['ethnicCulturalGender'] = str(major.ethnic_cultural_gender) + '</script>&amp;'
                majors['communication'] = str(major.communication) + '</script>&amp;'
                majors['communicationsTechnology'] = str(major.communications_technology) + '</script>&amp;'
                majors['computer'] = str(major.computer) + '</script>&amp;'
                majors['personalCulinary'] = str(major.personal_culinary) + '</script>&amp;'
                majors['education'] = str(major.education) + '</script>&amp;'
                majors['engineering'] = str(major.engineering) + '</script>&amp;'
                majors['engineeringTechnology'] = str(major.engineering_technology) + '</script>&amp;'
                majors['language'] = str(major.language) + '</script>&amp;'
                majors['familyConsumerScience'] = str(major.family_consumer_science) + '</script>&amp;'
                majors['legal'] = str(major.legal) + '</script>&amp;'
                majors['english'] = str(major.english) + '</script>&amp;'
                majors['humanities'] = str(major.humanities) + '</script>&amp;'
                majors['library'] = str(major.library) + '</script>&amp;'
                majors['biological'] = str(major.biological) + '</script>&amp;'
                majors['mathematics'] = str(major.mathematics) + '</script>&amp;'
                majors['military'] = str(major.military) + '</script>&amp;'
                majors['multiDiscipline'] = str(major.multidiscipline) + '</script>&amp;'
                majors['parksRecreationFitness'] = str(major.parks_recreation_fitness) + '</script>&amp;'
                majors['philosophyReligious'] = str(major.philosophy_religious) + '</script>&amp;'
                majors['theologyReligiousVocation'] = str(major.theology_religious_vocation) + '</script>&amp;'
                majors['physicalScience'] = str(major.physical_science) + '</script>&amp;'
                majors['scienceTechnology'] = str(major.science_technology) + '</script>&amp;'
                majors['psychology'] = str(major.psychology) + '</script>&amp;'
                majors['securityLawEnforcement'] = str(major.security_law_enforcement) + '</script>&amp;'
                majors['publicAdministration'] = str(major.public_administration_social_service) + '</script>&amp;'
                majors['socialScience'] = str(major.social_science) + '</script>&amp;'
                majors['construction'] = str(major.construction) + '</script>&amp;'
                majors['mechanicRepairTechnology'] = str(major.mechanic_repair_technology) + '</script>&amp;'
                majors['precisionProduction'] = str(major.precision_production) + '</script>&amp;'
                majors['transportation'] = str(major.transportation) + '</script>&amp;'
                majors['visualPerforming'] = str(major.visual_performing) + '</script>&amp;'
                majors['health'] = str(major.health) + '</script>&amp;'
                majors['businessMarketing'] = str(major.business_marketing) + '</script>&amp;'
                majors['history'] = str(major.history) + '</script>&amp;'

        if university.favorite.filter(id=self.request.user.id).exists():
            favorited = True

        context = super().get_context_data(**kwargs)
        context['admissions'] = admissions
        context['costs'] = costs
        context['institution_type'] = Institutiontypes.objects.all()
        context['majors'] = majors
        context['completion_rates'] = completion
        context['university_costs'] = university_costs
        context['undergraduates'] = undergraduates
        context['favorite'] = favorited
        context['university_admissions'] = university_admissions
        context['university_undergrads'] = university_undergraduates
        context['university_majors'] = university_majors
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

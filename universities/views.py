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
import logging


# Create your views here.
class QuizView(ListView):
    model = Institutions
    template_name = 'universities/quiz.html'
    context_object_name = 'universities'
    paginate_by = 50


    def get_queryset(self):
        query_dict = {
            "contLowCosts":(Q(costsid__tuition_in_state__lte=5000) & Q(zipcodeid__cityid__state='OH')) | (Q(costsid__tuition_out_of_state__lte=5000) & ~Q(zipcodeid__cityid__state='OH')),
            "contMedCosts":(Q(costsid__tuition_in_state__lte=10000) & Q(zipcodeid__cityid__state='OH')) | (Q(costsid__tuition_out_of_state__lte=10000) & ~Q(zipcodeid__cityid__state='OH')),
            "contHighCosts":(Q(costsid__tuition_in_state__gte=0) & Q(zipcodeid__cityid__state='OH')) | (Q(costsid__tuition_out_of_state__gte=0) & ~Q(zipcodeid__cityid__state='OH')),
            "contLowSelectivity":Q(admissionid__admission_rate_overall__gte=.7),
            "contMedSelectivity":Q(admissionid__admission_rate_overall__gte=.5),
            "contHighSelectivity":Q(admissionid__admission_rate_overall__gte=0),
            "contNoPrefInstitution":Q(institutiontypeid__gte=0),
            "contNoneInstitution":(Q(institutiontypeid__HBCU=0) & (Q(InstitutionTypeId__PBI=0)) & Q(InstitutionTypeId__ANNHI=0) & Q(InstitutionTypeId__TRIBAL=0) & Q(InstitutionTypeId__AANAPII=0) & Q(InstitutionTypeId__HSI=0) & Q(InstitutionTypeId__NANTI=0)
                                   & Q(InstitutionTypeId__MENONLY=0) & Q(InstitutionTypeId__WOMENONLY=0) & Q(InstitutionTypeId__RELAFFIL=0)),
            "contHBInstitution":Q(InstitutionTypeId__HBCU=1),
            "contNAInstitution":Q(InstitutionTypeId__TRIBAL=1),
            "contAAPIInstitution":Q(InstitutionTypeId__AANAPII=1),
            "contMenInstitution":Q(InstitutionTypeId__MENONLY=1),
            "contWomenInstitution":Q(InstitutionTypeId__WOMENONLY=1),
            "contPublic":Q(CostsId__avg_net_price_public__gt=0),
            "contPrivate":Q(CostsId__avg_net_price_private__gt=0),
            "contNoTypePref":(Q(CostsId__avg_net_price_public__gt=0) | Q(CostsId__avg_net_price_private__gt=0)),
            "contSmallSize":Q(UndergraduateId__enrollment_degree_seeking__lte=1000),
            "contMedSize":(Q(UndergraduateId__enrollment_degree_seeking__gte=1000) & Q(UndergraduateId__enrollment_degree_seeking__lte=10000)),
            "contLargeSize":Q(UndergraduateId__enrollment_degree_seeking__gte=10000),
            "contNoPrefSize":Q(UndergraduateId__enrollment_degree_seeking__gte=0),
            "contNoPrefGradRate":Q(CompletionRatesId__completion_rate_4yr_150_white__gte=0),
            "contAvgGradRate":Q(CompletionRatesId__completion_rate_4yr_150_white__gte=.5),
            "contHighGradRate":Q(CompletionRatesId__completion_rate_4yr_150_white__gte=.8),
            "contNoPrefHousingCosts":Q(CompletionRatesId__completion_rate_4yr_150_white__gte=0),
            "contLowHousingCosts":Q(CompletionRatesId__completion_rate_4yr_150_white__gte=0),
            "contMedHousingCosts":Q(CompletionRatesId__completion_rate_4yr_150_white__gte=0),
            "contNoPrefJobs":Q(CompletionRatesId__completion_rate_4yr_150_white__gte=0),
            "contEntryJobs":Q(CompletionRatesId__completion_rate_4yr_150_white__gte=0),
            "contMyFieldJobs":Q(CompletionRatesId__completion_rate_4yr_150_white__gte=0),
            "contBothJobs":Q(CompletionRatesId__completion_rate_4yr_150_white__gte=0),
            "contNoPrefCrime":(Q(zipcodeid__cityid__crimeId=0) | Q(zipcodeid__cityid__crimeId='null')),
            "contViolentCrime":(Q(zipcodeid__cityid__crimeId__violentCrimes__lte=100) | Q(zipcodeid__cityid__crimeId='null')),
            "contPropertyCrime":(Q(zipcodeid__cityid__crimeId__propertyCrimes__lte=100) | Q(zipcodeid__cityid__crimeId='null')),
            "contBothCrime":((Q(zipcodeid__cityid__crimeId__violentCrimes__lte=100) | Q(zipcodeid__cityid__crimeId='null')) & (Q(zipcodeid__cityid__crimeId__propertyCrimes__lte=100) | Q(zipcodeid__cityid__crimeId='null'))),
            "contNoPrefCommunity":~Q(Locale=-1),
            "contRuralCommunity":Q(Locale=12),
            "contSuburbanCommunity":Q(Locale=12),
            "contUrbanCommunity":Q(Locale=12),
            "contRuralSuburbanCommunity":(Q(Locale=12) | Q(Locale=12)),
            "contRuralUrbanCommunity":(Q(Locale=12) | Q(Locale=12)),
            "contSuburbanUrbanCommunity":(Q(Locale=12) | Q(Locale=12)),
            "contNoPrefSummers":Q(ClimateId__maxTemp__gte=0),
            "contCoolSummers":Q(ClimateId__maxTemp__lte=60),
            "contWarmSummers":(Q(ClimateId__maxTemp__lte=80) & Q(ClimateId__maxTemp__gte=60)),
            "contHotSummers":Q(ClimateId__maxTemp__gte=80),
            "contNoPrefWinters":Q(ClimateId__minTemp__lte=100),
            "contColdWinters":Q(ClimateId__minTemp__lte=0),
            "contCoolWinters":(Q(ClimateId__minTemp__lte=60) & Q(ClimateId__minTemp__gte=40)),
            "contWarmWinters":Q(ClimateId__minTemp__gte=60),
            "contNoPrefSnow":Q(ClimateId__maxTemp__gte=0),
            "contNoSnow":Q(ClimateId__maxTemp__gte=0),
            "contSomeSnow":Q(ClimateId__maxTemp__gte=0),
            "contLotsOfSnow":Q(ClimateId__maxTemp__gte=0),
            "contNoPrefSunny":Q(ClimateId__maxTemp__gte=0),
            "contSunny":Q(ClimateId__maxTemp__gte=0)
        }
        filters = Q(institutionid__in=[])

        filters.add(query_dict[self.request.GET.get('costs')], Q.AND)
        filters.add(query_dict[self.request.GET.get('selectivity')], Q.AND)
        filters.add(query_dict[self.request.GET.get('special')], Q.AND)
        filters.add(query_dict[self.request.GET.get('type')], Q.AND)
        filters.add(query_dict[self.request.GET.get('size')], Q.AND)
        filters.add(query_dict[self.request.GET.get('gradRate')], Q.AND)
        filters.add(query_dict[self.request.GET.get('housing_costs')], Q.AND)
        filters.add(query_dict[self.request.GET.get('job_availability')], Q.AND)
        filters.add(query_dict[self.request.GET.get('crime')], Q.AND)
        filters.add(query_dict[self.request.GET.get('community')], Q.AND)
        filters.add(query_dict[self.request.GET.get('summers')], Q.AND)
        filters.add(query_dict[self.request.GET.get('winters')], Q.AND)
        filters.add(query_dict[self.request.GET.get('snowy')], Q.AND)
        filters.add(query_dict[self.request.GET.get('sunny')], Q.AND)

        return self.model.objects.filter(filters)

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
        university_institutions = Institutions.objects.all()
        costs = {}
        admissions = {}
        undergraduates = {}
        completion = {}
        majors = {}
        institutions = {}

        for institution_dictionary in university_institutions:
            if university.institutionid == institution_dictionary.institutionid:
                institutions['latitude'] = str(institution_dictionary.latitude) + '</script>&amp;'
                institutions['longitude'] = str(institution_dictionary.longitude) + '</script>&amp;'
                institutions['instname'] = str(institution_dictionary.instname) + '</script>&amp;'

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
        context['university_institutions'] = institutions
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

class SearchResultsView(ListView):
    model = Institutions
    template_name = 'universities/search_results.html'
    context_object_name = 'universities'
    paginate_by = 26

    def get_queryset(self):
        queryset = super().get_queryset()
        return InstitutionFilter(self.request.GET, queryset=queryset).qs
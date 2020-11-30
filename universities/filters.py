import django_filters
from django.forms import TextInput
from django_filters import RangeFilter

from .models import Institutions


class InstitutionFilter(django_filters.FilterSet):
    institution_name = django_filters.CharFilter(field_name='instname', lookup_expr='icontains',
                                                 label='Institution Name',
                                                 widget=TextInput(attrs={'placeholder': 'Enter Name...'}))
    institution_city = django_filters.CharFilter(field_name='zipcodeid__cityid__city', lookup_expr='iexact',
                                                 label='City Name',
                                                 widget=TextInput(attrs={'placeholder': 'Enter City...'}))
    institution_state = django_filters.CharFilter(field_name='zipcodeid__cityid__state', lookup_expr='iexact',
                                                  label='State Abbreviation',
                                                  widget=TextInput(attrs={'placeholder': 'Enter State...'}))
    act_average = django_filters.NumberFilter(field_name='admissions__act_scores_midpoint_cumulative',
                                              label='ACT Score', lookup_expr='gt',
                                              widget=TextInput(attrs={'placeholder': 'Enter ACT Score...'}))
    sat_average = django_filters.NumberFilter(field_name='admissions__sat_scores_average_overall',
                                              label='SAT Score', lookup_expr='gt',
                                              widget=TextInput(attrs={'placeholder': 'Enter SAT Score...'}))

    class Meta:
        model = Institutions
        fields = ('institution_name', 'institution_city', 'institution_state', 'act_average',
                  'sat_average')
